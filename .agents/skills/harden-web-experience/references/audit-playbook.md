# Codebase audit playbook

## Contents

1. Fast surface map
2. Journey and action inventories
3. Data-flow review
4. Risk evidence
5. Search heuristics

## 1. Fast surface map

Inspect in this order:

1. Repository instructions, planning/source-of-truth documents, status/diff.
2. Manifests, lockfiles, workspace config, runtime versions, framework and deployment config.
3. Route trees, layouts, navigation, public pages, authenticated areas, admin/elevated areas, API/server-action handlers, webhooks, jobs, and scheduled work.
4. Authentication/session code, authorization helpers, schemas/models/migrations, request/data clients, query/cache layer, state stores, error boundaries, and design primitives.
5. Tests, fixtures, seeds, CI, environment templates, observability/error reporting, analytics, feature flags, and production headers.
6. Static assets, image/font pipeline, third-party scripts, generated bundles, and service worker/PWA behavior if present.

Run `scripts/repo_probe.py` for a read-only signal map when useful. Confirm every signal in source before reporting it.

## 2. Journey and action inventories

Create one row per critical journey:

| Journey | Actor/role | Entry | Goal | Data/side effects | Dependencies | Success proof | Recovery path |
| --- | --- | --- | --- | --- | --- | --- | --- |

Create one row per request-backed action:

| Route/component | Action | Endpoint/function | Read/write | Pending UI | Success UI | Failure UI | Duplicate/race policy | Authorization | Test |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include less-visible surfaces: keyboard shortcuts, autosave, optimistic controls, bulk actions, exports, modals/sheets, nested tabs, infinite scroll, uploads, webhooks, background refresh, reconnect, and browser back/forward.

## 3. Data-flow review

For each critical mutation answer:

- What is the trusted identity and authorization decision?
- Which input is untrusted, normalized, and validated where?
- Which records/files/external systems change? Must the change be atomic?
- What makes a retry safe? What happens when the response is lost after the server commits?
- What prevents duplicate, stale, reordered, cross-user, or cross-tenant effects?
- Which client caches and derived views must update? Can optimistic state roll back?
- What does the user see for success, known failure, unknown outcome, and later reconciliation?
- What telemetry proves the operation succeeded or failed without recording sensitive content?

For reads, examine cache keys, freshness, pagination cursors, filter serialization, authorization, overfetching, request deduplication, cancellation, loading priority, and stale-response handling.

## 4. Risk evidence

Use these confidence labels:

- `confirmed`: reproduced, test failed, unsafe path proven in code, or runtime evidence captured.
- `probable`: strong code evidence but a required runtime dependency or credential is unavailable.
- `hypothesis`: pattern match or plausible risk awaiting inspection.

Use impact plus likelihood, not scanner severity alone. Raise priority for cross-tenant access, data loss, secret exposure, financial/entitlement effects, unauthenticated write paths, silent false success, irreversible work loss, and failures on the product's main journey.

For each correction define proof before editing: a regression test, direct endpoint authorization test, browser state assertion, network trace, accessibility behavior, performance comparison, or operational signal.

## 5. Search heuristics

Search tools accelerate navigation; they do not establish findings. Adapt patterns to the stack.

- Requests and mutations: `fetch(`, request clients, query/mutation hooks, server actions, RPC/GraphQL calls, form actions, uploads, webhooks.
- Async states: `isLoading`, `isPending`, `loading`, `error`, `toast`, `Suspense`, error boundaries, disabled controls, optimistic updates.
- Trust boundaries: route handlers, controllers, actions, resolvers, middleware, authorization helpers, model/repository calls, file and URL processing.
- Risk signals: raw HTML sinks, dynamic code execution, unsafe process/database construction, wildcard CORS, client-stored credentials, unvalidated redirects, unchecked object IDs, verbose errors, debug endpoints.
- Data consistency: cache keys, invalidation, transactions, unique constraints, upsert, retry loops, job/webhook handlers, timestamps/timezones, money/rounding.
- Performance: unbounded lists, repeated effects/subscriptions, broad response fields, synchronous heavy work, large assets, eager third parties, missing image dimensions, dynamic imports, caching headers.
- Accessibility: click handlers on non-controls, missing labels/names, focus management, dialogs, keyboard events, live regions, alt text, motion, color-only status.
- Operations: environment reads, feature flags, health endpoints, logging, error capture, migrations, queues, cron, deployment config, debug/source maps, analytics consent/redaction.

Inspect generated files and vendored dependencies only when they are the actual source of shipped behavior. Do not patch build output instead of source.
