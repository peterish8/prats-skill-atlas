#!/usr/bin/env python3
"""Score CloudWatch agent traces on demand with AgentCore evaluators.

Bundled skill helper (retrieved via the skill's supplementary-file mechanism and run
with the agent's shell) for Section 5, Step C "on-demand (sync) evaluation". Given one or
more trace ids and one or more evaluator ids, it resolves each trace's session, fetches
that session's RAW `@message` OTLP spans from CloudWatch Logs, reshapes them into the exact
`sessionSpans` shape the scoring API needs (the fragile part — every span's `kind` is
coerced to a bare OTel string, since `bedrock-agentcore evaluate` rejects numeric/prefixed/
null kinds with `ValidationException: Failed to parse span data`), and scores every
(trace, evaluator) pair — fetching each unique trace ONCE, then reusing its spans across
every evaluator. It prints a compact JSON receipt (per-pair score / label / errorCode, and the
judge's explanation only when asked for it). Raw spans never leave this process (kept out of the
model's context).

Scoring goes through the AgentCore data plane (`bedrock-agentcore evaluate`) on RAW session
spans. Do NOT hand-extract input/output/toolCalls or call any other Evaluate API
(e.g. the CloudWatch Omni frontend's `structuredInput` Evaluate) — that manual reshaping is
exactly the error-prone work this helper exists to replace.

Doing the span-shaping in code is deliberate: hand-shaping raw OTLP spans turn-by-turn is
the step an agent thrashes on (reshape → ValidationException → retry → loop). This makes
the sync path deterministic. Batch is fetch-once/score-many so scoring N traces against M
evaluators is N fetches + N×M scores, never N×M fetches.

Each score is also written back as a `gen_ai.evaluation.result` telemetry record (the same
shape online evaluation emits, minus the online-config attribute) so it is queryable later
instead of living only in this conversation. That step is best-effort — it never fails the
run, and it is skipped silently when the caller lacks logs write permission. Pass
`--no-writeback` to turn it off.

SENSITIVE DATA: an evaluator's `explanation` is the judge's prose, and it quotes the agent's own
inputs and outputs. Two paths carry it, with different defaults:

  * The RECEIPT (stdout, so it reaches the calling agent's context, transcript and client logs)
    omits it unless `--include-explanations` is passed; by default each row reports only
    `hasExplanation`, so the caller knows one exists and can ask for it. Scores, labels and
    error codes are always returned.
  * The WRITEBACK record persists it as `gen_ai.evaluation.explanation` — that is the point of
    the record (a score without its "why" is not much use when read back later). So when this
    run CREATES the results log group it provisions it deliberately: `--retention-days`
    (DEFAULT_RESULTS_RETENTION_DAYS; 0 leaves the account default) bounds how long they live, and
    `--kms-key-id` encrypts the group with a customer-managed key instead of the AWS-owned
    default. Both apply ONLY to a group this run creates — a pre-existing group keeps whatever
    retention and key it already has, which are the owner's to set. If retention cannot be set
    the receipt says so in `notes` rather than leaving an unbounded group unremarked. Pass
    `--no-writeback` to persist nothing at all.

Requires boto3 + caller AWS credentials with CloudWatch Logs read + bedrock-agentcore
(data plane) evaluate; the writeback additionally uses logs:PutLogEvents (and
logs:CreateLogGroup / logs:CreateLogStream / logs:PutRetentionPolicy the first time). A
`--kms-key-id` key policy must let the `logs.<region>.amazonaws.com` service principal use the
key, or group creation fails (the run does NOT fall back to an unencrypted group).

Examples:
  # one trace, one evaluator
  python evaluate_traces.py --trace-id 6a82... --evaluator-id Builtin.Helpfulness
  # a sample of traces × two evaluators (matrix; each trace fetched once)
  python evaluate_traces.py --trace-ids 6a82...,7b91...,8c03... \
      --evaluator-ids Builtin.Helpfulness,Builtin.ToolSelectionAccuracy --level TOOL_CALL
  python evaluate_traces.py --trace-id 6a82... --include-explanations  # return the "why" too
  python evaluate_traces.py --trace-id 6a82... --no-writeback   # score only, don't persist
  # persist under a customer-managed key with 90-day retention
  python evaluate_traces.py --trace-id 6a82... --kms-key-id arn:aws:kms:... --retention-days 90
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from typing import NoReturn

import boto3
from botocore.exceptions import BotoCoreError, ClientError

SPANS_LOG_GROUP = "aws/spans"
EVALUATE_SERVICE = "bedrock-agentcore"  # data plane hosts `evaluate`
DEFAULT_EVALUATOR = "Builtin.Helpfulness"
LEVELS = ("TRACE", "TOOL_CALL", "SESSION")
# Batch bounds (match the on-demand evaluate-traces tool: 10 traces / 5 evaluators / 50 pairs).
# All THREE apply independently and are enforced by TRUNCATING with a note in the receipt — never a
# silent cap. `traces × evaluators` fans out into one evaluate call per pair, so a big matrix would
# throttle and blow the timeout.
MAX_TRACES = 10  # unique traces fetched per run
MAX_EVALUATORS = 5  # distinct evaluators per run
MAX_PAIRS = 50  # total (trace, evaluator) PAIRS per run
# Hard ceiling on ac.evaluate() calls per run. TRACE/SESSION issue 1 call per pair (so MAX_PAIRS
# bounds them), but TOOL_CALL chunks tool spans into ≤MAX_TARGET_IDS-id calls, so one pair can be
# many calls — this bounds the total fan-out (throttle/timeout guard) regardless of level.
MAX_EVALUATE_CALLS = 100
# Evaluators that require ground truth (an expected tool trajectory) and so CANNOT score a raw
# trace: this helper sends `sessionSpans` only, no `evaluationReferenceInputs`, so they would
# error or score nothing. The evaluator APIs expose NO machine-readable requirement flag
# (get-evaluator returns only id/name/description/evaluatorConfig/level/status), so this list is
# maintained by hand — the trajectory matchers are the built-ins that compare against an
# expected sequence. Do NOT "helpfully" delete it as a hardcoded catalog: there is no flag to
# read instead. Correctness / GoalSuccessRate are deliberately absent — they can optionally use
# ground truth but run without it, so on-demand scoring of a raw trace is valid for them.
_GROUND_TRUTH_REQUIRED = frozenset(
    {
        "Builtin.TrajectoryExactOrderMatch",
        "Builtin.TrajectoryInOrderMatch",
        "Builtin.TrajectoryAnyOrderMatch",
    }
)
# On-demand `evaluate` returns the score inline but does NOT persist it, so a score would be
# lost the moment the conversation ends. Write each one back as a telemetry record — same
# `gen_ai.evaluation.result` shape online evaluation emits — so scores can be queried later
# (by a later session or another user) alongside the online ones.
EVAL_RESULTS_LOG_GROUP_PREFIX = "/aws/cloudwatch/evaluations/results/"
EVAL_RESULTS_LOG_STREAM = "on-demand"
EVAL_RESULT_RECORD_NAME = "gen_ai.evaluation.result"
# The persisted record carries the judge's explanation (which quotes agent input/output), so a
# group this run creates gets a BOUNDED retention rather than inheriting the account default —
# which can be "never expire". Overridable per run; 0 opts out for accounts that manage retention
# centrally. Only ever applied to a group this run creates.
DEFAULT_RESULTS_RETENTION_DAYS = 30
# The only retentionInDays values CloudWatch Logs accepts. Validated up front so a bad value fails
# the run instead of failing put_retention_policy AFTER the group was created — which would leave
# exactly the unbounded group the default exists to avoid.
_RETENTION_DAYS_ALLOWED = frozenset(
    (
        1,
        3,
        5,
        7,
        14,
        30,
        60,
        90,
        120,
        150,
        180,
        365,
        400,
        545,
        731,
        1096,
        1827,
        2192,
        2557,
        2922,
        3288,
        3653,
    )
)
_MAX_LOG_GROUP_LEN = 512
# Log-group names allow [.-_/#A-Za-z0-9]; anything else in a service name is replaced.
_LOG_GROUP_SAFE_RE = re.compile(r"[^A-Za-z0-9_.\-/#]")
# Writeback is a courtesy, not the job: if the caller simply lacks logs write permission,
# skip silently rather than nagging about a permission they may not want to grant.
_ACCESS_DENIED_CODES = frozenset(
    ("AccessDenied", "AccessDeniedException", "UnauthorizedException", "AuthorizationError")
)
# Distinguishes "not written, but nothing worth telling the user about" from a real success,
# so the receipt never claims a score was persisted when it was not.
_WRITEBACK_SKIPPED = object()
# Used for BOTH the log-group segment and the record's service.name when the scored spans
# carry no service name, so the stored record always agrees with where it was filed.
_UNKNOWN_SERVICE = "default"
SPAN_ROW_LIMIT = 1000  # one session's spans; evaluate scores ONE session per call
MAX_TARGET_IDS = 10  # scoring service cap on ids per call (TOOL_CALL chunking)
QUERY_POLL_ATTEMPTS = 150  # × 2s = up to 5 min for a Logs Insights query to complete
_TRACE_ID_RE = re.compile(r"^[0-9a-fA-F]{1,64}$")
# Session ids are alphanumeric + a few separators; validate (reject) rather than mangle,
# so a malformed id never silently rewrites to a DIFFERENT real session's id.
_SESSION_ID_RE = re.compile(r"^[0-9A-Za-z._:\-]{1,128}$")

# OTLP SpanKind enum → bare OTel name. `evaluate` requires `kind` to be a STRING; the
# stored telemetry is polymorphic (some emitters use "SERVER", others the numeric enum,
# some spans omit kind / send null), so coerce every shape to the bare name.
_KIND_BY_NUMBER = {
    0: "UNSPECIFIED",
    1: "INTERNAL",
    2: "SERVER",
    3: "CLIENT",
    4: "PRODUCER",
    5: "CONSUMER",
}
_VALID_KINDS = frozenset(_KIND_BY_NUMBER.values())
_DEFAULT_KIND = "UNSPECIFIED"


def _die(payload) -> NoReturn:
    """Print an error receipt to stdout (so the agent sees it) and exit non-zero."""
    print(json.dumps(payload))
    sys.exit(1)


def _split_ids(*values, lower: bool = False):
    """Flatten comma-separated id args into a de-duplicated, order-preserving list.

    Pass lower=True for trace ids: Logs Insights `filter traceId = ...` is case-sensitive
    and stored values are lowercase hex, so normalise on input. Do NOT pass lower=True for
    evaluator ids — the evaluate API and _GROUND_TRUTH_REQUIRED use the original casing.
    """
    ids = []
    for v in values:
        if v:
            ids += [(x.strip().lower() if lower else x.strip()) for x in v.split(",") if x.strip()]
    return list(dict.fromkeys(ids))


def _normalize_span_kind(value):
    """Coerce a raw span `kind` (numeric enum / SPAN_KIND_* / null / missing) to a bare
    OTel SpanKind string. `bool` is NOT treated as a numeric enum."""
    if isinstance(value, bool):
        return _DEFAULT_KIND
    if isinstance(value, int):
        return _KIND_BY_NUMBER.get(value, _DEFAULT_KIND)
    if isinstance(value, float) and value.is_integer():
        return _KIND_BY_NUMBER.get(int(value), _DEFAULT_KIND)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return _DEFAULT_KIND
        if text.isdecimal():  # NOT isdigit(): "²"/"³" are digits but int() rejects them
            return _KIND_BY_NUMBER.get(int(text), _DEFAULT_KIND)
        upper = text.upper()
        for prefix in ("SPAN_KIND_", "SPANKIND."):
            if upper.startswith(prefix):
                upper = upper[len(prefix) :]
                break
        return upper if upper in _VALID_KINDS else _DEFAULT_KIND
    return _DEFAULT_KIND


def _run_query(logs, log_group, query, window_days, soft=False):
    """Run a Logs Insights query to completion. Returns `(rows, error)`: `(rows, None)` on success.

    soft=True: on a transient failure (API error, or a non-Complete Failed/Cancelled/Timeout
    status) return `(None, message)` — the caller can degrade gracefully (e.g. session resolution
    has a traceId fallback, one trace's fetch fails only its pairs) AND surface the real cause
    instead of a generic message. soft=False aborts via _die with the same message.
    """
    end = int(time.time())
    start = end - window_days * 24 * 3600
    try:
        qid = logs.start_query(
            logGroupName=log_group, startTime=start, endTime=end, queryString=query
        )["queryId"]
        status, result = None, None
        for _ in range(QUERY_POLL_ATTEMPTS):
            time.sleep(2)
            result = logs.get_query_results(queryId=qid)
            status = result.get("status")
            if status in ("Complete", "Failed", "Cancelled", "Timeout"):
                break
    except (BotoCoreError, ClientError) as e:
        msg = "CloudWatch Logs query failed: %s" % e
        if soft:
            return None, msg
        _die({"error": msg})
    if status != "Complete":
        msg = (
            "CloudWatch Logs Insights query did not complete (status=%s); "
            "narrow --window-days to speed it up" % status
        )
        if soft:
            return None, msg
        _die({"error": msg})
    assert result is not None
    return result.get("results", []), None


def _resolve_session_id(logs, log_group, trace_id, window_days):
    """Find the trace's session.id, or None. A transient query failure here is non-fatal —
    the caller falls back to a traceId filter — so this lookup runs in soft mode."""
    rows, _err = _run_query(
        logs,
        log_group,
        "fields `attributes.session.id` | filter traceId = '%s' "
        "and ispresent(`attributes.session.id`) | limit 1" % trace_id,
        window_days,
        soft=True,
    )
    for row in rows or []:
        for f in row:
            if f["field"] == "attributes.session.id" and f["value"]:
                return f["value"]
    return None


def _fetch_raw_spans(logs, log_group, filter_clause, window_days, soft=False):
    """Fetch RAW @message OTLP span docs for the filter; return (spans, truncated, error).

    soft=True returns (None, False, message) on a transient query failure instead of aborting, so
    one trace's failed fetch in a batch fails only its pairs — and the real cause (perms, wrong log
    group, throttling) is surfaced rather than a generic message. On success error is None.
    """
    rows, err = _run_query(
        logs,
        log_group,
        # sort by time so a >cap session truncates deterministically (not an arbitrary subset);
        # fetch one past the cap so an exactly-full (but complete) result isn't mistaken for truncation
        "fields @message | filter %s | sort @timestamp asc | limit %d"
        % (filter_clause, SPAN_ROW_LIMIT + 1),
        window_days,
        soft=soft,
    )
    if rows is None:  # soft-mode query failure — propagate the real error
        return None, False, err
    truncated = len(rows) > SPAN_ROW_LIMIT
    if truncated:
        rows = rows[:SPAN_ROW_LIMIT]  # drop the probe row before building spans
    spans = []
    for row in rows:
        for f in row:
            if f["field"] != "@message":
                continue
            try:
                doc = json.loads(f["value"])
            except (ValueError, TypeError):
                continue
            doc["kind"] = _normalize_span_kind(
                doc.get("kind")
            )  # the fragile step, done deterministically
            spans.append(doc)
    return spans, truncated, None


def _tool_span_ids(spans):
    """Span ids of TOOL spans (for TOOL_CALL level), matching the bespoke tool's detection."""
    ids = []
    for s in spans:
        attrs = s.get("attributes") or {}
        is_tool = (
            attrs.get("openinference.span.kind") == "TOOL"
            or attrs.get("gen_ai.operation.name") == "execute_tool"
        )
        sid = s.get("spanId")
        if is_tool and isinstance(sid, str) and len(sid) == 16:
            ids.append(sid)
    return ids


