---
name: frontend-design-fidelity
description: Carry an intentional frontend design through shared components, responsive layouts, real content, loading and recovery states, and generated outputs. Use when implementing a design or repairing visual drift in an existing website or app, prototype, or planning-only specification.
---

# Frontend design fidelity

Keep a product recognizably well designed beyond its ideal screenshot. Make the same visual intent survive first paint, small screens, large text, keyboard input, slow resources, failed operations and exported artwork.

This skill owns the implementation fidelity of a chosen design. It does not choose a new brand, invent an engagement loop or prescribe cinematic animation. Infer whether the request is existing-app work, a prototype, or planning only; preserve the user's scope, product features and unrelated edits. Do not treat permission to improve a frontend as permission to publish or change its data policy.

## Establish the actual design contract

Read the applicable repository instructions, current components, styles and product documentation. Inspect the implemented target surface when available. Separate current behavior, proposed designs and old plans: a gallery component or roadmap entry is not proof that a feature ships.

Capture the few things that make this product recognizable: surface hierarchy, type roles, accent meaning, control geometry, spacing relationships, media treatment and layout priorities. Record the target routes/states and what must remain stable. Prefer an existing token, primitive or shared renderer over a parallel local version.

For evidence and transferable lessons from the source website, read [references/source-lessons.md](references/source-lessons.md). Read [references/implementation-contracts.md](references/implementation-contracts.md) only for the relevant layout, resource, state or export work. Use [references/fidelity-brief-template.md](references/fidelity-brief-template.md) for planning or a substantial implementation.

## Turn visual intent into a reusable system

Use semantic roles such as primary text, selected border, inset field, raised control and destructive state. Preserve the target palette; gold, cream, dark backgrounds and wide display fonts are source choices, not mandatory output.

Assign typography by job. A distinctive display face can serve an identity or hero title while labels, errors, body copy and operational states remain easy to read. Use real strings: a long name, long action label, translated sentence and empty value expose problems an ideal screenshot hides. Prefer wrapping, flexible layout and sufficient space before shrinking text; reserve measured fitting for genuinely bounded artwork.

Repair the shared path that owns a mismatch. If several screens use the same field, fix the field and inspect its consumers. Keep a local exception explicit when the component's meaning differs. Do not rename the whole token system or create a design-system migration for a focused repair.

## Recompose around available space

Choose who owns scrolling for each surface. Content-led pages should grow; a viewport-sized workspace needs an accessible way to reach overflow. Keep intentional horizontal scrolling inside the relevant table, map or carousel rather than letting decoration widen the page.

Use actual container and height constraints, not device names alone. At narrow or short sizes, reduce ornament and redistribute space before clipping text, hiding options or shrinking usable controls. Allow native zoom and reflow. A large desktop can change the spatial relationship of media and controls instead of displaying a stretched phone layout.

Treat keyboard-open and focused states as layouts to inspect. The focused field, error and next useful action must remain reachable. Browser viewport hints are implementation choices with platform differences; do not assume an emulator or one CSS unit proves keyboard behavior on a device.

## Design the conditions around the happy path

First paint should belong to the product. Align document background, browser chrome and fallback resources where relevant. Gate a decorative opening only on what it actually needs, with a bounded wait and a usable fallback; do not hide ordinary content behind a full-screen loader by default.

Keep loading, validation, empty, offline, retry, unavailable and restored states in the same visual system. Explain the state beside its affected action and preserve usable input. Distinguish decorative completion from confirmed persistence. Browser connectivity and an attempted download are signals, not proof of server receipt or a file saved on a device.

Use native control semantics and visible focus. Scoped shortcuts must yield to focused fields and widgets. Retained drafts should be versioned, validated and privacy-appropriate; storage failure should degrade restoration rather than block ordinary use. Do not add persistence or automatic retries unless the task and product contract call for them.

## Preserve the design outside the screen

If the product generates an image, PDF, receipt, card or other artifact, inspect that actual output separately. Share the content model, palette and identity rules across renderers where practical; CSS glow, fonts and text fitting do not automatically transfer to canvas or PDF.

Tie asynchronous generated files to the current content snapshot. A late result from an old name or selection must not replace the current result. Show preparation and failure honestly and keep the user-controlled fallback appropriate to the platform.

## Finish according to the requested mode

- Existing app: implement the smallest change in the responsible shared path and verify affected consumers, boundaries and failure states.
- Prototype: complete the requested slice with representative content and explicit fixture/operation boundaries. Do not imply a mocked action persisted or delivered anything.
- Planning only: return the design contract, composition rules, component/state ownership, relevant output contract and observable acceptance criteria. Do not scaffold or install packages.

Report concrete changes and evidence: source review, rendered browser state, generated artifact and real-device observations are distinct. Run checks appropriate to the changed behavior and repository requirements. For a documentation-only skill task, do not imply application tests ran. If live access is unavailable, mark rendering and device claims unverified rather than treating static code inspection as a passed visual test.
