# Verification by failure boundary

Read relevant sections only. Existing repository requirements take precedence. Additional infrastructure needs a real verification gap within authorized scope.

## Choose the smallest useful test

| Changed behavior | First useful check | Broaden when |
| --- | --- | --- |
| Calculation/parser/validator | Specified input/output unit tests | Consumers interpret results differently |
| Permission/ownership/persistence | Integration through the actual callable boundary | Multiple entrypoints/tenants share the rule |
| API/transport | Request/event validation and caller-consumer integration | Versions/retries/reconnect/ordering change |
| UI interaction | Component/integration check and running journey | Routing/auth/browser state/layout changes |
| Shared library/component | Consumer checks and existing regression suite | Many routes/packages consume it |
| Migration/destructive work | Representative fixture, invariants, failure/recovery, supported dry run | Existing-data compatibility or recovery needs separate proof |
| Copy/style only | Rendered inspection and applicable existing checks | Interaction/accessibility semantics change |

Coverage percentages and test counts are diagnostic signals, not readiness targets. Do not replace a missing boundary test with many trivial unit tests.

## Test strength

- Derive expectations from requirements, not implementation. Assert identity/state/persisted effect/denial/output; "did not throw" or "button exists" rarely proves a journey.
- For a bug, show the regression failing for that behavior before the fix and passing afterward when practical. If impractical, explain why and use another direct reproduction.
- Exercise real first-party logic/adapters locally. Substitute nondeterministic third parties deliberately. Do not mock away the auth/transaction/validation/retry/protocol boundary under test.
- Control test data, clock, IDs, and randomness where irrelevant to behavior. Reuse the repo's facilities.
- Denial tests must prove no unauthorized effect, not merely an error response.
- Select relevant boundaries: exact/over limit, wrong identity, stale version, duplicate delivery, partial failure. Avoid an exhaustive generic test checklist.
- A useful test rejects a plausible defect. For critical assertions whose strength remains uncertain, replay a counterexample or check a representative defect in an isolated disposable copy, then restore/reverify. Full mutation testing is optional, never a default expensive gate.
- Do not weaken assertions, blanket-update snapshots, suppress errors, or skip tests to match accidental behavior. Inspect snapshots against the actual contract.

## Authorization and private data

For changed protected behavior, exercise applicable cases: unauthenticated caller; wrong role; correct role accessing another user's/tenant's resource; authorized success; missing resource; expired/revoked access.

Call backend entrypoints directly for denial tests. Derive identity from trusted server context, not user-controlled role/owner fields. Validate public input and check ownership at the operation boundary. Inspect response fields and telemetry for private-data leaks. Use pseudonymous fixtures/test credentials; never print secrets or real sensitive content as proof.

## Persistence, migrations, and asynchronous work

- Check durable writes when required. Optimistic UI state is not persistence.
- For retries, test duplicate delivery and partial failure. Charge/create/append once when idempotency is required; do not retry non-idempotent actions blindly.
- For transactions/concurrency, exercise relevant interleavings or uniqueness constraints. Happy-path tests do not prove race safety.
- Verify applicable cancellation, stale response handling, disposal, and reconnect/recovery. Use observable readiness and bounded waits rather than arbitrary sleeps.
- For schema changes, identify old-data handling, reader/writer compatibility, restart/backfill, and backup/recovery implications. Test representative existing data. A reversible code commit does not make a migration reversible.
- Document required configuration names and failure behavior. Distinguish missing configuration from service outage; do not fabricate production defaults.

## API and realtime protocols

Exercise request/event validation and authorization at ingress. Select applicable malformed payloads, version compatibility, oversize inputs, revocation, duplicates/out-of-order delivery, disconnect, and reconnect.

Trace changed DTO/event through sender, validator, handler, persistence/relay, and receiver. Use an available dependency graph to find affected consumers, otherwise search references deliberately.

Multi-user behavior needs independent contexts/sessions with distinct identities. Assert the intended recipient's result and other participants' unchanged state. One session cannot prove isolation.

Classroom example, only where those product rules apply: teacher mutation succeeds; student direct mutation fails without scene changes; one student's camera movement leaves other cameras unchanged; manual movement exits follow only for that student.

## UI and browser behavior

- Use the user-requested browser surface. Otherwise reuse existing browser tools. Screenshots/source inspection do not substitute for required interaction.
- Reuse existing Playwright/component suites. Prefer scoped accessible role/label locators or stable explicit contracts. Do not select the first ambiguous match merely to hide a locator defect.
- Isolate contexts/test data. Use observable readiness and retrying assertions; avoid fixed sleeps or retrying side-effecting clicks.
- Assert the outcome, including stored/backend effect where required. HTTP success, navigation, or a visible container may precede usable state.
- Check relevant loading/empty/error/retry/disabled/success states. For layout, inspect narrow viewports/long content. For controls, inspect keyboard/focus/labels and reachable actions.
- Mock third parties for deterministic local tests; separately label authorized sandbox/live smoke checks when integration correctness needs them. Mocks do not prove credentials/deployment wiring.
- Inspect relevant console/network errors. Capture visual evidence and failure traces with existing tooling; avoid recording every successful run by default.
- Missing browser access/auth fixtures/environment means missing runtime proof. Continue local checks but report the journey as unverified.

## Commands, baseline, and final state

Discover commands from scripts, docs, configuration, and CI. Reuse installed package manager/lockfile and installed-version API docs.

Record the smallest useful before-state check when practical. For suspected baseline failures, compare the same command/environment against a safe isolated before-state copy. Never overwrite another person's edits or reset their checkout to obtain a baseline.

Record PASS / FAIL / NOT RUN / NOT APPLICABLE with command, scope, outcome, and reason. A skipped test is NOT RUN despite runner success. Timeout is not pass. Check for zero selected tests and confirm intended checks ran.

Run required gates before delivery; use affected checks while iterating. After fixes, rerun failed and dependent checks. Relevant code/config changes invalidate earlier evidence. Keep a reviewed/tested state identifier where useful, include new task files, and distinguish task edits from baseline dirty changes.

## Production claim boundary

Before a release claim, identify applicable runtime/configuration, integration, authorization, persistence, recovery, and observability evidence. Use existing authorized environments; do not add infrastructure for a generic checklist.

Report separately local checks, runtime journeys, authorized integrations, deployment/CI, and device/load evidence where relevant. Name unproven layers and baseline failures. If a necessary check is absent, use implemented with verification incomplete. Reduce optional scope when authorized rather than weaken checks.
