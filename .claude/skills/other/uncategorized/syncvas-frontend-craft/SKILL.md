---
name: syncvas-frontend-craft
description: Improve Syncvas frontend UX, visual hierarchy, and purposeful motion while preserving its classroom-first MVP and existing design tokens. Use for Syncvas UI polish, interaction feedback, or animation work; do not use for realtime or domain behavior changes.
---

# Syncvas Frontend Craft

Build a calm, classroom-professional interface for a live whiteboard product. The design should feel precise and inviting, never decorative at the expense of teaching.

## Start with the product boundary

Read `AGENTS.md`, the requested route/components, and the applicable product docs before changing code. Preserve these invariants:

- The teacher is the only shared-board editor.
- Student pan and zoom are local; manual navigation exits follow mode locally.
- The canvas stays visually quiet, readable, and free of decorative color fields.
- Do not change socket, Convex, authentication, moderation, or AI behavior while doing visual work.

## Visual direction

- Treat this as a trust-first educational product: warm-neutral surfaces, a lime action accent, clear type hierarchy, and restrained rounded surfaces.
- Preserve the existing composition on a redesign. Do not add generic feature-card grids, fake analytics widgets, neon gradients, or glass everywhere.
- Use the semantic tokens and named motion roles in `app/styles/tokens.css`; do not introduce raw colors, radii, durations, or a parallel animation system in components.
- Prefer real hierarchy (spacing, text, borders) to extra containers. Keep dense teaching/product controls crisp and opaque.
- Maintain light and dark theme parity and visible keyboard focus.

## Motion and interaction

- Motion must communicate state or feedback. Use CSS transform and opacity for small transitions; do not animate layout, canvas state, or high-frequency board interactions.
- Reuse `--ease-press`, `--ease-out`, `--duration-press`, `--duration-hover`, `--duration-panel`, and `--duration-modal`.
- Fast press feedback belongs on buttons and icon controls. Inputs are recessed and do not move.
- Keep continuous motion contained to entry/marketing/summary surfaces. Never animate decoration over the Excalidraw drawing region.
- Respect the global `prefers-reduced-motion` contract in `app/styles/base.css`. New animation must have a non-moving reduced-motion result.
- Avoid an animation library unless existing CSS cannot express the interaction; do not make a page client-rendered just for cosmetic motion.

## Workflow

1. Inspect the route, its shared components, `app/styles/tokens.css`, `base.css`, and the relevant stylesheet. Check the installed Next.js docs for any new framework-specific API.
2. Audit first: identify hierarchy, touch/keyboard feedback, loading/empty/error clarity, motion purpose, and theme parity. Keep only findings that materially improve a teacher or student task.
3. Implement the smallest coherent set of changes. Extend the existing CSS layer instead of creating a new visual system.
4. Verify with the route in both themes where practical, reduced motion, keyboard focus, `npm.cmd run lint`, `npm.cmd run typecheck`, and a production build when the change justifies it. Report anything not browser-tested.

## Scope checks

- Do not treat a build as proof of visual or device quality.
- Do not add a dependency for simple CSS motion.
- Do not modify unrelated dirty files. If the target file has unrelated edits, preserve them and work around them.