def _summarize(response, evaluator_id, include_explanations=False):
    """Map a raw evaluate response to compact rows; the raw envelope is NOT returned.

    The explanation is the judge's prose and quotes the agent's own inputs and outputs, so it is
    kept OUT of the caller-facing receipt unless `--include-explanations` asks for it: the receipt
    goes to stdout, which lands in the calling agent's context, its transcript and client logs.
    `hasExplanation` still tells the caller one exists and can be requested, so the score is never
    silently un-explainable.

    The text is retained on the PRIVATE `_explanation` key either way, because the writeback record
    persists it regardless (see _eval_result_records — a stored score without its "why" is little
    use when read back later, and that path is bounded by retention/CMK instead of by omission).
    `_public_rows` strips every private key before the receipt is printed.
    """
    rows = []
    for res in response.get("evaluationResults") or []:
        explanation = str(res.get("explanation") or "")
        clipped = explanation[:600] + ("…" if len(explanation) > 600 else "")
        row = {
            "evaluatorId": res.get("evaluatorId", evaluator_id),
            "value": res.get("value"),
            "label": res.get("label"),
            "_explanation": clipped,
        }
        if include_explanations:
            row["explanation"] = clipped
        else:
            row["hasExplanation"] = bool(explanation)
        if res.get("errorCode"):
            row["errorCode"] = res.get("errorCode")
            if res.get("errorMessage"):
                row["errorMessage"] = str(res.get("errorMessage"))[:600]
        rows.append(row)
    return rows


