---
name: session-lessons
description: >
  End-of-session ledger for any codebase. Turns what happened in this session into durable,
  deduplicated records: mistakes into the repo's lessons log, choices into its decisions doc,
  distilled checkable rules into CLAUDE.md / AGENTS.md, and the user's preferences into memory.
  Use at the end of a coding session, or when the user says "record what we learned",
  "write the lessons", "update decisions", "add this to claude md so we avoid it",
  "session retro", "wrap up the session", or invokes /session-lessons.
---

# Session lessons

Record this session's mistakes, decisions, rules and preferences where the next session will
find them. Follow the steps in order. Do not skip a gate. Write nothing you cannot trace to
something that actually happened in this session.

Sources this follows: Claude Code memory docs (CLAUDE.md holds verifiable always-on rules, kept
under 200 lines; learnings and preferences go to memory), Nygard-style decision records (context,
decision, consequences; supersede, never rewrite), and blameless postmortems (what happened,
cause, fix, action; no blame).

## Step 1: Collect evidence

Do all of these before writing anything.

1. **Git.** Find the session's range: the commit the session started on if known, else
   `git merge-base HEAD <default-branch>`. Run `git log --oneline <base>..HEAD`,
   `git diff --stat <base>..HEAD` and `git status --short`. Note reverts, "fix" commits that
   follow "feat" commits for the same area, and version bumps.
2. **Conversation.** Walk the whole session and list every moment where:
   - the user corrected you, repeated a request, or said something was wrong or "still bad";
   - a test, typecheck, lint, build or deploy failed;
   - work was redone, reverted, or done twice to get it right;
   - something looked finished but was not (404, empty data, not deployed, never mounted,
     config missing);
   - an external API, tool, CLI or platform behaved differently than assumed;
   - a choice was made between real alternatives (design, architecture, product behaviour);
   - the user stated a taste, preference or working rule ("I want X", "never Y", "push to main ok").
3. **Production evidence** (only if tools allow and it is relevant): logs or status that confirm
   a root cause. Do not start deploys or paid work to collect evidence.

Gate 1: you have a numbered raw list. If it is empty, tell the user nothing qualified and stop.

## Step 2: Classify every item into exactly one bucket

| Bucket | What qualifies | Destination |
|---|---|---|
| LESSON | A mistake that happened or nearly shipped, with a known cause | Lessons log |
| DECISION | A choice someone could later undo by accident, with a reason | Decisions doc |
| RULE | A concrete, checkable instruction that would have prevented at least one LESSON in this repo | CLAUDE.md / AGENTS.md |
| PREFERENCE | The user's taste or working style, likely to apply again | Memory |
| DROP | One-off, already recorded, or derivable from code or git | Nowhere |

Gate 2, check every item:
- each LESSON has a symptom, a cause and a fix (file, command or commit);
- each RULE cites the LESSON it comes from and names a file, command, value or check; generic
  advice ("write tests", "be careful") is dropped;
- each DECISION states what was decided and why; if it replaces an earlier one, note what it supersedes;
- nothing contains secrets, tokens, keys, emails, or personal data. Mask them, or drop the item.

## Step 3: Find the destinations

Use the repo's existing conventions. Never create a parallel file when one exists.

- **Lessons log:** search for `LEARNING-LOG*`, `LESSONS*`, `lessons-learned*`, `docs/postmortems/`,
  `docs/incidents/`, `.planning/*LEARN*`. If none exist, create `docs/lessons.md` with a
  one-paragraph header saying what belongs there.
- **Decisions:** search for an ADR directory (`docs/adr/`, `adr/`, `decisions/`, `docs/decisions/`)
  and for `decisions.md` / `DECISIONS.md`. If an ADR directory exists, write one numbered file per
  decision using its template and numbering. Otherwise use or create `docs/decisions.md`
  (newest date first).
