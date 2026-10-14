# Building a CloudWatch Omni Dashboard

Use this when building a CloudWatch Omni dashboard — "build me a dashboard for
checkout", "show what's most critical for this service", "lay this out", "which
chart for this signal?", or when reading back and explaining a dashboard body.

A CloudWatch Omni dashboard is a set of **panels** laid out on a fixed grid, most
of them charts over CloudWatch Omni queries. The dashboard **body is JSON** — a
`panels[]` array (plus an optional `scope`) that the Omni UI renders. The
deliverable is a valid, grounded body the UI can render.

Two rules hold across every step:

- **Never chart a metric, field, or label you have not confirmed exists.** An
  invented name renders an **empty** panel, which on a saved dashboard reads like
  an outage — worse than no panel. Ground first (Step 2); drop what you cannot
  ground.
- **Query text follows the CloudWatch Omni query dialect.** The SQL rules for logs
  and traces live in [log-trace-query.md](log-trace-query.md). Metrics run as native
  PromQL — select by metric name (use an `{__name__="<exact>"}` matcher for a name
  that starts with a digit or contains `%`, `.`, or spaces; a plain name may be
  bare) scoped by the identity labels shown in Step 2 and the archetype templates
  below. This reference owns the dashboard body — the panel schema, chart choices,
  and grid math.

**ALWAYS STATE — two silent failures a dashboard body never warns you about.**
Neither raises an error; each just quietly does the wrong thing, so call them out
whenever you author, explain, or debug a body:

