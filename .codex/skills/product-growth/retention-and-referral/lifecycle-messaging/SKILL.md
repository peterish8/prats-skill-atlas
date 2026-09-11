---
name: lifecycle-messaging
description: "Design consented email, push, in-app, and transactional messages around timely user value. Use for activation reminders, education, re-engagement, renewal, or churn prevention."
---

# Lifecycle messaging

Deliver the smallest useful message at the moment it can help, with channel choice and frequency controlled by the user.

## Workflow

1. Define the user state, unmet job, trigger, message purpose, desired outcome, and why this channel is appropriate.
2. Separate transactional, product guidance, promotional, safety, renewal, and support communication.
3. Require permission or a valid basis, preference controls, quiet periods, frequency caps, and unsubscribe or disable behavior.
4. Use event-driven relevance without exposing sensitive context in lock screens, subjects, or shared channels.
5. Design copy that states value and action plainly; deep-link to the exact relevant state.
6. Experiment on incremental value with holdouts where feasible, not open or click rate alone.
7. Measure task completion, retention, opt-out, complaints, deliverability, notification disablement, and support effects.

## Deliverable

Return:
- state-trigger-message matrix
- channel and consent plan
- frequency and suppression rules
- copy variants and deep links
- incrementality and guardrail plan

## Guardrails

- Never send sensitive personal details in notifications.
- Do not repeat messages merely because a user ignored them.
- Open rate and clicks are diagnostics, not proof of durable value.

## Evidence baseline

- [Apple HIG, Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications)
- [Apple HIG, Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy/)
