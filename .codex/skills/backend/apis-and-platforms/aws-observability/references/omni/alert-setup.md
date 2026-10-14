# CloudWatch Omni Alerts

Reference for **CloudWatch Omni alerts** — what they are, how they are evaluated,
and the API operations that manage them.

CloudWatch Omni alerts and CloudWatch alarms are **completely separate entities** —
an Omni alert is its own resource type, with its own configuration and its own API.

Alert operations are signed with the SigV4 signing name **`cloudwatch`**.

---

## The alert API is real — but confirm Omni is enabled before acting

CloudWatch Omni alerts are a **real, first-class API surface**, distinct from
classic CloudWatch metric/composite/anomaly alarms. For an **informational** question
(what a field is, whether an operation exists, what the API supports), answer from the
facts below with confidence — do not tell the user the API "does not exist", and do not
stall with a clarifying question such as "what is your `profileId`?"; explain the field
and that it is caller-supplied.

Before you **create, update, or delete** an alert, confirm the account is on Omni:
the Omni alert API is only usable once a **Space exists in the target Region**. Probe
first — `aws cloudwatch-omni list-spaces` (and `list-domains`) in that Region:

- **A Space exists →** proceed with the Omni alert API below; `profileId` is a required
  input on `CreateAlert` with no service default — gather it first (per point 4).
- **No Space / Omni not enabled →** the Omni alert API is not reachable for this account.
  Say so plainly and use the classic CloudWatch alarm path instead — read
  [`../alarms.md`](../alarms.md). That is the correct fallback, not a wrong answer.

1. **The alert API is real and first-class.** Six operations manage alerts:
   `CreateAlert`, `GetAlert`, `ListAlerts`, `UpdateAlert`, `DeleteAlert`, and
   `ListAlertContributors`. They are **not** classic CloudWatch alarms — an Omni
   alert is its own resource type with its own configuration and API. Every
   operation is **space-scoped**: `spaceId` is required on all of them, so there is
   **no account-wide list of alerts** — you list per space.
