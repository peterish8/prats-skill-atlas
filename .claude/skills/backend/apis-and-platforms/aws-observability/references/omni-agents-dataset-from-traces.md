# Evaluation datasets (create, manage, and build from traces)

A dataset is a versioned collection of schema-typed **examples**. Use this reference to create a dataset, edit its examples, publish a version, and turn traces into examples. All ops on `bedrock-agentcore-control`.

**Writes are real** — creating/extending a dataset costs resources. Confirm with the user before any create or delete, and never act on a non-interactive request without confirmation.

## Dataset operations

| Intent | operation |
|---|---|
| Create (examples required) | `create-dataset` |
| Add / edit / remove examples | `add-dataset-examples` / `update-dataset-examples` / `delete-dataset-examples` |
| Publish an immutable version | `create-dataset-version` |
| Read (to support a write/summary) | `get-dataset`, `list-dataset-examples`, `list-dataset-versions` |
| Edit metadata / delete | `update-dataset` / `delete-dataset` |

## Core model — read before creating

- `schemaType` is chosen at creation and is **immutable**:
  - `AGENTCORE_EVALUATION_PREDEFINED_V1` — author-fixed conversation turns (what trace-derived examples use).
  - `AGENTCORE_EVALUATION_SIMULATED_V1` — an LLM actor drives the conversation from a goal; needs `actor_profile.goal`, so it cannot be derived from a trace.
  - `THIRD_PARTY_EVALUATION_V1` — the shape for datasets carrying third-party / external evaluation-framework examples. You will mostly **encounter** it on a dataset created elsewhere rather than create it here. Read the target dataset's `schemaType` with `get-dataset` before adding examples and build examples in the shape that dataset actually declares — a PREDEFINED-shaped example rejected against a third-party dataset fails the whole batch.
  - This type was renamed from `GENERIC_EVALUATION_PREDEFINED_V1`, and the old name was **removed rather than kept as an alias**: passing it to `create-dataset` now fails, and a dataset created with it earlier cannot be read back until its type is migrated. If `get-dataset` fails on a dataset that predates the rename, that is the cause — the dataset has to be recreated (or its type migrated by the service team), not worked around from here.
- A dataset **cannot be created empty** — `create-dataset` needs a `source`, either `inlineExamples.examples` (1–1000) or an `s3Source.s3Uri` pointing at a JSONL file.
- Writes edit the mutable **DRAFT**; `create-dataset-version` snapshots an immutable numbered version. Evaluations that need a stable target run against a published version.
- A dataset is keyed by **`datasetId`** (the name is a display label, pattern `[a-zA-Z][a-zA-Z0-9_]{0,47}` — use underscores); an example is keyed by its server-minted **`exampleId`** (returned by `add-dataset-examples`, shown by `list-dataset-examples`), **not** its `scenario_id`.
- **Editing or deleting an example keys off `exampleId` — resolve it first.** `update-dataset-examples` and `delete-dataset-examples` take `exampleId`s. A `traceId`, a `scenario_id`, or any id the user pasted is **not** the server-assigned `exampleId` — call `list-dataset-examples` and resolve it to the real `exampleId` before the write. Passing the wrong id deletes or overwrites the wrong example. Each entry in an update MUST carry the `exampleId` it replaces.
- **Validation is all-or-nothing.** Every example is validated against the dataset's `schemaType` before anything lands — one bad example rejects the whole batch (max 1000 examples / 5 MB inline per request). Fix and resubmit; a partial batch never writes.
- Writes accept an optional `clientToken` for idempotency — pass one when retrying a create/add so a retry cannot double-write.
- **`delete-dataset` and `delete-dataset-examples` are destructive and not undoable** — name what will be deleted and get the user's confirmation before calling, and never widen the scope they asked for. `update-dataset` edits metadata only (the name and `schemaType` are immutable).

## Example shapes

PREDEFINED example (the trace-derived shape):
```json
{
  "scenario_id": "checkout_happy_path",
  "turns": [{ "input": "Add the blue mug and check out", "expected_response": "Order placed — #A1B2." }],
  "expected_trajectory": ["search_catalog", "add_to_cart", "place_order"],
  "assertions": ["The order confirmation number is returned"],
  "metadata": { "sourceTraceId": "<traceId>" }
}
```
`scenario_id` + `turns` (each `input` non-empty) are the minimum. Optional ground-truth fields gate which evaluators can score the example: `expected_response` → correctness; `expected_trajectory` (ordered tool names) → tool-trajectory; `assertions` → goal-success. Omit them for ground-truth-free scoring.

