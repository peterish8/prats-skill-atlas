# Experiment rigor

Use this reference when planning, launching, or interpreting a controlled experiment.

## Design contract

Define before launch:

- decision and hypothesis;
- eligible population and exclusions;
- randomization unit, assignment key, allocation, and persistence;
- control and treatment behavior;
- exposure event and analysis window;
- one primary metric, a small set of secondary metrics, and two or three guardrails;
- baseline rate, minimum detectable effect, significance level, power, and target sample or duration;
- fixed-horizon, sequential, or Bayesian analysis method;
- stop, rollback, and segment-analysis rules.

Sample size is not a universal number. It depends on baseline variance or rate, effect worth detecting, Type I error, power, allocation, clustering, and expected attrition. If these inputs are unavailable, report that the test is not yet power-planned.

## Instrumentation contract

- Randomize on a stable unit that matches the intervention and analysis.
- Keep assignment sticky across sessions and devices when the product identity model permits it.
- Log assignment separately from actual exposure; analyze users only according to the declared estimand.
- Version experiment, variant, event schema, and metric definitions.
- Ensure exposure cannot occur after the outcome it claims to affect.
- Run an A/A or equivalent pipeline check when the experimentation path is new or materially changed.

## Trust checks before lift

1. Confirm expected allocation against observed allocation. An unexplained sample-ratio mismatch invalidates ordinary interpretation.
2. Check missing events, duplicate events, bot/internal traffic, crossover, variant jumping, delayed logging, and inconsistent eligibility.
3. Confirm the treatment shipped as designed and no unrelated release changed one group differently.
4. Review absolute counts and confidence intervals, not only percentage lift and p-values.
5. Treat post-hoc slices as exploratory unless multiplicity was controlled or the segment was pre-specified.

## Reading results

- `Significant and practically valuable`: consider rollout if guardrails and quality checks pass.
- `Significant but too small`: do not ship solely because the p-value crossed a threshold.
- `Not significant and adequately powered`: evidence does not support the target effect; consider stopping or reformulating.
- `Not significant and underpowered`: call it inconclusive, not neutral or failed.
- `Guardrail harm`: investigate and usually hold or rollback even if the primary metric improved.
- `SRM or broken telemetry`: diagnose first; do not choose a winner.

Fixed-horizon tests permit one planned inferential readout. Repeatedly checking and stopping on significance inflates false positives. If the business requires early decisions, choose and document a sequential method before using early readouts.

## Core sources

- Microsoft Research, [Diagnosing Sample Ratio Mismatch in Online Controlled Experiments](https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/), 2019.
- Microsoft Research, [A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls](https://www.microsoft.com/en-us/research/publication/a-dirty-dozen-twelve-common-metric-interpretation-pitfalls-in-online-controlled-experiments/), 2017.
- NIST, [Sample sizes required](https://www.itl.nist.gov/div898/handbook/prc/section2/prc222.htm).
- Statsig, [Frequentist Sequential Testing](https://docs.statsig.com/experiments/advanced-setup/sequential-testing).
- Statsig, [Managing Sample Ratio Mismatch](https://docs.statsig.com/experiments/monitoring/srm).
