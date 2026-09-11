# Research notes

Reviewed 2026-09-12.

## Convergent findings

- OpenAI's harness-engineering account emphasizes that a lead specifies intent and builds feedback loops while agents execute; repository knowledge, worktree-legible environments, mechanical architecture constraints, self-review, independent review, and continuous maintenance make autonomy reliable.
- Anthropic's long-running application work separates planner, generator, and evaluator, uses explicit criteria, and carries state through structured artifacts and context resets. Separate evaluation mitigates over-generous self-assessment.
- Anthropic's multi-agent research system shows strong value for broad, independent parallel work but much higher token cost and weaker fit for tightly coupled work. Worker prompts need objectives, boundaries, tools, and output formats.
- Anthropic's parallel compiler experiment demonstrates task ownership, isolated checkouts, strong tests, compact progress artifacts, and specialization, while also warning that an infinite loop belongs in a contained research harness rather than a normal workstation workflow.
- SWE-agent's Agent-Computer Interface work supports immediate syntax feedback, concise file/search interfaces, and explicit successful-empty output so agents receive useful deterministic feedback without context noise.

## Design decisions

1. **Runtime-neutral lead:** the agent currently talking to the user is the orchestrator. Permanent `Claude = lead` wiring would fail when Codex or Grok loads the same skill.
2. **Roster before routing:** user access, invocation methods, models, budgets, and permissions are environment data. Ask once, persist with consent, and allow project overrides.
3. **Capability-based workers:** roles follow confirmed strengths and task needs, not vendor stereotypes. User-specific preferences belong in the roster.
4. **Delegation economics:** multi-agent work is conditional because coordination and token costs can exceed its value.
5. **Deterministic truth first:** tests and artifacts outrank worker confidence; a separate evaluator is added when risk justifies it.
6. **Finite repair loop:** failures are classified, retries must change something, repeated failure improves the harness, and explicit stop conditions prevent runaway cost.
7. **Thin entrypoint:** detailed onboarding, contracts, and verification rules remain in references so ordinary invocations load only the control loop.

## Sources

- https://openai.com/index/harness-engineering/
- https://www.anthropic.com/engineering/harness-design-long-running-apps
- https://www.anthropic.com/engineering/multi-agent-research-system
- https://www.anthropic.com/engineering/building-c-compiler
- https://github.com/SWE-agent/SWE-agent/blob/main/docs/background/aci.md