SIMULATED example (author-supplied only — an LLM actor drives the turns, so this shape cannot come from a trace); `input`, `actor_profile.goal`, and `actor_profile.context` are required:
```json
{
  "scenario_id": "refund_dispute",
  "input": "I want a refund for an order that already shipped",
  "actor_profile": { "goal": "Get a full refund", "context": "Impatient customer",
                     "traits": { "tone": "frustrated" } },
  "max_turns": 8,
  "assertions": ["The agent explains the return policy"]
}
```

## Create a dataset

```
aws bedrock-agentcore-control create-dataset \
  --dataset-name checkout_regressions \
  --schema-type AGENTCORE_EVALUATION_PREDEFINED_V1 \
  --source '{"inlineExamples":{"examples":[ … ]}}'
```
Returns a `datasetId`; the dataset may be `CREATING` briefly — re-check `get-dataset` until `status` is `ACTIVE`.

## Build a dataset from traces

There is no server-side "trace → example" operation, so this skill **bundles a tested helper** that does the whole fetch → reshape → validate → write. **Do not hand-reshape spans in the conversation** — the one-shot flow is error-prone and bloats context. Use the helper:

1. **Retrieve and run the bundled helper** `scripts/capture_dataset_from_traces.py` (this skill's supplementary file — fetch it, then run it with your shell). It queries each trace's spans from CloudWatch Logs, converts each into a PREDEFINED example (root-span input/output, ordered tool trajectory), validates every example, and writes the batch:
   ```
   python capture_dataset_from_traces.py --mode create \
     --dataset-name checkout_regressions --trace-ids <id1>,<id2>,… --region <region>
   ```
   Append to an existing dataset with `--mode add --dataset-id <id>`. It reads the `aws/spans` log group by default (`--log-group` to override) and prints a compact JSON **receipt** (`datasetId`, `examplesWritten`, any per-trace `conversionErrors`) — raw spans never enter the conversation, and a partial/invalid batch never lands.
2. **Report the receipt** — the returned `datasetId` and counts. You are **not done** until the helper prints a `datasetId`. Relay it honestly: if the receipt lists per-trace `conversionErrors`, say which traces did not become examples rather than reporting only the successes; and when an example is stamped `metadata.partial = true` (its trace's span set was truncated, so the turns/trajectory may be incomplete), tell the user which ones are partial instead of presenting the set as complete.

(First resolve the trace ids with a telemetry query if the user named traces by symptom rather than id.)

## Summarize a dataset

Read with `list-dataset-examples` (paginate with `nextToken`) and report a compact synthesis — the count, the schema type, a few representative scenarios, notable gaps. Do not dump every example into the conversation.

---

## Span → field mapping (reference for the helper / hand-reshaping)

The exact span → `AGENTCORE_EVALUATION_PREDEFINED_V1` mapping the helper implements. Read this only if you need to reshape by hand or extend the mapping.

### Example shape (one per trace)

```json
{
  "scenario_id": "<traceId>",
  "turns": [{ "input": "<user input>", "expected_response": "<agent output>" }],
  "expected_trajectory": ["search_catalog", "add_to_cart", "place_order"],
  "metadata": { "sourceTraceId": "<traceId>", "sessionId": "<sessionId>" }
}
```

### Span → field mapping (do exactly this)

- **Root span** = the span with no `parentSpanId` (fall back to the first span).
- **`turns[0].input`** — first non-empty string, preferring the **root span**, else the **first** span in order; COALESCE these **string-valued** keys: `input.value` → `gen_ai.input_value`.
- **`turns[0].expected_response`** — same COALESCE on output keys, preferring the **root span**, else the **last** span (final answer): `output.value` → `gen_ai.output_value`. **Omit** it entirely if the trace has no output.
- Note: the OTel GenAI `gen_ai.input.messages` / `gen_ai.output.messages` keys are **structured arrays**, not strings, so they are **not** used here (treating them as a string would be dead or inject a raw JSON blob). Frameworks that emit only those message-array keys aren't captured by this string COALESCE — extracting text from the message structure would be a separate enhancement.
- **`expected_trajectory`** — the ordered `tool.name` of the TOOL spans (by start time), with **adjacent duplicates collapsed** (`[a,a,b,a] → [a,b,a]` — a retried tool adds no signal; non-adjacent repeats keep real order). **Omit** if no tools were called.
- **`scenario_id`** — the trace id (stable, unique per batch).
- **`metadata`** — `{ "sourceTraceId": <traceId> }`, plus `"sessionId"` when the spans carry `session.id`. Add `"partial": true` when the trace's spans were truncated (see guardrails).

(`input.value` / `output.value` / `tool.name` are the OpenInference names; `gen_ai.*` are OTel GenAI-semconv fallbacks for frameworks that emit those instead.)

### Validate before writing (all-or-nothing)

The write validates the whole batch server-side and rejects it if any example is invalid,
so validate locally first: each example needs **≥1 turn**, and every `turns[].input` must be
a **non-empty string** (or non-empty object). Drop or repair any trace whose input didn't
extract — don't send a batch that will be rejected wholesale.

### Reference converter (author at runtime — NOT shipped in the skill)

Adapt this; it mirrors the create-dataset flow's converter. It reads spans grouped per
trace and emits a `source.json` ready for `--source file://source.json`.

```python
import json

INPUT_KEYS  = ("input.value", "gen_ai.input_value")   # string-valued only; gen_ai.*.messages are arrays
OUTPUT_KEYS = ("output.value", "gen_ai.output_value")

def attr_text(span, keys):
    attrs = (span or {}).get("attributes") or {}
    for k in keys:
        v = attrs.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None

def scan(spans, keys, reverse=False):
    for s in (reversed(spans) if reverse else spans):
        t = attr_text(s, keys)
        if t:
            return t
    return None

def root(spans):
    return next((s for s in spans if not s.get("parentSpanId")), spans[0] if spans else None)

def collapse_adjacent(items):
    out = []
    for i in items:
        if not out or out[-1] != i:
            out.append(i)
    return out

def to_example(trace_id, session_id, spans, tool_names, partial=False):
    r = root(spans)
    turn = {"input": attr_text(r, INPUT_KEYS) or scan(spans, INPUT_KEYS) or ""}
    out = attr_text(r, OUTPUT_KEYS) or scan(spans, OUTPUT_KEYS, reverse=True)
    if out:
        turn["expected_response"] = out
    md = {"sourceTraceId": trace_id}
    if session_id:
        md["sessionId"] = session_id
    if partial:
        md["partial"] = True
    ex = {"scenario_id": trace_id or "", "turns": [turn], "metadata": md}
    traj = collapse_adjacent(tool_names or [])
    if traj:
        ex["expected_trajectory"] = traj
    return ex

def invalid(ex):  # returns an error string, or None if valid
    turns = ex.get("turns")
    if not isinstance(turns, list) or not turns:
        return "no turns"
    for i, t in enumerate(turns):
        v = t.get("input")
        if isinstance(v, str) and v.strip():
            continue
        if isinstance(v, dict) and v:
            continue
        return f"turn {i + 1} missing non-empty input"
    return None

# Build `traces` from the dumped Logs Insights results, grouped by trace id. The
# converter assumes each trace's inputs are prepared as:
#   traces = {trace_id: {"session_id": ..., "spans": [...], "tool_names": [...], "partial": bool}}
# where, per trace:
#   - "spans": ALL of that trace's spans, SORTED BY START TIME (the root-first / last-output
#     COALESCE and the trajectory order both rely on ascending start-time order).
#   - "tool_names": the `attributes.tool.name` of the TOOL-kind spans only (span kind =
#     attributes.openinference.span.kind == "TOOL", or attributes.aws.genai.span_kind == "TOOL"),
#     in that same start-time order. collapse_adjacent() then removes consecutive repeats.
#   - "partial": True if the trace's span fetch was truncated (hit a page/row cap).
examples = [to_example(tid, t["session_id"], t["spans"], t["tool_names"], t.get("partial"))
            for tid, t in traces.items()]
examples = [e for e in examples if invalid(e) is None]   # keep only schema-valid
json.dump({"inlineExamples": {"examples": examples}}, open("source.json", "w"))
# aws bedrock-agentcore-control create-dataset --dataset-name <name> \
#   --schema-type AGENTCORE_EVALUATION_PREDEFINED_V1 --source file://source.json
```

### Orchestration guardrails (match the bespoke tool's behavior)

- **Dedupe** trace ids; fetch each trace's spans once.
- **Cap the batch** — the create/add API takes up to 1000 inline examples / 5 MB per request; keep one capture reasonable (~25 traces) and split beyond that, telling the user rather than silently dropping.
- **Flag partial traces per-trace (not batch-wide)** — with a `sort traceId asc … | limit N` fetch, a row-cap hit only cuts the **boundary** trace (the last one returned) mid-way; every lower-sorted trace is complete. Set `metadata.partial = true` on the boundary trace **alone**, not on the whole batch. Requested traces that sort **after** the boundary were never reached — report them as a distinct "row cap reached before this trace; not fetched" error (re-run with fewer ids / a narrower window), **not** as "no spans found."
- **create vs add** — `create-dataset` needs a new `--dataset-name`; `add-dataset-examples` needs the existing `--dataset-id` (or resolve a name → id via `list-datasets`).
- **Confirm before mutating** — creating/extending a dataset is a write: confirm with the user first, and never do it on a non-interactive / automated request without confirmation (the bespoke tool refuses outright there).
- **Report a receipt, not the data** — after writing, report the dataset id, example count, and any per-trace conversion errors; do not echo the example JSON or raw spans back into the conversation.
