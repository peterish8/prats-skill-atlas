---
name: caveman-poteto-unslop
description: Run rigorous work in Poteto Mode, design deep modules when structure matters, answer concisely in Caveman mode, and remove AI writing tells with Unslop. Use when the user wants this combined workflow.
---

# Caveman, Poteto, and Unslop

Read and apply these skills for this task, in this order.

1. [Poteto Mode](C:\\Users\\nithy\\.codex\\skills\\poteto-mode\\SKILL.md). It owns task planning, engineering choices, verification, and autonomy.
2. [Codebase Design](C:\\Users\\nithy\\.agents\\skills\\codebase-design\\SKILL.md). Use it when the task changes code structure, module ownership, or a module's interface. It owns the module, interface, depth, seam, adapter, leverage, locality, and deletion-test analysis.
3. [Caveman](C:\\Users\\nithy\\.agents\\skills\\caveman\\SKILL.md). It owns response compression. Use its default `full` level unless the user selects another level or clarity requires normal prose.
4. [Unslop](C:\\Users\\nithy\\.codex\\skills\\unslop\\SKILL.md). It owns the final prose pass. Keep the response concrete, direct, and free of stock AI phrasing.

## Conflict handling

Safety and clarity win. Poteto controls how work is done. Codebase Design controls structural reasoning when it applies. Caveman controls how concisely work is reported. Unslop improves wording without adding length or changing technical meaning.

## What each skill adds

- Poteto Mode makes work deliberate, verified, and willing to push back on bad scope.
- Codebase Design finds modules that earn their complexity and rejects pass-through layers.
- Caveman keeps the final response short without dropping technical facts.
- Unslop removes filler, fake polish, and chatbot voice.