def _public_rows(rows):
    """Drop private (`_`-prefixed) keys — what the receipt may print, vs. what writeback may read.

    Kept as the LAST step before printing so nothing that only exists for the writeback path can
    reach stdout by accident.
    """
    return [{k: v for k, v in row.items() if not k.startswith("_")} for row in rows]


def _log_group_segment(service):
    """Sanitize a service name into a single log-group path segment."""
    seg = _LOG_GROUP_SAFE_RE.sub("_", (service or "").strip()) or _UNKNOWN_SERVICE
    return seg[: _MAX_LOG_GROUP_LEN - len(EVAL_RESULTS_LOG_GROUP_PREFIX)]


def _service_name(spans, trace_id):
    """The scored trace's `resource.attributes['service.name']` (its own span wins)."""
    fallback = None
    for s in spans:
        name = ((s.get("resource") or {}).get("attributes") or {}).get("service.name")
        if not isinstance(name, str) or not name:
            continue
        if s.get("traceId") == trace_id:
            return name
        fallback = fallback or name
    return fallback


def _eval_result_records(rows, trace_id, session_id, level, service, ts_ms, partial=False):
    """Build one `gen_ai.evaluation.result` record per SCORED row.

    Deliberately omits `aws.bedrock_agentcore.online_evaluation_config.name` — that attribute
    is what marks a result as online, so leaving it out is what identifies these as on-demand.
    The score is written as a STRING for parity with the online records. Rows that carry an
    errorCode are skipped: an error is not a score, and persisting it would pollute later
    aggregates.

    `partial=True` (the span fetch hit its row cap, so the trace was scored on an incomplete
    span set) stamps `gen_ai.evaluation.partial` on the record. The receipt's partial note only
    reaches THIS caller; whoever queries the stored score later never sees it, so without the
    attribute a partial score would read back as a clean, complete one.

    The explanation is read off the private `_explanation` key, NOT the receipt's optional
    `explanation`: whether the caller asked to see the "why" is a separate question from whether
    the stored score should carry it. Reading the public key would mean the persisted corpus
    silently lost every explanation whenever --include-explanations was omitted. This is why the
    log group this run creates is retention-bounded and CMK-capable — see _provision_group.
    """
    records = []
    for row in rows:
        if row.get("errorCode") or row.get("value") is None:
            continue
        attributes = {
            "gen_ai.evaluation.name": row.get("evaluatorId"),
            "gen_ai.evaluation.score.value": str(row.get("value")),
            "aws.bedrock_agentcore.evaluation_level": level,
        }
        if session_id:
            attributes["session.id"] = session_id
        if row.get("label") is not None:
            attributes["gen_ai.evaluation.score.label"] = row.get("label")
        if row.get("_explanation"):
            attributes["gen_ai.evaluation.explanation"] = row.get("_explanation")
        if partial:
            attributes["gen_ai.evaluation.partial"] = "true"
        records.append(
            {
                "name": EVAL_RESULT_RECORD_NAME,
                "traceId": trace_id,
                "attributes": attributes,
                "resource": {"attributes": {"service.name": service}},
                "@timestamp": ts_ms,
            }
        )
    return records


