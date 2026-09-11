---
name: ab-test-planning
description: "Design trustworthy randomized product experiments with clear assignment, exposure, metrics, power, duration, and stopping rules. Use before implementing or launching an A/B test."
---

# A/B test planning

Produce an experiment specification that engineering, analytics, product, and review stakeholders can execute and audit.

## Workflow

1. State the decision, hypothesis, population, eligibility, exclusions, and expected mechanism.
2. Choose the randomization unit and stable assignment key; address cross-device identity, shared accounts, and interference.
3. Define control, treatments, allocation, exposure event, analysis window, and implementation parity.
4. Choose one primary metric, limited secondary metrics, and two or three guardrails.
5. Estimate baseline, minimum detectable effect, significance level, power, sample size, duration, and seasonality coverage.
6. Declare fixed-horizon, sequential, or Bayesian method and all stopping rules before launch.
7. Pre-specify segments and multiplicity handling; make all later cuts exploratory.
8. Add A/A, SRM, crossover, telemetry, rollback, accessibility, privacy, and policy checks.

## Deliverable

Return:
- complete experiment brief
- metric and event definitions
- power and duration assumptions
- quality and rollback checklist
- planned analysis and decision rules

## Guardrails

- Never choose sample size from a generic rule of thumb.
- Do not repeatedly peek at a fixed-horizon test to decide when to stop.
- Do not launch without stable assignment and actual-exposure logging.

## Evidence baseline

- [NIST, Sample sizes required](https://www.itl.nist.gov/div898/handbook/prc/section2/prc222.htm)
- [Statsig, Sequential Testing](https://docs.statsig.com/experiments/advanced-setup/sequential-testing)
- [Microsoft Research, SRM taxonomy](https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/)
