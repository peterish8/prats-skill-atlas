---
name: onboarding-personalization
description: "Design proportional onboarding personalization from user goals, context, and permissions. Use when one generic path serves distinct jobs or when collected answers do not improve first-session value."
---

# Onboarding personalization

Ask the few questions that materially change the experience, then deliver a visibly relevant first session.

## Workflow

1. List each proposed question, the decision it changes, and the user benefit it unlocks. Remove questions with no immediate use.
2. Classify data sensitivity, permission or consent need, retention, and safe default for every answer.
3. Design branches around jobs and constraints rather than decorative personas.
4. Show why information is requested and allow skip, correction, and later change where feasible.
5. Carry answers into content, defaults, navigation, and the activation path; do not stop at personalized copy.
6. Instrument question-level completion, skip, time, activation, retention, and privacy or support signals.
7. Test personalization against a strong non-personalized baseline and monitor segment fairness.

## Deliverable

Return:
- question-to-decision matrix
- branching and fallback logic
- first-session personalization contract
- data and consent map
- experiment and guardrail plan

## Guardrails

- Do not collect sensitive data merely to increase conversion.
- Never infer sensitive attributes from unrelated answers.
- Keep a useful default path for users who decline or have unknown context.

## Evidence baseline

- [Apple HIG, Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy/)
- [W3C, Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/)
- [NIST, Privacy Framework](https://www.nist.gov/privacy-framework)
