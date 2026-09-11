---
name: harden-web-experience
description: Turn an existing web application into a production-grade product by auditing, fixing, and verifying security, hidden bugs, edge cases, accessibility, async loading/error/empty states, data integrity, network and Core Web Vitals performance, resilience, observability, deployment safety, privacy, and public-site discoverability. Use for website hardening, launch-readiness reviews, production polish, full-stack quality passes, request/network optimization, or when every user action and failure path must work reliably. Also use when the user runs /harden-web-experience or says "harden this website", "make this production-ready", or "launch readiness".
---

# Harden Web Experience

Make the existing product trustworthy under success, failure, delay, abuse, concurrency, and real-world devices. Work in the real codebase. Preserve its design language, architecture, scope contracts, and unrelated changes.

When the user asks to fix, harden, optimize, or make the app production-ready, implement and verify improvements instead of stopping at an audit. When the user asks only for review or diagnosis, report evidence without changing code.

## Non-negotiable rules

- Read repository instructions and source-of-truth documents before acting.
- Inspect the current implementation before proposing a replacement. Reuse existing primitives and patterns.
- Never treat client-side visibility as authorization, a build as runtime proof, a scanner warning as a confirmed vulnerability, or a Lighthouse score as the whole user experience.
- Do not run destructive, intrusive, load, or exploit testing against production without explicit permission. Use local, test, or preview environments and disposable data.
- Do not expose secrets, personal data, tokens, raw exceptions, or sensitive request bodies in output, logs, fixtures, screenshots, or telemetry.
- Avoid speculative rewrites and dependency churn. Make the smallest coherent change that fixes the root cause.
- Record each claim as `confirmed`, `probable`, or `hypothesis`. Verify before fixing a hypothesis unless the change is independently required and low-risk.

## Load the right playbooks

- Always read [references/standards.md](references/standards.md) before choosing security, accessibility, performance, or operational requirements.
- Read [references/audit-playbook.md](references/audit-playbook.md) before mapping an unfamiliar codebase or prioritizing findings.
- Read [references/testing-playbook.md](references/testing-playbook.md) before adding or running browser, failure-injection, security, or performance tests.
- Read [references/product-states.md](references/product-states.md) when changing actions, forms, loaders, errors, empty states, destructive flows, or offline behavior.
- Read [references/production-readiness.md](references/production-readiness.md) for a launch-readiness or production-grade request, or whenever the app has a backend, persistent data, authentication, payments, uploads, jobs, email, third-party integrations, or deployment configuration.

If present, run `python scripts/repo_probe.py <repo>` from this skill to create a read-only first-pass surface map. Treat its matches as navigation signals, never findings.

## Phase 1: Establish the product contract

1. Check worktree status and preserve user changes. Identify package managers, frameworks, runtimes, test tools, deployment targets, environment/config handling, and existing quality commands.
2. Map routes, layouts, APIs, server actions, jobs, webhooks, data stores, caches, third parties, assets, authentication boundaries, roles, and tenant/ownership boundaries.
3. Identify the product's critical user journeys and business invariants. Include anonymous, authenticated, elevated, expired-session, first-time, returning, and empty-account experiences as applicable.
4. Build an action inventory for every request-backed or long-running control: create, read, update, delete, save, submit, login/logout, upload/download, search/filter, pagination, import/export, payment, sharing, retry, refresh, and background synchronization.
5. Trace each critical journey end-to-end:

   `user intent -> UI state -> client validation -> request -> trusted authorization/validation -> transaction/side effect -> response -> cache/state reconciliation -> visible feedback -> telemetry`

6. Establish a reproducible baseline: install state, environment blockers, lint/typecheck/tests/build, representative browser flows, console/network errors, accessibility scan if available, and cold/repeat performance measurements on key routes.

Do not create new product behavior from assumptions. Derive intended behavior from code, tests, schemas, copy, design primitives, planning documents, and existing routes. Ask only when a missing decision would materially change the product.

## Phase 2: Build an evidence-backed risk register

