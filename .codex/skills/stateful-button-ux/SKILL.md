---
name: stateful-button-ux
description: "Audit and implement async button feedback in React apps, using loading and success states only where a user action waits or mutates data."
---

# Stateful Button UX

Use this skill when a task asks for a stateful button, async action feedback, a loading/success animation, or an audit of whether buttons need richer feedback.

## Workflow

1. Inspect the project before changing code. Confirm TypeScript, Tailwind CSS v4, Motion (or the project's existing animation system), `components/ui`, and the local class-name helper. If a prerequisite is missing, report the exact setup command or file location; do not install or scaffold a parallel design system without approval.
2. Inventory the target buttons and classify each action with `references/decision-guide.md`.
3. Use a stateful button for actions that submit, save, export, generate, retry, or otherwise wait on a network/server mutation. It should show a disabled loading state, then a brief success state, and return to idle.
4. Keep navigation links, local toggles, disclosure controls, tab/selection controls, modal open/close buttons, and instant icon actions simple. Do not add a fake async animation to make these controls look busy.
5. Do not double-wrap controls that already expose a correct busy/disabled label and error path. Improve the existing state in place only when it is missing accessibility or duplicate-click protection.
6. Preserve the product's visual language. Reuse existing tokens/classes through `cn`; do not introduce a hard-coded green button into a product that uses another palette. Keep motion subtle, keyboard accessible, and compatible with reduced-motion preferences.
7. For the shared primitive, preserve normal button semantics (`type`, keyboard activation, form behavior, `disabled`, and `aria-busy`). Prevent duplicate invocations, await promise-returning handlers, reset on failure, and expose an error callback when the caller needs to render an error message.
8. Verify the smallest relevant surface first, then run TypeScript/lint/tests appropriate to the change. Check that the loading state is visible, the button cannot be clicked twice, success is transient, errors recover to idle, and reduced motion does not break the action.

## Component contract

The reusable implementation belongs at `components/ui/stateful-button.tsx`. A demo may live at `components/stateful-button-demo.tsx`, but demos are not a reason to add the component to unrelated product flows. Integrate the primitive only into the candidates selected by the audit.

See `references/decision-guide.md` for suitability examples and setup guidance.
