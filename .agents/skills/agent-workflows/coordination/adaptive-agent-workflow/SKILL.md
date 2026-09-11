---
name: adaptive-agent-workflow
description: Coordinate a development or general-agent task through targeted context, execution, evidence-based verification, recovery, and justified model escalation. Use for ordinary substantive requests without requiring the user to manage the workflow.
---

# Adaptive agent workflow

Keep the user experience simple: make routing decisions internally and mention them only when they materially affect the work, require authority, or explain a limitation.

## Scale the workflow

- Tiny, reversible task: understand -> execute -> lightweight verification.
- Bounded implementation or diagnosis: classify, gather targeted context, execute, verify.
- Broad, risky, or uncertain work: additionally decompose, identify truly independent work, select specialist skills, and consider an independent cross-check.

Do not turn every request into a committee. Do not read an entire repository when the affected area can be found through targeted inspection.

## Lifecycle

1. Use `classifying-agent-tasks` to establish scope, risk, required evidence, and interfaces.
2. Use `gathering-project-context` before changing an existing codebase. Use `decomposing-agent-work` only when it clarifies meaningful units and dependencies. Use `parallelizing-agent-work` only for independent work.
3. Select a specialist skill when the task needs domain-specific guidance. Use `routing-agent-tools` to choose the most reliable execution interface.
4. Start the requested substantive work at level 1 through `escalating-agent-models`; use `executing-agent-work` to make changes.
5. Use `verifying-agent-work`. Implementation is only ready for verification, never automatically complete.
6. On a failed check, use `recovering-agent-failures`. Retry the current level only with new evidence or a materially different approach; otherwise use `escalating-agent-models` to hand off to exactly the next level.
7. For high-impact or unresolved work, use `cross-checking-agent-work`, reconcile evidence, and verify again. Finish only with evidence and precise limits.

## Dispatch boundary

This skill is routing policy, not a hidden scheduler. When the active runtime exposes subagent dispatch with explicit model and reasoning-effort selection, dispatch the current level with the mapping in `escalating-agent-models`; preserve the compact handoff. Do not claim that the already-running primary agent was switched. If dispatch is unavailable or disallowed, keep the decision and handoff packet, explain the limitation only if it matters, and continue within the available runtime.

Micro-skills are on-demand guidance, not mandatory nested invocations. This skill is the sole composition layer, so do not create mandatory circular chains among them.
