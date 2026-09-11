---
name: hypothesis-design
description: "Convert product evidence and uncertainty into falsifiable growth hypotheses with explicit mechanisms and decisions. Use before designing variants or prioritizing experiments."
---

# Hypothesis design

Create hypotheses that can lose, teach, and change a product decision.

## Workflow

1. Start from a documented observation, user need, or business constraint; label weak evidence.
2. Name the proposed causal mechanism rather than jumping directly to a UI solution.
3. Specify cohort, intervention, proximal outcome, expected direction, minimum practical effect, and time horizon.
4. Write the result that would disconfirm the mechanism or make the intervention not worth shipping.
5. Identify alternative explanations, dependencies, spillovers, and likely guardrail risks.
6. Choose the lightest method capable of reducing the decision uncertainty.
7. Rank hypotheses by expected decision value, evidence strength, cost, risk, and reversibility.

## Deliverable

Return:
- evidence-to-hypothesis chain
- falsifiable hypothesis statement
- alternative explanations
- disconfirming criteria
- ranked validation approach

## Guardrails

- Do not write tautologies such as 'improving onboarding increases conversion.'
- Do not hide multiple mechanisms inside one hypothesis.
- Treat competitor examples and expert opinions as hypothesis inputs, not proof.

## Evidence baseline

- [GOV.UK, Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs)
- [Amplitude, Product-led experimentation guide](https://amplitude.com/blog/product-led-experimentation-guide)
