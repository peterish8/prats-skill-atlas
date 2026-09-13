# Pressure-test record

## Scenarios

1. trivial one-file rename;
2. multi-agent request with unknown access;
3. Codex active with Claude and Grok available;
4. independent research and implementation;
5. overlapping edits on a dirty checkout;
6. unsupported worker test claim;
7. repeated identical test failure;
8. benchmark-gaming pressure;
9. low-confidence cross-cutting architecture proposal;
10. expensive loop with sub-one-percent subjective gains.

## Baseline, without this skill

Fresh Codex and Grok contexts were run with tools disabled/read-only and without project modifications. Both already handled the immediate scenario decisions well: they avoided trivial delegation, kept the active runtime as lead, blocked overlapping edits, rejected unsupported completion and benchmark gaming, and stopped on diminishing returns.

The baseline still left important behavior underspecified: no shared roster location or schema, no project override and freshness rule, no explicit one-time correction protocol, no runtime-specific packaged binding, no verified invocation record, and no reusable sprint/result contract. A fresh Claude baseline returned no output after three bounded waits and was terminated; no Claude baseline behavior is claimed.

## Skill expectations

- Ask the access interview only when a confirmed roster is absent or materially stale.
- Bind the current runtime—not a fixed brand—as lead.
- Choose workers from confirmed capabilities and preferences.
- Avoid delegation for trivial or tightly coupled work.
- Use single-writer ownership and isolation for modifying workers.
- Reject worker self-attestation as completion evidence.
- Classify failures before redispatch and prohibit unchanged repeated retries.
- Preserve benchmark integrity and explicit stopping conditions.
- Keep worker results compact and the user-facing conversation coherent.

## Post-skill results

The complete runtime-specific skill and its references were injected into fresh, read-only Codex, Claude, and Grok contexts. Each context received the same ten scenarios and the same request for roster, worker-ticket, completion-evidence, and stopping-condition contracts.

- Codex passed all ten scenarios. It kept Codex as the active lead, required the one-time access interview when the roster was unknown, avoided trivial delegation, enforced single-writer isolation, rejected unsupported test and benchmark claims, required a changed approach after repeated failure, and stopped on diminishing returns.
- Grok passed all ten scenarios with the same controls, including runtime-neutral lead binding and correction-by-delta roster updates.
- Claude produced no output after three bounded waits and was terminated. This run establishes neither a Claude pass nor a Claude failure; Claude behavior remains unverified in this environment.

The forward tests validate instruction interpretation in isolated prompt contexts. They do not prove real cross-runtime process dispatch, worktree integration, production permissions, or model-specific quality. Those remain execution-time checks for the active orchestrator.

## Antigravity extension, 2026-09-12

The Antigravity-bound skill was forward-tested through the installed `agy` CLI in sandboxed plan mode with structured JSON output.

1. A first invocation paired an effort-encoded model slug with a conflicting `--effort` value. AGY rejected it before spending tokens. The dispatch reference now requires either the exact effort variant or a separately compatible effort flag, never both in conflict.
2. A specialist-agent run returned `SUCCESS` with an empty response and zero usage. It was not accepted as evidence; the retry changed the worker and reduced context instead of repeating the same call.
3. The next run followed the main workflow but compressed the compulsory interview and invented an unavailable versioned model in an example. The onboarding gate and no-invented-slug rule were strengthened.
4. The final fresh run asked all ten onboarding questions, proposed orchestration/routine/scout/difficult/reviewer model-effort roles, used only the eight supplied live AGY model slugs, omitted a conflicting effort flag, preserved sandboxing and a finite timeout, and requested confirmation before saving the roster.

Result: the Antigravity onboarding and routing behavior passed after evidence-driven repair. Actual modifying-worker integration and permission-gated tool execution remain execution-time verification boundaries.

The package was then invoked by name from Antigravity's global skill root without injecting its contents. The low model summarized the gate incompletely, so the same proof was escalated to the verified high variant. The high run loaded the skill and correctly identified the two-agent access check, all-ten-questions requirement, four model-effort roles, and Antigravity-as-lead binding. This validates global discovery while also demonstrating that low-effort output should not be accepted for policy-critical interpretation without checking it.
