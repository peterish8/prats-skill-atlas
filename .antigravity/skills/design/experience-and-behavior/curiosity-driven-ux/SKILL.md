---
name: curiosity-driven-ux
description: Design engaging product journeys through narrative, low-effort choices, meaningful progress, user agency and personalized completion. Use to adapt the Polaris experience to existing websites or apps, prototypes, or planning-only UX and behavioral specifications.
---

# Curiosity-driven UX

Make people want to take the next useful action because the product is clear, responsive and interesting. Capture the Polaris feeling of “my small actions are building something” without requiring its survey layout, cube, dark theme or badge.

Treat “addictive” as the user's shorthand for compelling, satisfying and worth revisiting. Optimize for successful use and voluntary exploration. The source supplies observable mechanics; it does not prove a psychological or retention effect.

## Start with the product and mode

Identify the user's actual goal, existing product promises, primary journey, user vocabulary and current state contracts. Read the applicable repository/docs and inspect the implemented journey if present. Preserve the target brand, features, navigation and unrelated edits. Do not turn an ordinary focused UX repair into a redesign.

| Mode | Action | Deliverable |
| --- | --- | --- |
| Existing app | Find friction and disconnected feedback; implement improvements using existing components and state | Complete scoped journey and exact verification |
| Prototype | Build a representative end-to-end loop, including correction and completion | Runnable interaction with prototype facts/data clearly distinguished |
| Planning only | Define journey and state contracts without scaffolding | Storyboard, interaction map, copy and observable acceptance checks |

For the source mechanisms and their limits, read [references/behavioral-patterns.md](references/behavioral-patterns.md). For adapting across products, read [references/adaptation-playbook.md](references/adaptation-playbook.md). Use [references/journey-brief-template.md](references/journey-brief-template.md) for an implementation-ready plan.

## Define a concrete engagement loop

Write the loop before adding features:

> A clear invitation creates [specific question]. A small useful action changes [visible product state]. That change shows [meaning/progress]. Completion gives [real outcome]. The user can optionally explore [bounded next action].

Examples: an answer adds a visible turn toward a finished pattern; choosing a lesson lights one connection in a learning map; adding a song assembles a playable queue. The next action must make sense even if all animation is off.

Choose one loop around the main task. Points, streaks, leaderboards and endless feeds are not default ingredients. Prefer visible construction or improving competence when the product can represent it honestly.

## Invite without making people sit through a pitch

Give the first screen one plain benefit, a concrete effort expectation and an obvious primary action. A narrative can explain who cares, what changed, why it matters and why the person belongs. Use it only when it helps the product; provide a direct route to the task.

Do not transplant Polaris's “60 seconds” claim to another app. Estimate from the actual journey or test it. Keep future benefits conditional and distinguish demonstrated results from aspirational illustrations.

Compose curiosity around a destination the person can understand: “What will this become?” works when each step reveals more of the object or result. Avoid obscuring necessary information to force another click. Let people reveal text immediately, skip optional content, pause background motion and leave.

## Make the smallest useful action obvious

Use one decision at a time for onboarding, surveys or guided setup when it reduces effort. Preserve overview and bulk actions in dashboards, editors, search and other expert workflows.

- Prefer a tap choice for a small stable set; preserve search or typing for large/open sets.
- Ask dependent questions only when they apply; clear incompatible values after the parent changes.
- Show concise labels and one helper sentence when it removes ambiguity.
- Explain auto-advance before using it. Apply it to low-risk reversible single choices, not text, destructive actions, purchases or final submission.
- Keep Back and edit available and restore previous selections without replaying celebrations.
- Include valid neutral/uncertain/decline choices when the question warrants them. Give them equal clarity and feedback quality.

In the source, Semester 5 has no batch question, and novices can say they are just exploring. The portable principle is truthful eligibility and low-pressure participation, not those exact options.

## Connect action, feedback and progress

