# Research and rationale

Researched 2026-10-14 from primary sources. Verify current installed APIs when applying the workflow. Budget policy and task statuses are design choices for this user's constraints.

| Source | Supported practice | Adaptation |
| --- | --- | --- |
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Simplicity, complexity only when justified, environment feedback, stopping conditions | Main agent and executable checks; zero subagents by default; bounded optional reviewer |
| [Claude Code: Best practices](https://code.claude.com/docs/en/best-practices) | Specific context, appropriate planning, runnable checks, concise instructions, evidence | Compact acceptance contract, narrow exploration, completion tied to tested state |
| [Google: Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html) | Focused self-contained changes with related tests aid review and rollback | One coherent behavior slice and task-owned diff; no arbitrary line-count cap |
| [Google: Review contents](https://google.github.io/eng-practices/review/reviewer/looking-for.html) | Functionality, complexity, useful tests, context, relevant docs | Challenge implementation and assertions against product rules/consumers |
| [Google: Review standard](https://google.github.io/eng-practices/review/reviewer/standard.html) | Improve code health without perfection; evidence outranks preferences | Demonstrated defects drive repair; optional style does not block |
| [Playwright: Best practices](https://playwright.dev/docs/best-practices) | User-visible behavior, isolation, resilient locators, waiting assertions, controlled third parties | Real journeys, separate sessions, deterministic tests with explicit live-proof limits |

Anthropic's agent-pattern article originated in 2024 and notes evolved tooling. Its workflow principles inform this skill; historical framework/API examples are not implementation instructions.

## Local choices

- Zero or one reviewer is a total-task cap, not a concurrency cap. Same-model review is allowed; separate context does not remove shared model errors.
- Two repair cycles and one review follow-up are default cost controls after initial implementation. Smaller budgets win; exhaustion yields an incomplete report.
- Use risk-based tests. No universal coverage percentage, test count, quality score, or promise of bug-free code.
- Require no paid scanner, second subscription, or orchestration tool. Use available capabilities; report environment gaps.
- Load conditional detail only when relevant. More instructions do not inherently improve code.
- Reuse improves process consistency, not the underlying model automatically. Propose narrow changes after observed misses; skill/global-memory changes need authorization.

## Non-claims

This research does not verify creator PR/hackathon claims, universal vendor rankings, AI equivalence to human approval, or local-build equivalence to production reliability. Measure real outcomes before claiming efficiency gains.
