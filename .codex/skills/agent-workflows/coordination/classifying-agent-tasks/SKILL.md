---
name: classifying-agent-tasks
description: Use before a substantive task when execution, verification, tools, context, risk, or decomposition need to be chosen deliberately.
---

# Classify the task

Create a compact working classification before choosing an approach. This skill does not choose a model; use `escalating-agent-models` for that decision.

Capture only decision-relevant fields:

```text
type: coding | debugging | research | design | configuration | planning | file-operation | testing | deployment
scope: tiny | bounded | broad
risk: low | medium | high
needs: repository context, external evidence, browser/computer interaction, runtime verification, independent review
constraints: user authority, project rules, reversibility, sensitive systems
```

Use the classification to decide whether to gather project context, decompose work, select a specialist skill, and verify. Revise it when observed evidence changes the task. Do not confuse uncertainty, a long prompt, or a large repository with model failure.