def _err_code(e):
    """The `Error.Code` of a ClientError, or "" when the envelope does not carry one."""
    return (e.response.get("Error") or {}).get("Code") or ""


def _provision_group(logs, group, retention_days, kms_key_id):
    """Create the results log group + stream, retention-bounded and optionally CMK-encrypted.

    Returns `(outcome, warning)`. `outcome` is None when the group and stream are ready,
    `_WRITEBACK_SKIPPED` when the caller cannot create them, or a note string for a real failure —
    the same three-way contract _write_back reports upward.

    `warning` is set when the group was created but its posture is weaker than asked for. That is
    NEVER silent: a group created without the bounded retention keeps the account default, which
    can be "never expire", so the explanations about to be written into it would outlive what the
    caller asked for with nothing in the receipt to say so.

    Retention and the key are applied ONLY to a group this call creates. A pre-existing group is
    left alone — its retention and encryption are its owner's to set, and quietly re-pointing
    someone else's group at our defaults would be the more surprising behavior.

    Every AWS call here catches BotoCoreError as well as ClientError. _write_back calls this from
    INSIDE its own `except ClientError` block, so a transport-level error escaping this function
    would bypass _write_back's BotoCoreError handler entirely and break its "never raises" contract
    — crashing the run after the score already succeeded. They cannot share one except clause
    because the ClientError paths call _err_code(e), and BotoCoreError has no `response`.
    """
    warning = None
    kwargs = {"logGroupName": group}
    if kms_key_id:
        kwargs["kmsKeyId"] = kms_key_id
    try:
        logs.create_log_group(**kwargs)
        created = True
    except BotoCoreError as e:
        return "could not persist the score for later querying: %s" % e, None
    except ClientError as e:
        code = _err_code(e)
        if code in _ACCESS_DENIED_CODES:
            return _WRITEBACK_SKIPPED, None
        if code == "ResourceAlreadyExistsException":
            created = False
        elif kms_key_id and code in ("InvalidParameterException", "ValidationException"):
            # Do NOT retry without the key. The caller explicitly asked for a customer-managed
            # key, so falling back to an AWS-owned-key group would hand them the exact posture
            # they opted out of, and report success while doing it.
            return (
                "could not create %s with kmsKeyId %s (does the key policy allow the CloudWatch "
                "Logs service principal to use it?): %s" % (group, kms_key_id, e)
            ), None
        else:
            return "could not persist the score for later querying: %s" % e, None

    if created and retention_days:
        try:
            logs.put_retention_policy(logGroupName=group, retentionInDays=retention_days)
        except (ClientError, BotoCoreError) as e:
            warning = (
                "created %s but could not set %d-day retention (needs logs:PutRetentionPolicy), "
                "so it keeps the account default retention — which may be 'never expire', and "
                "these records carry the evaluator's explanation: %s" % (group, retention_days, e)
            )

    try:
        logs.create_log_stream(logGroupName=group, logStreamName=EVAL_RESULTS_LOG_STREAM)
    except BotoCoreError as e:
        return "could not persist the score for later querying: %s" % e, warning
    except ClientError as e:
        code = _err_code(e)
        if code in _ACCESS_DENIED_CODES:
            return _WRITEBACK_SKIPPED, warning
        if code != "ResourceAlreadyExistsException":
            return "could not persist the score for later querying: %s" % e, warning
    return None, warning


