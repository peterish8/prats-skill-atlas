#!/usr/bin/env python3
"""Offline behavioral tests for `evaluate_traces.py` — no AWS, no external dependencies.

Stubs `boto3`/`botocore` so the bundled batch/matrix helper runs deterministically and its
contract is inspectable/reproducible. Covers: single-trace back-compat, the trace x evaluator
matrix with fetch-once, ground-truth gating (drop-mixed / die-if-all), the 10 / 5 / 50 caps and
the evaluate-call budget, `pairsScored` / `tracesScored` honesty, session de-duplication, and
real Logs-error propagation.

Run: `python test_evaluate_traces.py` (exits non-zero on any failure). This file is NOT executed
by the package's no-op build; it is a hand-run, reviewable regression suite for the helper.
"""

import contextlib
import importlib.util
import io
import json
import os
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
_N = 0


# Stable across every _load so a raised error is caught by whatever evaluate_traces copy imported it.
class _ClientError(Exception):
    def __init__(self, response=None, op=None):
        self.response = response or {}
        super().__init__(str(response))


class _BotoCoreError(Exception):
    pass


def _load(make_session):
    """Import a fresh copy of evaluate_traces with boto3/botocore stubbed to `make_session()`."""
    global _N
    _N += 1
    be = types.ModuleType("botocore.exceptions")
    setattr(be, "ClientError", _ClientError)
    setattr(be, "BotoCoreError", _BotoCoreError)
    bc = types.ModuleType("botocore")
    setattr(bc, "exceptions", be)
    b3 = types.ModuleType("boto3")
    setattr(b3, "Session", lambda **_k: make_session())
    sys.modules.update({"boto3": b3, "botocore": bc, "botocore.exceptions": be})

    spec = importlib.util.spec_from_file_location(
        "evaluate_traces_under_test_%d" % _N, os.path.join(HERE, "evaluate_traces.py")
    )
    assert spec is not None
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _make_session(
    counters,
    *,
    tool_spans=1,
    session_id=None,
    eval_mode="ok",
    raise_cls=None,
    group_exists=False,
    retention_raises=None,
):
    """Build a fake boto3 Session. `counters` records span-fetch and evaluate-call counts, and —
    for the writeback path — the log-group calls made and the kwargs they were made with.

    `group_exists=True` makes put_log_events succeed straight away (the group is already there, so
    nothing is provisioned). Otherwise the first put raises ResourceNotFoundException, driving the
    create/retention path. `retention_raises` is an error Code for put_retention_policy, to cover a
    group created without the bounded retention.
    """

    def _span(span_id, is_tool):
        attrs = {}
        if session_id:
            attrs["session.id"] = session_id
        if is_tool:
            attrs["gen_ai.operation.name"] = "execute_tool"
        return {
            "traceId": "t",
            "spanId": span_id,
            "kind": 2,
            "attributes": attrs,
            "resource": {"attributes": {"service.name": "svc"}},
        }

    docs = [_span("0" * 16, False)] + [_span("%016x" % (i + 1), True) for i in range(tool_spans)]

    class FakeLogs:
        def start_query(self, **k):
            self._q = k["queryString"]
            return {"queryId": "q"}

        def get_query_results(self, queryId):
            if raise_cls is not None:
                raise raise_cls(
                    {"Error": {"Code": "AccessDeniedException", "Message": "no logs:StartQuery"}},
                    "StartQuery",
                )
            if "fields `attributes.session.id`" in self._q:
                rows = (
                    [[{"field": "attributes.session.id", "value": session_id}]]
                    if session_id
                    else []
                )
                return {"status": "Complete", "results": rows}
            counters["fetch"] = counters.get("fetch", 0) + 1
            return {
                "status": "Complete",
                "results": [[{"field": "@message", "value": json.dumps(d)}] for d in docs],
            }

        def put_log_events(self, **k):
            counters.setdefault("put", []).append(k)
            if not (group_exists or counters.get("created")):
                raise _ClientError(
                    {"Error": {"Code": "ResourceNotFoundException", "Message": "no group"}},
                    "PutLogEvents",
                )
            return {}

        def create_log_group(self, **k):
            counters["created"] = k  # kwargs recorded so the CMK assertion can read kmsKeyId
            return {}

        def put_retention_policy(self, **k):
            counters["retention"] = k
            if retention_raises:
                raise _ClientError(
                    {"Error": {"Code": retention_raises, "Message": "nope"}}, "PutRetentionPolicy"
                )
            return {}

        def create_log_stream(self, **k):
            counters["stream"] = k
            return {}

    class FakeAC:
        def evaluate(self, **k):
            counters["eval"] = counters.get("eval", 0) + 1
            if eval_mode == "error":
                return {
                    "evaluationResults": [
                        {
                            "evaluatorId": k["evaluatorId"],
                            "value": None,
                            "errorCode": "AgentSpanMappingException",
                            "errorMessage": "boom",
                        }
                    ]
                }
            return {
                "evaluationResults": [
                    {
                        "evaluatorId": k["evaluatorId"],
                        "value": 0.5,
                        "label": "ok",
                        "explanation": "why",
                    }
                ]
            }

    class FakeSession:
        def client(self, name):
            return FakeLogs() if name == "logs" else FakeAC()

    return FakeSession()


