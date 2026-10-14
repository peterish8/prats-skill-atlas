---
name: recovering-agent-failures
description: Use after a verification, tool, research, or implementation attempt fails and you need a diagnosis before retrying or escalating.
---

# Recover before escalating

Classify the observed failure: context, implementation, test, tool, environment, dependency, reasoning, capability, or transient. Preserve the exact symptom, command/output, changed area, and what would count as improvement.

Retry at the current level only when the next attempt adds meaningful change: new evidence, a different hypothesis, another appropriate tool, missing context, a smaller reproduction, or a materially different implementation strategy.

| Situation | Response |
| --- | --- |
| Missing context, typo, import, format issue, transient tool error | Correct or gather evidence, then retry and verify. |
| Wrong interface | Use `routing-agent-tools`, change interface, then retry. |
| Evidence contradicts hypothesis or same approach has no progress | Stop repeating it and prepare an escalation handoff. |
| Conflicting evidence | Gather more facts or request `cross-checking-agent-work`. |
| Unsafe/destructive state | Stop, inspect and stabilize changes before continuing. |

Do not decide a level merely feels uncertain. When meaningful progress has stalled or a capability is genuinely missing, invoke `escalating-agent-models` with the evidence packet.