def _write_back(logs, service, records, ts_ms, retention_days=None, kms_key_id=None):
    """Persist scores to the evaluation-results log group. Best-effort: never raises and never
    fails the run — the score itself already succeeded.

    Returns `(outcome, warning)`. `outcome` is None on a real write, `_WRITEBACK_SKIPPED` when the
    caller simply lacks logs write permission (nothing was written, but that is not worth nagging
    about), or a note string for any other failure — the three are kept distinct so the receipt's
    `persisted` count is honest. `warning` carries a group-provisioning caveat (see
    _provision_group) that must surface even when the write itself succeeded.
    """
    if not records:
        return _WRITEBACK_SKIPPED, None
    group = EVAL_RESULTS_LOG_GROUP_PREFIX + _log_group_segment(service)
    events = [{"timestamp": ts_ms, "message": json.dumps(r, default=str)} for r in records]
    warning = None
    for attempt in (1, 2):  # attempt 2 runs only after creating a missing group/stream
        try:
            logs.put_log_events(
                logGroupName=group, logStreamName=EVAL_RESULTS_LOG_STREAM, logEvents=events
            )
            return None, warning
        except ClientError as e:
            code = _err_code(e)
            if code in _ACCESS_DENIED_CODES:
                # no logs:PutLogEvents — not durable, but not an error
                return _WRITEBACK_SKIPPED, warning
            if code == "ResourceNotFoundException" and attempt == 1:
                outcome, warning = _provision_group(logs, group, retention_days, kms_key_id)
                if outcome is not None:
                    return outcome, warning
                continue
            return "could not persist the score for later querying: %s" % e, warning
        except BotoCoreError as e:
            return "could not persist the score for later querying: %s" % e, warning
    return None, warning


def _fetch_trace(logs, tid, log_group, window_days, session_id=None, span_cache=None):
    """Resolve one trace's session and fetch its RAW spans ONCE (soft: one trace's failure does
    not sink the batch). Returns {traceId, sessionId, spans, truncated} on success, or
    {traceId, error} on any failure.

    `span_cache` (dict, optional) de-duplicates fetches by RESOLVED session id: two requested trace
    ids in the same session fetch that session's spans only once. Keyed by session id (or the trace
    id when no session resolves)."""
    sid = session_id or _resolve_session_id(logs, log_group, tid, window_days)
    # A telemetry-resolved id is untrusted too (a crafted span could carry a bad session.id);
    # if it isn't a clean id, don't interpolate it — fall back to the traceId filter.
    if sid and not _SESSION_ID_RE.match(sid):
        sid = None
    cache_key = sid or ("trace:" + tid)
    if span_cache is not None and cache_key in span_cache:
        spans, truncated = span_cache[cache_key]  # same session already fetched — reuse
    else:
        filter_clause = (
            ("`attributes.session.id` = '%s'" % sid) if sid else ("traceId = '%s'" % tid)
        )
        spans, truncated, err = _fetch_raw_spans(
            logs, log_group, filter_clause, window_days, soft=True
        )
        if spans is None:
            return {"traceId": tid, "error": err or "span fetch query did not complete"}
        if not spans:
            return {"traceId": tid, "error": "no spans found in the last %d day(s)" % window_days}
        if span_cache is not None:
            span_cache[cache_key] = (spans, truncated)
    # If a >cap session was truncated, the target trace's own spans may have been cut, so scoring
    # would misrepresent (or error on) the target — fail this trace loudly instead of scoring a
    # subset. (The traceId-filter fallback can't hit this: it only fetches the target.)
    if sid and truncated and not any(s.get("traceId") == tid for s in spans):
        return {
            "traceId": tid,
            "error": "session has more than %d spans and the target trace was not in the fetched "
            "set; narrow --window-days, or the session is too large to score whole"
            % SPAN_ROW_LIMIT,
        }
    return {"traceId": tid, "sessionId": sid, "spans": spans, "truncated": truncated}


