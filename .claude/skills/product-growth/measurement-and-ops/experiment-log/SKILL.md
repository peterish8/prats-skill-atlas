---
name: experiment-log
description: "Create and maintain a searchable record of product hypotheses, implementations, metrics, results, decisions, and reusable learning. Use when teams repeat tests or lose experiment context."
---

# Experiment log

Preserve institutional memory so negative, inconclusive, and positive results improve future decisions.

## Workflow

1. Assign a stable experiment ID and record owner, dates, product version, cohort, platform, and links to code or flags.
2. Store the pre-launch hypothesis, evidence, variants, metrics, power assumptions, and decision rules before results.
3. Capture implementation changes, incidents, exclusions, analysis deviations, and data-quality status.
4. Record estimates, intervals, guardrails, segments, practical significance, and final decision.
5. Separate reusable learning from context-specific result and list where the result should not be generalized.
6. Link follow-up experiments, rollout, rollback, and long-term measurement.
7. Use consistent tags and searchable fields without overwriting prior conclusions.

## Deliverable

Return:
- auditable experiment record
- decision and evidence trail
- generalization boundary
- follow-up links
- portfolio-level learning tags

## Guardrails

- Do not delete losing or inconclusive experiments.
- Never rewrite a pre-registered hypothesis after seeing results.
- Keep personal data and raw participant material outside the general experiment log.

## Evidence baseline

- [Amplitude, Product-led experimentation guide](https://amplitude.com/blog/product-led-experimentation-guide)
- [Microsoft Research, Dirty Dozen metric pitfalls](https://www.microsoft.com/en-us/research/publication/a-dirty-dozen-twelve-common-metric-interpretation-pitfalls-in-online-controlled-experiments/)