Acceptance should be immediate and visibly owned by the action. Coordinate a short control confirmation, a meaningful object change and the next content reveal. Keep logical acceptance separate from animation timing and server persistence.

Track two things independently:

1. Current product data, which can change during edits.
2. Milestones whose visual construction has already played.

This prevents Back, retries and replay from corrupting cumulative progress or duplicating effects. Distinguish answered, reviewed, submitted and saved states. A glossy bar may carry personality, but its accessible text and success state must remain accurate.

Choose progress the product can justify. Learning progress can represent completed activities; travel setup can represent answered constraints; a portfolio need not display artificial completion points. Do not animate business metrics or forecasts as though they were live verified results.

## Design contrast rather than constant stimulation

Alternate meaningful visual modes: invitation, demonstration, action, review and completion. Keep a stable spatial anchor so variation reads as a changing story rather than a new interface each time.

Quiet down at moments that require careful reading or decision-making. A dense table, complex edit, error or consent notice deserves stable content. Let optional showcases be richer than repeated utility interactions. Interaction frequency determines the amount of spectacle worth retaining.

## Give completion value and closure

Show explicit success only after the actual operation succeeds. Preserve work through pending and failure states, and explain the next useful recovery action. Animation must not fake persistence.

Offer a result the person can use or feel ownership of: a playable queue, saved itinerary, learning summary, export, personalized preview or genuinely relevant badge. Let them customize when customization improves the result. An ornamental reward is optional, not a substitute for the task.

Keep Save, Share, Finish and replay voluntary. Sharing is never required to access a result. Explain what will be shared, including any visible personal data, and let cancellation return calmly to the result. Replay only the presentation; do not repeat submissions, registrations or purchases.

Close with one concrete next move. A finale can connect the user's action back to the opening purpose, but an urgent utility task may simply need a clear saved state and Done.

## Preserve agency through interruption and failure

Specify how the journey behaves on Back, edit, reload, privacy/help detour, duplicate activation, network error and late server response. Use the target app's existing persistence policy. Do not add personal-data storage, analytics, reminders or new backend infrastructure solely to make the flow engaging.

If draft restoration is appropriate, retain only the data needed and explain its boundary. If retries write data, preserve the app's idempotency contract. Cancel stale scene timers. Screen changes should maintain a sensible keyboard/focus path and communicate their state to assistive technology.

Reduced motion and a paused background must preserve curiosity through content, choices and meaningful state changes. They should not lose functionality, completion value or the ability to explore.

## Translate into a complete result

For substantial work, produce a short journey map and one beat contract per key interaction:

```text
User intention:
Prompt/copy:
Small action:
Accepted product state:
Immediate acknowledgement:
Meaningful visual consequence:
Next action and when available:
Back/edit/cancel/failure behavior:
Static/reduced-motion equivalent:
```

Then implement the authorized changes or finish the planning artifact. If working alongside a UI/motion skill, this skill owns task sequence, copy, choices, progress meaning, success and recovery contracts. UI/motion work owns composition, material and choreography. Both operate on the same contracts; neither independently invents new product features.

## Verify usefulness and appeal separately

Check a new user, a returning/skipping user and someone correcting an answer. Verify primary-task completion, reachability on 390×844 and a short screen, real keyboard-open behavior when available, keyboard access, reduced motion, duplicate input and relevant failure states. Use isolated data; do not create production test submissions without authorization.

For an existing app, run checks appropriate to the edits and record browser evidence where available. For planning, specify checks and unknowns. Inspect actual exports separately if part of the experience.

Behavioral hypotheses need observation: do people understand what changes, discover the next action, finish without pressure and choose to explore? Use the validation approach in the behavioral reference. Do not claim increased retention, “dopamine,” addiction or completion from the presence of an animation or a score.

Deliver the working journey or completed plan, the mechanics chosen and their purpose, exact check results, and the boundaries of any claims. Avoid ending with generic suggestions to “gamify it.”