- **Rules:** the root `CLAUDE.md`, or `AGENTS.md` if that is what the repo uses. If `.claude/rules/`
  exists, add a rule file there instead. A rule that only concerns a sub-project goes in that
  sub-project's `CLAUDE.md`.
- **Preferences:** the harness's memory system if one is provided (follow its file format and
  index). If none, list them in the report instead.
- **Index:** if the repo has a docs index (`docs/README.md`), a new lessons or decisions file gets a row.

Read every destination fully before editing it. If an equivalent entry exists, update or extend it
instead of adding a second one.

## Step 4: Write with these exact templates

Dates are absolute (`YYYY-MM-DD`), never "today" or "yesterday". Lessons are past tense, rules
are imperative. Be specific: file paths, commands, numbers, error text. Blameless: describe what
the system and process did, not who erred.

**Lessons log entry** (one per session, items numbered):

```markdown
## YYYY-MM-DD — <area>: what went wrong

**1. <The symptom as someone saw it.>** <What happened, one or two sentences.>
*Cause:* <root cause>. *Fix:* <what changed: file, command or commit>. *Rule:* <one line, if any>.

**2. ...**

**Would do differently:** <one line that covers the pattern behind the items>.
```

**Decision in a decisions doc:**

```markdown
### <The decision, stated as a fact>
**Decided:** <what, precisely enough to check>.
**Why:** <the forces: constraint, evidence, user requirement>.
**Changes if:** <the condition that would reopen it>.
**Supersedes:** <link to the earlier decision> (only when replacing one)
```

**Decision as an ADR file** (when the repo uses ADRs): `NNNN-kebab-title.md` with
`# NNNN. Title`, `Date`, `Status: Accepted` (or `Superseded by NNNN`), `## Context`,
`## Decision`, `## Consequences`. Never rewrite an accepted ADR: add a new one and mark the old
one superseded.

**Rule in CLAUDE.md / AGENTS.md** (one line each, in a single section such as
"Before you call it done"; reuse an existing equivalent section):

```markdown
- **<When this applies>:** <the action, naming the command or file>.
```

**Preference in memory:** the memory system's own format, with **Why** (the session evidence) and
**How to apply**.

## Step 5: Keep CLAUDE.md lean

1. Count its lines first and after. Keep the file under 200 lines.
2. Add only RULE items. Put the story in the lessons log and point to it in one line.
3. If the budget is exceeded, compress or merge the rules you added (never delete the user's own
   rules); if still over, move the section to `.claude/rules/<topic>.md` or a linked doc and leave
   a one-line pointer.
4. If a rule could be enforced by a test, lint, type, script or CI check cheaply, list that in the
   report as a proposed guard. Build it only if the user asks.

## Step 6: Verify

- Re-read every diff you made.
- Every path, command, script and env var you mention exists: check with `ls`, `grep` or the
  project's tooling. Fix or remove anything that does not.
- No secrets, tokens, emails or personal data anywhere you wrote.
- No duplicate entries; the decisions doc stays newest first.
- Follow the repo's commit and attribution rules (some forbid AI footers).

## Step 7: Commit, then report

- Commit only if the user asked, or the session already established that docs changes get
  committed. Message: `docs: record <area> lessons and decisions`. Push only if asked.
- Report in the chat, short:
  - a table: destination, entries added or updated, counts;
  - dropped items in one line each, with the reason;
  - proposed structural guards (tests, lints, CI checks) that would make a rule unnecessary.

## Anti-patterns (each one fails the skill)

- Recording an incident that did not happen, or inventing a cause you did not confirm.
- Rules with no incident behind them, or rules nobody can check.
- Dumping a session narrative into CLAUDE.md.
- Two entries for the same lesson, or a new decision that contradicts an old one without superseding it.
- Editing an accepted ADR's decision in place.
- Relative dates, vague nouns ("the bug", "that file"), or secrets in any record.
- Skipping the conversation scan and recording only what git shows: user corrections never
  appear in git.
