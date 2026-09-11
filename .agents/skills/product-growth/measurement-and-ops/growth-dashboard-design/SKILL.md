---
name: growth-dashboard-design
description: "Build decision-focused dashboards for acquisition, activation, engagement, retention, monetization, and experiment health. Use when metric sprawl or inconsistent definitions blocks action."
---

# Growth dashboard design

Give each audience a small, traceable view of product health and the decisions they own.

## Workflow

1. Define dashboard audience, decisions, review cadence, and accountable metric owners.
2. Create a metric tree linking user value and business outcomes to controllable inputs.
3. Specify formula, unit, population, exclusions, time zone, attribution window, source, freshness, and owner for every metric.
4. Separate health trends, funnel diagnostics, cohorts, experiment scorecards, and alerts rather than mixing them into one number wall.
5. Show rates with denominators and absolute counts; include uncertainty and data freshness where relevant.
6. Add segment and cohort controls that answer known questions without encouraging post-hoc fishing.
7. Validate dashboard values against source queries and document discrepancies.

## Deliverable

Return:
- audience and decision map
- metric tree and data dictionary
- dashboard information architecture
- validation and freshness checks
- review cadence and owner matrix

## Guardrails

- Do not use vanity metrics without a decision attached.
- Never display a rate without its denominator and timeframe.
- A dashboard is not proof of causality; label experiment and observational views clearly.

## Evidence baseline

- [Amplitude, Product Analytics](https://amplitude.com/docs/analytics/product-analytics)
- [Microsoft Research, Dirty Dozen metric pitfalls](https://www.microsoft.com/en-us/research/publication/a-dirty-dozen-twelve-common-metric-interpretation-pitfalls-in-online-controlled-experiments/)
