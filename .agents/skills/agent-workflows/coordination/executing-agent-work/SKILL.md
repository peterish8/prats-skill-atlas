---
name: executing-agent-work
description: Use while performing an approved implementation, repair, configuration change, or other bounded task after relevant context and constraints are known.
---

# Execute with discipline

Implement the requested outcome using repository evidence, applicable specialist skills, and existing project patterns. Keep scope tight: do not refactor unrelated areas, add dependencies, or broaden external effects without a demonstrated need and authority.

After a meaningful change, inspect the diff and record what changed plus the intended validation. If the task encounters failure, do not guess or repeat the same action: hand the evidence to `recovering-agent-failures`.

The only completion state this skill may produce is:

```text
IMPLEMENTATION COMPLETE — READY FOR VERIFICATION
```

`verifying-agent-work` determines whether the requested outcome is actually complete.
