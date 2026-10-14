# Omni Views Reference

Views in CloudWatch Omni are named SQL queries that can be referenced as tables. They allow reusing common query logic without repeating it — use `FROM view.<name>` in any query to inline the view's stored SQL.

## 1. Using Views in Queries

Reference a view by its name with the `view.` prefix in the FROM clause:

```sql
SELECT `@timestamp`, `@record`
FROM view.my-error-logs
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1 HOUR' AND NOW()
ORDER BY `@timestamp` DESC
```

Views behave like inline subqueries:
- They **inherit the outer query's `@timestamp` bounds** — no need to specify a time range inside the view definition
- They can be used anywhere a table is used: JOINs, subqueries, UNION, etc.
- They can reference other views (up to 32 levels of nesting)
- Cyclic references (a view referencing itself, directly or transitively) are detected and rejected
- The view's SQL is re-evaluated fresh on every query execution (not cached results)

### Views in JOINs

```sql
SELECT e.`@timestamp`, e.`@record`
FROM view.error-logs AS e
INNER JOIN view.slow-traces AS s
  ON e.traceId = s.traceId
WHERE e.`@timestamp` BETWEEN NOW() - INTERVAL '1 HOUR' AND NOW()
  AND s.`@timestamp` BETWEEN NOW() - INTERVAL '1 HOUR' AND NOW()
```

### Composing Views (nested)

A view can reference other views in its definition:

```sql
-- If view.base-errors is defined as:
--   SELECT * FROM logs.default WHERE severity = 'ERROR'
-- Then another view can build on it:
--   SELECT * FROM view.base-errors WHERE service = 'checkout'
-- And queries can reference the composed view:
SELECT COUNT(*) FROM view.checkout-errors
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1 HOUR' AND NOW()
```

## 2. Managing Views

### CreateView

Creates a new named view.

| Parameter | Required | Description |
|---|---|---|
| `name` | Yes | View name. Must start with `view.`. Max 128 characters. Allowed characters: alphanumeric, `-`, `_`, `.` |
| `definition` | Yes | A single SQL SELECT statement |
| `description` | No | Human-readable description of the view's purpose |

Example:
```
CreateView
  name: "view.error-logs-last-hour"
  definition: "SELECT `@timestamp`, `@record` FROM logs.default WHERE severity = 'ERROR'"
  description: "All error-level log entries"
```

### UpdateView

Updates an existing view's definition and/or description.

| Parameter | Required | Description |
|---|---|---|
| `name` | Yes | The view name to update |
| `definition` | No | New SQL SELECT statement |
| `description` | No | New description |

A new `definition` replaces the old one in place, changing results for everything that
reads the view. Draft the change and confirm with the user before calling `UpdateView`.

### DeleteView

Deletes a view by name.

| Parameter | Required | Description |
|---|---|---|
| `name` | Yes | The view name to delete |

**Confirm before deleting.** Deleting a view is a destructive write and cannot be
undone — any saved query or dashboard panel that reads `FROM view.<name>` breaks once
it is gone. Name the specific view and confirm with the user before calling `DeleteView`;
do not delete on inference.

### ListViews

Lists all views in the account. Returns name, definition, description, scope, and timestamps for each view.

### GetView

Gets a single view by name. Returns the view's definition, description, scope, and timestamps.

## 3. View Naming Rules

- Must start with `view.` prefix
- Maximum 128 characters total
- Allowed characters: letters, digits, `-`, `_`, `.`
- The prefix `view.aws.` is reserved for managed/curated views provided by AWS — user-created views cannot use this prefix

Examples of valid names:
- `view.my-error-logs`
- `view.checkout.slow-requests`
- `view.team_dashboard_metrics`

## 4. View Definition Rules

- Must be a single SQL SELECT statement
- Cannot contain multiple statements (no semicolons)
- Can reference any table: `logs.default`, `traces.default`, `metrics.default`, `default`
- Can reference other views: `FROM view.other-view`
- Does NOT need its own `@timestamp` filter — it inherits from the outer query
- Can include any supported SQL: JOINs, CTEs, window functions, aggregations, etc.

## 5. Constraints

- Maximum **100 views per account**
- Maximum nesting depth: **32 levels** (views referencing views referencing views...)
- Cyclic references are rejected (a → b → a, or a → a)
- `view.aws.*` prefix is reserved (cannot create or modify)
- View names are case-sensitive

## 6. Common Patterns

### Encapsulate a filtered subset

```
CreateView
  name: "view.production-errors"
  definition: "SELECT * FROM logs.default WHERE environment = 'production' AND severity = 'ERROR'"
```

Then query it:
```sql
SELECT COUNT(*) AS error_count, service
FROM view.production-errors
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1 HOUR' AND NOW()
GROUP BY service
ORDER BY error_count DESC
```

### Create a view for cross-telemetry correlation

```
CreateView
  name: "view.errors-with-traces"
  definition: "SELECT * FROM default WHERE severity = 'ERROR' OR statusCode = 'ERROR'"
```

### Create a view for a specific metric

```
CreateView
  name: "view.high-cpu"
  definition: "SELECT `@timestamp`, value, `@resource.service.name` FROM metrics.default WHERE name = 'CPUUtilization' AND value > 80"
```

Then alert or dashboard on it:
```sql
SELECT `@timestamp`, `@resource.service.name`, value
FROM view.high-cpu
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '6 HOURS' AND NOW()
ORDER BY value DESC
```
