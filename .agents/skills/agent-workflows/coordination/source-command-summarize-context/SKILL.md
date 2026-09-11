---
name: "source-command-summarize-context"
description: "Summarize the entire conversation into a copy-paste context block for a new Codex chat"
---

# source-command-summarize-context

Use this skill when the user asks to run the migrated source command `summarize-context`.

## Command Template

Read the entire conversation from the beginning and produce a single context block using the exact format below. Do not add any preamble or explanation — output only the block itself.

Rules:
- Be exhaustive on "What Was Built / Decided" and "Key Code / Logic" — do not summarize away any technical detail
- Paste all code, config, DNS records, commands, and file contents inline — never just describe them
- The reader of this block has zero prior context
- If nothing was coded (e.g. a setup/config conversation), put the relevant commands, values, or config in "Key Code / Logic" instead

---
## Project Context
[2-3 lines: what the project is, the tech stack, and the overall goal]

## What Was Built / Decided
[Exhaustive bullet list of every concrete decision, implementation, configuration, or architecture choice made in this conversation]

## Key Code / Logic
[Every important snippet, config value, DNS record, command, or file structure that was finalized — pasted inline verbatim, never summarized]

## Last Thing We Were Working On
[The exact current task — what was just completed and what the immediate next step is]

## Important Rules / Preferences
[Any preferences the user stated about how Codex should respond — ask before acting, no assumptions, terse responses, etc. If none were stated, write "None stated."]
---
