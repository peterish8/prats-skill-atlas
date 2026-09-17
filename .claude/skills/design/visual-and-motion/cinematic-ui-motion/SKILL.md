---
name: cinematic-ui-motion
description: Design or implement tactile cinematic interfaces with product-specific hero objects, coherent scene choreography and satisfying gesture feedback. Use for existing websites or apps, prototypes, or planning-only motion and UI specifications inspired by the Polaris experience.
---

# Cinematic UI and motion

Make the interface feel like a coherent place in which the user's actions have visible consequences. Translate the Polaris quality of staging and touch into the target product's own visual language.

## Choose the working mode

Infer the mode from the request and artifacts; ask only if a missing choice materially blocks work.

| Input | Work | Result |
| --- | --- | --- |
| Existing app | Inspect real screens, shared controls, state ownership, routes and current edits; implement in the existing system | Working scoped patch and verification evidence |
| Prototype | Build a complete representative interaction, including reversal and failure states | Runnable demonstration with clear prototype boundaries |
| Planning only | Specify scenes, poses, transitions and state contracts | Implementation-ready storyboard and motion brief; no scaffolding |

If the request is only about a hero or a control, keep the improvement there. Preserve the current brand, product purpose, navigation and unrelated work. Do not install an animation library merely to reproduce the reference's stack.

For exact visual and timing extraction, read [references/polaris-patterns.md](references/polaris-patterns.md). For event handling, engines and interruption behavior, read [references/implementation-recipes.md](references/implementation-recipes.md). Use [references/design-brief-template.md](references/design-brief-template.md) for planning or a substantial change.

## Establish the visual contract

Before editing, identify the primary action, the object that represents the product, existing color/type tokens, the smallest important viewport, and the available motion engine. Inspect actual implementation before trusting an old design document. Capture the current journey if browser tools are available.

Write a short decision statement:

> The user does [task]. The persistent [object] changes by [meaningful transformation]. The stage supports that object with [light/depth]. The controls remain [material and hierarchy]. The journey concludes with [real outcome].

Choose a product object rather than inserting a decorative cube everywhere. A learning map can grow connections; a music queue can assemble a sleeve; a travel plan can join route segments. If no object clarifies the product, use continuity of the content itself.

## Compose atmosphere around usable controls

Use a focal object, an action area, and quiet utilities. On a short mobile guided flow, a top utility row, upper stage and reachable lower dock work well. On a dashboard, keep the working canvas dominant and confine theatrical staging to onboarding, meaningful milestones or a focused detail view. On a landing page, preserve native document scrolling and let sections become story beats without turning navigation into a wizard.

Create depth in distinct layers:

1. Quiet canvas or texture.
2. Static light pool, perspective or spatial framing.
3. Grounded hero object with contact shadow and coherent highlights.
4. Readable content and stable controls.
5. Temporary feedback whose origin and destination explain the action.

Keep text out of the brightest light. Material depth comes from top highlights, edge shadows, face differentiation and grounding before additional blur. Render a compelling static frame first; motion cannot repair weak hierarchy.

Use the target brand's palette. Polaris uses near-black, cream, charcoal and gold, but a light interface can achieve the same craft through paper, ink, restrained tint and soft shadows.

## Give controls consistent physics

For raised controls, use a fine border, a restrained top highlight, a visible bottom edge and a small contact shadow. Press by roughly 2px and remove the edge; release cleanly. Keep the layout footprint stable. Inputs should read as recessed and remain still on focus.

Separate pointer press feedback from activation. Pointer-down changes appearance; click or native keyboard activation commits the action. Clear press on up, leave and cancel. Hover effects belong only on hover-capable devices. Use actual buttons and fields; a CSS appearance never substitutes for semantics.

Selected state must survive without animation: outline, material change, keycap or check, and appropriate accessible state. Do not make a choice's animation intensity depend on whether its answer benefits the business. A 44px hit target is a useful default here; smaller desktop controls may use an expanded hit area. Preserve legibility and focus visibility.

## Choreograph one action across the scene

Build a cause-and-effect chain:

