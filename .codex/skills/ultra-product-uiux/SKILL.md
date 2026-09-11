---
name: ultra-product-uiux
description: Design, improve, audit, and validate polished web product interfaces with clear UX, accessible responsive systems, and purposeful motion. Use for substantial frontend design work or visual UX audits, not trivial CSS or backend-only tasks.
---

# Ultra Product UI/UX

Create product interfaces that make the next user action clear, safe, and satisfying. Design is a decision-making system, not decoration.

## When to use it

Use for new web applications, meaningful redesigns, page or screenshot critiques, UX/visual audits, design-system work, conversion flows, responsive repair, or intentional motion. Do not use for a one-property CSS fix, isolated recoloring, or backend work unless a design-quality review is requested.

## Choose the mode

- **Build or improve:** inspect, define the experience, implement the smallest coherent change, then validate.
- **Critique:** audit before proposing a redesign. Do not edit source unless asked.
- **Reference-led:** extract reusable hierarchy, density, type, contrast, and interaction principles; never copy a brand's assets or identity without authorization.
- **System:** first inspect existing tokens and components. Extend the established system rather than create a competing one.

## Core workflow

1. **Understand.** Inspect routes, components, assets, fonts, tokens, existing states, and project constraints. Identify user, primary task, desired action, anxieties, current visual language, reusable parts, and actual data shape. Ask only questions code or supplied artifacts cannot answer.
2. **Define.** State the screen's primary job; primary and secondary actions; reading order; decision-blocking uncertainties; success, loading, empty, error, and permission behavior; mobile constraints; and accessibility needs. For each major element, identify the user question it answers.
3. **Direct.** Declare a one-line design read and define the personality, color roles, type roles, spacing/radius/elevation scales, image treatment, icon family, interaction style, and motion vocabulary. Read [design principles](references/design-principles.md) before a substantial visual change.
4. **Plan states.** List the conditions that can change the interface and define the visible state, user action, and recovery path for each. For multi-screen flows, trace entry, progress, confirmation, interruption, and return paths before implementation.
5. **Implement.** Use semantic HTML, existing tokens and components, stable responsive primitives, accessible controls, and real-content constraints. Keep scope focused; do not add fake behavior to decorate a screen.
6. **Review.** Recheck hierarchy, alignment, contrast, focus, keyboard access, content overflow, responsive breakpoints, motion, and performance. Fix the highest-impact issue first. Read [critique rubric](references/critique-rubric.md) for a structured audit.

## Minimum design brief

Before substantial implementation, write a compact brief in the response or plan:

| Item | Required decision |
| --- | --- |
| User and context | Who arrives, what they are trying to accomplish, and what constraints they have. |
| Primary job | The one task this screen must make easier. |
| Primary action | The clear next action and what happens after it. |
| Information order | What users must understand first, second, and only on demand. |
| Trust/recovery | What could cause hesitation or failure and how the UI resolves it. |
| Responsive rule | What remains visible, wraps, collapses, or moves at narrow widths. |
| Accessible behavior | Keyboard, focus, labels, validation, and non-visual feedback requirements. |

## Required principles

- Give every screen one primary job. Quiet secondary content so the main action is obvious.
- Use familiar patterns where they reduce cognitive load. Distinction comes from a coherent system, not arbitrary layouts.
- Design for real content: long and missing values, dense data, image variance, localization, slow networks, and future expansion.
- Use motion only to confirm, reveal, connect, or explain. It must be fast, interruptible where state can change, and fully optional under `prefers-reduced-motion`.
- Never trade clarity, accessibility, trust, or task completion for visual novelty.

## Load guidance only when relevant

- [Product-page UX](references/product-page-ux.md): catalog, product detail, purchase, booking, pricing, checkout, and subscription flows.
- [Conversion and content](references/conversion-and-content.md): decision support, honest trust signals, prices, policies, and high-intent copy.
- [Motion and interaction](references/motion-and-interaction.md): state feedback, transitions, loading, and reduced motion.
- [Design systems](references/design-systems.md): multi-screen consistency, tokens, variants, and state coverage.
- [Accessibility and responsiveness](references/accessibility-and-responsive.md): keyboard, touch, contrast, semantic structure, and viewport resilience.
- [Critique rubric](references/critique-rubric.md): severity-scored audit format.

## Implementation guardrails

- Preserve the product's core functionality and platform conventions.
- Inspect dependency and framework documentation before adding or using a library/API you have not verified in this project.
- Do not make an interface client-rendered solely for cosmetic effects.
- Avoid generic centered heroes, purple-blue gradient defaults, unrelated 3D decoration, card-on-card layouts, fake testimonials, unverified metrics, and theatrical animation.
- Every critical interaction must work with keyboard and touch, not hover alone.
- Do not claim a visual, responsive, or accessibility result is verified unless the relevant route and state were actually exercised.

## Report on completion

State what changed, why it helps the user, affected files/components, handled states and breakpoints, verification performed, remaining limitations, and one sensible next improvement. For audit-only work, report concrete prioritized findings without changing files.
