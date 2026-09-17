# Implementation contracts for frontend fidelity

Read only the sections that match the task. Each contract starts with the intended behavior; choose mechanisms that fit the target stack.

## Shared component and state ownership

For each affected primitive, map its visual role, semantic element, valid states and consumers. Keep error, selected, disabled/busy and focus styles attached to that role. Do not use a visual press state as application selection or server success.

A shared field should connect its label to the actual input and expose the relevant hint/error. A custom widget needs defined focus and keyboard ownership, not only an accessible-looking wrapper. Document whether busy controls keep focus and how cancellation works. Inspect prop forwarding and consumer overrides so the declared contract survives actual use.

Fix duplicated literals that cause drift when it materially helps the requested change. Avoid turning an incidental one-off visual into a global token. When the same content has several representations, use stable IDs and a single content model; do not let display order silently determine stored meaning.

## Layout and content bounds

Record the useful region after header, safe areas, browser UI and any persistent controls. Decide which element scrolls and which items stay visible. Use flexible min/max constraints where content length varies. Keep transformed decorative children from creating page-level overflow without clipping the useful text or focus ring.

Pick breakpoints where the composition stops working. Inspect immediately below and above a changed breakpoint plus a short-height case. Test a long label, an error that wraps and large text. A screenshot at one phone size is a reference state, not proof of responsive coverage.

For ordinary content, let text wrap and regions grow. For compact identity artwork, define an explicit text box, typography range and fallback: wrap to a permitted number of lines, reduce within a readable range, or provide a full-value accessible alternative when truncation is allowed. Do not alter a person's name merely to fit the design.

If an element's geometry truly depends on measured content, observe its container/content and update only when measurements change. Disconnect observers on teardown and avoid read/write cycles that resize their own observed input repeatedly. A ticker, canvas annotation or compact card may need measurement; ordinary flow layout usually does not.

## Keyboard, zoom and platform layout

Treat software keyboard behavior as a separate concern from viewport width. Preserve field visibility, inline feedback and an escape or next action. Prefer native scrolling/focus behavior unless it breaks the required surface. Choose overlay versus resize behavior consciously; browser metadata support and platform behavior differ.

Do not suppress zoom to protect the composition. Test reflow and distinguish legitimate two-dimensional work areas from decorative overflow. Larger comfortable controls can be a product preference without being mislabeled as a universal standard requirement.

Consult [W3C reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), [W3C target-size guidance](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) and [Chrome viewport/keyboard behavior](https://developer.chrome.com/blog/viewport-resize-behavior) when these implementation decisions matter. The Chrome article describes browser-specific behavior; it is not a guarantee for Safari or every WebView.

## Resource readiness and the first frame

Identify critical dependencies separately for page content, decorative startup and generated outputs. Use a product-compatible fallback background/font/media and reserve sensible space to limit disruptive changes. Do not wait for every image merely to begin an unrelated interaction.

Where a bounded gate is justified, specify its trigger, maximum wait, fallback and cleanup. Clear timers and cancel owned frame callbacks where practical; stale asynchronous work must not update an unmounted or superseded view. Font readiness does not prove the preferred typeface loaded successfully: inspect representative text and fallback behavior.

See [Document font readiness](https://developer.mozilla.org/en-US/docs/Web/API/Document/fonts) for the actual API contract. Choose a target-appropriate timeout rather than copying the source's 1500ms value into every app.

## Recovery and local continuity

Write the contract for initial, loading, success, empty, error, retry and restore only where they are applicable. Errors should preserve usable input and explain the next valid action. A status should not cover the control the user needs to recover.

Specify whether a draft is in memory, tab storage, durable local storage or on a server, why that lifetime is appropriate, and what is removed after completion. Validate version, types, enum values and allowed bounds before restoring; malformed/unavailable storage should yield a safe usable state. Browser-tab storage is not a secure vault and may be copied into a new tab in some circumstances; avoid absolute secrecy or lifetime claims. See [sessionStorage behavior](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage).

A browser online indicator is a connectivity hint; confirm persistence with the actual operation result. Preserve retry identity when the product's backend supports idempotency. Do not automatically retry irreversible actions without the product's authorization and retry contract. Show prototype fixtures and simulated operations honestly.

## Artifact and external-output parity

Define a content snapshot: identity, selected item ID, localized copy, theme, output dimensions and applicable fonts. Share portable palette/data definitions or intentionally maintain a documented mapping across DOM, SVG, canvas or PDF.

Tie a prepared artifact to a snapshot key or generation counter. On a content change, mark it stale. Publish an asynchronous result only if its snapshot is still current and its owner is alive. An older task completing last must not become the current download. Expose preparing/ready/failed when that distinction matters.

Inspect the actual encoded file at full resolution and the size users will see it. Check long text, contrast, cropping, required footer content and the chosen design's material cues. A CSS preview, Blob creation or successful unit test alone does not prove appearance in a viewer.

Keep user-activated external actions in their valid gesture path and provide appropriate save/copy alternatives. Cancellation is neutral; requesting a share or clicking a download is not proof that another application delivered or stored it. Verify device-sensitive behavior separately when it is in scope.
