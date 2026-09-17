---
name: motion-animate-ux-stack
description: Design and implement motion graphics, intentional scene choreography and continuous transitions for websites and apps. Use for hero sequences, animated diagrams, shared-element transformations, editorial reveals, gesture-driven objects and reusable motion specifications, including planning-only work.
---

# Motion, animation and UX stack

Make motion explain what happened, where something came from and how one state becomes another. Design a temporal composition rather than adding unrelated effects to individual elements.

This skill is a motion-design workshop: principles, spatial grammar, storyboarding, timing, continuity, runtime behavior and critique. It is independent of a UI theme or engagement strategy. Preserve the target product, brand, existing navigation and requested scope. A hero-only request stays hero-only. Do not install a library or publish a result merely because this skill was loaded.

## Identify the job of motion

Inspect the existing scene, state model, rendering paths and relevant design requirements. Infer the mode: implement in an existing app, create a requested prototype, or produce planning-only specifications. Distinguish present code from old plans and live observations.

For each proposed effect, name its job: acknowledge input, orient navigation, show a relationship, explain a transformation, guide attention, establish identity or mark real completion. If no job can be named, remove it or contain it to an optional expressive scene.

Write the sequence in one sentence: “When [trigger], [primary object] changes from [meaningful pose] to [next pose]; [supporting layers] explain the change; the user can [next action] at [readiness condition].”

Read [references/principles-and-grammar.md](references/principles-and-grammar.md) for motion-design decisions. Read [references/sequence-recipes.md](references/sequence-recipes.md) for a relevant scene pattern, [references/runtime-continuity.md](references/runtime-continuity.md) for implementation and interruption, and [references/motion-brief-template.md](references/motion-brief-template.md) for deliverables. [references/source-map.md](references/source-map.md) records source evidence and official technical references; the original website is not a dependency.

For a verified reference implementation's motion technologies and their responsibilities, read [references/motion-ux-stack.md](references/motion-ux-stack.md). Treat that stack as a worked example, not a requirement to install those packages in another product.

## Design the resting poses before the movement

Create a readable initial frame, transformation frame and final frame. Set a focal subject, quiet reading area, supporting graphic layers and stable action area. Use silhouette, contrast, negative space, material and scale to make each pose understandable without playback.

Choose a spatial grammar: entry/exit origin, depth plane, travel direction, anchor, light source and persistent identity. Define which object carries continuity and which layers may be replaced. Keep typography readable and controls predictable throughout. Motion cannot rescue a weak final composition.

## Storyboard the action as a coordinated sequence

Map trigger → acknowledgement → transformation → arrival → settle. Use one primary movement, with supporting events related to it. Distinguish a transient impact from a lasting state change. Keep confirmation truthful: speculative preview, pending operation and confirmed completion have different meanings.

Write a timeline with explicit start offsets, durations, easing/physical behavior, property ownership and readiness. Overlap independent events instead of adding their durations serially. Budget the time until useful interaction separately from the decorative tail. Allow essential orientation to finish without forcing every sparkle, word or spring to settle before the next action.

Tune distance, timing and easing together. Direct manipulation follows the pointer; settling can be spring-driven. Repeated controls favor brief acknowledgement. A first-time identity sequence can be longer if skip or immediate reveal is available. Treat timing ranges as starting points, not universal rules.

## Preserve intentional continuity

Keep semantic identity stable through transforms, shared-element transitions or compatible shape changes. Match anchors and coordinate systems; avoid teleporting an object, resetting its orientation or changing scale origin between cuts. Use distinct wrappers when scene position, local shape and idle motion need different transform owners.

Retarget an interruptible object from its current pose rather than restarting from an arbitrary initial keyframe. Use velocity continuity where the engine supports it and it serves the gesture. If geometry cannot morph convincingly, use an explicit cut, occlusion or readable crossfade instead of pretending unrelated shapes are the same object.

Decide the Back, rapid-input, resize, hidden-tab and cancellation policies before implementation. Cosmetic transitions can be replaced; stateful physical operations may need ordered completion or reconciliation. Skipping visual work must still resolve to the correct logical final state and cannot replay a backend action.

## Implement the motion contract

Choose the existing engine by need: CSS for simple states/loops, Web Animations for controllable fixed keyframes, the current state/gesture engine for springs and presence, SVG for vector construction, and custom rendering only for a model that needs it. Keep timing units explicit across APIs.

Give each animated property one owner at a time. Use named role tokens and shared sequence offsets, not an unrelated duration per component. Keep visual progress separate from operation state. Own timers, frame callbacks, animation handles, subscriptions and temporary graphics so cancellation and teardown have defined results.

Prefer transform/opacity for frequent motion, but profile rather than declaring a scene compositor-only. Layout, masks, filters, shadow work, large layers and custom per-frame shading need an explicit budget. Simplify supporting decoration before sacrificing input responsiveness.

## Design alternative playback as part of the sequence

Specify normal playback, reduced motion, ambient pause and skip/replay separately. Reduced motion retains content, operation state, orientation and feedback using static poses or brief appropriate fades; remove unnecessary travel, rotation, parallax, overshoot and stagger delays. Pause qualifying ambient motion without disabling useful controls. Avoid repetitive high-contrast flashes and examine actual rendered output when flash risk is relevant.

Preserve complete accessible phrases during typographic reveals. Decorative letter clones and duplicate scene layers must not become repeated announcements or focus targets. Use native activation, visible focus and concise semantic status updates. A motion preference in one library does not automatically govern other engines.

## Review and finish

Inspect the still frames, full-speed playback and the busiest overlap. Check current-pose retargeting, rapid reversal, Back, resize, hidden/resumed tabs, reduced motion and keyboard operation as relevant. Check low-resource behavior and the actual target viewport/device when available. Static code inspection cannot prove smoothness or accessibility conformance.

Deliver the requested implementation/prototype or planning brief with: motion intent, storyboard, reusable grammar/tokens, timeline and readiness, transition ownership/interruption policy, alternative playback and testable acceptance criteria. Report exact checks and unverified conditions. Do not claim engagement or device performance from attractive animation alone.
