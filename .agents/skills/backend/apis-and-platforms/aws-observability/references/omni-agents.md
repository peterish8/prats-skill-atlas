# CloudWatch Omni: Agent Datasets & Evaluation

> **Tool capability:** Optional — the AWS CLI (`aws___call_aws`) for the AgentCore Evaluations control/data planes (datasets, evaluators, and on-demand / online evaluation). For cloud telemetry queries, use the dedicated query reference [`omni/log-trace-query.md`](omni/log-trace-query.md) for logs and traces; metrics run as native PromQL (see the metric-panel examples in [`omni/dashboard.md`](omni/dashboard.md)).

Use when the user asks to:

- "Create a dataset from traces" / "Run an evaluation"
- "Score/evaluate these traces" / "How helpful was my agent on this trace/session?" (on-demand)
- "Set up online / continuous evaluation" / "monitor my deployed agent's quality"
- "What evaluators are available?"
- "Is my agent's instrumentation healthy / are traces flowing end-to-end?" (audit)

---

## Operating Contract

Before any action that **scores, creates, edits, or deletes**, confirm the specifics with the user first. This contract governs every step below, even where a step does not restate it:

- **The evaluator set is the user's choice, never yours.** If the user names no evaluator ("evaluate these traces", "check my agent"), recommend the one or two that fit and **ask which to run — then STOP** and wait. Never default to "all evaluators" or silently pick one.
- **Never skip data-source verification when creating an online-eval config.** Run the `@logGroupName` query first — a user naming a log group is **not** permission to skip it. If the group isn't confirmed, do **not** create: report what you found and wait.
- **Writes are real** (create/update/delete of datasets, evaluators, online-eval configs; running evaluations costs quota). Draft → confirm the specifics → then call, and report the returned id. Never claim a resource was created without the API returning its id.
- An override ("just do it", "I don't need you checking") only counts when it comes **after** you have reported the concern — never inferred from the original request.

## Instrumentation health audit

Use when the user asks whether an agent's instrumentation is healthy or traces are flowing end-to-end. This is a **query-based** check over the agent's own telemetry in `traces.default` (a bounded `@timestamp` window; see [`omni/log-trace-query.md`](omni/log-trace-query.md) for the dialect) — it verifies the telemetry that actually reached CloudWatch Omni, **not** the OTel SDK/collector/runtime *setup* (that belongs to the onboarding/instrumentation skill).

Staged, over a bounded window (start ~1 hour, widen if the agent is idle):

1. **Are spans arriving?** Filter by the agent's `service.name` (and `aws.service.type = 'gen_ai_agent'`); check span/trace counts and a recent `MAX(@timestamp)` (last_seen). No rows → nothing is reaching Omni — an upstream instrumentation gap, not something to fix here.
2. **Is the trace continuous?** Confirm agent / LLM / tool spans are present and linked within a trace (parent/child), not orphaned single spans.
3. **Is telemetry quality good?** Confirm the expected GenAI attributes are populated — model, token counts, and input/output — not just bare spans. Missing/empty attributes mean the agent emits spans but not usable agent-observability data.

Report what the queries showed. If spans are absent or attributes empty, say it's an upstream instrumentation gap to fix in the agent's OTel/ADOT setup (see the onboarding skill), not something to change here.

## Datasets & Evaluation

Everything in this section is driven by the **AWS CLI** (`aws___call_aws`) against two AgentCore services — no dedicated MCP tool is required:

- **`bedrock-agentcore-control`** (control plane) — datasets, evaluators, and online-evaluation configs.
- **`bedrock-agentcore`** (data plane) — on-demand `evaluate`.

**Prerequisites (every path):** the agent must be emitting telemetry with **CloudWatch Transaction Search enabled**, and there is a 2–5 min ingestion lag before a fresh session is evaluable. **Custom** evaluators that invoke Bedrock need `bedrock:InvokeModel` on the caller (on-demand) or on the execution role (online); built-in evaluators do not — the service invokes the judge model itself. All of these resources are Region-scoped — they appear only in the Region they were created in.

**These steps perform real writes** (create a dataset, create/update/delete an online-eval config). You are **not done until the API call actually returns the resource id** — make the call and report it (the `datasetId` / `onlineEvaluationConfigId`). Never describe a resource as created or configured from local files/prep alone unless the create call returned one.

### Step A — Discover evaluators first

Never hardcode evaluator ids; list them:

```
aws___call_aws → aws bedrock-agentcore-control list-evaluators
```

