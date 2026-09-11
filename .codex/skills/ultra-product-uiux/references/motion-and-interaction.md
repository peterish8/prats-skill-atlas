# Motion and interaction

Motion earns its place when it confirms an action, signals progress, reveals information, connects a panel to its trigger, preserves spatial context, or makes loading/success/failure legible.

Use transform and opacity for normal UI transitions. Keep durations brief, easing consistent, and state changes responsive to interruption. Buttons can have a small press response; inputs should stay stable. Do not animate layout continuously, delay essential actions, or add motion merely to fill space.

Good patterns: opacity/transform entry for a contextual overlay, a short expand/collapse with an accessible state change, a skeleton matching its eventual layout, or a compact success transition after an action completes.

Avoid scroll hijacking, long staggered copy, bouncing, persistent floating objects, hover-only communication, and animation on every component. Respect `prefers-reduced-motion`; motion cannot carry required information or prevent an action.

Check performance on low-end mobile conditions: avoid expensive filters over scrolling content, broad `transition: all`, animated large shadows, and JavaScript-driven values that rerender a page each frame.

## Motion selection

| Event | Suitable response | Avoid |
| --- | --- | --- |
| Button/tap | Brief press feedback and immediate disabled/progress state where needed. | Delayed response or bounce. |
| Menu or popover | Short opacity/transform transition from the trigger direction. | A full-page entrance sequence. |
| Expand/collapse | Height-free composition when possible; preserve semantic expanded state. | Motion that hides the final state from assistive technology. |
| Async loading | Layout-matched skeleton or progress copy. | Indeterminate motion when a real progress value exists. |
| Success/error | Short status transition plus persistent text feedback. | Color-only or animation-only confirmation. |
| Navigation | Keep context stable; use a small route or shared-element transition only if it clarifies place. | Scroll reset surprises or long interstitials. |

Default to a single predictable easing family. Entrance transitions should normally finish in a few hundred milliseconds; repeated or user-triggered feedback should be shorter. Use a different value only with a reason tied to content weight or physical metaphor.