- **Unknown or misspelled keys are silently dropped.** Any key not in the panel
  schema — including a correctly-placed field whose *name is misspelled* — is
  silently ignored on save; nothing errors, the value just never persists (a field
  you set "doesn't take effect"). Validate every key's spelling against this
  reference (Step 3's schema).
- **`queryLanguage` must be set explicitly per panel; a mismatch fails silently.**
  Set each `explore` panel's `queryLanguage` to `'sql'` or `'promql'` yourself — it
  is **not** inferred from the query text, and a language that doesn't match the
  query is a silent failure, not an error. (Metrics → `promql`; log/trace content →
  `sql`.)

Work the steps in order — each depends on the one before:

1. **Decide what the dashboard shows** — the panels and their order.
2. **Ground every panel query** against real telemetry.
3. **Author the panel bodies** — the JSON schema, panel types, and chart choices.
4. **Lay them out** on the 60-column grid.

---

## Step 1 — Decide what the dashboard shows

Pick the panels, order them into sections, and choose a visualization per signal.

### Start focused — a tight dashboard beats an exhaustive one

- **The default is a FOCUSED ~6–8 panels:** roughly **4 KPI tiles + 2–3
  golden-signal trends + at most one breakdown table.** A single-signal dashboard
  is smaller still (**3–6 panels**). Don't emit dozens of panels for a vague ask.
- **Cap the KPI row at 4 tiles** (`number` panels). Four is also the natural grid
  fit — `15 × 4 = 60` columns — so a fifth tile forces an awkward wrap.
- **Keep it to ~12 panels.** Section dividers, markdown notes, and the title header
  all count, so budget the headers before the data panels.
- **Build the core, then offer depth as a follow-up "add section."** Defer these
  rather than placing them up front: per-service latency, error / status-code
  breakdown, infra / USE health, and log signals. Name the one the user most
  likely wants next instead of pre-building all of them.
- **Saturation is CORE, not deferred.** ALWAYS include one saturation panel —
  backlog / queue depth, consumer lag / liveness, or circuit-open / write-denied —
  in the core WHENEVER the grounded catalog has one; it is what surfaces incident
  visibility. (The broad "infra / USE health" line above stays a deferrable
  follow-up — it is specifically this incident-visibility saturation signal that
  becomes core.)

### Ordering principle — headline first, detail last

Every dashboard reads top-to-bottom as **summary → trend → breakdown → raw**:

1. **KPI row** — a few `number` panels with the headline figures (availability,
   error rate, p99 latency, request rate). The fast "is it healthy?" read.
2. **Trend charts** — `line` / `area` / `bar` time series for the golden signals.
3. **Ranked breakdown** — a `table` (top-N by the primary signal) so the worst
   offenders surface.
4. **Raw / drill-down** — logs, spans, alerts, or an application map. Optional
   depth, offered as a follow-up.

Open a logically distinct group with a `divider`, and open an on-call / incident
dashboard with a short `markdown` runbook panel.

### If the ask names a resource type, start from a template

When the request names a known resource TYPE — a Lambda function, a
Kubernetes/EKS workload, an RDS/database instance, an ECS/web service, or an API
Gateway API — start from that archetype's ready panel set in the **Appendix**,
then ground and lay it out.

### Recipes (for a general intent)

- **Golden-signals service health (the default when the ask is vague).** Use RED
  (rate/errors/duration) for a request-serving service, USE (utilization,
  saturation, errors) for an infrastructure resource. CORE (~6–8): a KPI row
  (availability %, error rate, p99 latency, request rate); a request-rate `line`;
  an errors `bar` (stacked) or `area`; a latency `line` (p50/p90/p99) **when a real
  percentile source exists**; and a top-N `table`. Build each family from the
  service's OWN grounded metric first (Step 2), falling back to a generic OTel
  metric or a span / log derivation only when it doesn't.
- **Errors-focused.** A headline error-rate `number`; a stacked `bar`/`area` of the
  status-code or fault/error breakdown over time; a `table` of top error sources.
  Offer a recent-error log panel and an `alerts` panel as a follow-up.
- **Latency-focused.** A p99 `number`; a `line` of p50/p90/p99 together; a `table`
  of the slowest operations. If the service exposes no percentile-capable source,
  chart the average with an honest title — never a fake p99.
- **Throughput-focused.** A request/message-rate `number`; a `line` over time
  grouped by the identity label — read the aggregation off the counter's
  temporality (`sum_over_time` for a delta Sum, `rate()` / `increase()` for a
  cumulative Sum), not a uniform `rate()`; for a queue, pair inbound vs. outbound
  counters and add the backlog gauges (depth, age).
- **Saturation / capacity.** Utilization gauges (`solidgauge` for a bounded %
  against a threshold, `line` for a trend): CPU, memory, disk/queue depth, credit
  balances; a `table` of the resources closest to their limit. An empty series
  often means "not applicable," not zero.
- **Incident review (a fixed past window).** Open with a `markdown` summary, set a
  **fixed** `scope.timeRange` (absolute start and end) so every panel covers the
  incident, then golden-signal charts plus a `spans` / `trace-details` panel for
  the offending path.
- **Multi-service overview (a fleet or whole space).** One compact row per service
  — a `number` KPI plus a small `line` — under a `divider` per service, or a single
  wide `table` ranking all services by health. Prefer a `table` or `topk(...)` over
  a `line` with more than ~25 series.

One query per `explore` panel. To compare two signals, emit two side-by-side
panels (Step 4), never one overlaid panel. If the intent is genuinely one number, a
single `number` panel is a complete answer — don't pad it.

---

## Step 2 — Ground every panel query

Ground each data panel's query against live telemetry **before** you write the
body. The SQL dialect for logs and traces is deferred to
[log-trace-query.md](log-trace-query.md); the PromQL metric-selector rules you need
are inlined below.

**The grounding loop, per data panel:**

1. **Discover what exists.** Learn which services, accounts, and regions are real;
   follow a service's dependencies to find neighbors worth a panel. Don't guess
   service names.
2. **List the real names.** For each signal a panel will chart, list the actual
   metric / field / label names for that data set and signal kind (LOGS, TRACES,
   METRICS). Use those names **exactly** — don't shorten, alias, pluralize, or
   invent them. Nouns in the request ("throttles", "5xx", "timeouts") describe
   *what to aggregate*, not field names — map them to a real grounded name.
   **Pick the SOURCE per signal by a strict 3-tier priority — reach for a lower
   tier only when no higher tier grounds the signal:** (1) the service's OWN domain
   metric it emits (a business counter / gauge / histogram) FIRST; (2) a generic
   OTel metric (e.g. `Count` / `Errors`) as a fallback; (3) a trace-span / log
   derivation (span `durationNano` percentiles, log counts) LAST.
3. **Pick the surface and set `queryLanguage` to match.** Metrics → **PromQL**; log
   or trace content → **SQL**. Metrics execute as NATIVE PromQL
   (`queryLanguage: "promql"`), NEVER SQL — there is **no** `metrics.default` SQL
   `FROM`; a SQL `FROM` is only `logs.default` / `traces.default`. Set the panel's
   `queryLanguage` explicitly — it is **not** inferred from the query text, and a
   mismatch is a silent failure.
4. **Self-check the draft.** Scan every field / metric / label reference in the
   drafted `queryString` against the grounded lists. If a reference cannot be
   confirmed, re-ground; if a signal has no grounded source on its preferred
   surface, **fall back to another surface (metrics → traces → logs)** before
   giving up, so a metrics-sparse service still yields a full dashboard. Only when
   NO surface grounds the signal, **drop that panel** rather than shipping an
   invented query.

**Bind panels to the grounded metric identity.** Vended AWS metrics carry an
instrumentation scope (`@instrumentation.@name="cloudwatch.aws/<service>"`) plus a
datapoint attribute (e.g. `FunctionName`); OTLP-native signals carry
`@resource.*` labels. Select the metric by name — use an `{__name__="<exact>"}`
matcher for a name that starts with a digit or contains `%`, `.`, or spaces (e.g.
`4xxErrors`, `traces.span.metrics.*`); a plain non-dotted name may be used bare.
A bare Prometheus `job=` / `service=` selector is an ungrounded reference — drop
panels that use one.

**Pick the aggregation from the metric's type.** The grounded metric names carry
each metric's instrument type (Sum / Gauge / Histogram) and temporality (delta /
cumulative); read the aggregation off it — `sum_over_time(<m>[w])` for a DELTA Sum,
`rate()` / `increase()` for a CUMULATIVE Sum, `avg()` / `max()` for a Gauge, and
`histogram_quantile(0.99, rate(<base>[5m]))` for a Histogram (use the BASE metric
name — NO `_bucket`, NO `by (le)`).

