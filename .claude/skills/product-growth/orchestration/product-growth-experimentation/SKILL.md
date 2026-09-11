---
name: product-growth-experimentation
description: Orchestrate evidence-led product growth across user research, acquisition, onboarding, activation, experimentation, monetization, retention, referral, and measurement. Use for end-to-end growth programs or ambiguous growth problems; use a narrower product-growth skill for a single bounded task.
---

# Product growth experimentation

Build a trustworthy learning system that improves durable user and business outcomes. Do not cargo-cult another product's winning tactic or optimize a conversion metric while hiding harm elsewhere.

## Start with the decision

Clarify the product, audience, lifecycle stage, business model, current bottleneck, available traffic, decision deadline, and what authority exists to change production behavior. Inspect existing research, analytics definitions, experiment history, and platform constraints before proposing work.

Maintain an evidence ledger with five labels:

- `OBSERVED`: directly supported by product data or user research
- `EXPERIMENTAL`: supported by a valid randomized or quasi-experimental result
- `EXTERNAL`: supported by applicable outside research or official guidance
- `ASSUMED`: plausible but unverified in this product
- `CONTRADICTED`: evidence points against the claim

Case studies and competitor patterns generate hypotheses. They do not establish local truth.

## Route only what is needed

- User problem unclear: use `jobs-to-be-done`, `user-interview-analysis`, or `market-and-competitor-research`.
- Acquisition promise and first experience do not connect: use `acquisition-to-onboarding` or `onboarding-personalization`.
- Users fail to reach value: use `activation-design`.
- A test needs framing, design, analysis, or safety metrics: use `hypothesis-design`, `ab-test-planning`, `experiment-analysis`, or `guardrail-metrics`.
- Revenue model is the bottleneck: use `paywall-optimization`, `pricing-and-packaging`, `trial-strategy`, or `billing-compliance`.
- Durable use or organic distribution is weak: use `retention-loops`, `lifecycle-messaging`, or `viral-sharing`.
- Data or decision operations are weak: use `product-instrumentation`, `growth-dashboard-design`, `experiment-log`, or `growth-decision-making`.
- Any flow processes personal data, excludes users, or pressures choice: use `privacy-and-consent`, `accessibility-growth`, or `dark-pattern-prevention`.

Do not load every complementary skill. Read only the ones required for the current decision.

## End-to-end workflow

1. Define the user job, target cohort, current behavior, desired durable outcome, and business constraint.
2. Map the journey from acquisition source through first value, monetization, repeat value, and referral. Mark evidence gaps and handoff failures.
3. Locate the highest-leverage bottleneck using rates, absolute counts, cohort quality, economics, and qualitative evidence.
4. Form a falsifiable hypothesis: evidence, proposed mechanism, intervention, target cohort, expected change, and disconfirming result.
5. Choose the lightest valid method: usability test, prototype test, survey, observational analysis, A/A test, randomized A/B test, staged rollout, or holdout.
6. Pre-register the randomization unit, eligibility, variants, primary metric, guardrails, minimum detectable effect, power, duration, exclusions, stop rules, and segment policy.
7. Verify instrumentation before launch. Assignment must be stable; exposure must be logged at actual treatment; control and treatment must share metric definitions.
8. Monitor operational safety without repeatedly making inferential decisions. Under fixed-horizon testing, do not stop because an early p-value looks favorable. Use a valid sequential method when early decisions are required.
9. Before interpreting lift, check sample-ratio mismatch, crossover, missing telemetry, novelty or seasonality, implementation parity, and guardrail regressions.
10. Decide `SHIP`, `ITERATE`, `ROLLBACK`, `KEEP TESTING`, or `COLLECT MORE DATA`. Separate statistical evidence, practical value, uncertainty, and risk.
11. Record the result, context, implementation, metrics, segments, decision, and reusable learning. Preserve negative and inconclusive results.

## Required decision frame

Every recommendation must report:

- user and business outcome;
- evidence level and uncertainty;
- primary metric and why it is proximal enough to the change;
- retention, quality, performance, accessibility, privacy, and economic guardrails as applicable;
- expected practical effect, not only statistical significance;
- rollout and rollback conditions;
- jurisdiction or platform-policy checks that still require live verification.

## Hard boundaries

- Never present correlation, funnel comparison, or before/after movement as causal proof.
- Never declare an experiment valid when SRM or material instrumentation defects remain unexplained.
- Never invent benchmarks, sample sizes, conversion rates, social proof, urgency, scarcity, or customer evidence.
- Never optimize subscriptions through hidden terms, obstructed cancellation, disguised ads, forced consent, or misleading price units.
- Do not collect personalization data merely because it might improve conversion. Require purpose, proportionality, consent or another valid basis, retention limits, and deletion handling.
- Treat Apple, Google, consumer-protection, privacy, and accessibility requirements as current-state checks. Verify official sources at execution time.
- Do not recommend a web funnel, long onboarding, hard paywall, free trial, or personalization pattern as universally superior. Test the mechanism in context.

## Supporting references

- For statistical and instrumentation standards, read [references/experiment-rigor.md](references/experiment-rigor.md).
- For consent, accessibility, billing, subscription, and dark-pattern boundaries, read [references/growth-ethics-and-compliance.md](references/growth-ethics-and-compliance.md).
- For planning and reporting structures, read [references/artifact-templates.md](references/artifact-templates.md).
- For the source-backed rationale and freshness notes, read [references/evidence-and-sources.md](references/evidence-and-sources.md).
- For lessons extracted from the supplied subscription-app case study, read [references/case-study-lessons.md](references/case-study-lessons.md).