def _score_pair(ac, tid, spans, evaluator_id, level, max_calls, include_explanations=False):
    """Score ONE (trace, evaluator) pair against the AgentCore data plane. `max_calls` caps how many
    ac.evaluate() calls this pair may issue — 1 for TRACE/SESSION, but TOOL_CALL fans tool spans into
    ≤MAX_TARGET_IDS-id calls, so the caller's per-run budget is enforced here. Returns
    (rows, errors, calls_made, note); per-call errors are collected, never raised, so one pair never
    sinks the batch; `note` (or None) flags TOOL_CALL chunk truncation from the budget."""
    evaluation_input = {"sessionSpans": spans}
    # Level → target: TRACE → traceIds; TOOL_CALL → spanIds (chunked ≤10); SESSION → no target.
    calls, note = [], None
    if level == "SESSION":
        calls.append({"evaluatorId": evaluator_id, "evaluationInput": evaluation_input})
    elif level == "TOOL_CALL":
        span_ids = _tool_span_ids(spans)
        if not span_ids:
            return [], ["TOOL_CALL requested but the trace has no tool spans"], 0, None
        for i in range(0, len(span_ids), MAX_TARGET_IDS):
            calls.append(
                {
                    "evaluatorId": evaluator_id,
                    "evaluationInput": evaluation_input,
                    "evaluationTarget": {"spanIds": span_ids[i : i + MAX_TARGET_IDS]},
                }
            )
        if len(calls) > max_calls:
            note = "tool-span scoring truncated to %d of %d chunks (evaluate-call budget)" % (
                max(0, max_calls),
                len(calls),
            )
    else:  # TRACE
        calls.append(
            {
                "evaluatorId": evaluator_id,
                "evaluationInput": evaluation_input,
                "evaluationTarget": {"traceIds": [tid]},
            }
        )
    calls = calls[: max(0, max_calls)]  # never exceed the run's remaining evaluate-call budget

    rows, errors = [], []
    for kwargs in calls:
        try:
            resp = ac.evaluate(**kwargs)
        except (BotoCoreError, ClientError) as e:
            # Don't discard chunks that already scored (TOOL_CALL fans out into ≤10-id calls);
            # collect the error and keep going.
            msg = str(e)
            if "Unknown evaluator" in msg and "provider" in msg:
                # Advertised by list-evaluators/get-evaluator but not invocable by evaluate — a
                # service-side discovery/evaluate mismatch, not a payload problem.
                msg += (
                    " — this evaluator is listed by list-evaluators/get-evaluator but not "
                    "invocable by evaluate (a service-side discovery/evaluate mismatch, not "
                    "a payload problem); pick a different evaluator"
                )
            errors.append("evaluate failed: %s" % msg)
            continue
        resp.pop("ResponseMetadata", None)
        rows.extend(_summarize(resp, evaluator_id, include_explanations))
    return rows, errors, len(calls), note