**Two grounding cautions:**

- **Keep every panel query WINDOWLESS.** Never embed a time window in the
  `queryString` — no `` `@timestamp` `` bound, no `NOW() - INTERVAL`, no PromQL
  range that pins an absolute time. The panel (or dashboard) `scope` drives the
  time range; a hard-coded window fights the time picker and freezes the panel.
  (This is the one place a dashboard query differs from an interactive one, which
  *requires* a time bound — so don't copy an interactive query verbatim.)
- **An empty series is often correct.** A signal that only exists under a specific
  configuration (an agent installed, request metrics enabled, a burstable
  instance) returns nothing when that condition is absent. Confirm a metric is
  expected to have data before making it a headline panel.

---

## Step 3 — Author the panel bodies

This is the JSON schema the UI persists — the format you hand-edit in the source
editor. Every field here survives save → reopen; anything not in it is dropped on
read.

### Top-level shape

```jsonc
{
  "panels": [ /* Panel[] — required, may be empty */ ],
  "scope": { "timeRange": { "start": "now-3h", "end": "now" } }  // optional
}
```

- **`panels`** is the only required key. Panels sit on a **fixed 60-column grid**;
  the column count is not a field and is not configurable.
- **`scope.timeRange`** is the window the whole dashboard opens under. Omit it to
  inherit whatever range is already active.

> There is no `views`, no `layout: { columns: 60 }`, no per-panel `id`, no
> `refreshInterval`, and no top-level `owner`. Author bodies in the `panels[]` form.

### Panel

```jsonc
{
  "type": "explore",                 // required — selects the panel and its config shape
  "layout": { "x": 0, "y": 0, "w": 30, "h": 320 },  // required (Step 4)
  "title": "Read IOPS",              // optional
  "description": "…",                // optional, one line
  "config": { /* shape depends on type */ },
  "scope": { "timeRange": { "start": "now-7d", "end": "now" } }, // optional per-panel override
  "variant": "transparent"           // optional — drop the card frame (headings, spacers, prose)
}
```

Only `type` and `layout` are required. An untitled panel takes a heading from its
content. `variant` accepts `'transparent'`; `'default'` is an explicit no-op.

### Scope and time range

`scope.timeRange` has the same shape at the dashboard and panel level; a panel's
scope overrides the dashboard's for that panel only (e.g. a 7-day baseline beside a
1-hour detail view).

```jsonc
"timeRange": { "start": "now-1h", "end": "now" }               // rolling window
"timeRange": { "start": "2026-01-01T00:00:00Z", "end": "now" } // growing window (since incident)
"timeRange": { "start": "2026-01-01T00:00:00Z",
               "end":   "2026-02-01T00:00:00Z" }               // fixed window
```

Each bound is independently an ISO-8601 instant, the literal `now`, or a relative
`now-<N><unit>`. Units: `m` minutes, `h` hours, `d` days, `w` weeks, `mo` months.
There is no seconds or years unit and no rounding syntax — use an absolute instant
for a calendar boundary. The scope drives a query's time range; never embed a
window in a `queryString` (Step 2).

### Panel types

`explore` · `markdown` · `divider` · `navigation` · `alerts` · `alert-detail` ·
`application-map` · `spans` · `dashboards-list` · `trace-details`. A type the
product does not recognize renders a placeholder and is preserved on save.

#### explore — charts and query results (the workhorse)

