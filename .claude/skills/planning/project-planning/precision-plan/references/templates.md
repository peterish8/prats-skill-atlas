# Templates

Paths are relative to the repo root. Keep a milestone in its own folder
(`.planning/<slug>/`) when the repo already has planning files you must not overwrite.

## PLAN.md (all depths; at Less it is the only file)

```markdown
# <Feature>: implementation plan

Status: draft for owner review, <date>. Nothing is built yet.

## 0. Rules for the implementing agent
Read first, in order: <rule files>.
Non-negotiable: <one line per house rule, plus: tests first; contract first; one commit per
task; stop and report when the code disagrees with this plan>.
Do not: <the traps found in the fact sweep, the things out of scope>.

## 1. What we are building
<Two or three short paragraphs: who it is for and what changes for them.>

## 2. Decision log
| # | Decision | Why |

## 3. Vocabulary
| Term | Meaning | Code name |

## 4. The model
<Data shapes, formulas, constants (one exported object), algorithms; simulation table if any.>

## 5. Data model
<Tables / schemas with indexes and size budget.>

## 6. Tasks            (Less: every task here. Medium/More: phase summaries, details in plan files)
### Phase N. <name>
**T1. <title>.** Files: … Steps: … Done when: <command + observable result>.

## 7. Cost and limits      ## 8. Edge cases      ## 9. Copy
## 10. Verification per phase      ## 11. Out of scope      ## 12. Sources
```

## ROADMAP.md (Medium, More)

```markdown
# Milestone: <name>
Spec: PLAN.md. Requirements: REQUIREMENTS.md (More). Progress: STATE.md (More).

## How to execute a plan
1. Read the plan fully. 2. Read every read_first. 3. Tasks in order; run verify and acceptance.
4. Code contradicts plan → write it in SUMMARY and stop. 5. One commit per task.
6. Write NN-MM-SUMMARY.md. 7. Update STATE.md.
Global gates: <commands>. <Registration rules found in the fact sweep.>

## Phases
| # | Phase | Goal | Depends on | Requirements |

### Phase NN: <name>
Plans:
- [ ] NN-01 <title> (wave 1)
Success criteria: <observable, numbered>
```

## REQUIREMENTS.md (More)

```markdown
## <Area> (phase NN)
- **ABC-01** <one testable sentence>
```
Ids are 2–5 capital letters, a dash, two digits. Every id must be claimed by at least one plan.

## STATE.md (More)

```markdown
| Plan | Status | Commit | Notes |
Owner actions outstanding: …
```

## Phase plan file: phases/NN-slug/NN-MM-PLAN.md (Medium: one per phase; More: 2–3 tasks each)

```markdown
---
phase: NN-slug
plan: MM
type: execute | tdd
wave: 1
depends_on: ["NN-MM"]          # earlier wave, or another phase
files_modified:
  - path/one.ts
autonomous: true               # false when a checkpoint task exists
requirements: [ABC-01]
user_setup: []                 # owner actions, if any
must_haves:
  truths:
    - "<observable behaviour a test or command can confirm>"
  artifacts:
    - path: path/one.ts
      provides: "<exports>"
  key_links:
    - from: <caller>
      to: <callee>
---

<objective>
<What and why, two to four sentences.>
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
@$HOME/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@<rule files>
@<exact source files the plan touches or copies patterns from>
</context>

<tasks>
<task type="auto" tdd="true">
  <name>Task 1: <action-oriented name></name>
  <files>path/one.ts, path/one.test.ts</files>
  <read_first>path/existing.ts (function name), path/rules.md</read_first>
  <action>
<Exact steps. Signatures in a code block. Constants with values. Copy text verbatim.
What not to do and why.>
  </action>
  <verify>exact command</verify>
  <acceptance_criteria>
    - path/one.ts contains "export function x("
    - test "duplicate is ignored" passes
  </acceptance_criteria>
  <done>One sentence.</done>
</task>

<task type="checkpoint:human-verify" gate="blocking">
  <what-built>…</what-built>
  <how-to-verify>Steps a person does, no CLI.</how-to-verify>
  <resume-signal>Type "approved" or describe issues</resume-signal>
</task>
</tasks>

<verification>
- [ ] <gate commands>
</verification>

<success_criteria>
- <requirement ids satisfied>
</success_criteria>

<output>
Write `phases/NN-slug/NN-MM-SUMMARY.md`.
</output>
```

Sizing: 2–3 tasks per plan, one subsystem per plan, waves so that plans in one wave touch
different files.