Record: journey/route, action, user role, data touched, failure mode, evidence, impact, likelihood, confidence, proposed correction, and verification method.

Prioritize in this order:

| Priority | Meaning |
| --- | --- |
| P0 | Exploitable access, secret or personal-data exposure, corruption/data loss, incorrect payment/entitlement, or production outage risk. |
| P1 | Broken critical journey, missing server authorization/validation, false success, duplicate mutation, unrecoverable user work, or severe accessibility failure. |
| P2 | Material slowness, confusing failure/empty state, stale data, partial keyboard/screen-reader failure, weak observability, or costly network waste. |
| P3 | Low-risk polish, maintainability, minor consistency, or preventive improvement. |

Fix confirmed P0/P1 issues first. Group related issues into vertical journey slices rather than broad technology-layer rewrites.

## Phase 3: Make every action reliable

For every inventoried asynchronous action:

- Model `idle`, `pending`, `success`, and `error`; add `empty`, `refreshing`, `offline`, `conflict`, or `partial` when the domain requires them.
- Show immediate local feedback. Disable only the initiating control when appropriate, preserve its context, expose progress text, and prevent accidental repeated submission.
- Make retry semantics explicit. Retry safe/idempotent reads with bounded backoff and cancellation when appropriate. Never automatically retry a non-idempotent write without an idempotency guarantee.
- Cancel or ignore superseded reads. Protect against stale responses, unmount updates, rapid filters, route changes, double clicks, multiple tabs, and out-of-order completion.
- Preserve user input on failure. Put validation errors next to the relevant field, focus the first invalid field when helpful, and provide an error summary for long forms.
- Reconcile caches deliberately after mutations. Confirm optimistic updates can roll back and that invalidation cannot cause a refetch storm or overwrite newer data.
- Distinguish validation, unauthenticated, forbidden, not found, conflict, rate limit, offline, timeout, dependency failure, and unexpected failure. Give a human-readable next action without leaking internals.
- Confirm success only after the trusted operation succeeds. If the result is ambiguous, say it was not confirmed and offer a safe recovery path.
- Announce status accessibly without flooding assistive technology. Preserve keyboard focus and never trap users inside a loader or toast.

Apply the detailed state and message contracts in `references/product-states.md`.

## Phase 4: Complete the production surface

Audit and improve every applicable dimension:

### Correctness and data integrity

- Enforce one clear source of truth per datum and make derived state deterministic.
- Validate at trust boundaries; use transactions/atomic operations for coupled writes; define uniqueness, referential, ordering, pagination, timezone, currency, locale, rounding, and boundary behavior.
- Handle concurrent edits, webhook retries, job retries, partial dependency failures, refresh/back navigation, and schema/version mismatches without silent loss or duplication.
- Make destructive actions intentional and recoverable where the domain permits. Clearly distinguish archive, remove, revoke, cancel, and permanent delete.

### Security and privacy

- Threat-model assets, actors, entry points, trust boundaries, and abuse cases. Verify server-side authentication, authorization, ownership/tenant isolation, input validation, output encoding, session/CSRF/CORS behavior, uploads/downloads, outbound URLs, secrets, cryptography usage, rate limits, dependencies, headers, logging, and exceptional conditions.
- Test direct API access and modified identifiers; do not infer protection from hidden controls.
- Minimize collected, returned, cached, logged, and retained data. Verify analytics/error reporting redact sensitive fields. Treat legal/compliance obligations as jurisdiction- and product-specific; flag them for qualified review instead of inventing compliance.

### Accessibility and inclusive interaction

- Target WCAG 2.2 AA unless the repository specifies a stronger contract. Use semantic HTML before ARIA.
- Verify keyboard order, visible focus, dialogs/menus, labels/instructions, error association, live updates, headings/landmarks, alternative text, contrast, zoom/reflow, reduced motion, pointer target size, touch behavior, and screen-reader names/states.
- Test manually as well as with automation; automated scans cannot establish conformance.

### Network and runtime performance

