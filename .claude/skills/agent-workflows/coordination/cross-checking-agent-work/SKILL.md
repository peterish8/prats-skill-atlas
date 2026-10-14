---
name: cross-checking-agent-work
description: Use when an independent second opinion would materially reduce risk for an important, uncertain, security-sensitive, or surprising result.
---

# Seek independent evidence when it earns its cost

Use an independent check for difficult bugs, consequential architecture choices, significant refactors, production/security changes, conflicting evidence, or a major feature whose confidence is otherwise weak. Do not use it ceremonially for trivial, well-verified work.

Give the reviewer the original question, relevant facts, reproduction or acceptance criteria, and necessary context. Do not lead with the first agent's conclusion. Separate observations from interpretations so the reviewer can disagree.

Compare conclusions:

- Agreement raises confidence but does not replace task-appropriate verification.
- Disagreement means investigate the concrete divergence.
- A newly discovered risk must be addressed and reverified.

This skill requests an independent perspective; `escalating-agent-models` owns model-level escalation and handoff policy.
