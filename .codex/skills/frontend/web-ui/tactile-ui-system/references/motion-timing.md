# Motion timing

Speed is what makes this system read as a precision tool rather than a soft consumer
app. Keep every duration in this range — don't let panels or modals drift slower "for
elegance."

| Interaction         | Duration          |
| -------------------- | -----------------: |
| Button press          | 100-120ms |
| Hover state change     | 130-160ms |
| Tooltip                | 100-140ms |
| Dropdown open           | 160-190ms |
| Side panel open/close    | 220-260ms |
| Modal open/close          | 200-240ms |
| Card flip (e.g. flashcard) | 300-360ms |
| Block/item reorder          | spring animation |

## Easing tokens

```css
:root {
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-press: cubic-bezier(0.2, 0, 0, 1);
}
```

Use `--ease-press` for the button-down transform (`transform 120ms var(--ease-press)`).
Use `--ease-out` for things settling into place (panels, dropdowns, modals).

## Rules

- Never use `scale()` on hover for ordinary controls. A 2px vertical `translateY` on
  press reads as physical; a hover scale reads as a generic web hover effect.
- No slow floating/ambient animation on static elements.
- No continuous pulsing on "AI is active" indicators — show a brief transition into and
  out of the active state instead of looping.
- No large hover scaling on cards or thumbnails.
- Don't add a glow transition on every interactive element — reserve glow/ring effects
  for focus states and the accent button variant only.