def _run(mod, **kw):
    ns = mod.argparse.Namespace(
        trace_id=None,
        trace_ids=None,
        session_id=None,
        evaluator_id=None,
        evaluator_ids=None,
        level="TRACE",
        log_group="aws/spans",
        region="us-east-1",
        window_days=30,
        no_writeback=True,
        include_explanations=False,
        retention_days=30,
        kms_key_id=None,
    )
    for k, v in kw.items():
        setattr(ns, k, v)
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            mod._run(ns)
    except SystemExit:
        pass
    return json.loads(out.getvalue())


RESULTS = []


def check(name, cond):
    RESULTS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def test_single_trace_back_compat():
    c: dict = {}
    mod = _load(lambda: _make_session(c))
    r = _run(mod, trace_id="aa")
    check("single-trace: one pair scored, one fetch", r["pairsScored"] == 1 and c["fetch"] == 1)
    check(
        "single-trace: row tagged with traceId + evaluatorId",
        {"traceId", "evaluatorId", "value"} <= set(r["results"][0]),
    )


def test_matrix_fetch_once():
    c: dict = {}
    mod = _load(lambda: _make_session(c))
    r = _run(mod, trace_ids="aa,bb", evaluator_ids="E1,E2")
    check("matrix 2x2: 4 pairs scored", r["pairsScored"] == 4)
    check("matrix 2x2: fetch-once (2 fetches, not 4)", c["fetch"] == 2)


def test_ground_truth_gating():
    mod = _load(lambda: _make_session({}))
    r = _run(
        mod, trace_id="aa", evaluator_ids="Builtin.Helpfulness,Builtin.TrajectoryExactOrderMatch"
    )
    check(
        "mixed GT: drops trajectory matcher, scores the rest",
        r.get("evaluators") == ["Builtin.Helpfulness"],
    )
    r2 = _run(mod, trace_id="aa", evaluator_ids="Builtin.TrajectoryExactOrderMatch")
    check("all-GT: refuses the run", "error" in r2)


def test_caps():
    mod = _load(lambda: _make_session({}))
    r = _run(mod, trace_ids=",".join("%02x" % i for i in range(15)))
    check(
        "trace cap: 15 -> 10 with a note",
        r["tracesScored"] == 10 and any("capped to 10 traces" in n for n in r.get("notes", [])),
    )
    r2 = _run(mod, trace_ids="aa,bb,cc", evaluator_ids=",".join("E%d" % i for i in range(7)))
    check(
        "evaluator cap: 7 -> 5 with a note",
        len(r2["evaluators"]) == 5
        and any("capped to 5 evaluators" in n for n in r2.get("notes", [])),
    )


def test_evaluate_call_budget():
    c: dict = {}
    mod = _load(lambda: _make_session(c, tool_spans=25))  # 25 tool spans -> 3 chunks/pair
    mod.MAX_EVALUATE_CALLS = 5
    r = _run(mod, trace_ids="aa,bb,cc", evaluator_ids="E1,E2", level="TOOL_CALL")
    check("TOOL_CALL: total evaluate calls bounded by budget", c["eval"] <= 5)
    check("TOOL_CALL: budget/truncation noted", any("budget" in n for n in r.get("notes", [])))


def test_pairs_scored_excludes_errors():
    mod = _load(lambda: _make_session({}, eval_mode="error"))
    r = _run(mod, trace_id="aa")
    check("error-only result: not counted in pairsScored", r["pairsScored"] == 0)
    check(
        "error-only result: still surfaced in results",
        any(x.get("errorCode") for x in r["results"]),
    )


def test_traces_scored_honesty_under_budget():
    c: dict = {}
    mod = _load(lambda: _make_session(c, tool_spans=25))
    mod.MAX_EVALUATE_CALLS = 3  # only the first trace's chunks fit
    r = _run(mod, trace_ids="aa,bb,cc", level="TOOL_CALL")
    check(
        "tracesScored < tracesFetched when budget truncates", r["tracesScored"] < r["tracesFetched"]
    )
    check(
        "tracesScored == distinct traces with a real score",
        r["tracesScored"]
        == len(
            {
                x["traceId"]
                for x in r["results"]
                if x.get("value") is not None and not x.get("errorCode")
            }
        ),
    )


def test_session_dedup():
    c: dict = {}
    mod = _load(lambda: _make_session(c, session_id="S1"))  # both trace ids resolve to session S1
    r = _run(mod, trace_ids="aa,bb", evaluator_ids="E1", level="SESSION")
    check("same-session: fetched once", c["fetch"] == 1)
    check(
        "same-session: SESSION scored once (no duplicate)",
        len([x for x in r["results"] if x.get("value") is not None]) == 1,
    )


def test_real_error_propagated():
    mod = _load(lambda: _make_session({}, raise_cls=_ClientError))
    r = _run(mod, trace_id="aa")
    blob = json.dumps(r)
    check(
        "real Logs error surfaced (not the generic window message)",
        "AccessDenied" in blob or "logs:StartQuery" in blob,
    )


