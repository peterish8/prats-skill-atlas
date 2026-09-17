# UI and motion brief

Fill only the sections needed for this assignment. Replace sample fields with concrete decisions; do not deliver an empty checklist.

## Context

- Mode: existing app / prototype / planning only.
- Product task, audience, current scope and surfaces.
- Existing design contract, source files and unrelated edits to preserve.
- Product-specific focal object and why it explains the task.
- Brand/color/type/material direction; static fallback.

## Scene storyboard

| Scene/state | User intent | Focal object pose | Content and controls | Spatial/lighting change | Entry/exit | Reduced-motion view |
| --- | --- | --- | --- | --- | --- | --- |

Include necessary pending, failure, reversal and completion states. A focused repair may need only two states.

## Action contract

| Event | Logical state accepted | Immediate feedback | Secondary object response | When next input becomes ready | Duplicate/interruption behavior |
| --- | --- | --- | --- | --- | --- |

Give a concrete overlapping timeline for the most frequent action. List named tokens, travel distances, spring/easing decisions and which changes are optional.

## Layout and engines

- Mobile/short-screen/desktop composition and scroll owner per state.
- Keyboard-open field and action placement; safe-area handling.
- Persistent-object ownership versus scene content ownership.
- CSS/WAAPI/library/custom-loop responsibility and cleanup.
- Expensive layout/paint effects and how they will be measured or simplified.
- Pause, reduced motion, focus, accessible names, status and gesture alternatives.
- Export renderer and share/download states if the task includes an artifact.

## Acceptance evidence

| Scenario | Expected observable behavior | Verification method | Actual result or planned check |
| --- | --- | --- | --- |
| Static first paint | Clear task and readable controls before motion | Screen inspection | |
| Main activation | Choice recorded before feedback; no skipped state | Interaction and state trace | |
| Back/edit | Prior data visible, no repeated construction | Journey walkthrough | |
| Rapid/cancelled input | One intended activation; no stale callback | Double activation / pointer cancel | |
| 390×844 and short screen | Relevant controls reachable, no sideways overflow | Browser inspection | |
| Keyboard/reduced motion | Same task works with minimal physical travel | Keyboard and preference/device pass | |
| Success/failure | Real success controls celebration; failure preserves work | Isolated backend/stub according to mode | |

Report verification boundaries. Planning-only output uses expected checks; it does not label them passed.