```jsonc
"config": {
  "queryString": "sum by (FunctionName) (rate({__name__=\"Invocations\", \"@instrumentation.@name\"=\"cloudwatch.aws/lambda\"}[5m]))",
  "queryLanguage": "promql",      // 'sql' | 'promql' — SET IT EXPLICITLY; not inferred
  "visualization": "line",         // one of the nine below; default 'table'
  "autoRun": true,                 // run on open — set this on any data panel
  "promqlQueryOptions": { "step": 300 },  // PromQL step in SECONDS (default 60)
  "chartOptions": { /* appearance — see below */ }
}
```

- **Always set `queryLanguage` explicitly** — it is **not** inferred from the query
  text; a mismatch is a silent failure. The telemetry source is the query's `FROM`
  clause (SQL) or metric selector (PromQL); there is no separate source field.
- **Always set `autoRun: true`** on a panel meant to show data without a click —
  otherwise it opens showing its query, not its result.
- **Match `step` to the range vector.** A `[5m]` window sampled at the default 60s
  over-samples 5×; set `promqlQueryOptions.step` to `300` (SECONDS).
- **`inputMode`.** Omit for a chart tile (the default). Set `"inputMode": "editor"`
  **only** when authoring a full Explore-surface panel — that is the one accepted
  value, and it is load-bearing on read (a saved Explore surface with `inputMode`
  dropped reopens as a tile).
- The `@`-labels are double-quoted PromQL selectors, so they are JSON-escaped
  (`\"`) once more inside the `queryString`. Identity as shown in Step 2 and the
  archetype templates below.

#### markdown — formatted text

```jsonc
"config": { "content": "## On call\n\n1. Check error rate.\n2. Open the failing trace." }
```

Pair with `"h": "auto"` and `"variant": "transparent"` for prose that reads as
part of the canvas.

#### divider — collapsible section heading

```jsonc
"config": { "title": "Service health", "collapsed": false }
```

Always full width (`x: 0, w: 60`); give it a small fixed height (`40`). Groups the
panels beneath it, down to the next divider, into a collapsible section.

#### navigation — links to this dashboard's sections

`"config": {}` — no fields. Full width; natural height `28`. Meaningless without
dividers.

#### alerts / alert-detail

```jsonc
{ "type": "alerts",       "config": { "state": "ALERT" } }          // ALERT | OK | INSUFFICIENT_DATA; omit for all
{ "type": "alert-detail", "config": { "alertName": "checkout-error-rate-high" } }  // alerts keyed by NAME
```

The `alert-detail` panel is keyed by the alert's **name** (that is the config
field the panel accepts). Note that alert names are **not** unique within a space
(see [alert-setup.md](alert-setup.md) — an alert's stable identity is its
`alertId`), so a name can match several alerts; point the panel at a uniquely-named
alert.

#### application-map / spans

Insertable and saveable; their `config` is not yet public. Author them with no
`config` — they render correctly and pick up the dashboard's time range. Camera,
node selection, and query-seed state are per-user console state, not saved.

#### dashboards-list

`"config": {}` — a list of saved dashboards.

#### trace-details

```jsonc
"config": { "traceId": "…", "startTime": 1730000000000, "endTime": 1730000600000,
            "initialMode": "waterfall",  // waterfall | flamegraph
            "focusSpanId": "…" }         // optional — deep-link to a specific span
```

`startTime`/`endTime` are epoch **milliseconds** on the config (not the panel
scope), fixed at author time. A saved `trace-details` panel is useful only while
its trace is still retained — prefer a `spans` panel for a durable dashboard.

### Visualizations — exactly nine legal values

`line` · `area` · `bar` · `scatter` · `pie` · `table` · `number` · `solidgauge` ·
`heatmap`.

> `stacked-bar`, `single-metric`, and `donut` are **not** valid — use `bar` with a
> stacking flag, `number`, and `pie` respectively.

Pick by signal kind:

| Signal | Visualization |
|--------|---------------|
| Time series, ≤ ~25 series, comparable units | `line` |
| Additive series / discrete buckets (2xx/4xx/5xx, per-AZ) | `bar` (stacked) or `area` |
| Correlation point cloud (no connecting line) | `scatter` |
| One number, with a delta | `number` |
| Resources ranked by a metric | `table` (default sort: descending on the primary signal) |
| Genuine part-of-whole | `pie` |
| A bounded ratio against thresholds (availability %) | `solidgauge` |

Anti-patterns: no `line` past ~25 series (use `topk(...)` or a `table`); don't
stack a `bar` whose series go negative; don't put two units on one chart — split
into two `w: 30` panels. `heatmap` does not yet ingest histogram-bucket output —
for a latency distribution use `line` with a `histogram_quantile`.