2. **The four alert states are `OK`, `WARNING`, `CRITICAL`, and `NODATA`.** `OK` =
   the query ran and did not breach; `WARNING` = breaching the warning threshold;
   `CRITICAL` = breaching the critical threshold; `NODATA` = the evaluation produced
   no data (subject to the rule's no-data treatment).
3. **`ListAlerts` vs `GetAlert` return different things.** `ListAlerts` returns
   `AlertSummary` items — identity and current status only (`name`, `alertId`,
   `spaceId`, `state`, `createdAt`, `updatedAt`, `alertArn`) — and **deliberately
   does not carry the rule or its configuration** (no threshold, query expression,
   cadence, recipients, or notification flag). Call **`GetAlert`** (per alert) to
   read the full rule: the query, condition and thresholds, cadence, notification
   configuration, and no-data treatment.
   `ListAlerts` is paginated — follow `nextToken`.
4. **`CreateAlert` takes a `profileId`, and it is required.** It is the access
   profile the alert runs under; the service does **not** pick a default. The profile
   grants the alert access to (a) run its query and fetch results, and (b) reach any
   notification target that is an Omni integration (such as Slack). It needs an
   `ALERT`-principal grant, plus grants for the data the query reads and for any
   referenced integration.
5. **Alert ARN, mute-vs-delete, notification targets/triggers, query languages:**
   - **ARN:** `arn:<partition>:cloudwatch:<region>:<account-id>:alert/<alertId>`.
     The resource id is the immutable `alertId`; the **`spaceId` is not in the ARN**,
     and neither is the name.
   - **Mute vs delete:** to stop notifications while keeping the alert, use
     `UpdateAlert` with `notificationsEnabled=false` — **do not** delete it and
     **do not** raise the threshold out of reach.
   - **Notification targets:** the only target types are **`sns` and `slack`**,
     addressed by ARN. **PagerDuty is not a supported target.**
   - **Notification triggers:** `trigger.stateValues` lists the states that fire a
     rule (OR-combined); empty/omitted means **any** state. Add `OK` for a recovery
     notification.
   - **Query languages:** both **`SQL`** (the Omni SQL dialect) and **`PROMQL`** are
     accepted for alert rule queries. PromQL is **not** rejected for alerts, and the
     query is **not** a classic CloudWatch metric-math or Logs Insights query.

---

## Summary

### What an alert is

An alert **runs one query on a fixed schedule and compares the result against a
threshold**, reporting a state. That is the whole concept: a query, a condition, a
cadence, what to do when there is no data, and optionally where to send a
notification.

An alert has two identifiers:

- **`alertId`** — a UUID with its hyphens removed, so 32 lowercase hex characters.
  It is assigned when the alert is created and is **immutable**. It is the alert's
  identity: it is the ARN's resource id and what you pass to `GetAlert`,
  `UpdateAlert`, and `DeleteAlert`. It carries no name, so renaming an alert never
  changes its identity or breaks ARNs, saved links, or IAM policies pointing at it.
- **`name`** — a display label, 1–256 characters, charset `[a-zA-Z0-9_.@~()-]` (no
  spaces). It is **mutable** — `UpdateAlert` can rename an alert at any time — and
  it is **not unique** within a space. Because it is neither unique nor stable, it
  is **not** how an alert is addressed: two alerts can share a name, so resolve a
  name to an `alertId` before acting on it.

### ARN format

An alert's ARN uses the `cloudwatch` vendor namespace with an `alert/` resource
type, and the resource id is the bare `alertId`:

```
arn:<partition>:cloudwatch:<region>:<account-id>:alert/<alertId>
```

For example:

```
arn:aws:cloudwatch:us-east-1:123456789012:alert/6c8971b543d54148a26fc793f46db68c
```

Two things to note about the shape: the **`spaceId` does not appear in the ARN**,
and neither does the alert's name — the resource id is only the immutable
`alertId`. That is deliberate, so that renaming an alert or reorganizing spaces
never changes its ARN and never breaks IAM policies or saved links that point at
it. `CreateAlert` returns this ARN as `alertArn`, and `Alert`/`AlertSummary` both
carry it.

### Ownership: alerts belong to an Omni Space

Every alert is **owned at the Omni Space level**. `spaceId` is a required parameter
on every alert operation, including the reads — there is no account-wide alert list,
only per-space ones. An alert also carries the `accountId` that owns it.

Each alert additionally references a **`profileId`** — the access profile the alert
runs under. **A `profileId` must be provided when creating an alert.** The profile
is used for two things:

1. **Running the query.** It grants the alert access to execute its query and fetch
   the query's results.
2. **Reaching an Omni integration.** It grants the alert access to any notification
   rule target that is an Omni integration — Slack, for example.

For the alert to work, the profile therefore needs the right grants for how the
alert is configured:

- An access grant allowing the **`ALERT` principal** to assume the profile.
- Grants allowing access to **the data the alert's query reads**.
- Grants allowing access to **any Omni integration referenced in the alert's
  `notificationRules`**.

### Query languages

An alert's rule carries a query **expression** plus the **language** it is written
in (`rule.telemetryRule.query`, up to 10,000 characters). Both languages are
accepted:

- **`SQL`** — the CloudWatch Omni SQL dialect over the Omni telemetry data sets:
  `logs.default`, `traces.default`, `metrics.default`, and views. Use it for log
  and trace conditions, and for gauge-style metric conditions. For the dialect
  itself — table addressing, `` `@timestamp` `` bounds, `date_bin`, JSON field
  extraction — see [log-trace-query.md](log-trace-query.md).
- **`PROMQL`** — PromQL over metrics, for metric-shaped conditions including
  histogram percentiles via `histogram_quantile`.

Pick the language that fits the signal and set `language` to match the expression;
it is not inferred from the query text.

The alert supplies **no evaluation window of its own**, so the query is expected to
carry its own time bound (a `` `@timestamp` `` `BETWEEN` bound in SQL, a range
selector like `[5m]` in PromQL). The query should also **not** contain the
threshold comparison — the threshold is a separate field on the condition, so a
comparison baked into the expression is applied twice and cannot be retuned.

### How an alert is evaluated

Each evaluation runs the query and compares the result against the condition's
thresholds. **`thresholdMode` decides what is compared**, and the two modes behave
very differently:

**`FIELD_VALUE` — compare a value per returned row, producing contributors.**

The alert evaluates **each row the query returns**. For each row it reads the
column named by **`thresholdField`** and compares that value against the threshold.

Because a row-per-entity query yields a value per entity, this mode produces
**contributors**. A contributor is a sub-entity of the alert representing the state
of one specific row. For example: a query returning the CPU utilization of every
instance in a fleet returns one row per instance; each instance's CPU value is
compared against the threshold, and **each instance/row that breaches becomes a
contributor**. An alert tracks up to **100** contributors, readable via
`ListAlertContributors`. Only breaching contributors are tracked — a contributor's
state is always `WARNING` or `CRITICAL`, never `OK` and never `NODATA`.

**`COUNT_OF_RESULTS` — compare the number of rows.**

The measure is simply the **count of rows the query returned**, compared against the
threshold. No column is read, so `thresholdField` does not apply. Note that a
`LIMIT` in the query caps the row count and therefore caps the measure.

**The condition** (`AlertCondition`) carries the comparison itself:

| Field | Meaning |
|---|---|
| `thresholdMode` | `FIELD_VALUE` or `COUNT_OF_RESULTS` (above) |
| `thresholdField` | The column whose value is compared, ≤256 chars. `FIELD_VALUE` only |
| `comparator` | `GT`, `LT`, `GTE`, or `LTE` |
| `warningThreshold` | Double — the value at which the alert enters `WARNING` |
| `criticalThreshold` | Double — the value at which the alert enters `CRITICAL` |

Both thresholds are optional and independent; supplying only `criticalThreshold`
gives a single-tier alert. Keep them ordered so `CRITICAL` is the more severe.

**The cadence** (`AlertEvaluation`):

| Field | Meaning |
|---|---|
| `intervalSeconds` | **Required.** How often the alert evaluates. One of `30`, `60`, `120`, `300`, `600`, `900`, `1800`, `3600` — nothing else is accepted |
| `pendingDurationSeconds` | How long a breach must persist before the alert fires. Must be a multiple of `intervalSeconds`; defaults to `0` |
| `recoveryDurationSeconds` | How long a recovery must persist before the alert clears. Must be a multiple of `intervalSeconds`; defaults to `0` |

A non-zero `pendingDurationSeconds` is what stops a single spike from firing the
alert; `recoveryDurationSeconds` is the equivalent damping on the way back to `OK`.

### Alert state

An alert's state has four possible values:

| State | Meaning |
|---|---|
| `OK` | The alert is within its normal threshold — the query ran and did not breach |
| `WARNING` | The alert is breaching its **warning** threshold |
| `CRITICAL` | The alert is breaching its **critical** threshold |
| `NODATA` | The evaluation produced no data, subject to the rule's no-data treatment |

State is read-only and system-managed, returned as `AlertStateInfo`:

- **`value`** — the current state from the table above.
- **`transitionedAt`** — when the alert last moved into that state.
- **`contributorSummary`** — `warningCount` and `criticalCount`, the number of
  contributors currently breaching each tier. Present only once contributor-level
  tracking is active.
- **`data`** (`AlertStateData`) — structured detail on the current evaluation:
  `thresholdBreached` (the row count that breached, for `COUNT_OF_RESULTS` alerts;
  null for `FIELD_VALUE`), `contributors` (the breaching contributors backing the
  state, possibly truncated), and `truncatedContributorCount`.

### No-data treatment

`rule.telemetryRule.noData.treatAs` decides **which state an evaluation that
produced no data reports**. It takes any alert state — `OK`, `WARNING`,
`CRITICAL`, or `NODATA` — and **defaults to `NODATA`** when omitted.

This matters because "no rows" is not always a problem. A query counting errors
returns nothing when the service is healthy, so leaving `treatAs` at `NODATA` makes
every quiet interval look like a data outage; `OK` is usually the intent there.
Conversely, for a heartbeat-style query where silence means the thing being watched
has stopped, `CRITICAL` is the meaningful treatment.

### Notification rules

An alert may carry **`notificationRules`** — **1 to 5** rules. Notifications are
optional: an alert with none is valid and simply reports state. The whole list is
gated by **`notificationsEnabled`** (defaults to `true`), which is the switch to
mute an alert without changing what it watches or deleting it.

Each rule pairs a **trigger** with a **target**:

- **`trigger.stateValues`** — the alert states that fire this rule, OR-combined.
  Empty or omitted means **any** state. Firing states are `WARNING` and `CRITICAL`;
  include `OK` for a recovery notification, or `NODATA` to be told when the query
  goes silent.
- **`target`** — where the notification goes:
  - **`type`** — the target type: **`sns` or `slack`**.
  - **`arn`** — the target's ARN, 1–1024 characters. An SNS topic ARN, or the ARN
    of the account's connected Slack integration.
  - **`metadata`** — up to 20 target-specific key/value pairs (keys ≤128 chars,
    values ≤1024), carrying details such as Slack channel routing.

For SNS delivery, the topic's own resource policy must allow the
`cloudwatch.amazonaws.com` principal to call `sns:Publish`; that is the customer's
to configure and is not validated when the alert is created, so it is the first
thing to check when an alert fires but no message arrives. Slack must be connected
as an integration in the console before its ARN exists.

### Tags

An alert can be tagged at create time via **`CreateAlert.tags`**, a key/value map.
Keys are 1–128 characters and values 0–256 characters (an empty value is allowed).
As with any AWS resource, the `aws:` key prefix is reserved. `UpdateAlert` does not
carry tags, so tags are set at create time.

---

## APIs

Six operations manage alerts. All of them are **space-scoped** — `spaceId` is
required on every one — and all can return `ValidationException`,
`AccessDeniedException`, `InternalServiceException`, and `ThrottlingException` in
addition to the per-operation errors noted below.

### CreateAlert

Creates a new alert in a space. Returns **`alertArn`** only — to read the created
alert back, including its `alertId` and live state, call `GetAlert`.

| Input | Required | Notes |
|---|---|---|
| `spaceId` | ✔ | The space to create the alert in |
| `profileId` | ✔ | The access profile the alert evaluates its query with. Caller-supplied; the service does not pick one |
| `name` | ✔ | Display name, 1–256 chars, `[a-zA-Z0-9_.@~()-]`. Not unique, not the identity |
| `rule` | ✔ | The evaluation rule — `rule.telemetryRule` with `query`, `condition`, `evaluation`, `noData` |
| `description` | | ≤1024 chars |
| `notificationsEnabled` | | Defaults to `true` |
| `notificationRules` | | 1–5 rules |
| `tags` | | Key/value map |

`rule` is the substance of the call, and `rule.telemetryRule` is the rule type an
alert uses. On create, all four of its blocks — `query`, `condition`, `evaluation`,
and `noData` — are expected to be present; they are individually optional only so
that `UpdateAlert` can change one block on its own.

Errors beyond the common set: `QuotaExceededException` (the space's alert limit),
`ResourceNotFoundException` (unknown space or profile), `ConflictException`.

### GetAlert

Retrieves a **single alert in full** by `alertId`. This is the only way to read an
alert's rule — the query expression it evaluates, its condition and thresholds, its
cadence, and its no-data treatment — none of which appear in list results.

| Input | Required |
|---|---|
| `spaceId` | ✔ |
| `alertId` | ✔ |

Returns the full `Alert`: `name`, `alertId`, `description`, `accountId`, `spaceId`,
`profileId`, `rule`, `notificationsEnabled`, `state` (`AlertStateInfo`),
`notificationRules`, `createdAt`, `updatedAt`, and `alertArn`. Read-only. Returns
`ResourceNotFoundException` when the alert does not exist.

### ListAlerts

Enumerates alerts in a space, with **server-side filtering, sorting, and
pagination**.

**Read the summaries from `items`.** That is the field guaranteed to be present;
the response also carries an `alerts` field holding the same list, but it is
optional and may be absent, so an agent that reads `alerts` can find nothing and
wrongly report that the space has no alerts.

Each entry is an `AlertSummary` — `name`, `alertId`, `spaceId`, `profileId`,
`notificationsEnabled`, `state`, `createdAt`, `updatedAt`, `alertArn`. A summary
deliberately **does not carry the rule**, so it cannot answer "what is this alert's
threshold or query" — use `GetAlert` for that.

| Input | Notes |
|---|---|
| `spaceId` | Required |
| `filterCriteria` | `AlertFilterCriteria`, below |
| `sortBy` | `NAME` or `STATE` |
| `sortOrder` | `ASC` or `DESC` |
| `maxResults` | 1–100 per page |
| `nextToken` | Pagination token |

`AlertFilterCriteria` members combine with AND, except that the three name/id
filters are **mutually exclusive — at most one may be provided**, and the service
rejects more than one:

- **`names`** — up to 50 exact names, OR-combined. Because names are not unique,
  one name can match several alerts; this is the usual way to resolve a name to an
  `alertId`.
- **`namePrefix`** — a single prefix, ≤256 chars.
- **`ids`** — up to 50 exact `alertId`s, OR-combined.
- **`stateValue`** — any of `OK`/`WARNING`/`CRITICAL`/`NODATA`, OR-combined. This
  is how "what is firing right now" is answered.
- **`notificationsEnabled`** — filter by whether notifications are on.

Results are paginated: follow `nextToken` rather than treating the first page as the
complete set.

### UpdateAlert

Modifies an existing alert in place, addressed by `alertId`. Returns an **empty
response** — read the alert back with `GetAlert` to confirm the new configuration.

| Input | Required | Notes |
|---|---|---|
| `spaceId` | ✔ | |
| `alertId` | ✔ | The alert to update |
| `name` | | **Renaming is supported.** The `alertId` does not change |
| `description` | | |
| `profileId` | | The access profile can be changed |
| `rule` | | Send only the sub-blocks that change |
| `notificationsEnabled` | | The mute/unmute switch |
| `notificationRules` | | **Full replace** — see below |

Two semantics matter here:

- **Most fields are PATCH (apply-if-present).** Only non-null fields overwrite
  existing values; an omitted field is left unchanged. This extends into `rule` —
  `telemetryRule`'s members are optional precisely so a single sub-block (just the
  condition, say) can be sent on its own.
- **`notificationRules` is the exception: present, it replaces the entire list.**
  It does not merge. To add one target, send every rule the alert should end up
  with, not just the new one. Omitting the field leaves existing rules unchanged.

`@idempotent`. Errors beyond the common set: `ResourceNotFoundException`,
`ConflictException`.

**Confirm before updating.** `UpdateAlert` mutates live alerting configuration.
Draft the exact change, state which fields it will overwrite (and that
`notificationRules` replaces the whole list), and confirm with the user before
calling.

### DeleteAlert

Permanently removes an alert by `alertId`. Returns an empty response.

| Input | Required |
|---|---|
| `spaceId` | ✔ |
| `alertId` | ✔ |

**Idempotent** — deleting an alert that has already been removed succeeds without
error, so a successful response does not prove the alert existed beforehand.
Deletion removes the alert along with its rule and its notification rules, and it
cannot be undone. To stop an alert notifying while keeping it, use `UpdateAlert`
with `notificationsEnabled=false` instead.

**Confirm before deleting.** This is a destructive, irreversible write against live
alerting. Name the specific alert (id and name) and confirm with the user before
calling `DeleteAlert` — never delete on inference. Because the call is idempotent, a
success does not tell you whether you deleted the alert you meant, so confirm the
target up front rather than checking after.

### ListAlertContributors

Returns **per-contributor state and values** for a multi-contributor alert — the
breakdown behind a `FIELD_VALUE` alert (see
[How an alert is evaluated](#how-an-alert-is-evaluated)). This answers "which
specific hosts / rows are breaching?".

| Input | Notes |
|---|---|
| `spaceId` | Required |
| `alertId` | Required — the alert whose contributors to list |
| `filterCriteria` | `ContributorFilter` — `stateValue`, one of `WARNING` or `CRITICAL` |
| `maxResults` | 1–100 per page |
| `nextToken` | Pagination token |

Each `AlertContributor` carries:

- **`contributorId`** — the contributor's id, 1–256 chars. For a SQL alert this is
  already the human-readable `GROUP BY` value.
- **`state`** — `WARNING` or `CRITICAL`. **Only threshold-breaching contributors
  are tracked, so `OK` contributors are never returned** — which is also why
  `ContributorFilter.stateValue` only accepts those two values.
- **`value`** — the contributor's most recent evaluated value.
- **`labels`** — the PromQL label set for display, as a name→value map (keys 1–256
  chars, values ≤1024). **Null for SQL alerts**, whose `contributorId` is already
  readable.
- **`transitionedAt`** — when the contributor last moved into its current state.
- **`updatedAt`** — when the contributor record was last changed by anything.

An alert currently tracks at most **100** contributors. The operation is paginated
so that cap can be raised later without a breaking change, so follow `nextToken`
rather than assuming one page holds them all. Read-only.