Each summary carries `evaluatorId`, `evaluatorName`, `evaluatorType` (`Builtin` | `Custom` | `CustomCode`), `level` (`TRACE` | `TOOL_CALL` | `SESSION`), and `description` — enough to choose. Call `get-evaluator --evaluator-id <id>` when you need more detail (the rating scale under `evaluatorConfig`, or a custom evaluator's judge model). Note the detail response does **not** carry machine-readable input-requirement flags — judge an evaluator's ground-truth needs from its identity and description (see the ground-truth check below).

**Use only the ids `list-evaluators` returns — never assume an id scheme and never hardcode a set.** The catalog varies by account and Region and changes over time, so a name baked into this doc goes stale. Current accounts expose `Builtin.<Name>` (e.g. `Builtin.Helpfulness`, `Builtin.ToolSelectionAccuracy`) and third-party evaluators namespaced `ThirdParty.<Provider>.<Name>` (e.g. `ThirdParty.DeepEval.ToolUse`), plus any custom evaluators created in the account — but treat the live list as the only source of truth. An id you did not see in this account's list output may not exist here; do not recommend or run it.

**Listed ≠ invocable.** If `evaluate` rejects an id that `list-evaluators` returned (e.g. `ValidationException: Unknown evaluator`), treat it as a service-side issue, offer a different evaluator, and never self-assign a score to compensate.

**Before recommending an evaluator for on-demand scoring, check whether it needs ground truth.** There is no machine-readable requirement flag — decide from the evaluator's identity and description. A live trace carries **no ground truth**, so an evaluator that needs an expected value cannot score it on-demand:

- **Ground-truth-required (on-demand: no) — the trajectory matchers** `Builtin.TrajectoryExactOrderMatch`, `Builtin.TrajectoryInOrderMatch`, `Builtin.TrajectoryAnyOrderMatch` compare the actual tool sequence against an **expected** trajectory. They only work against a dataset whose examples carry `expected_trajectory` (Step B) — never on a raw trace.
- **Ground-truth-free (on-demand: yes)** — response-quality/safety judges (`Builtin.Helpfulness`, `Builtin.Coherence`, `Builtin.Faithfulness`, and the like) and the tool judges `Builtin.ToolSelectionAccuracy` / `Builtin.ToolParameterAccuracy` score a trace on its own merits. **For "does my agent pick the right tools?" use `Builtin.ToolSelectionAccuracy`, not a trajectory matcher.** `Builtin.Correctness` and `Builtin.GoalSuccessRate` also run without ground truth (they can optionally use it, but do not require it).

When a user's question maps only to a ground-truth-required evaluator, say the raw-trace path can't supply the expected values and offer the dataset path (Step B) instead of substituting an evaluator that doesn't answer their question.

**Level decides what gets scored** — `TRACE` (whole request/response), `TOOL_CALL` (individual tool invocations; needs tool spans), `SESSION` (whole conversation). Every evaluator in one call shares one level.

**The evaluator set is the user's choice — never yours.** If the user named the evaluators or a clear dimension ("score for correctness", "helpfulness and goal success"), use exactly those and run. If they did NOT ("evaluate these traces", "check my agent"), list the available evaluators, recommend the one or two that fit the trace and their question, and **ask which to run — then STOP** and wait for their answer. Never default to "all evaluators" or substitute one you think is close: scoring runs cost quota and money, and an unrequested evaluator produces a number the user did not ask for. If the id they gave is not an exact match to a `list-evaluators` id (a typo, different casing, or an encoded/escaped string), surface the id you resolved it to and confirm before scoring — never silently substitute one.

### Step A2 — Author a custom evaluator (only when no built-in fits)

Built-ins are referenced, never created. Author a **custom** evaluator only when the user wants something the built-in set does not score — either an **LLM-as-judge** (a judge model plus scoring instructions and a rating scale) or a **code-based** one (`CustomCode`). All three operations are CLI calls: `create-evaluator`, `update-evaluator`, `delete-evaluator`.

**These are writes — draft with the user, then confirm.** Gather what it should score, the `level` (`TRACE` / `TOOL_CALL` / `SESSION` — a **response-quality** dimension such as brand voice, tone, or conciseness is judged at `TRACE` level), and, for an LLM judge, the judge model, the scoring instructions, and the scale. **Present the draft back before creating** — its name, what it judges, the level, the judge model, and the rubric — and create only after the user confirms *that specific draft*. Never invent the rubric, and never treat a "yes" from an earlier turn as approval of a rubric the user has not seen. A delete is destructive and a change alters what every future run is judged on, so confirm those too.

- **Read the exact `evaluatorConfig` shape from the CLI's own model — do not guess it.** `aws bedrock-agentcore-control create-evaluator help` gives the required fields, types, and nesting (`llmAsAJudge` vs `codeBased`; the judge model under `modelConfig.bedrockEvaluatorModelConfig`; the `ratingScale`). If a create still fails validation, the error carries the input schema — correct against it.
- On `update-evaluator`, resend the **FULL** evaluator config; fields you omit revert.
- The name must match `[a-zA-Z][a-zA-Z0-9_]{0,47}` (start with a letter; letters, digits, underscores; no hyphens; ≤48 chars) and must not collide with a built-in name.
- `description` is a short **label** for the listing (≤200 chars) and is **not** read by the judge — only `instructions` is. Keep it to one crisp sentence; put the rubric in `instructions`.
- Creation is asynchronous (`CREATING → ACTIVE`, terminal `CREATE_FAILED`) and Region-scoped — wait for `ACTIVE` before scoring with it, and keep the judge model in the same Region.
- While an online-evaluation config that uses a custom evaluator is ENABLED, that evaluator is locked — disable the config before editing or deleting it.

**Judge model (LLM-as-judge).** `evaluatorConfig.llmAsAJudge.modelConfig.bedrockEvaluatorModelConfig.modelId` must be a foundation model available in the Region — don't guess it. Discover it and fold a recommended model into the draft you present rather than asking as a separate step:

- Inference profiles (prefer these): `aws bedrock list-inference-profiles --type-equals SYSTEM_DEFINED` → `us.` / `global.`-prefixed ids, the form these judges use.
- On-demand text models: `aws bedrock list-foundation-models --by-inference-type ON_DEMAND --by-output-modality TEXT`.

**Instructions must embed a placeholder valid for the level.** A create with none, or with an unrecognized token, is rejected — a content rule the schema does not express. Use **single** curly braces (`{context}`); `{{context}}` and `${...}` / `%s` forms are rejected.

| `level` | Allowed placeholders (embed at least one, as `{token}`) |
|---|---|
| `TRACE` | `context`, `assistant_turn`, `expected_response`, `system_instructions` |
| `TOOL_CALL` | `context`, `available_tools`, `tool_turn`, `user_message`, `system_instructions`, `available_skills`, `invoked_skill`, `skill_content` |
| `SESSION` | `context`, `available_tools`, `actual_tool_trajectory`, `expected_tool_trajectory`, `assertions` |

`{context}` is valid at every level, so it is the safe default; add the level-specific tokens the rubric actually judges (e.g. `{assistant_turn}` for TRACE response quality, `{actual_tool_trajectory}` for SESSION tool use). Example TRACE instruction: `"Evaluate the assistant's response for conciseness.\n\nConversation:\n{context}\n\nResponse:\n{assistant_turn}\n\nScore 1-5, where 5 = tight and precise and 1 = excessively verbose."` If a create is rejected for placeholders, its validation error enumerates the allowed set for that level — follow that, and re-check single braces.

### Datasets (optional; for repeatable / regression evaluation)

For all dataset operations — creating, editing examples, publishing versions, and building datasets from traces — see [`omni-agents-dataset-from-traces.md`](omni-agents-dataset-from-traces.md).

### Step C — On-demand (sync) evaluation — score specific traces now

Best when the user has a specific session/trace and wants a score now — **no dataset and no online config are required**, so this is the answer to "score this one trace without setting up a whole pipeline." **You MUST run the real evaluator — never judge quality yourself.** Reading a trace and assigning a number is wrong: the score has to come from the AgentCore `evaluate` API (service `bedrock-agentcore`, data plane), not from you.

**Use the bundled helper on the AgentCore raw-spans path — do not hand-build an evaluation request.** The helper (below) calls `bedrock-agentcore evaluate` on the trace's raw session spans. Do **not** instead call the CloudWatch Omni frontend's `Evaluate` (the `cloudwatch-omni` service) or assemble `structuredInput` (input / output / toolCalls extracted from spans) by hand: that is a different API on a different shape, and hand-extracting the pieces from spans is precisely the slow, error-prone work the helper exists to replace. If you catch yourself writing code to pull messages/tool-calls out of spans, stop and use the helper.

`evaluate` needs the trace's spans in an unforgiving shape — the **full raw `@message` OTLP span documents** (not flattened Logs Insights rows), one session per call, and **each span's `kind` coerced to a bare OTel string** (`SERVER`/`INTERNAL`, never a number or null) or it fails with `ValidationException: Failed to parse span data`. **Do not hand-shape spans in the conversation** — reshaping raw OTLP turn-by-turn is exactly where a one-shot flow thrashes (reshape → ValidationException → retry → loop). This skill **bundles a tested helper** that does resolve-session → fetch raw spans → normalize `kind` → call `evaluate` deterministically:

1. **Pick the evaluator** (Step A) — e.g. `Builtin.Helpfulness` (TRACE level). A raw trace has no ground truth, so pick a ground-truth-free evaluator (see Step A's ground-truth check); ground-truth evaluators belong to dataset-based evaluation (Step B).
2. **Retrieve and run the bundled helper** `scripts/evaluate_traces.py` (this skill's supplementary file — fetch it, then run it with your shell):
   ```
   # one trace, one evaluator
   python evaluate_traces.py --trace-id <traceId> --evaluator-id Builtin.Helpfulness \
     --level TRACE --region <region>
   # many traces and/or many evaluators — ONE run, each trace fetched once, every
   # (trace, evaluator) pair scored:
   python evaluate_traces.py --trace-ids <id1>,<id2>,… \
     --evaluator-ids Builtin.Helpfulness,Builtin.ToolSelectionAccuracy --level TRACE --region <region>
   ```
   It accepts one or many trace ids (`--trace-id` / `--trace-ids`) and one or many evaluator ids (`--evaluator-id` / `--evaluator-ids`), auto-resolves each trace's session (`--session-id` pins it for a single trace), fetches every session's raw spans from `aws/spans` **once** (`--log-group` to override), normalizes every span's `kind`, scores each (trace, evaluator) pair via `evaluate` (level → target: TRACE → `traceIds`; TOOL_CALL → `spanIds`; SESSION → no target), and prints a compact JSON **receipt** — a per-(trace, evaluator) `results` matrix (`traceId` / `evaluatorId` / `value` / `label` / `hasExplanation`, plus `errorCode` if the evaluator returned one) with a small rollup. Raw spans never enter the conversation.
3. **Report the receipt** — carry `value` / `label`, and the `explanation` as the "why." You are **not done** until the helper prints a `results` array (or an error).

**Pass `--include-explanations` whenever you are going to report the "why."** The explanation is the judge's prose and it quotes the agent's own inputs and outputs, so the helper withholds it by default and returns `hasExplanation: true` instead — that keeps potentially customer-sensitive trace content out of the conversation on the runs that only need a score (a gate check, a regression sweep, a rollup). Add the flag on the runs where the explanation is the point: any first-pass diagnosis, the bad-end drill-down below, or an explicit user request for the reasoning. Do not add it to a bulk matrix run you are only going to summarize numerically. The persisted record carries the explanation either way, so a score queried back later still has its "why."

**Scores are persisted so they can be read back later.** `evaluate` returns a score inline but does not store it, so the helper also writes each one back as a `gen_ai.evaluation.result` telemetry record under `/aws/cloudwatch/evaluations/results/<service.name>` — the same shape online evaluation emits. A score therefore outlives this conversation and can be queried later, by a later session or another user, alongside the online results. This is best-effort: the receipt reports `persistedTraces` (how many traces' scores were written) plus the `resultsLogGroupPrefix`, or carries a `notes` entry explaining why a write did not happen (for example the caller has no `logs:PutLogEvents` — the score is still in `results`, it just is not durable). Pass `--no-writeback` when the user does not want scores written into their logs.

**Writeback creates a log group, and what it stores is sensitive.** If
`/aws/cloudwatch/evaluations/results/<service.name>` does not exist, the helper creates it, and its
stored data is billed like any other log data. The records include
`gen_ai.evaluation.explanation`, the judge's prose, which quotes the agent's own inputs and outputs —
so this log group inherits the sensitivity of the conversations being scored, and it is queryable
later by anyone with read access to it. Because of that, a group the helper creates is provisioned
deliberately rather than left on the account defaults:

- **Retention is bounded at 30 days** by default (`--retention-days`, or `0` to leave the account
  default for accounts that manage retention centrally), so scored prompt and completion text is not
  held indefinitely.
- **`--kms-key-id` encrypts the group with a customer-managed key.** Without it the group uses the
  AWS-owned key. The key policy must allow the `logs.<region>.amazonaws.com` service principal to
  use it; if it does not, group creation fails and the helper does **not** silently fall back to an
  unencrypted group.
- **Both apply only to a group the helper creates.** A pre-existing group keeps whatever retention
  and key it already has — those are its owner's to set.

The receipt reports the posture it filed under (`resultsRetentionDaysOnCreate`,
`resultsKmsKeyOnCreate`), and adds a `notes` entry if retention could not be set (which needs
`logs:PutRetentionPolicy`) so an unbounded group never goes unremarked. Name the results log group
to the user before the first writeback, and when the scored conversations are sensitive, recommend
`--kms-key-id` with their own key — the same treatment Dynamic Instrumentation requires for its
snapshot log group. Pass `--no-writeback` to persist nothing at all.

### Reading stored eval scores

Reading stored scores is a **two-part** job: the **query surface** (schema + filters + patterns — what to fetch) and the **reader** (rollup + drill for the WHY — how to report). Every scored result — online, on-demand, or batch — lands as a `logs.default` record; query them, then report per this two-part contract.

#### Query surface — schema & filters

Records live in **`logs.default`** (not `traces.default` — that is the agent's own spans). Identify eval records by the evaluator-name attribute:

```
attributes['gen_ai.evaluation.name'] IS NOT NULL
```

Attribute keys are read **literally** — a shortened or paraphrased path (e.g. `attributes['score.value']` for `attributes['gen_ai.evaluation.score.value']`) does not error; it silently returns NULL for every row. Use these paths verbatim:

| Field | What it is |
|---|---|
| `attributes['gen_ai.evaluation.name']` | The identifier the score is filed under — filter/group on this attribute. For built-in evaluators this is the display name (e.g. `Builtin.Helpfulness`, where id and name coincide). For **custom** evaluators, on-demand records written by `evaluate_traces.py` carry the server-minted `evaluatorId` here (not the human-readable name), so resolve the id from `list-evaluators` before filtering |
| `attributes['gen_ai.evaluation.score.value']` | Numeric score, **string-typed** — `CAST(... AS DOUBLE)` before aggregation. **NULL for a categorical evaluator**; **empty and non-numeric on a failed job** (see the `error.type` gate below) |
| `attributes['gen_ai.evaluation.score.label']` | Human-readable label. A **categorical** evaluator has ONLY this. Empty on a failed job |
| `attributes['gen_ai.evaluation.explanation']` | The evaluator's rationale (the "why"). Empty on a failed job |
| `attributes['session.id']` | The scored session |
| `resource['attributes']['service.name']` | The agent scored. **Online evaluation** records use `'<service>.DEFAULT'`; **on-demand** records written by `evaluate_traces.py` use the raw service name (no `.DEFAULT` suffix). Scope accordingly, or use `LIKE '<service>%'` to match both |
| `attributes['aws.bedrock_agentcore.online_evaluation_config.name']` | Online-eval config that produced the record; **NULL for on-demand** |
| `attributes['aws.bedrock_agentcore.evaluation_level']` | `TRACE` / `TOOL_CALL` / `SESSION` |
| `attributes['gen_ai.evaluation.partial']` | `'true'` when scored on a truncated span set (span fetch hit its row cap); exclude or caveat when aggregating |
| `traceId`, `` `@timestamp` `` | The scored trace and when the score was written. `traceId` is **empty on a failed job** |
| `attributes['error.type']` | Present **only when the eval JOB FAILED**. NULL on success. The failure gate |

**Filter rules:**

- **`error.type IS NULL` is the "job succeeded" gate.** A record with `gen_ai.evaluation.name` present may be a **failed** job (`error.type` set), where `score.value`/`label`/`explanation` are empty and `score.value` is non-numeric. Every score query adds `AND attributes['error.type'] IS NULL`. This also prevents `CAST(<non-numeric> AS DOUBLE)` failures on those failed records (most visibly where the CAST is in a `WHERE` / `ORDER BY` comparison). The bundled `evaluate_traces.py` helper filters failed jobs on the write path so they never persist for on-demand, but **online-evaluation records can still fail server-side and land in `logs.default` with `error.type` set** — keep the gate on every score query rather than assuming the corpus is failure-free.
- **On-demand writeback covers numeric scores only.** `evaluate_traces.py` also skips any successful row whose numeric `value` is `None` (that is, categorical-only scores), so an on-demand categorical result is returned in the receipt but is **not** written back to `logs.default`. Online-evaluation categorical scores are persisted server-side and do land in `logs.default`. When a categorical-label-distribution query returns fewer rows than expected for a service, check whether the missing scores were on-demand categorical runs — those live only in the receipt, not in the corpus.
- **A scored record has a `score.value` OR a `score.label`.** Categorical evaluators have ONLY a label. The valid-result predicate is `error.type IS NULL AND (score.value IS NOT NULL OR score.label IS NOT NULL)`.
- **Do NOT gate on `score.value IS NOT NULL` alone** — it silently drops every categorical evaluator. Let `error.type IS NULL` do the gating.

**Polarity for filtering — pick the "bad" end.** Don't hardcode one comparison for every evaluator:

- **Higher-is-better is the default** — bad end is `< threshold` (e.g. `< 0.5`).
- **Inverted evaluators flip to the HIGH end** — for **Toxicity, Harmfulness, Bias, Stereotyping, Refusal, PII-leakage** a higher score is worse; bad end is `> threshold`.
- **Categorical evaluators are judged by their LABEL**, never a number.
- The inverted list is a hint, not exhaustive. For an unknown/custom evaluator, judge by its label; **never** assume higher-is-better, and **never** flag "failing" with `score.value = 0` or `score.label LIKE '%fail%'` — evaluators sit on their own scales with no universal pass/fail.

**Query patterns.** All over `FROM "logs.default"` with a bounded `` `@timestamp` `` (relative form `NOW() - INTERVAL 'N HOUR'`; see [`omni/log-trace-query.md`](omni/log-trace-query.md) for the dialect) and, for scored results, `AND attributes['error.type'] IS NULL`. **The defaults below include both online and on-demand records** — on-demand-only reports have to scope explicitly (see "Other scopes" below), or an on-demand quality regression can be masked by a larger online-eval sample scoring well over the same window.

**Average per evaluator** — `CAST` before aggregating, `GROUP BY` the evaluator name. `MIN`/`MAX` give the spread the rollup reports alongside the average (a range needs no dialect-specific `STDDEV`). No `score.value IS NOT NULL` filter — `AVG` skips a categorical NULL and returns `avg_score = NULL` for it (read those by label with the next pattern):

```sql
SELECT attributes['gen_ai.evaluation.name'] AS evaluator,
       AVG(CAST(attributes['gen_ai.evaluation.score.value'] AS DOUBLE)) AS avg_score,
       MIN(CAST(attributes['gen_ai.evaluation.score.value'] AS DOUBLE)) AS min_score,
       MAX(CAST(attributes['gen_ai.evaluation.score.value'] AS DOUBLE)) AS max_score,
       COUNT(*) AS n
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '7 DAY' AND NOW()
  AND attributes['gen_ai.evaluation.name'] IS NOT NULL
  AND attributes['error.type'] IS NULL
  AND resource['attributes']['service.name'] LIKE '<service>%'
GROUP BY evaluator
```

**Categorical label distribution** (for evaluators the average returned with `avg_score = NULL`):

```sql
SELECT attributes['gen_ai.evaluation.name']        AS evaluator,
       attributes['gen_ai.evaluation.score.label'] AS label,
       COUNT(*)                                    AS n
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '7 DAY' AND NOW()
  AND attributes['gen_ai.evaluation.name'] IS NOT NULL
  AND attributes['error.type'] IS NULL
  AND attributes['gen_ai.evaluation.score.value'] IS NULL
  AND resource['attributes']['service.name'] LIKE '<service>%'
GROUP BY evaluator, label
ORDER BY evaluator, n DESC
```

`GROUP BY evaluator, label` — never `GROUP BY label` alone, which mixes distinct evaluators' categories.

**Bad-end + why** (polarity-aware — the example is higher-is-better; for inverted, flip **both** the comparison to `> 0.5` **and** the `ORDER BY` from `ASC` to `DESC` so `LIMIT` returns the actual worst, not the least-bad breachers near the threshold; for categorical, filter `score.label` instead). Scope to specific evaluators with `IN (...)`, one query per polarity — do **not** mix inverted (Toxicity/Harmfulness/…) and higher-is-better evaluators in the same `IN` list, or the single `<` / `>` comparison will surface desired-outcome rows on one side and hide the actual bad-end on the other. Run one query per polarity group; combine categorical evaluators in a separate label-filtered query:

```sql
SELECT attributes['session.id']                    AS session_id,
       attributes['gen_ai.evaluation.name']        AS evaluator,
       attributes['gen_ai.evaluation.score.value'] AS score,
       attributes['gen_ai.evaluation.explanation'] AS why,
       traceId                                     AS trace_id
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '7 DAY' AND NOW()
  AND attributes['gen_ai.evaluation.name'] IS NOT NULL
  AND attributes['error.type'] IS NULL
  AND attributes['gen_ai.evaluation.name'] IN ('<eval1>', '<eval2>')
  AND resource['attributes']['service.name'] LIKE '<service>%'
  AND CAST(attributes['gen_ai.evaluation.score.value'] AS DOUBLE) < 0.5
ORDER BY CAST(attributes['gen_ai.evaluation.score.value'] AS DOUBLE) ASC
LIMIT 50
```

**Failed to run** (run **only** when the ask is about errored evals — `error.type IS NOT NULL`, the inverse of the score gate):

```sql
SELECT attributes['gen_ai.evaluation.name'] AS evaluator,
       attributes['error.type']             AS error_type,
       attributes['error.message']          AS error_message,
       COUNT(*)                             AS n
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '7 DAY' AND NOW()
  AND attributes['gen_ai.evaluation.name'] IS NOT NULL
  AND attributes['error.type'] IS NOT NULL
  AND resource['attributes']['service.name'] LIKE '<service>%'
GROUP BY evaluator, error_type, error_message
ORDER BY n DESC
```

Other scopes: **one session** → `AND attributes['session.id'] = '<sid>'`. **One trace** → `AND traceId = '<traceId>'`. **Online only** → `attributes['aws.bedrock_agentcore.online_evaluation_config.name'] IS NOT NULL` (or `= '<config_name>'`); **on-demand only** → the same field `IS NULL`.

#### Reader — how to report

Reading is a **two-pass** job: a per-evaluator rollup says *which* evaluators are doing badly; the drill-down says *why*. Do NOT stop at the rollup and do NOT punt the "why" — after the rollup you MUST drill into the worst evaluator(s) yourself.

**First pass — per-evaluator rollup.** Summarize each evaluator on its own — **numerical** evaluators by avg + spread + count, **categorical** evaluators by label distribution + count (they have no numeric score; never report them as scoreless). **Never blend a single number across evaluators** — no overall average, no "pass rate", no "% good"; a 0.8 Helpfulness and a 0.8 Toxicity are opposite outcomes.

Read per polarity — never a blanket "low = bad." `0` can be the DESIRED outcome (e.g. a toxicity or refusal check). Don't rank "worst" by low score alone.

**Second pass — drill into the worst evaluator(s).** Pull `explanation` for the bad-end results (the bad-end query above). Unprompted, drill into the top 2–3 worst evaluators **in total** (not 2–3 per polarity group) — this is a default, not a ceiling; widen if the user asks. **Split those 2–3 across polarity-homogeneous queries** — one query for the higher-is-better ones (single `<` comparison), one for the inverted ones (single `>` comparison + `DESC` order), and, when any picked evaluator is categorical, a separate label-filtered query — per the bad-end template's own polarity rule. Do NOT put mixed-polarity evaluators into one `IN (...)` list, or the single comparison surfaces the wrong end for the odd one out. **The fetched WHY MUST appear in the final answer** — report the shared cause per evaluator with a real example ("Correctness (6 low): mostly missing-context, e.g. *'…'*"), not just "6 scored low." Show one representative bad-end **score** (not a failed job — those have no explanation).

**Execution failures vs. low scores.** A record with `error.type` is a job that errored and produced no score — not a "failing" evaluation. There is no pass/fail and no "pass rate"; scores sit on each evaluator's own scale. Fetch scored results only; query failed-to-run records only when the user explicitly asks — and when any fall in the window, say so ("N scored, **Y failed to run** (`<error.type>`)") rather than silently omitting them.

**If the evaluator can't score the trace, report that — never self-judge.** When the receipt has a top-level `error` (e.g. the `evaluate` call raised) or a `results[].errorCode` (e.g. `AgentSpanMappingException`, `ValidationException: Failed to parse span data`), tell the user the evaluator couldn't score this trace and give the exact error/`errorCode`, then STOP. Do **not** fall back to reading the trace and assigning a number yourself — a self-assigned "helpfulness" score is never an acceptable substitute for the evaluator's, even when the API errors. (If the error looks like an unsupported instrumentation scope or a fixable span issue, you may retry the helper **once**; if it still errors, report the error.)

(First resolve the trace id with a telemetry query if the user named the trace by symptom rather than id.) For many sessions or continuous coverage, use online evaluation (below).

**Volume — the helper batches in one run; don't loop it or hand-roll a scorer.** Pass every trace id and evaluator id to a **single** run (`--trace-ids`, `--evaluator-ids`); it fetches each trace once and scores every (trace, evaluator) pair. It **caps at 10 traces, 5 evaluators, and 50 total pairs per run** (three independent bounds), truncating with a note in the receipt rather than silently — so a request above any bound (e.g. "score these 40 traces for helpfulness and correctness" — over the 10-trace bound, and 80 pairs) is capped: tell the user the count and split the work (narrow the time window, sample fewer traces, or run in batches), rather than removing the cap or writing your own loop/script.

- A handful → just run it.
- Over the cap → say the count first and split into runs the user agrees to.
- Quotas are **100 evaluations/min** and **200,000 input tokens/min** per Region, so a big matrix throttles and takes a while; the helper paces within a run.
- If the cap truncated, an error hit partway, or you scored only a subset, report "scored N of M" and name what was skipped (the receipt's `notes` / `fetchErrors` / `scoreErrors` carry this). Never present a partial pass as if it covered everything.

**Synthesizing multiple results.** A batch run returns one receipt whose `results` is the per-(trace, evaluator) matrix — synthesize from it (and across runs if you had to split), turning it into a finding, not a table dump:

- **Report each evaluator separately — never blend different evaluators into one "overall" score.** They use different rubrics and scales, so averaging across them is meaningless. Give each evaluator its own mean and range, and if a single headline is wanted, name the weakest dimension instead of inventing a combined number.
- Scores are graded, not binary — carry the evaluator's own `explanation` as the "why" behind a 0.67 or a 1.0. Synthesizing a batch is a reporting-the-why run, so pass `--include-explanations`; if you already ran without it and the rows show `hasExplanation: true`, re-run with the flag rather than reporting bare numbers.
- Cluster by shared reason: when several traces score low for the same cause, say that once and name the traces rather than repeating the reasoning per row.
- Surface the outliers and the errored runs specifically — the lowest scores and the failures — not every item.

### Step D — Online (continuous) evaluation — score live traffic over time

Best for **continuously monitoring** a deployed agent — it samples live sessions and scores them, accruing results. All ops on `bedrock-agentcore-control`: `create-online-evaluation-config`, `list-online-evaluation-configs`, `get-online-evaluation-config`, `update-online-evaluation-config`, `delete-online-evaluation-config`.

Gather before creating:
- **One agent per config.** `dataSourceConfig.cloudWatchLogs.serviceNames` is **exactly one** service (`logGroupNames` up to 5). To watch N agents, create N configs — never fold several agents into one.
- **Log group(s) — read them off the agent's own spans; never derive, construct, or guess a name.** The `@logGroupName` column records the log group each span actually landed in:

  ```sql
  SELECT `@logGroupName` AS log_group, COUNT(*) AS spans
  FROM "traces.default"
  WHERE `@timestamp` BETWEEN NOW() - INTERVAL '24 HOUR' AND NOW()
    AND resource['attributes']['service.name'] = '<service>'
    AND resource['attributes']['aws.service.type'] = 'gen_ai_agent'
    AND (scope['name'] IS NULL OR scope['name'] NOT LIKE 'gen_ai.evaluation%')
  GROUP BY `@logGroupName`
  ORDER BY spans DESC
  LIMIT 10
  ```

  (`gen_ai.evaluation%` must be a **prefix** match — evaluation-result records carry a `gen_ai.evaluation` scope with the same `service.name`, so matching only `gen_ai.evaluation.result` lets an evaluation's own output surface as a candidate data source.)

  - Every returned row is a group **proven** to hold this service's spans — the row is the proof, so run no separate span check. Pass each name **verbatim**: never add or remove a leading slash (`aws/spans` is a real group, `/aws/spans` is not). Skip NULL/empty rows.
  - **Pass every returned group**, highest span count first, up to the 5-group cap — a service may legitimately emit to several, and passing only one leaves the rest unevaluated. If more than 5 return, pass the top 5 and say which you dropped.
  - **Show the resolved group(s) with their span counts and get the user's approval before creating.** `service.name` is self-declared by whatever emits the telemetry, so a resolved group is a proposal, not a fact to act on.
  - **Never** resolve from `resource['attributes']['aws.log.group.names']`. It is absent for many agents (it is self-declared by the OTel/ADOT config, so EKS/ECS/other-hosted ones omit it), and where present it names the runtime's `<name>-<id>-DEFAULT` application group — which exists and holds stdout lines but **zero spans**. Creating against it yields a config that goes ACTIVE/ENABLED and scores nothing, silently.
  - **Always run the query before any create — no request waives it.** A user naming a log group is not permission to skip verification and not consent to an unverified create; it is the group you verify.
  - **When the query does not confirm the group** — no rows (widen to 7 days and re-run first), the query errored, or it returned rows and the named group is not among them — **do not create.** Report what the query showed (naming the groups it did return), say the group is unconfirmed and that if it is wrong the config will score nothing without erroring, then stop and let the user decide. An unconfirmed group is not necessarily wrong: online evaluation only scores sessions arriving after it is enabled, so an idle agent is legitimate to configure.
  - **If the user answers that report by telling you to create anyway** ("I don't care", "go ahead"), create it and state in the result that the log group is unverified. That override requires an instruction given **after** you reported the problem — never infer it from the original request.

  **HARD STOP — run the `@logGroupName` query before every create, and never create against an unconfirmed group until the user has been told it is unconfirmed and has answered that you should proceed.** The same applies to an `update` that changes the data source. A misresolved group produces a config that goes ACTIVE/ENABLED and scores nothing, with no error to signal it — the user must hear it from you before the write, not from empty dashboards afterwards.
- **Evaluators (1–10)** — from `list-evaluators`.
- **Sampling percentage (required, 0.01–100)** — there is no server default; 10 is a reasonable start.
- **Execution role ARN (required)** — online eval runs under an IAM role AgentCore assumes to
  read traces, write results, and (for custom evaluators) invoke the judge model. You cannot
  create IAM roles from this skill, so resolve one in this order:
  1. **Reuse an existing role.** Discover candidates with `aws iam list-roles` and offer any
     whose NAME starts with `AgentCoreEvaluationRole` / `AgentCoreEvalRole`, OR whose TRUST
     POLICY PRINCIPAL is `bedrock-agentcore.amazonaws.com`. An account that already runs
     evaluations usually has one — show the matches and let the user pick.
  2. **Else have the user create one** — the AgentCore Evaluations console ("Create and use a
     new service role"), or the AgentCore CLI/SDK (`auto_create_execution_role=True`) — then
     use the returned ARN.

  Do NOT hardcode the role's IAM policy here — it drifts; the console/CLI build the
  authoritative policy on creation. At a glance the role trusts `bedrock-agentcore.amazonaws.com`
  and needs CloudWatch Logs read/write + log-index and (for custom evaluators) Bedrock invoke,
  but confirm the exact current trust + permission policy against the AWS documentation rather
  than reciting a possibly-stale one.
- `enableOnCreate` (required) — `true` scores immediately, `false` creates it paused.

```
aws bedrock-agentcore-control create-online-evaluation-config \
  --online-evaluation-config-name my_agent_helpfulness \
  --rule '{"samplingConfig":{"samplingPercentage":10.0}}' \
  --data-source-config '{"cloudWatchLogs":{"logGroupNames":["<every confirmed @logGroupName, verbatim, highest span count first, max 5 — never a constructed name>"],"serviceNames":["<resolved service.name>"]}}' \
  --evaluators '[{"evaluatorId":"Builtin.Helpfulness"}]' \
  --evaluation-execution-role-arn <execution-role-arn> \
  --enable-on-create
```
The config name uses **underscores, not hyphens**. `status` (ACTIVE / CREATING / …) is the provisioning state; `executionStatus` (ENABLED / DISABLED) is whether it is actively scoring — flip it with `update-online-evaluation-config` (`{"executionStatus":"DISABLED"}`). This sets up and manages scoring; to **report** what it found, query the evaluation-result telemetry, not the config.

### Which path / evaluator, when?

| You want to… | Path | The one move that makes or breaks it |
|---|---|---|
| Score a few specific traces/sessions now, no setup | **On-demand** — `bedrock-agentcore evaluate` (Step C; use `evaluate_traces.py`) | `evaluate` scores the trace's **raw session spans fetched from Logs** — not a flattened query row, not a trace id alone — and each span's `kind` must be a bare OTel string (`SERVER`/`INTERNAL`) or it fails `ValidationException: Failed to parse span data`; the bundled helper normalizes it. No dataset or online config needed. |
| Continuously monitor a live agent's quality | **Online** — `create-online-evaluation-config` (Step D) | Resolve the log group from the agent's own spans via the `@logGroupName` query — **never** from `resource['attributes']['aws.log.group.names']`, or the config goes ACTIVE and silently scores nothing. Show groups + span counts for approval before creating. |
| Reuse traces as a re-runnable regression / golden set | **Dataset** — see [`omni-agents-dataset-from-traces.md`](omni-agents-dataset-from-traces.md) | Build the examples **from the traces** (no server-side "trace → example" op — use `capture_dataset_from_traces.py`), then **publish an immutable version** — a repeatable target evaluates against the version, not the mutable DRAFT. |
| Score a dimension no built-in covers (e.g. brand voice, tone) | **Custom evaluator** — `create-evaluator` (Step A2) | An LLM-as-judge at **`TRACE` level** for response quality; `instructions` must embed a **single-brace** placeholder (`{context}`/`{assistant_turn}`, not `{{context}}`), the judge model must be **discovered** (`list-inference-profiles --type-equals SYSTEM_DEFINED`, prefer `us.`/`global.` ids), and you present the draft for confirmation before creating. |

### After Analysis — Offer Follow-up Actions

```markdown
**What would you like to do next?**
1. **Score these traces now** — run an on-demand evaluation with a chosen evaluator
2. **Monitor continuously** — set up an online evaluation on live traffic
3. **Save as a dataset** — capture these traces as a regression / golden set for reuse
```

Wait for the user to pick an action before proceeding.