> **The composer honors the visualization you pick, with exactly two exceptions.**
> It applies only two robust query-shape overrides — a scalar-aggregate query →
> `number`, and a top-N ranking (`ORDER BY … LIMIT` / `topk(...)`) → `table` — and
> OTHERWISE keeps the visualization you chose. So the recipe guidance for `bar` /
> `area` / `solidgauge` / `spans` / `trace-details` / `pie` / `heatmap` stands as
> written.

### Chart options

`chartOptions` sets appearance and is a discriminated union keyed on `view`, which
must match the panel's `visualization` (when both are present, `view` wins — so
setting only `visualization` is the simpler, recommended form).

```jsonc
"chartOptions": {
  "view": "line",
  "title": { "text": "Requests/sec", "show": true },
  "plotOptions": {
    "legend": { "show": true, "position": "bottom" },
    "yAxis": [ { "min": 0, "title": "req/s" } ]   // TUPLE of 1 or 2 axes (2nd = right-hand)
  }
}
```

- **Cartesian** (`line`/`area`/`bar`/`scatter`): `legend`, `stacking`, `xAxis`, and
  `yAxis` as a **tuple** of one or two axes (the second is the right-hand axis). Use
  `type: 'datetime'` for a time axis (not `'time'`).
- **`solidgauge`**: `yAxis` is an **object** `{ min, max }` (not a tuple), plus
  `plotBands: [{ from, to, color }]`.
- **`heatmap`**: `xAxis`/`yAxis` with `categories`, and `colorScale`.
- **`table`**: `hiddenColumns`, `columnOrder`. `number` and `pie` take little
  beyond the base fields.
- **Stacking has two legal forms.** Either set `plotOptions.stacking: "normal"` (or
  `"percent"`) — an **enum**, not a boolean, keyed directly on `plotOptions` — or
  use the nested `plotOptions.style.<view>Options.stacked: true` (e.g.
  `plotOptions.style.barOptions.stacked: true`). There is **no**
  `plotOptions.stacked` field; a flag placed there is an unknown key, silently
  dropped on save, and the chart will not stack.

### Validation — what happens to a body on read/write

- **Rejected:** a missing or non-array `panels`; a panel with no `type` or no
  `layout`; a layout with a non-integer `x`/`w`, a negative bound, or a malformed
  `h`.
- **Accepted but adjusted:** an unrecognized panel type renders a placeholder and
  is preserved. An off-grid panel is not reflowed for you — see Step 4.
- **Silently ignored:** any key not in the schema — including a misspelled field
  name. A typo does not error; the field is just dropped. Check spelling against
  this reference.
- **Dashboard names** must be non-empty, ≤ 512 chars, trimmed of surrounding
  whitespace, and printable ASCII.

---

## Step 4 — Lay out on the 60-column grid

Assign each panel's `layout: { x, y, w, h }` so panels tile cleanly with no overlap
and no overflow. This is the single most error-prone part of a body.

### The two-unit rule (memorize this)

`x`/`w` and `y`/`h` do **not** share a unit:

| Field | Unit | Rule |
|-------|------|------|
| `x` | grid **column** | integer `0`–`59`; `x: 0` is the left edge |
| `w` | grid **columns** | integer `1`–`60`; **`x + w` must not exceed `60`** |
| `y` | **pixels** | integer pixels from the top (`0` or greater), not a row index |
| `h` | **pixels** (integer `100`–`2000`) or `'auto'` | e.g. `320`, `'auto'`; never fractional, never a relative unit (`vh`/`%`/`vw`); structural rows (`divider` `40`, `navigation` `28`) are the sanctioned sub-100 exception |

Mixing the units (treating `y` as a row index, or `w` as pixels) is the most common
authoring bug. Heights are ABSOLUTE PIXELS or `'auto'` — **never** a relative CSS
unit (`vh`/`%`/`vw`), which the layout schema rejects (a relative `h` fails
validation and the whole canvas fails to render). Keep a numeric `h` within roughly
**100–2000** (e.g. `320` for a chart) — an integer, never fractional (`320.5` fails
the same `int()` check); a `divider` (`40`) and `navigation` (`28`) are
intentionally thinner. Prefer `'auto'` for content-sized panels (markdown, lists).

### Width conventions

Every row MUST match one of the width-per-count patterns below. Author the correct
shape yourself — nothing re-shapes it for you.

