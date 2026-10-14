# Sources and evidence boundaries

Research and wording review: 2026-10-12. The initial research used Firecrawl search/scrape and Context.dev search. This review used both again to recheck primary accessibility guidance and chart-scale advice. These sources support their stated topics; they do not validate every design preference or establish AI authorship.

## Source keys used by the audit map

| Key | Direct source and scope |
| --- | --- |
| nng-heuristics | [NN/g usability heuristics: status, familiar language, control, consistency, error prevention, recognition, and recovery.](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| wai-design | [W3C WAI design guidance: readable content, labels, feedback, navigation, and color-independent information.](https://www.w3.org/WAI/tips/designing/) |
| govuk-error | [GOV.UK error messages: specific corrective guidance and field association.](https://design-system.service.gov.uk/components/error-message/) |
| web-vitals | [web.dev Web Vitals: measured loading, responsiveness, and layout stability; a measurement is scoped to its conditions.](https://web.dev/articles/vitals) |
| wcag-core | [Normative WCAG 2.2: 1.1.1 alternatives; 1.4.1 use of color; 2.1.1 keyboard; 2.4.1 bypass blocks; 2.4.3 focus order; 2.4.7 visible focus; 2.4.11 focus not obscured; other applicable criteria.](https://www.w3.org/TR/WCAG22/) |
| wcag-contrast | [W3C understanding 1.4.3: contrast thresholds, large text definition, and exemptions.](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) |
| wcag-resize | [W3C understanding 1.4.4: text resizing to 200% without loss, excluding captions and images of text.](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) |
| wcag-target | [W3C understanding 2.5.8: target dimensions and all five exceptions.](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) |
| wcag-motion | [W3C understanding 2.2.2: qualifying automatic moving/scrolling/blinking and auto-updating content.](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) |
| wcag-reflow | [W3C understanding 1.4.10: reflow dimensions and genuine two-dimensional layout exceptions.](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) |
| wcag-status | [W3C understanding 4.1.3: programmatically determinable status updates without taking focus.](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) |
| wcag-spacing | [W3C understanding 1.4.12: resilience to user spacing overrides, with language/script exceptions.](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) |
| apg-dialog | [WAI-ARIA APG dialog pattern: initial focus, tab containment, closure, return focus, and roles. This is pattern guidance, not an independent conformance standard.](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) |
| gov-charts | [UK Government Analysis Function chart guidance: avoid misleading scales, preserve bar proportions, and choose chart-specific axes.](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/) |

## Accessibility qualifiers

- **Contrast:** normal text requires 4.5:1, large text 3:1 under 1.4.3 AA. Large means at least 18 pt or 14 pt bold, approximately 24 CSS px or 18.67 CSS px bold. Logotypes, inactive controls, and qualifying incidental text have exceptions. Evaluate actual foreground/background contrast, including changing gradients.
- **Target size:** 2.5.8 AA uses 24 by 24 CSS pixels or applicable spacing, equivalent-control, inline, user-agent, or essential exceptions. Inspect the actual hit area. A 24-pixel-diameter circle does not automatically contain a 24-by-24 square; evaluate the rule rather than an icon's nominal size.
- **Resize versus reflow:** 1.4.4 checks resizing text to 200%; 1.4.10 checks vertical content at a width equivalent to 320 CSS px and horizontal content at 256 CSS px height. A 1280-pixel viewport at 400% zoom is an example for vertical reflow. Legitimate two-dimensional regions have exceptions; a 200% zoom screenshot alone does not establish reflow conformance.
- **Motion:** 2.2.2 covers qualifying automatic moving/blinking/scrolling content lasting more than five seconds alongside other content, and automatic updates alongside other content without that five-second exception. Essential activity exceptions apply. Reduced-motion support is separate design guidance; do not describe every animation as an AA violation.
- **Text spacing:** test user overrides of 1.5 line height, 2 paragraph spacing, 0.12 letter spacing, and 0.16 word spacing, each relative to font size, without information or functionality loss. These are not required default design tokens. Applicable language/script exceptions remain.
- **Status messages:** inspect programmatic relationships and actual announcement behavior when assistive technology testing is available. A DOM role alone does not prove an audible announcement on a particular reader/device.

## Provenance and inference

Checks 1–100 adapt the user's pasted starting document. Original input remains at the user's private source attachment (not distributed). Checks 101–150 were added in the initial skill creation and refined during this review. The operational list now has 150 distinct inspection prompts, with related facets grouped during reporting.

The inherited HCI preprint citation was removed from the operational introduction because its specific claims were not independently established by this review. No claim that it is false is made. Broad visual preferences have been qualified instead of attributed to a standard.

Each audit-map record labels its basis and source relation: `criterion` for a scoped standard; `supporting_pattern` for the APG dialog pattern; `derived_guidance` for recommendations informed by a source; `author_judgment` for product/design reasoning without a direct external requirement. Product truth must be checked against the actual approved documents and evidence. Source links are not proof that a particular website passed.
