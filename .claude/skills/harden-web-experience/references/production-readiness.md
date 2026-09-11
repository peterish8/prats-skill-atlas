# Production readiness matrix

## Contents

1. Product and data
2. Security and privacy
3. Reliability and operations
4. Delivery and rollback
5. Performance and accessibility
6. Public web and support
7. Readiness decision

Use `applicable`, `not applicable with reason`, `passed with evidence`, or `blocked` for each row. Do not silently skip a dimension.

## 1. Product and data

- Critical journeys and roles are identified and tested end-to-end.
- Every request-backed action has pending, success, failure, duplicate, and recovery behavior.
- Every data surface has loading, empty, partial, error, permission, and not-found behavior where applicable.
- Business invariants live at trusted boundaries and have tests.
- Transactions, uniqueness, referential integrity, concurrency, ordering, pagination, timezones, currencies, and rounding are intentional.
- Destructive operations, retention, export, account deletion, and recovery match actual product promises.
- Jobs, webhooks, imports, and retries are idempotent or deduplicated and observable.

## 2. Security and privacy

- Authentication, role, ownership, and tenant isolation are enforced server-side for every protected read/write.
- Inputs, files, URLs, and outputs are validated/encoded for their context.
- Sessions, cookies/tokens, CSRF, CORS, redirects, headers, and cache policies match the architecture.
- Secrets are absent from source/client bundles/logs and rotate/revoke safely.
- Sensitive data is minimized, encrypted using platform-vetted mechanisms where required, redacted from telemetry, and retained intentionally.
- Rate/abuse controls protect expensive and high-impact paths without locking out legitimate recovery.
- Dependencies and build provenance are reproducible; known reachable critical vulnerabilities are resolved.
- Applicable legal/compliance claims have qualified review; the code audit does not self-certify compliance.

## 3. Reliability and operations

- Required configuration is validated at startup and environment separation is clear.
- Health/readiness signals reflect ability to serve, not merely process existence.
- Structured logs, errors, traces, and metrics identify failed critical journeys while avoiding secrets, personal data, and unbounded cardinality.
- Request/correlation identifiers join user-visible support references to server evidence where appropriate.
- Alerts are actionable and tied to user impact, latency, error rate, saturation, dependency failure, or backlog age as appropriate.
- Timeouts, retry caps, exponential backoff/jitter, circuit/bulkhead behavior, and fallbacks match dependency semantics.
- Backups and restore expectations are defined and tested proportionally to the data's value.
- Operational ownership and a recovery path exist for critical third-party, queue, job, email, payment, and storage failures.

## 4. Delivery and rollback

- CI runs deterministic formatting, lint, types, tests, build, and applicable security/schema checks.
- Production artifacts are built from locked dependencies and contain no debug routes, test credentials, or unsafe development defaults.
- Database/data migrations are reviewed for locking, runtime, backward compatibility, retry, partial failure, and rollback/roll-forward.
- Old and new application versions can coexist during rolling deployment where required.
- Feature flags have safe defaults, ownership, and cleanup plans; kill switches protect high-risk integrations when justified.
- Preview/staging smoke tests cover environment wiring and critical journeys.
- Deployment, rollback/roll-forward, and incident recovery steps are known and do not depend on one person's memory.

## 5. Performance and accessibility

- Representative routes have comparable cold/repeat/mobile performance evidence and route-appropriate regression budgets.
- Core Web Vitals, request/payload budgets, image/font/JS behavior, caching, and third parties are measured and no known critical regression remains.
- Critical journeys pass keyboard and screen-reader-oriented manual checks plus available automated checks.
- WCAG 2.2 AA requirements are met or gaps are explicitly recorded; no conformance claim relies only on automation.
- Responsive layouts, zoom/reflow, reduced motion, touch targets, and supported browsers/devices are verified.

## 6. Public web and support

- Intended public pages return correct status codes, metadata, canonical/indexing intent, internal links, social previews, sitemap/robots behavior, and truthful structured data.
- Private/staging/duplicate/filter pages do not accidentally expose or index sensitive/low-value content.
- 404, 500, maintenance, offline, expired-session, and unsupported-state pages give a useful next action.
- User-facing errors are searchable/supportable without exposing internals; contact/help paths are real.
- Analytics and consent behavior match the product's actual policy and applicable requirements; essential journeys do not silently depend on blocked analytics.

## 7. Readiness decision

`READY` requires evidence for every applicable critical row and no known P0/P1 risk.

`CONDITIONALLY READY` requires no known unresolved code-level P0/P1 risk, but may have explicit external gates such as production credentials, restore drill, legal review, field telemetry, or staging verification.

`NOT READY` applies when a critical journey is broken, security/data integrity risk remains, deployment cannot be recovered safely, required configuration is unknown, or evidence is too incomplete to support launch.