| Row count | Width per panel (`w`) | Use for |
|-----------|-----------------------|---------|
| 1 panel | `60` | full-width strip (hero chart, table, status strip, divider, navigation, application-map) |
| 2 panels | `30` each | two halves side-by-side (most time-series pairs) |
| 3 panels | `20` each | three thirds (read/write/idle, 2xx/4xx/5xx) |
| 4 panels | `15` each | four quarters (KPI row) |

**Hard rules — all MUST:**

- A row's widths sum to **EXACTLY 60**, with `x` as the cumulative sum from 0
  (`0, 30`; `0, 20, 40`; `0, 15, 30, 45`).
- Every panel in a row shares the **same `y`** AND the **same `h`**.
- **Never more than 4 panels in one row.** A 5th starts a new row below: 5 panels =
  3 then 2; 6 = 3+3; 7 = 4+3.
- **No mixed-width rows** except an intentional hero-supporting layout, which uses
  TWO rows: row 1 is one `w: 60` hero, row 2 is `w: 30`×2 or `w: 20`×3 supporting
  panels — never side-by-side with the hero.
- **No heterogeneous chart/table rows.** A `line` chart and a `table` on the same
  row read badly — split them into two rows (chart row above, table row below).

### Stacking rows with `y`

`y` is the pixel offset from the top and it orders rows. Give successive rows
**increasing `y`** equal to the running sum of prior row heights:

- KPI row (`h: 120`) at `y: 0`
- first chart row (`h: 320`) at `y: 120`
- next chart row at `y: 440`, and so on.

When a row uses `'auto'` heights, still give the next row a larger `y`; the renderer
resolves final positions from each row's height, so approximate but
monotonically-increasing `y` values are fine.

### Height guidance by panel kind

| Panel kind | Suggested `h` |
|------------|---------------|
| `number` KPI tile | `120` (short — one figure) |
| Time-series (`line`/`area`/`bar`/`scatter`) | ~`320` |
| `table` | ~`320`–`400`, taller for many rows |
| `pie` / `solidgauge` | ~`280`–`320` (roughly square reads best) |
| `divider` | `40` (always full width, `x: 0, w: 60`) |
| `navigation` | ~`28` (full width; meaningless without dividers) |
| `markdown` runbook | `'auto'` (pair with `variant: 'transparent'`) |
| `application-map` / `spans` | full width, tall (~`480`) |

### Overflow and overlap

- A panel that overflows the grid (`x + w > 60`) is never reflowed into what you
  meant — it is narrowed or refused. Keep `x + w <= 60` on every panel yourself.
- The renderer does not reflow overlaps. Two panels sharing a `y` must not share
  columns — give them non-overlapping `[x, x+w)` ranges. Follow the
  width-per-count patterns above and give each row a larger `y` and you will never
  overlap.

---

## Appendix — Archetype templates

When the ask names a known resource TYPE, start from its ready panel set below,
then **ground** every query (Step 2) and **lay it out** (Step 4). Build the CORE
subset by default and offer the optional-depth panels as a follow-up "add section."
Ground each panel's real metric name and reading (gauge vs. counter, derived
formulas) against the live catalog (Step 2); the query strings are TEMPLATES — the
identity form is canonical, but the metric name and statistic MUST be grounded. If
a signal cannot be grounded, **drop that panel** and re-sequence `y` so no blank row
is left. Set `queryLanguage` explicitly, `autoRun: true` on every data panel, and
`promqlQueryOptions.step` to match the range vector; keep every query windowless.

### Lambda

Serverless function — RED-shaped; scope `cloudwatch.aws/lambda` by `FunctionName`.

**CORE (~8 panels — the default build):**

| Panel | Viz | Query template | Layout |
|-------|-----|----------------|--------|
| Invocations/s | `number` | `sum(rate({__name__="Invocations", "@instrumentation.@name"="cloudwatch.aws/lambda", FunctionName="<fn>"}[5m]))` | `{x:0,y:0,w:15,h:120}` |
| Error rate | `number` | `sum(rate({__name__="Errors", …, FunctionName="<fn>"}[5m])) / sum(rate({__name__="Invocations", …, FunctionName="<fn>"}[5m]))` | `{x:15,y:0,w:15,h:120}` |
| Throttles/s | `number` | `sum(rate({__name__="Throttles", …, FunctionName="<fn>"}[5m]))` | `{x:30,y:0,w:15,h:120}` |
| Concurrency | `number` | `max({__name__="ConcurrentExecutions", …, FunctionName="<fn>"})` | `{x:45,y:0,w:15,h:120}` |
| Invocation rate | `line` | `sum by (FunctionName) (rate({__name__="Invocations", …, FunctionName="<fn>"}[5m]))` | `{x:0,y:120,w:30,h:320}` |
| Errors/s | `line` | `sum by (FunctionName) (rate({__name__="Errors", …, FunctionName="<fn>"}[5m]))` | `{x:30,y:120,w:30,h:320}` |
| Duration (ms) | `line` | `{__name__="Duration", …, FunctionName="<fn>"}` | `{x:0,y:440,w:60,h:320}` |
| Recent errors | `table` (SQL) | scope to `/aws/lambda/<fn>` with a grounded log-group filter; `queryLanguage:'sql'` | `{x:0,y:760,w:60,h:360}` |

