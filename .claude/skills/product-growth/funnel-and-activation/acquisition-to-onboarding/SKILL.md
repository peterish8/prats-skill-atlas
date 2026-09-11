---
name: acquisition-to-onboarding
description: "Connect acquisition intent to landing pages, store listings, onboarding, and first value. Use when traffic converts poorly, channel cohorts differ, or the first experience breaks the promise."
---

# Acquisition to onboarding

Preserve the user's intent across campaign, click, install or signup, onboarding, and activation without using invasive attribution.

## Workflow

1. Map each meaningful source and campaign to its promise, audience, landing destination, first-session state, and target value event.
2. Audit message match across ad or search term, page or store listing, onboarding questions, default content, and first action.
3. Define privacy-safe attribution identifiers and the minimum granularity needed for decisions.
4. Measure qualified arrival, start, step completion, activation, paid conversion, retention, and unit economics by cohort.
5. Design source-aware paths only when the source materially predicts a different job; provide a coherent default for unknown attribution.
6. Test the complete path when the mechanism spans multiple surfaces, while retaining component diagnostics.

## Deliverable

Return:
- source-to-value journey map
- message-match audit
- attribution and event contract
- cohort metric tree
- prioritized end-to-end experiments

## Guardrails

- Do not fingerprint users or reconstruct identities from aggregate attribution.
- Do not personalize from a source label that can expose sensitive traits.
- Treat missing attribution as a first-class cohort, not bad data to discard.

## Evidence baseline

- [Apple, AdAttributionKit](https://developer.apple.com/documentation/AdAttributionKit)
- [Amplitude, Product Analytics](https://amplitude.com/docs/analytics/product-analytics)
