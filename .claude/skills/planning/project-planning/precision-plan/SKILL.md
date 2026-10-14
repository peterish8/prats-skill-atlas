---
name: precision-plan
description: Write an implementation plan so exact that a small or cheap coding agent (Codex mini, Haiku, a "luna" worker) can build it with the precision of a top model. Grounds every instruction in the real code, settles decisions with reasons, simulates any formula before committing to it, and writes GSD-format phases and plans with files, signatures, tests and done-checks. Asks one question first: Less, Medium or More detail. Use when the user says "precision plan", "detailed plan any agent can code", "plan so a normal agent codes like Opus", "GSD-style plan", "hardened implementation plan", or invokes /precision-plan.
---

# Precision plan

A plan is good when an agent with no context and modest skill cannot get it wrong. That takes
three things a normal plan skips: facts checked in the code instead of assumed, decisions written
down with their reasons, and every task closed by a check the agent runs itself.

## Step 0. Ask the depth (one question, nothing else first)

Use AskUserQuestion with exactly these three options. Recommend the one that fits the size of
the work (a single feature in one area → Medium; a multi-area feature with data, API and UI →
More; a bug or a small change → Less).

| Option | What gets written | Typical files |
|---|---|---|
| **Less** | One `PLAN.md`: goal, decision log, ordered tasks, each with files, steps and a done-check. | 1 |
| **Medium** | `PLAN.md` (spec and decisions) + `ROADMAP.md` (phases, order) + one plan file per phase with its tasks. | 4–12 |
| **More** | The full GSD tree: `PLAN.md` spec, `ROADMAP.md`, `REQUIREMENTS.md` (testable ids), `STATE.md`, and `phases/NN-slug/NN-MM-PLAN.md` files of 2–3 tasks each in GSD `execute` format, plus any simulation script and fixtures. Validated by `scripts/check-plans.mjs`. | 20–50 |

Put the option descriptions in the question so the user sees the file counts before choosing.
If the user already named a depth, skip the question.

## Step 1. Read the house rules

Before planning anything, read whatever the repo uses to state its rules, in this order:
`CLAUDE.md` / `AGENTS.md` (root and per app), architecture docs, the API contract, and any
platform guideline file the repo points to (for example `convex/_generated/ai/guidelines.md`).
Every rule you find becomes a line in the plan's "Rules for the implementing agent" section.
A small agent will not go looking for them.

## Step 2. The fact sweep (the part that makes plans work)

Answer each question in [references/fact-checklist.md](references/fact-checklist.md) from the
code, with a file and line, before writing tasks. Use the repo's code-search tool (graft, grep)
and read the spans. Most failed plans fail on one of these: a shared file the API cannot import,
a test file the test script never runs, a request body limit, a batch cap, a deep-link scheme
that is not what you assumed.

Record each answer in a "Facts" section of the working notes. Any fact you could not confirm
becomes a `read_first` instruction plus a "stop and report if different" line in the task.

## Step 3. Outside facts

When the work depends on a third party (an API's quota, a file format, a platform rule), look
it up with the user's preferred research tool (default Firecrawl, then Context.dev), cite the
URL in the plan's Sources, and write the constraint as a decision. Never write a file format or
API field from memory. If a real sample is needed (an export file, a webhook body), make getting
it the first plan, as a `checkpoint:human-action`.

## Step 4. Decisions

Build a decision log: `| # | Decision | Why |`. Technical decisions: make them yourself from
best practice and the facts, unless the user wants to weigh in. Product decisions (who sees
what, limits a user feels, copy, privacy): ask in rounds, grilling style, numbered with your
recommendation, only the questions whose prerequisites are settled. When the user says "you
decide", decide, and keep the reason in the log so they can veto later.

## Step 5. Prove any formula before writing it

If the plan contains a score, ranking, pricing rule, decay, matching threshold or any algorithm
with tuning constants: write a throwaway simulation (a single `.mjs` file) over synthetic cases
that cover the extremes (identical, unrelated, thin data, one huge input, a broad vs a narrow
case). Run it. If an obvious case gives a silly number, change the formula and run again. Record
the final results as a table in the plan, ship the script next to the plan, and make the table's
**ordering** (not exact numbers) the acceptance test. Keep every constant in one exported object.

## Step 6. Write it

Use the templates in [references/templates.md](references/templates.md) for the chosen depth.
Writing rules, all depths:

- **Concrete values only.** Exact file paths, function names, signatures, constants, copy
  strings, status codes, limits. Never "align X with Y" or "handle errors appropriately".
- **`read_first` on every task**, naming the exact files and functions to read, because line
  numbers drift.
- **Every task ends with `verify` (a command that exists in this repo) and grep-able acceptance
  criteria.** "Tests pass" is not a criterion; "file contains 'X'" and "test named Y passes" are.
- **Tests first** where behaviour is testable: one commit with failing tests, one with the code.
- **Contract first** for any API change: the doc edit is the first task of the plan.
- **One source of truth.** If two copies of a helper exist, the plan merges them before
  building on them.
- **Bounded everything:** caps on reads, batches, list sizes, timeouts, retries, each with a
  test.
- **Privacy and retention:** new stored data gets disclosure text, erase, export and a
  retention rule in the same phase that stores it.
- **Flags:** new user-facing features ship behind a boolean flag, off by default.
- **Checkpoints** only for what an agent cannot do: getting a real sample, credentials, a
  device, human visual approval.
- **Stop-and-report rule** in every plan: when the code contradicts the plan, the agent writes
  what it found and stops; it does not improvise.
- **No debug routes, query-parameter switches or dev-only endpoints** as a way to test states.
- Write the prose clean: short sentences, no filler, no stock AI phrasing.

## Step 7. Check it

- More: run `node <skill-dir>/scripts/check-plans.mjs <planning-dir>`. It fails on uncovered
  requirement ids, unknown ids, missing frontmatter, tasks missing `files` / `read_first` /
  `action` / `verify` / `acceptance_criteria` / `done`, missing dependencies and same-wave
  dependencies. Fix until it prints `ok`.
- All depths: re-read the plan once as the weakest agent that might run it. For each task ask:
  could I do this without guessing a name, a path, a limit or a format? If not, add the fact or a
  `read_first`.
- Write files with LF line endings.

## Step 8. Report

Tell the user: depth chosen, files written (paths as links), the decisions you made for them,
facts that changed the plan, what blocks the start (owner actions, samples, credentials), and
the checker's output. Keep it short.