**Optional depth (follow-up):** Throttles `line`; Concurrent executions `line`;
Stream-consumer lag `line` (`IteratorAge` — only for a stream/event-source
consumer). Append two-up (`w:30,h:320`) and re-sequence `y`.

### Kubernetes/EKS

OTLP-native — no vended scope. **RED** from the span metrics grouped by
`@resource.service.name`; **USE** from the OTLP Kubernetes resource metrics grouped
by `@resource.k8s.*`. Ground the span-metric names and `k8s.*` resource-metric
names against the live catalog (Step 2).

**CORE (~8 panels — the default build):**

| Panel | Viz | Query template | Layout |
|-------|-----|----------------|--------|
| Request rate | `number` | `sum(rate({"traces.span.metrics.calls", "@resource.service.name"="<svc>"}[5m]))` | `{x:0,y:0,w:15,h:120}` |
| Error rate | `number` | ratio of `…calls, "@status.code"="ERROR"` to all calls | `{x:15,y:0,w:15,h:120}` |
| p99 latency | `number` | `histogram_quantile(0.99, rate({"traces.span.metrics.duration", …}[5m]))` | `{x:30,y:0,w:15,h:120}` |
| Running pods | `number` | `count({"k8s.pod.phase", "@resource.k8s.namespace.name"="<ns>", "@resource.k8s.deployment.name"="<deploy>"})` | `{x:45,y:0,w:15,h:120}` |
| Request rate | `line` | `sum by ("@resource.service.name") (rate({"traces.span.metrics.calls", …}[5m]))` | `{x:0,y:120,w:30,h:320}` |
| Errors by status | `bar` | `sum by ("@status.code") (rate({"traces.span.metrics.calls", …}[5m]))` | `{x:30,y:120,w:30,h:320}` |
| Latency p50/p90/p99 | `line` | `histogram_quantile(0.99, rate({"traces.span.metrics.duration", …}[5m]))` — add one series per quantile (0.50, 0.90, 0.99) | `{x:0,y:440,w:60,h:320}` |
| Top services by errors | `table` | `topk(10, sum by ("@resource.service.name") (rate({"traces.span.metrics.calls", "@status.code"="ERROR"}[5m])))` | `{x:0,y:760,w:60,h:360}` |

**Optional depth (follow-up "infra / USE health"):** Pod CPU usage, Pod memory
usage, Container restarts — grouped by `@resource.k8s.*` (`k8s.pod.cpu.usage`,
`k8s.pod.memory.usage`, `increase(k8s.container.restarts[15m])`). Append two-up and
re-sequence `y`.

### RDS/database

Infrastructure resource — USE/saturation; scope `cloudwatch.aws/rds` by
`DBInstanceIdentifier`. Reading rules: IOPS is already per-second → never `rate()`;
latency is in seconds → × 1000 for ms; mind `FreeStorageSpace` / `FreeableMemory`
polarity (higher is healthier).

**CORE (~7 panels — the default build):**

| Panel | Viz | Query template | Layout |
|-------|-----|----------------|--------|
| CPU % | `number` | `max({__name__="CPUUtilization", …, DBInstanceIdentifier="<db>"})` | `{x:0,y:0,w:15,h:120}` |
| Connections | `number` | `max({__name__="DatabaseConnections", …, DBInstanceIdentifier="<db>"})` | `{x:15,y:0,w:15,h:120}` |
| Free storage | `number` | `min({__name__="FreeStorageSpace", …, DBInstanceIdentifier="<db>"})` | `{x:30,y:0,w:15,h:120}` |
| Read latency (ms) | `number` | `max({__name__="ReadLatency", …, DBInstanceIdentifier="<db>"}) * 1000` | `{x:45,y:0,w:15,h:120}` |
| CPU % | `line` | `{__name__="CPUUtilization", …, DBInstanceIdentifier="<db>"}` | `{x:0,y:120,w:30,h:320}` |
| Connections | `line` | `{__name__="DatabaseConnections", …, DBInstanceIdentifier="<db>"}` | `{x:30,y:120,w:30,h:320}` |
| Top instances by CPU | `table` | `topk(10, max by (DBInstanceIdentifier) ({__name__="CPUUtilization", …}))` | `{x:0,y:440,w:60,h:360}` |

