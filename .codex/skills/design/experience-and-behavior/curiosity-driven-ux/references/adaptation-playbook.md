# Adapt the experience to the product

Translate purpose, action and consequence together. Keep the target's own visual identity and navigation unless the user asked to change them.

## Existing product procedure

Inspect one main journey from its entry to its actual useful result, including a reversal. Note where users type unnecessarily, lose context, cannot see feedback or cannot understand their progress. Identify the shared renderer/control paths before changing individual screens.

Choose a concrete change set, then implement it under existing architecture. A good first change set might be: immediate selection feedback, a persistent preview, retained Back/edit and an improved result. It need not include a new story, badge or carousel.

If the user asked for the entire experience, work through all important user-facing states rather than finishing after one hero. If the scope is focused, deepen that surface without widening the assignment. Run relevant checks and report what actually works.

## Prototype procedure

Create a coherent entry → action → result slice, not disconnected pretty screens. Show at least a correction and one relevant pending/failure state. Use clearly labelled fixture data when the assignment is a prototype; do not imply production persistence, current external facts or working native sharing from a visual stub.

Use real provisioned services only when required by the user's intended scope and follow the environment's integration guidance. This UX skill alone never implies authorization to deploy, sign up for services or submit to a live backend.

## Planning-only procedure

Deliver the scene sequence, working loop, copy, state transitions, object meaning, reduced-motion equivalents and testable acceptance criteria. Put unresolved backend/device questions into an explicit assumptions list. Do not install, scaffold or fabricate verification evidence. If a UI storyboard is useful, it is a design artifact and should be labelled as such.

## Worked transfer examples

### Learning app

**Task:** choose and complete a short lesson.

**Motif:** a knowledge map in the existing brand, one node connected by each real completed exercise.

**Loop:** preview a learnable capability → answer one exercise → show confirmation and a new connection → correct or continue → finish with a useful worked summary.

**Useful novelty:** each exercise changes the same map; the completion lets the user inspect how ideas connect. Keep browsing, search and established study navigation available.

**Guardrails:** an incorrect answer gets useful correction, not a fake completion node. Do not infer mastery from clicks. Replay the explanation without changing the attempt record. A reduced-motion view shows the same node/connection state immediately.

**Verify:** correction retains context, lesson result matches actual activities, mobile answer reachability, keyboard and static map reading.

### Music app

**Task:** assemble and play a queue.

**Motif:** a sleeve/stack representing selected tracks, with materials adapted to the app.

**Loop:** discover a song → add it with immediate acknowledgement → stack grows → reorder with direct manipulation → play or save the usable queue.

**Useful novelty:** the object visibly assembles; a small sleeve picker is optional personalization after the queue exists.

**Guardrails:** keep bulk selection and normal queue navigation. No forced onboarding wizard, automatic playback or new audio effects. Save success follows actual persistence. Gesture reordering has button/keyboard equivalents.

**Verify:** rapid adds do not duplicate tracks, reorder cancellation leaves a valid queue, playback controls remain reachable and saved result matches the queue.

### Travel planning

**Task:** select constraints and build an itinerary.

**Motif:** one route assembled from real selected locations.

**Loop:** enter essential constraints → tap a suitable option → route segment appears → review dates and costs → save/export the plan.

**Useful novelty:** route continuity expresses construction; a completed itinerary is the payoff.

**Guardrails:** show price/date/availability plainly; distinguish proposed routes from booked travel. A saved plan is not a reservation. Do not serialize comparison into one-at-a-time cards when side-by-side comparison helps.

**Verify:** parent changes invalidate incompatible selections, review matches actual dates, no booking or payment is implied by animation, export is readable.

### Portfolio / landing page

**Task:** understand the person's work and open a relevant project.

**Motif:** an unfolding project artifact, track or diagram linked to the actual work.

**Loop:** clear opening promise → a visible project example → deliberate section transition → open real work or contact path.

**Useful novelty:** a single coherent hero object and varied editorial reveals make exploration worthwhile.

**Guardrails:** keep native page scroll and direct project links. No survey steps, invented completion score, reading gate or obligatory badge. All project content remains readable without animation.

**Verify:** project links, scroll and keyboard remain native, anchor targets are visible, small-screen content does not clip, reduced motion retains all information.

### Finance, admin or other dense utility app

**Task:** review accurate records and complete a precise operation.

**Motif:** the real summary/document/plan rather than unrelated scenery.

**Loop:** understand current state → make a reversible selection → receive short local acknowledgement → review consequences → confirm → see actual saved result.

**Useful novelty:** tactile controls, clear continuity, subtle preview updates and a crisp finish; a more expressive stage can fit optional first-time education.

**Guardrails:** keep tables, bulk actions, density and accurate comparisons. Financial outcomes, record values or authority do not change for theatrical effect. No “reward” for a riskier choice or celebration before an operation completes.

**Verify:** data accuracy, explicit confirmation, stale-request behavior, full accessibility and useful failure recovery. A quiet interface can still be exceptionally satisfying.

## Select the intensity

| Context | Good default | Usually reduce |
| --- | --- | --- |
| First-time invitation | One signature entrance and skippable narrative | Long initial waits |
| Repeated useful action | Tactile response and quick state continuity | Repeated particles or story |
| Optional exploration | Direct object manipulation and bounded picker | Gesture-only control |
| Careful review | Stable data, clear edit and confirm | Ambient competing movement |
| Confirmed milestone | One meaningful reveal or useful artifact | Celebrations that block result |
| Reduced motion | Strong hierarchy and immediate visual consequences | Travel, spin and delayed text |

## Recognize a weak adaptation

| Symptom | Likely problem | Repair |
| --- | --- | --- |
| “Looks fancy but I don't know what to do” | Stage overwhelms hierarchy | Make task and action dominant |
| “Everything bounces” | No contrast or frequency budget | Reserve movement for meaningful events |
| “Why is there a cube here?” | Reference copied literally | Find the target product's own object |
| “I just want to finish” | Optional story became a gate | Restore direct task path |
| “I lost my answer” | State contract weaker than appearance | Repair Back/edit/persistence ownership |
| “It says done but wasn't saved” | Visual completion confused with operation success | Tie success to confirmed result |
| “I cannot scroll while picking” | Gesture ownership is wrong | Distinguish horizontal intent and allow vertical scrolling |
| “It only works with animation” | Meaning embedded in movement alone | Make static state carry meaning |

Resolve these before adding further novelty.
