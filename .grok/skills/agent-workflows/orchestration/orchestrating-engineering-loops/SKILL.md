---
name: orchestrating-engineering-loops
description: Use when substantial software-engineering work may benefit from multiple agents, independent parallel tasks, extended implementation or debugging, benchmarking, or separate implementation and evaluation. Skip for trivial changes where delegation overhead exceeds its value.
---

# Orchestrating Engineering Loops

Lead → Contract → Fan-out → Execute → Evaluate → Repair → Integrate.

## Runtime binding

This copy is bound to Grok. Grok is the active orchestrator, principal engineer, integrator, and final evaluator for the current user conversation. Claude, Codex, and other confirmed agents are bounded workers, not peer orchestrators.

## First-use gate

Before delegating, load the project roster from `.orchestration/agent-roster.yaml`, otherwise the user roster from `~/.agents/orchestration/agent-roster.yaml`. If neither contains confirmed access that is still applicable, ask the access interview in [references/onboarding-and-roster.md](references/onboarding-and-roster.md) before proposing workers.

CLI detection is evidence that software exists, not proof that the user has access, budget, authorization, or a preferred model. Confirm those once, save them when the user agrees, and reuse the roster. When the user corrects a role, model, budget, or preference, update the roster delta instead of defending an old default or repeating the full interview.

## Lead responsibilities

The active orchestrator owns user intent, architecture, decomposition, dependency order, ambiguity, risky decisions, acceptance criteria, benchmark methodology, integration, and the final completion claim. Delegate bounded work; never delegate accountability.

Before substantial work:

1. Orient: inspect repository instructions, architecture and plans, current branch and dirty state, relevant implementation, and existing verification.
2. Define the outcome: what must work, what must not regress, and how each requirement will be proven. Do not invent numerical targets.
3. Decide whether delegation has positive value. Prefer a deterministic tool when it can answer reliably; do tiny or tightly coupled work directly.
4. Build a task graph only when it clarifies real units, dependencies, ownership, and verification.

## Routing workers

Choose workers from the confirmed roster by demonstrated capability, current access, cost, context capacity, and independence—not brand stereotypes. The current runtime remains lead whether it is Claude, Codex, Grok, or another compatible agent.

Delegation is useful when parallelism, specialization, context isolation, or independent verification outweigh startup cost, worker tokens, merge risk, and review effort. Read-only workers may intentionally overlap for cross-checking. Modifying workers must have non-overlapping ownership or run serially.

Never invent a CLI flag, model ID, reasoning level, API, or dispatch capability. Inspect the current interface before first use and record the verified invocation in the roster. If dispatch is unavailable, produce a compact handoff packet and continue without claiming a worker ran.

For non-trivial work, use the sprint and worker contracts in [references/contracts.md](references/contracts.md). Modifying workers should normally use isolated worktrees or equivalent checkouts. Preserve unrelated user changes; never solve coordination mistakes with destructive cleanup.

## Engineering control loop

1. Establish a reproducible baseline when debugging, optimizing, or benchmarking.
2. Dispatch only ready tasks whose dependencies, boundaries, output, and evaluator are clear.
3. Fan in concise results: inspect diffs, commits, evidence, benchmark artifacts, assumptions, and unresolved risks—not full transcripts.
4. Run progressive deterministic verification from the cheapest reliable check to affected, integration, regression, UI/device, or benchmark checks as applicable.
5. Keep builder and judge separate for meaningful or high-risk work. A worker's self-report is never sufficient evidence.
6. On failure, classify the cause before retrying. Retry only with new evidence, changed context, or a materially different approach.
7. If a failure class repeats, improve the harness—tests, diagnostics, invariants, docs, scripts, or task decomposition—instead of issuing another generic retry.
8. Integrate only accepted work, then verify the integrated state against the original contract.

Read [references/verification-and-recovery.md](references/verification-and-recovery.md) for the verification ladder, benchmark rules, failure taxonomy, and stopping policy.

## Context and communication

The user interacts with one coherent lead. Do not make them coordinate workers or read worker chatter. Keep durable state only for substantial work; prefer compact task, decision, failed-approach, and result artifacts under `.orchestration/` rather than transcript dumps.

Report what was delegated only when it affects cost, timing, authority, risk, or trust. Distinguish local proof, worker claims, deterministic evidence, and unverified external gates.

## Stop intentionally

Stop on verified success, diminishing returns, exhausted budget or retry limit, an external dependency, missing authority, unsafe scope, an unrealistic target, or a decision requiring user judgment. Never run an infinite improvement loop and never game tests or benchmarks to manufacture completion.

For the design basis and actual pressure-test record, read [references/research-notes.md](references/research-notes.md) and [references/pressure-tests.md](references/pressure-tests.md).
