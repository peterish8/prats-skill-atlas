# Accessibility and responsive behavior

Use semantic landmarks, headings in order, native controls where possible, visible focus, accessible names, descriptive error recovery, and non-color status signals. Every important action must work through keyboard and touch as well as pointer hover.

Check text and control contrast, target size, zoom/reflow, text resizing, screen-reader reading order, form labels, validation messages, focus trapping/restoration in overlays, and reduced motion. Do not remove outlines without an equal or better focus treatment.

Test at a small mobile width, large mobile width, tablet, desktop, narrow landscape, and with unusually long content. Use resilient grids and wrapping rather than brittle absolute positioning. Images need useful alternatives or empty alt text only when decorative.

For responsive priority, preserve core task, context, primary action, and recovery path first. Reflow or defer secondary decoration; do not simply shrink everything until it technically fits.

## Required interaction checks

- Tab through the screen in visual order. Focus must remain visible and never disappear behind a sticky or modal surface.
- Test Enter/Space for buttons, Escape for dismissible overlays, and arrow-key behavior only where the native or established pattern expects it.
- Ensure labels, helper text, and errors are programmatically connected to their fields; preserve entered values after recoverable failures.
- Use text and icons/patterns together for success, warning, and error states. Never rely on color alone.
- Verify touch targets are practical at narrow widths and that hover content has a tap/keyboard equivalent.
- Test at 200% browser zoom and with longer localized strings before declaring a layout responsive.