- Measure the same routes under cold and repeat caches, mobile viewport, and throttled network/CPU where possible. Inspect LCP, CLS, INP, document latency, critical request chains, render blocking, duplicate/failed/redirected calls, transfer size, compression, caching, images, fonts, JavaScript, long tasks, rerenders, and third parties.
- Remove duplicate/eager/unused work, request only necessary fields, paginate or virtualize large collections, share request state, define cache freshness/invalidation, compress text, right-size responsive media, reserve layout space, prioritize the true LCP resource, and defer noncritical code.
- Establish route-appropriate performance budgets from the measured baseline and product needs. Do not chase a score by breaking functionality, accessibility, analytics, or content.

### Product finish and discoverability

- Verify responsive layouts, touch and keyboard behavior, first-use guidance, empty search/filter results, permissions, 404/500 pages, offline/reconnect, account/session transitions, confirmations, undo/recovery, consistent copy, and visual stability.
- For public indexable pages, verify unique useful titles/descriptions, canonical intent, crawl/index controls, sitemap/robots behavior, semantic headings, link purpose, social previews, and valid structured data only where it truthfully matches visible content.
- Preserve the established product feel. Improve state coverage and clarity without turning the interface into generic component-library output.

### Operations and release safety

- Validate configuration at startup; fail safely on missing required values; keep secrets out of source/client bundles; separate environments.
- Add or improve actionable structured error reporting, correlation/request IDs, health/readiness behavior, user-centered metrics for critical journeys, and alert signals without sensitive or high-cardinality data.
- Verify schema/data migrations, background jobs, webhook idempotency, backup/restore expectations, deployment ordering, backward compatibility during rollout, and rollback/roll-forward paths where applicable.
- Keep CI checks reproducible and production builds free of debug behavior, source secrets, unsafe defaults, and environment-specific assumptions.

Use `references/production-readiness.md` as the completion matrix.

## Phase 5: Implement in vertical slices

For each highest-priority journey:

1. Reproduce the defect or missing state and capture evidence.
2. Add the narrowest useful failing test when feasible.
3. Fix the trusted boundary and data flow first, then client state and presentation.
4. Exercise success, slow, empty, expected failure, unexpected failure, duplicate/concurrent, expired/forbidden, and recovery paths that apply.
5. Run focused checks, inspect the diff, then run broader regression checks.
6. Record the verification and move to the next risk.

Continue while safe, in scope, and supported by evidence. If the full product is too large for one pass, leave a ranked, evidence-backed remainder; never present partial route coverage as complete production readiness.

## Phase 6: Prove readiness

Run every applicable gate:

- Repository formatting, linting, type checks, unit/integration tests, production build, dependency/security checks, and migrations or schema validation.
- Browser tests of critical journeys and all changed states with console and failed-request review.
- Role/ownership tests at the server boundary, including direct calls and identifier substitution.
- Keyboard and screen-reader-oriented checks, automated accessibility scan, mobile/reflow, and reduced-motion behavior.
- Cold/repeat and throttled performance/network comparison using identical conditions; real-user telemetry when available.
- Preview/staging smoke test, deployment configuration check, observability signal check, and rollback/migration readiness when authorized and available.

Do not mark a gate passed because a neighboring gate passed. A production build does not prove runtime behavior; an automated accessibility score does not prove WCAG conformance; local mocks do not prove third-party integration; and local performance does not prove field performance.

## Final output contract

Lead with one verdict:

- `READY`: all applicable critical gates passed and no known P0/P1 risks remain.
- `CONDITIONALLY READY`: implementation is strong, but named external or environment gates remain.
- `NOT READY`: a confirmed P0/P1 risk or broken critical journey remains.

Then report:

1. Critical journeys and surfaces covered.
2. Production issues fixed, grouped by impact rather than file.
3. Exact verification run and its result.
4. Comparable before/after measurements when available.
5. Remaining risks, blockers, and the next highest-value action.

Never claim complete coverage without an action inventory and recorded verification for every critical journey.