**Optional depth (follow-up "infra / USE health"):** Read IOPS `line`; Read latency
(ms) `line`; add the `WriteIOPS` / `WriteLatency` counterparts for a full
read+write view. Append two-up and re-sequence `y`.

### ECS/web service

Cross-signal — **USE** from the ECS service tier combined with **RED** from the
load balancer in front (or from Application Signals). Identity + reading rules: ECS
scopes by `ClusterName` + a non-empty `ServiceName`; ALB `TargetResponseTime` is a
gauge in seconds; the target status-code metrics carry the `_Count` suffix.

**CORE (~7 panels — the default build; this archetype has no ranked table):**

| Panel | Viz | Query template | Layout |
|-------|-----|----------------|--------|
| Request rate | `number` | `sum(rate({__name__="RequestCount", "@instrumentation.@name"="cloudwatch.aws/applicationelb", LoadBalancer="<lb>"}[5m]))` | `{x:0,y:0,w:15,h:120}` |
| 5xx rate | `number` | `sum(rate({__name__="HTTPCode_Target_5XX_Count", …, LoadBalancer="<lb>"}[5m]))` | `{x:15,y:0,w:15,h:120}` |
| Peak response (ms) | `number` | `max({__name__="TargetResponseTime", …, LoadBalancer="<lb>"}) * 1000` | `{x:30,y:0,w:15,h:120}` |
| Service CPU % | `number` | `max({__name__="CPUUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs", ClusterName="<cluster>", ServiceName="<svc>"})` | `{x:45,y:0,w:15,h:120}` |
| Request rate | `line` | `sum(rate({__name__="RequestCount", …, LoadBalancer="<lb>"}[5m]))` | `{x:0,y:120,w:30,h:320}` |
| Status codes | `bar` | `sum by (__name__) (rate({__name__=~"HTTPCode_Target_..._Count", …, LoadBalancer="<lb>"}[5m]))` | `{x:30,y:120,w:30,h:320}` |
| Response time (ms) | `line` | `{__name__="TargetResponseTime", …, LoadBalancer="<lb>"} * 1000` | `{x:0,y:440,w:60,h:320}` |

**Optional depth (follow-up "infra / USE health"):** Memory util % `line`; Running
tasks `line` (`RunningTaskCount`). If the space runs Application Signals, swap the
RED panels for `Service`/`Fault`/`Error` and the availability formula
`(1 − Fault/Total) × 100`. Append two-up and re-sequence `y`.

### API Gateway

Request-serving — RED. Identity split: REST v1 on `ApiName` with `4XXError` /
`5XXError`, HTTP v2 on `ApiId` with `4xx` / `5xx`; gateway overhead is the formula
`Latency − IntegrationLatency`.

**CORE (~8 panels — the default build):**

| Panel | Viz | Query template | Layout |
|-------|-----|----------------|--------|
| Request count/s | `number` | `sum(rate({__name__="Count", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiName="<api>"}[5m]))` | `{x:0,y:0,w:15,h:120}` |
| 5xx rate | `number` | `sum(rate({__name__="5XXError", …, ApiName="<api>"}[5m]))` | `{x:15,y:0,w:15,h:120}` |
| 4xx rate | `number` | `sum(rate({__name__="4XXError", …, ApiName="<api>"}[5m]))` | `{x:30,y:0,w:15,h:120}` |
| Peak latency (ms) | `number` | `max({__name__="Latency", …, ApiName="<api>"})` | `{x:45,y:0,w:15,h:120}` |
| Request count | `line` | `sum(rate({__name__="Count", …, ApiName="<api>"}[5m]))` | `{x:0,y:120,w:30,h:320}` |
| Errors 4xx/5xx | `bar` | `sum by (__name__) (rate({__name__=~"[45]XXError", …, ApiName="<api>"}[5m]))` | `{x:30,y:120,w:30,h:320}` |
| Latency (ms) | `line` | `{__name__="Latency", …, ApiName="<api>"}` | `{x:0,y:440,w:60,h:320}` |
| Top resources by 5xx | `table` | `topk(10, sum by (Resource) (rate({__name__="5XXError", …, ApiName="<api>"}[5m])))` | `{x:0,y:760,w:60,h:360}` |

**Optional depth (follow-up "per-service latency"):** Integration latency (ms)
`line` (`IntegrationLatency`) — chart it beside `Latency` so the gap reads as
gateway overhead. Append two-up and re-sequence `y`.
