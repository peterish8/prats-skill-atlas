---
name: guardrail-metrics
description: "Choose metrics that prevent a growth experiment from winning by damaging trust, retention, quality, accessibility, performance, privacy, or economics. Use during experiment planning and launch review."
---

# Guardrail metrics

Define a small safety set that catches plausible harm without burying the decision in hundreds of metrics.

## Workflow

1. Identify how the intervention could harm users, systems, revenue quality, or another team even if the primary metric rises.
2. Choose two or three sensitive, interpretable guardrails tied to those mechanisms.
3. Define direction, acceptable change, measurement window, population, alert threshold, and operational owner.
4. Separate hard-stop safety metrics from decision-context metrics.
5. Ensure each guardrail is instrumented for both groups before exposure.
6. Review guardrails throughout rollout for operational safety and at the planned inferential readout for decision quality.
7. Document tradeoffs rather than averaging harm into a composite score.

## Deliverable

Return:
- harm-mechanism map
- guardrail definitions and thresholds
- monitoring and escalation owner
- rollback conditions
- tradeoff statement

## Guardrails

- Do not select guardrails merely because they are easy to measure.
- Avoid too many guardrails, which increases false alarms and obscures ownership.
- Never let conversion uplift erase serious safety, accessibility, privacy, or cancellation harm.

## Evidence baseline

- [Amplitude, Define experiment goals](https://www.amplitude.com/docs/feature-experiment/workflow/define-goals)
- [Mixpanel, Guardrail metrics](https://mixpanel.com/blog/guardrail-metrics/)
