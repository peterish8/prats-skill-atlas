# Agent access onboarding and roster

## Discovery order

1. Read `.orchestration/agent-roster.yaml` when the project intentionally overrides the user profile.
2. Otherwise read `~/.agents/orchestration/agent-roster.yaml`.
3. Inspect locally available interfaces and versions without mutating configuration.
4. Ask only for missing or stale facts that materially affect routing.

Do not expire a confirmed roster merely because time passed. Treat a fact as stale when the user says it changed, its recorded interface is unavailable or materially different, a project override conflicts with it, or the current task needs a missing access, permission, model, or budget fact.

The active runtime is the default orchestrator. Do not ask the user to select a permanent lead unless they want one; the same skill must work when opened from Claude, Codex, Grok, or another runtime.

## First-run interview

Ask these together before the first delegation plan. Accept short answers and `unknown`.

1. Which agents do you actually have access to—Claude, Codex, Grok, local models, or others?
2. How can each be invoked here: native subagent, desktop task, CLI, API, MCP, or manual handoff?
3. Which models and reasoning or effort levels are allowed or preferred for routine, difficult, and review work?
4. What is each agent especially good or poor at in your experience?
5. May workers edit files, or are some read-only/research-only?
6. Are isolated git worktrees available for modifying workers?
7. What concurrency, token, monetary, time, or rate limits should the lead respect?
8. Which actions require permission: external writes, pushes, deployments, production access, destructive commands, or paid calls?
9. Where should persistent orchestration state live: user-wide, project-local, or nowhere?
10. What would make the system feel correct for you, and what behavior should it never repeat?

Summarize the proposed roster and ask one confirmation before saving it. The interview authorizes saving preferences only in the chosen location; it does not authorize worker execution or external side effects.

## Roster schema

```yaml
schemaVersion: 1
confirmedAt: 2026-01-01T00:00:00Z
orchestratorPolicy: active-runtime
preferences:
  persistentScope: user
  maxConcurrentWorkers: 2
  modifyingWorkersRequireIsolation: true
  correctionPolicy: update-delta-once
agents:
  example-agent:
    available: true
    invocation:
      kind: cli
      command: example
      verifiedVersion: unknown
    models:
      routine: configured-default
      difficult: configured-default
      review: configured-default
    strengths: [bounded implementation]
    restrictions: []
permissions:
  externalWrites: ask
  destructiveCommands: ask
  productionAccess: ask
  paidCalls: ask
```

Store no tokens, cookies, API keys, session IDs, or credentials. Paths and versions are environment facts; recheck them cheaply before dispatch when they may have changed.

## Correction protocol

An explicit user correction outranks inferred preferences and prior roster defaults. State the changed field, apply it to the current plan, and—if persistence was approved—update only that field plus `confirmedAt`. Do not rerun the full interview unless the roster is broadly invalid.
