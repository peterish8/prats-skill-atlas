# Critique rubric

For audit-only requests, inspect before redesigning. Return findings ordered by impact and label them:

- **P0:** blocks core task completion or accessibility.
- **P1:** serious confusion, trust loss, or conversion friction.
- **P2:** noticeable weakness in quality, consistency, or efficiency.
- **P3:** contained polish opportunity.

For each finding include the affected user, concrete evidence/location, why it matters, exact recommended change, and expected result. Do not say only “make it cleaner.”

Cover: first impression; user intent; primary action; reading order; layout and spacing; typography; contrast; content truthfulness; controls and forms; empty/loading/error/success states; responsive behavior; keyboard/focus; motion; performance; and real-content resilience.

Close with the five highest-leverage fixes and a dependency-aware implementation order. A screenshot can reveal visual hierarchy but cannot prove keyboard behavior, responsiveness, or real-data resilience—label those as unverified until tested.

## Finding format

| Priority | Evidence | User impact | Exact fix | Verification |
| --- | --- | --- | --- | --- |
| P1 | Identify the route, component, screenshot region, or behavior. | State who is blocked or confused and when. | Describe a specific layout, copy, state, or interaction change. | Name the state, viewport, and input method to exercise. |

Separate corrective findings from optional opportunities. Do not treat personal style preference as a defect. If an issue depends on runtime data, a device, or a missing reference, state the assumption and show how it should be verified.
