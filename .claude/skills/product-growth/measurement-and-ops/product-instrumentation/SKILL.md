---
name: product-instrumentation
description: "Design a versioned product analytics and experimentation event contract tied to user decisions and value. Use when funnels, cohorts, experiments, or growth metrics cannot be trusted."
---

# Product instrumentation

Create telemetry that answers named product questions without collecting unnecessary data or coupling analytics to fragile UI details.

## Workflow

1. List decisions and questions first, then derive events and properties.
2. Define actors, entities, identity states, consent states, value events, funnel events, experiment assignment, exposure, and outcomes.
3. Use stable semantic names, explicit versions, ownership, type constraints, and allowed values.
4. Specify client versus server authority, deduplication, timestamps, offline behavior, late events, and identity merge rules.
5. Minimize personal data and prohibit secrets, free-form sensitive payloads, and unnecessary high-cardinality properties.
6. Create validation, debug views, A/A checks, and monitoring for volume, nulls, duplicates, ordering, and schema drift.
7. Document retention, access, deletion, and downstream destinations.

## Deliverable

Return:
- decision-to-event map
- event and property dictionary
- identity and experiment exposure contract
- data quality checks
- privacy, retention, and governance plan

## Guardrails

- Do not track every click by default.
- An assignment event is not the same as actual treatment exposure.
- Never put credentials or uncontrolled sensitive text in analytics properties.

## Evidence baseline

- [Amplitude, Product Analytics](https://amplitude.com/docs/analytics/product-analytics)
- [Microsoft Research, SRM taxonomy](https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/)
- [NIST, Privacy Framework](https://www.nist.gov/privacy-framework)
