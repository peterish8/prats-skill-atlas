# Production testing playbook

## Contents

1. Layered test strategy
2. Failure-injection matrix
3. Security verification
4. Accessibility verification
5. Performance verification
6. Test integrity

## 1. Layered test strategy

Use the cheapest layer that proves the behavior, then retain a small number of real browser journeys:

- Unit: parsing, validation, authorization predicates, state reducers, cache-key construction, formatting, boundaries, and retry decisions.
- Integration: endpoint plus trusted authorization/validation/data store, transactions, jobs, webhooks, cache invalidation, and dependency adapters.
- Component: request-state rendering, form errors, focus, empty/partial states, optimistic rollback, and accessible names/states.
- End-to-end: critical journeys, role boundaries, navigation/reload, real request wiring, and cross-component data reconciliation.
- Operational smoke: deployed health, environment wiring, migrations, third parties, telemetry, and rollback-sensitive behavior.

Test behavior and invariants, not implementation trivia. A critical mutation should have trusted-boundary integration coverage even if it also has a browser test.

## 2. Failure-injection matrix

Apply relevant rows to every critical request-backed action:

| Scenario | Assert |
| --- | --- |
| Delayed response | Progress appears promptly, control cannot duplicate work, layout stays stable, eventual result is correct. |
| 400/validation | Input remains, precise correction appears, request is not falsely successful. |
| 401 | Session recovery/sign-in path is clear and safe work is preserved. |
| 403 | Protected data remains hidden and the user gets a truthful permitted route. |
| 404 | Deleted/missing data has a recovery destination. |
| 409 | Concurrent changes cannot silently overwrite newer state. |
| 429 | Retry respects server timing when supplied and avoids a request storm. |
| 500/dependency failure | Safe message, actionable retry/support path, internal error evidence without leaked details. |
| Timeout/connection drop | No false success; unknown outcome is distinguished from confirmed failure. |
| Offline | Cached/pending state is clear and non-idempotent writes are not duplicated. |
| Double/rapid activation | At most one intended effect or documented idempotent result. |
| Out-of-order reads | Latest intent wins and obsolete response cannot overwrite it. |
| Reload/back/multiple tabs | State and server truth reconcile without corruption or surprising loss. |
| Empty/partial payload | Empty/partial UI is intentional and resilient to optional/missing fields. |

With Playwright or equivalent, intercept network responses for deterministic delay/error/empty tests. Use observable assertions and auto-waiting; avoid fixed sleeps. Use isolated accounts/data for tests that mutate server state.

## 3. Security verification

- Test unauthenticated, wrong-role, wrong-tenant/owner, expired/revoked session, and modified object IDs at the server/API boundary.
- Verify inputs at minimum/maximum/empty/malformed/unexpected-type boundaries and relevant injection contexts.
- Check upload size/type/content policy, download authorization, redirect allowlists, outbound URL controls, CORS/CSRF/session behavior, cache headers for sensitive data, and error redaction where applicable.
- Review dependency and secret-scanning results, but reproduce or inspect the reachable path before calling a vulnerability confirmed.
- Use OWASP ASVS for controls and WSTG for authorized runtime techniques. Never perform denial-of-service, credential attacks, destructive payloads, or broad live scanning without explicit permission.

## 4. Accessibility verification

Automated checks: semantics, names, contrast detectable by tooling, landmark/heading issues, form associations, and common ARIA misuse.

Manual checks:

1. Complete critical journeys using keyboard only.
2. Verify focus visibility/order, modal focus containment/return, skip/navigation behavior, and no keyboard traps.
3. Zoom/reflow and test narrow mobile viewport without loss of content or two-dimensional scrolling unless essential.
4. Verify status, loading, validation, error, and success changes have useful accessible announcements.
5. Inspect screen-reader-oriented names, roles, values, descriptions, and state changes.
6. Verify reduced motion, target size, non-color indicators, text alternatives, and media alternatives where applicable.

Do not claim WCAG conformance from an automated score alone.

## 5. Performance verification

For each representative route capture the environment, device/viewport, CPU/network profile, cache state, build mode, and run count.

- Cold navigation: document latency, LCP resource discovery/priority, render blocking, transfer size, request chains, and layout shifts.
- Repeat navigation: cache hits/revalidation, duplicate requests, client navigation, stale/refetch behavior, and bfcache eligibility where applicable.
- Interaction: INP/long tasks, handler work, rerenders, DOM/list size, layout work, and third-party impact.
- Media/assets: dimensions, responsive source selected, compression/format, offscreen lazy loading, font behavior, and unused resources.
- API: payload fields/size, pagination, compression, cache policy, duplicate calls, waterfalls, retries, and failure rate.

Compare at least three lab runs when practical and use a median, not a cherry-picked result. Prefer field data for actual-user conclusions. Establish regression budgets that reflect the route and baseline rather than universal magic numbers.

## 6. Test integrity

- Record exact commands, environment, and exit status.
- Keep authentication state and secrets out of version control and reports.
- Avoid mocks that bypass the code being verified. Retain integration coverage for trust boundaries and data invariants.
- Confirm a test fails before the fix when feasible and passes after it.
- Investigate flakes; do not hide them with sleeps, retries, or weakened assertions without finding the cause.
- Mark unavailable checks as blocked with the exact dependency: credentials, browser, database, preview URL, device, or external sandbox.