def test_explanation_withheld_from_receipt_by_default():
    mod = _load(lambda: _make_session({}))
    r = _run(mod, trace_id="aa")
    row = r["results"][0]
    check(
        "default receipt: no explanation text, but hasExplanation flags that one exists",
        "explanation" not in row and row.get("hasExplanation") is True,
    )
    check(
        "default receipt: no private key leaks to stdout",
        not any(k.startswith("_") for k in row),
    )
    r2 = _run(mod, trace_id="aa", include_explanations=True)
    check(
        "--include-explanations: explanation returned",
        r2["results"][0].get("explanation") == "why",
    )


def test_writeback_still_persists_explanation_without_the_flag():
    """The receipt flag and the stored record are independent — the corpus keeps its "why"."""
    c: dict = {}
    mod = _load(lambda: _make_session(c))
    r = _run(mod, trace_id="aa", no_writeback=False, include_explanations=False)
    written = json.loads(c["put"][-1]["logEvents"][0]["message"])
    check(
        "writeback: explanation persisted even though the receipt omitted it",
        written["attributes"].get("gen_ai.evaluation.explanation") == "why",
    )
    check("writeback: reported as persisted", r.get("persistedTraces") == 1)


def test_created_group_is_bounded_and_can_use_a_cmk():
    c: dict = {}
    mod = _load(lambda: _make_session(c))
    r = _run(mod, trace_id="aa", no_writeback=False, kms_key_id="arn:aws:kms:k")
    check("create: bounded retention applied", c.get("retention", {}).get("retentionInDays") == 30)
    check("create: CMK passed to create_log_group", c["created"].get("kmsKeyId") == "arn:aws:kms:k")
    check(
        "receipt states the posture it filed under",
        r.get("resultsRetentionDaysOnCreate") == 30
        and r.get("resultsKmsKeyOnCreate") == "arn:aws:kms:k",
    )
    c2: dict = {}
    mod2 = _load(lambda: _make_session(c2))
    r2 = _run(mod2, trace_id="aa", no_writeback=False, retention_days=0)
    check(
        "--retention-days 0: leaves the account default, and says so",
        "retention" not in c2 and r2.get("resultsRetentionDaysOnCreate") == "account default",
    )


def test_existing_group_is_left_alone():
    c: dict = {}
    mod = _load(lambda: _make_session(c, group_exists=True))
    r = _run(mod, trace_id="aa", no_writeback=False, kms_key_id="arn:aws:kms:k")
    check(
        "pre-existing group: retention/key untouched, write still counted",
        "created" not in c and "retention" not in c and r.get("persistedTraces") == 1,
    )


def test_unset_retention_is_never_silent():
    c: dict = {}
    mod = _load(lambda: _make_session(c, retention_raises="AccessDeniedException"))
    r = _run(mod, trace_id="aa", no_writeback=False)
    check(
        "retention denied: write succeeds but the receipt warns about account-default retention",
        r.get("persistedTraces") == 1
        and any("could not set 30-day retention" in n for n in r.get("notes", [])),
    )


def test_provisioning_transport_error_does_not_escape():
    """_provision_group runs inside _write_back's `except ClientError`, so a BotoCoreError from a
    create call would bypass _write_back's own BotoCoreError handler and crash a run whose score
    already succeeded. The receipt must come back with the score and a note instead."""
    c: dict = {}
    mod = _load(lambda: _make_session(c))
    logs = mod.boto3.Session(region_name="us-east-1").client("logs")

    def boom(**k):
        raise _BotoCoreError()

    logs.create_log_group = boom
    outcome, _ = mod._write_back(logs, "svc", [{"a": 1}], 0, retention_days=30)
    check(
        "provisioning BotoCoreError: reported, not raised",
        isinstance(outcome, str) and "could not persist" in outcome,
    )


def test_invalid_retention_fails_before_creating_anything():
    c: dict = {}
    mod = _load(lambda: _make_session(c))
    r = _run(mod, trace_id="aa", no_writeback=False, retention_days=45)
    check(
        "invalid --retention-days: refused up front, nothing created",
        "error" in r and "created" not in c,
    )


def main():
    for fn in [
        test_single_trace_back_compat,
        test_matrix_fetch_once,
        test_ground_truth_gating,
        test_caps,
        test_evaluate_call_budget,
        test_pairs_scored_excludes_errors,
        test_traces_scored_honesty_under_budget,
        test_session_dedup,
        test_real_error_propagated,
        test_explanation_withheld_from_receipt_by_default,
        test_writeback_still_persists_explanation_without_the_flag,
        test_created_group_is_bounded_and_can_use_a_cmk,
        test_existing_group_is_left_alone,
        test_unset_retention_is_never_silent,
        test_provisioning_transport_error_does_not_escape,
        test_invalid_retention_fails_before_creating_anything,
    ]:
        fn()
    passed = sum(1 for _, ok in RESULTS if ok)
    print("\n%d/%d passed" % (passed, len(RESULTS)))
    sys.exit(0 if passed == len(RESULTS) else 1)


if __name__ == "__main__":
    main()
