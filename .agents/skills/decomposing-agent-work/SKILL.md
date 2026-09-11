---
name: decomposing-agent-work
description: Use for broad work that benefits from coherent, dependency-aware implementation units; do not use to fragment a small task.
---

# Decompose meaningful work

Split only when it improves correctness, sequencing, or reviewability. Give each unit a clear outcome, owner/area, prerequisites, and verification signal.

Mark relationships explicitly when useful:

```text
schema -> API -> UI -> integration verification
```

Independent discovery may proceed together; dependent design and implementation must wait for their inputs. Avoid splitting tightly coupled changes across agents or creating tasks merely to appear agentic. Keep integration and end-to-end verification as real final units rather than assuming independently completed pieces compose correctly.