def _run(args):
    trace_ids = _split_ids(args.trace_ids, args.trace_id, lower=True)
    if not trace_ids:
        _die({"error": "no trace ids given (use --trace-id or --trace-ids)"})
    for t in trace_ids:
        if not _TRACE_ID_RE.match(t):
            _die({"error": "invalid trace id (expected hex): %r" % t})
    evaluator_ids = _split_ids(args.evaluator_ids, args.evaluator_id) or [DEFAULT_EVALUATOR]
    if args.session_id:
        if len(trace_ids) > 1:
            _die(
                {
                    "error": "--session-id applies to a single trace; omit it when scoring multiple traces"
                }
            )
        if not _SESSION_ID_RE.match(args.session_id):
            _die({"error": "invalid session id: %r" % args.session_id})
    # Validated BEFORE any AWS call: an unaccepted value would otherwise only fail at
    # put_retention_policy, i.e. after create_log_group already left an unbounded group behind.
    if args.retention_days and args.retention_days not in _RETENTION_DAYS_ALLOWED:
        _die(
            {
                "error": "invalid --retention-days %r; CloudWatch Logs accepts one of %s (or 0 to "
                "leave the account default)"
                % (args.retention_days, sorted(_RETENTION_DAYS_ALLOWED)),
            }
        )

    notes = []
    # Ground-truth preflight over the WHOLE evaluator set (before any AWS call): this helper sends
    # `sessionSpans` only, no `evaluationReferenceInputs`, so an evaluator that requires an expected
    # trajectory cannot score a raw trace. Drop those (with a note) and score the rest; only refuse
    # the run if that leaves nothing — matching the batch's isolate-don't-sink behavior.
    gt = [e for e in evaluator_ids if e in _GROUND_TRUTH_REQUIRED]
    if gt:
        evaluator_ids = [e for e in evaluator_ids if e not in _GROUND_TRUTH_REQUIRED]
        msg = (
            "evaluator(s) %s require ground truth (an expected tool trajectory), which a raw "
            "trace does not carry — on-demand scoring here supplies no reference inputs. Use "
            "ground-truth-free evaluators (e.g. Builtin.ToolSelectionAccuracy for tool quality), "
            "or evaluate against a dataset whose examples carry the expected trajectory."
            % ", ".join(gt)
        )
        if not evaluator_ids:
            _die({"error": msg, "evaluatorIds": gt})
        notes.append("skipped " + msg)

    # Caps: three independent bounds (mirror the evaluate-traces tool), each truncating with a note,
    # never silently. Evaluators ≤ MAX_EVALUATORS, unique traces ≤ MAX_TRACES, and total pairs ≤
    # MAX_PAIRS (with evaluators already capped, traces are bounded to floor(MAX_PAIRS / n_eval)).
    if len(evaluator_ids) > MAX_EVALUATORS:
        dropped_evals = evaluator_ids[MAX_EVALUATORS:]
        evaluator_ids = evaluator_ids[:MAX_EVALUATORS]
        notes.append(
            "capped to %d evaluators (≤%d-evaluator limit); NOT run: %s"
            % (len(evaluator_ids), MAX_EVALUATORS, ", ".join(dropped_evals))
        )
    n_eval = len(evaluator_ids)
    allowed_traces = min(MAX_TRACES, max(1, MAX_PAIRS // n_eval))
    if len(trace_ids) > allowed_traces:
        dropped = trace_ids[allowed_traces:]
        trace_ids = trace_ids[:allowed_traces]
        notes.append(
            "capped to %d traces (≤%d-trace / ≤%d-pair limit at %d evaluators); NOT scored: %s"
            % (len(trace_ids), MAX_TRACES, MAX_PAIRS, n_eval, ", ".join(dropped))
        )

    session = boto3.Session(region_name=args.region)
    logs = session.client("logs")
    try:
        ac = session.client(EVALUATE_SERVICE)
    except (
        Exception
    ) as e:  # noqa: BLE001 — e.g. UnknownServiceError on a boto3 too old for this service
        _die(
            {
                "error": "could not create a %s client (is boto3 recent enough?): %s"
                % (EVALUATE_SERVICE, e)
            }
        )

    # Fetch spans once per unique trace; span_cache also de-dups by resolved session id, so several
    # requested trace ids in the same session fetch that session's spans only once.
    fetched: dict = {}
    fetch_errors: list = []
    span_cache: dict = {}
    for tid in trace_ids:
        f = _fetch_trace(
            logs,
            tid,
            args.log_group,
            args.window_days,
            session_id=args.session_id if len(trace_ids) == 1 else None,
            span_cache=span_cache,
        )
        if f.get("error"):
            fetch_errors.append({"traceId": tid, "error": f["error"]})
        else:
            fetched[tid] = f

    # Score every (fetched trace, evaluator) pair; persist each trace's scores as we go.
    # calls_budget caps total ac.evaluate() calls across the run (TOOL_CALL fans out per pair).
    results: list = []
    score_errors: list = []
    pairs_scored = 0
    persisted_traces = 0
    calls_budget = MAX_EVALUATE_CALLS
    budget_hit = False
    scored_sessions = set()  # (sessionId, evaluator) already scored at SESSION level — dedup
    ts_ms = int(time.time() * 1000)
    for tid in trace_ids:
        if budget_hit:
            break
        f = fetched.get(tid)
        if not f:
            continue
        trace_rows = []
        for ev in evaluator_ids:
            # SESSION level scores the whole session (no per-trace target), so several trace ids in
            # the same session would otherwise produce duplicate identical scores + double writeback.
            # Score each (session, evaluator) once.
            if args.level == "SESSION" and f["sessionId"]:
                skey = (f["sessionId"], ev)
                if skey in scored_sessions:
                    continue
                scored_sessions.add(skey)
            if calls_budget <= 0:
                notes.append(
                    "evaluate-call budget (%d) reached; remaining (trace, evaluator) pairs "
                    "not scored" % MAX_EVALUATE_CALLS
                )
                budget_hit = True
                break
            rows, errs, made, pair_note = _score_pair(
                ac, tid, f["spans"], ev, args.level, calls_budget, args.include_explanations
            )
            calls_budget -= made
            for r in rows:
                r["traceId"] = tid  # tag so the flat results list is a (trace, evaluator) matrix
            # Count a pair as scored only if it produced a REAL score — a row with a value and no
            # errorCode. An error-only row (evaluate returned an errorCode, value None) is not a score.
            if any(r.get("value") is not None and not r.get("errorCode") for r in rows):
                pairs_scored += 1
            trace_rows.extend(rows)
            for err in errs:
                score_errors.append({"traceId": tid, "evaluatorId": ev, "error": err})
            if pair_note:
                notes.append("trace %s / %s: %s" % (tid, ev, pair_note))
        results.extend(trace_rows)

        if trace_rows and not args.no_writeback:
            # Normalize ONCE so the record's service.name and the log-group segment agree.
            service = _service_name(f["spans"], tid) or _UNKNOWN_SERVICE
            records = _eval_result_records(
                trace_rows, tid, f["sessionId"], args.level, service, ts_ms, partial=f["truncated"]
            )
            if records:
                outcome, warning = _write_back(
                    logs, service, records, ts_ms, args.retention_days, args.kms_key_id
                )
                # Provisioning caveats surface even when the write itself succeeded, and only
                # once per group — the group is created by the first trace that needs it.
                if warning and warning not in notes:
                    notes.append(warning)
                if outcome is None:
                    persisted_traces += 1
                elif outcome is not _WRITEBACK_SKIPPED:
                    notes.append("trace %s: %s" % (tid, outcome))
        if f["truncated"]:
            notes.append(
                "trace %s: span fetch hit the %d-row cap; scored on a partial span set"
                % (tid, SPAN_ROW_LIMIT)
            )

    # Nothing scored at all → fail loudly with whatever went wrong.
    if not results:
        _die(
            {
                "error": "no (trace, evaluator) pair produced a score",
                "level": args.level,
                "evaluators": evaluator_ids,
                "fetchErrors": fetch_errors,
                "scoreErrors": score_errors,
            }
        )

    # tracesScored counts traces that actually produced a real score — NOT len(fetched): the
    # evaluate-call budget can break the loop early, leaving some fetched traces unscored, and
    # counting those would present a partial pass as complete. tracesFetched is reported alongside.
    scored_trace_ids = {
        r["traceId"] for r in results if r.get("value") is not None and not r.get("errorCode")
    }
    receipt = {
        "level": args.level,
        "evaluators": evaluator_ids,
        "tracesFetched": len(fetched),
        "tracesScored": len(scored_trace_ids),
        "pairsScored": pairs_scored,
        # Private keys stripped here, at the boundary: `results` is the only part of the receipt
        # built from evaluator output, and _explanation must not reach stdout unasked.
        "results": _public_rows(results),
    }
    if not args.no_writeback:
        receipt["persistedTraces"] = persisted_traces
        if persisted_traces:
            receipt["resultsLogGroupPrefix"] = EVAL_RESULTS_LOG_GROUP_PREFIX
            # State the posture the records were filed under rather than leaving the caller to
            # infer it — these records carry the evaluator's explanation. "OnCreate" because a
            # pre-existing group keeps its own settings; `notes` says so when one could not be set.
            receipt["resultsRetentionDaysOnCreate"] = args.retention_days or "account default"
            receipt["resultsKmsKeyOnCreate"] = args.kms_key_id or "aws-owned"
    if notes:
        receipt["notes"] = notes
    if fetch_errors:
        receipt["fetchErrors"] = fetch_errors
    if score_errors:
        receipt["scoreErrors"] = score_errors
    print(json.dumps(receipt, default=str, indent=2))


def main():
    ap = argparse.ArgumentParser(
        description="Score CloudWatch traces on demand with AgentCore evaluators."
    )
    ap.add_argument(
        "--trace-id", help="a single trace id to score (or use --trace-ids for a batch)"
    )
    ap.add_argument("--trace-ids", help="comma-separated trace ids to score (each fetched once)")
    ap.add_argument(
        "--session-id",
        help="the trace's session id (single-trace only; resolved automatically if omitted)",
    )
    ap.add_argument("--evaluator-id", help="a single evaluator id, e.g. Builtin.Helpfulness")
    ap.add_argument(
        "--evaluator-ids",
        help="comma-separated evaluator ids; every one is run against every trace",
    )
    ap.add_argument("--level", choices=LEVELS, default="TRACE")
    ap.add_argument(
        "--log-group", default=SPANS_LOG_GROUP, help="span log group (default aws/spans)"
    )
    ap.add_argument("--region", default="us-east-1")
    ap.add_argument("--window-days", type=int, default=30, help="trace lookback window")
    ap.add_argument(
        "--include-explanations",
        action="store_true",
        help="return the evaluator's explanation text in the receipt. Off by default because it "
        "quotes the agent's own inputs and outputs, and the receipt reaches the calling agent's "
        "context and transcript; without it each row reports hasExplanation instead. The "
        "persisted record carries the explanation either way",
    )
    ap.add_argument(
        "--no-writeback",
        action="store_true",
        help="do not persist scores to the evaluation-results log group (persisted by default "
        "so they can be queried later)",
    )
    ap.add_argument(
        "--retention-days",
        type=int,
        default=DEFAULT_RESULTS_RETENTION_DAYS,
        help="retention for the evaluation-results log group when this run CREATES it, bounding "
        "how long the persisted explanations live (default %d, 0 leaves the account default; a "
        "pre-existing group keeps its own)" % DEFAULT_RESULTS_RETENTION_DAYS,
    )
    ap.add_argument(
        "--kms-key-id",
        help="customer-managed KMS key (arn or id) to encrypt the evaluation-results log group "
        "with when this run CREATES it; its key policy must allow the CloudWatch Logs service "
        "principal (default: AWS-owned key)",
    )
    args = ap.parse_args()
    # Guarantee a JSON receipt on ANY unexpected error (never a raw traceback). _die raises
    # SystemExit (a BaseException), so its clean JSON exit is not swallowed by this guard.
    try:
        _run(args)
    except Exception as e:  # noqa: BLE001
        _die({"error": "unexpected error: %s" % e})


if __name__ == "__main__":
    main()
