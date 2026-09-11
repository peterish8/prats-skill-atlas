---
name: gathering-project-context
description: Use before modifying an existing repository when targeted evidence about its architecture, conventions, or affected code is needed.
---

# Gather targeted project context

Start from the requested outcome and inspect the smallest useful evidence set: repository instructions, status/diff when relevant, manifests, the directly affected source, adjacent patterns, tests, schemas, and configuration. Search before broad reading.

Produce a compact internal brief:

```text
Stack and entry points:
Relevant files and existing pattern:
Constraints and project instructions:
Likely impact and validation path:
Unknowns that block a safe change:
```

Prefer source-of-truth evidence over generic framework assumptions. Preserve unrelated changes. Do not blindly scan the whole repository; widen exploration only when the current evidence cannot answer a necessary question.
