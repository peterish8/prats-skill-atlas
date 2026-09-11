---
name: parallelizing-agent-work
description: Use when a task contains multiple candidate workstreams and you need to decide whether concurrent agent work is safe and worthwhile.
---

# Route parallel work safely

Parallelize only when work has no unmet dependency and does not contend for the same critical files, schema, mutable state, external resource, or unresolved decision.

Good candidates include independent architecture inspection, log analysis, source research, and read-only comparison. Keep schema -> API -> UI sequential until the upstream contract is settled.

Before dispatching, state internally: purpose, bounded inputs, expected artifact, allowed files, and integration owner. Prefer read-only parallel discovery when writes could collide. If the elapsed-time benefit is small or coordination cost is high, work sequentially.

Use `escalating-agent-models` for any model choice; this skill does not escalate merely because work is parallel.
