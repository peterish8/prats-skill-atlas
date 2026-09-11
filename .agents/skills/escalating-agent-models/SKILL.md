---
name: escalating-agent-models
description: Use when observable evidence shows the current model has stalled after meaningful recovery attempts, or a required capability is unavailable.
---

# Evidence-based model escalation

## Canonical ladder

Use this exact order. Start at level 1 and move exactly one level only when objective evidence justifies it:

1. **Luna 5.6 High** — runtime: `gpt-5.6-luna`, reasoning effort: `high`
2. **Terra Medium** — runtime: `gpt-5.6-terra`, reasoning effort: `medium`
3. **Terra High** — runtime: `gpt-5.6-terra`, reasoning effort: `high`
4. **Sol Medium** — runtime: `gpt-5.6-sol`, reasoning effort: `medium`
5. **Sol High** — runtime: `gpt-5.6-sol`, reasoning effort: `high`

Never reorder, skip a level because the work looks hard, or continue to a higher level after the current level succeeds and verification passes.

## Escalation threshold

Escalate only after the caller's recovery assessment finds a genuine stuck state: repeated materially different attempts with no progress, contradicted root-cause hypotheses, failing behavior after reasonable repair, an unresolved requirement/architecture contradiction, unverifiable critical research, or a true tool/capability gap. This skill consumes that evidence; it does not invoke a recovery skill itself.

Do not escalate for a typo, missing import/dependency, path correction, one repairable lint/test issue, incomplete context, transient tool failure, long request, or model-reported complexity. Correct those at the current level first.

## Handoff and runtime

Create a compact packet, separating facts from hypotheses:

```text
ORIGINAL TASK / SUCCESS CRITERIA
RELEVANT CONTEXT AND CONSTRAINTS
FACTS: files, commands, tests, logs, observed results
CHANGES AND MEANINGFUL ATTEMPTS
HYPOTHESES RULED OUT / UNRESOLVED QUESTIONS
CURRENT FAILURE
WHAT THE NEXT LEVEL MUST SOLVE AND VERIFY
```

If the active runtime exposes subagent dispatch with model and reasoning-effort parameters, dispatch only the next listed level and include this packet. The dispatch can select a child model; it cannot change an already-running primary model. If that dispatch is unavailable or prohibited, retain the packet and report the routing decision only when relevant. Never invent a command or claim a model switch that did not occur.
