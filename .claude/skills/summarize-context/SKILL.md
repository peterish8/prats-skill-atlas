---
name: summarize-context
description: Summarizes the entire current conversation into a structured, copy-paste context block for starting a new Claude chat with full continuity. Use when the user runs /summarize-context or asks to "summarize context", "make a context block", or "summarize for new chat".
user-invocable: true
---

Read the entire conversation from the beginning and produce a single context block using the exact format below. Do not add any preamble or explanation — output only the block itself.

Rules:
- Be exhaustive on "What Was Built / Decided" and "Key Code / Logic" — do not summarize away technical detail
- Paste all code, config, DNS records, commands, and file contents inline — never just describe them
- The reader of this block has zero prior context
- If nothing was coded (e.g. a setup/config conversation), leave "Key Code / Logic" with the relevant commands, values, or config used instead

---
## Project Context
[2-3 lines: what the project is, the tech stack, and the overall goal]

## What Was Built / Decided
[Exhaustive bullet list of every concrete decision, implementation, configuration, or architecture choice made in this conversation]

## Key Code / Logic
[Every important snippet, config value, DNS record, command, or file structure that was finalized — pasted inline verbatim]

## Last Thing We Were Working On
[The exact current task — what was just completed and what the immediate next step is]

## Important Rules / Preferences
[Any preferences the user stated about how Claude should respond — ask before acting, no assumptions, terse responses, etc. If none were stated, write "None stated."]
---
