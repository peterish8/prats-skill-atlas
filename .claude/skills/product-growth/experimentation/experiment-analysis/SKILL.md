---
name: experiment-analysis
description: "Validate and interpret controlled product experiments, separating data quality, statistical evidence, practical value, segments, and guardrails. Use at experiment readout or when results conflict."
---

# Experiment analysis

Reach a defensible decision without converting noisy or broken data into false certainty.

## Workflow

1. Freeze the declared analysis plan and identify any deviations before viewing preferred outcomes.
2. Verify allocation, SRM, exposure, telemetry completeness, crossover, implementation parity, and analysis population.
3. Report control and treatment counts, absolute metric values, effect estimates, intervals, and method.
4. Evaluate the primary metric first, then guardrails and pre-specified secondary metrics.
5. Distinguish statistical significance, practical significance, uncertainty, and business value.
6. Treat post-hoc segments and metric fishing as exploratory; apply multiplicity controls when relevant.
7. Investigate novelty, seasonality, network effects, delayed outcomes, and survivorship where applicable.
8. Issue a decision with rollout, rollback, follow-up measurement, and learning-log entry.

## Deliverable

Return:
- data-quality verdict
- primary and guardrail scorecard
- effect estimates with intervals
- pre-specified versus exploratory findings
- ship, iterate, rollback, continue, or inconclusive decision

## Guardrails

- Unexplained SRM blocks an ordinary winner decision.
- A non-significant underpowered test is inconclusive, not proof of no effect.
- A statistically significant but immaterial effect does not automatically justify shipping.

## Evidence baseline

- [Microsoft Research, Dirty Dozen metric pitfalls](https://www.microsoft.com/en-us/research/publication/a-dirty-dozen-twelve-common-metric-interpretation-pitfalls-in-online-controlled-experiments/)
- [Statsig, Managing SRM](https://docs.statsig.com/experiments/monitoring/srm)