> activate → record state → confirm at the control → change the persistent object → reveal the next content.

The logical action happens before decorative animation. Overlap the confirmation, object response and content transition; do not concatenate their durations into a forced wait. Use named timing tokens and explicitly budget the time until the next controls can accept input. Do not confuse a selection-hold token with total journey latency.

Use a restrained outgoing/arriving language: words lift and fade, spatial objects sink toward their origin, new content rises, and the persistent object keeps its identity. For local state changes, a 140–180ms exit and 220–340ms entrance are useful starting ranges. Tune the complete transition to task frequency; repeated utility actions should be faster than a first-time story.

If using particles, emit one small bounded burst from the activated element toward the changing object. Fixed offsets make the result predictable and reproducible. Let particles finish independently of input readiness. Omit them when they obscure content or add no meaning.

Reuse the hero instance across related states. Position it with transforms rather than remounting it or switching its alignment abruptly. Track completed milestones separately from answers so Back and edit do not replay construction effects or corrupt the object's final state.

## Pace novelty and the ending

Give different beats different jobs: object entrance, visual comparison, short demonstration, quiet question, then a completion showcase. Keep their spatial grammar consistent. Avoid making every screen equally loud.

Reveal words through small masks when an editorial entrance adds value; reveal a whole sentence at once for reading-heavy work. Provide immediate reveal or skip. Preserve a stable button position across varying text lengths using intrinsic sizing or a deliberately sized content area; never clip long content to preserve a composition.

After real success, let the object resolve into a coherent state. A single showcase, small halo or personalized artifact can make the ending memorable. Keep the success acknowledgement and next action available while the showcase plays. Offer replay only for the visual experience, without repeating a backend action.

## Implement according to the work

Use existing CSS or Web Animations for fixed one-shot entrances and ambient transform/opacity loops. Use the current declarative engine for state exits, springs and continuity. Use motion values or equivalent for pointer-driven gestures rather than React rerenders every frame. Custom requestAnimationFrame work is justified when a changing physical model or shading requires it, and needs profiling and cleanup.

Prefer transform and opacity for frequent animation. The reference also morphs dimensions, masks and progress width; those are observed exceptions, not proof of cheap rendering. Treat them as a limited budget, profile them, and simplify if they compete with input. Static gradients and blur layers can still cost paint. Do not claim compositor-only or smooth-on-device performance from source alone.

For a carousel, derive the card positions from one fractional center value, follow the finger directly, apply modest edge resistance, then settle to a bounded item. Provide visible previous/next controls and keyboard access. Vertical scroll must continue to work. See the implementation reference for cancellation and fast-change handling.

## Preserve the experience without physical motion

Design three behaviors separately: normal motion, paused ambient motion, and reduced motion. A global animation setting does not automatically govern CSS, Web Animations, custom loops, haptics or every animated property.

- Reduced motion: retain selection, progress, logical object state and completion; remove travel, spin, overshoot, particles and vibration, and use immediate changes or short fades without long stagger delays.
- Ambient pause: hold background loops while user-triggered task feedback still works; stop associated timers and custom render work where possible.
- Keyboard and assistive technology: native activation, visible focus, logical focus after transitions, intact accessible phrases rather than a stream of letters, and concise status announcements.

A beautiful paused frame should remain useful. Haptics are optional direct-gesture feedback, feature-detected, with a no-op fallback; never promise them on all phones.

## Finish with observable proof

Check the requested journey at mobile 390×844, a smaller/shorter viewport, and a relevant desktop size. Inspect typing with the keyboard open on a real device when available; desktop viewport resizing does not prove keyboard behavior. Check Back, edit, rapid activation, pointer cancel, fast picker changes, reload, pending/failure/success states and reduced motion as relevant.

Inspect exported artwork separately from its screen preview. Run the repository's appropriate checks when code changes. For planning, give testable acceptance criteria instead of claiming tests passed. Report what was observed, what was inferred, and what remains untested.

Deliver the scoped implementation or storyboard, its visual/motion decisions, exact check results and material limitations. Do not stop at recommending that somebody add animations.
