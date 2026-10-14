# Spectral atmosphere

Primary references: [02](../references/02-upgrade-modal-soft-ui.png), [03](../references/03-agent-platform-modal.png), [11](../references/11-spectral-gradient-poster-cards.png), [12](../references/12-pastel-onboarding-cards.png), [13](../references/13-cyan-research-feature-card.png). Reference 05 contributes warm atmosphere. Use `Theme direction="spectral"`.

## Visual contract

Luminous blue, lavender and cyan fields are bounded inside artwork or a few tall posters. Calm white copy planes make the color feel intentional. This is not a requirement to blur the entire page or surround every element with glowing gradients.

| Setting | Rebuild estimate / target |
|---|---|
| Substrate / ink | `#f2f3fc` / `#202327`; blue accent `#3755d8` |
| Color fields | Cyan `#b9eaf9`, lavender `#c9bbfa`, pale ice `#edf1ff`; saturated blue in art only |
| Radius | Card 28 px, object 18–24 px, control 14 px |
| Heading | Hero 48–72 px; feature 24–36 px; poster 30–44 px, line-height 1.05–1.15 |
| Body | 15–17 px / 1.5–1.6; marketing explanation ≤52 characters per line |
| Poster aspect | Approximately 0.46–0.65 width/height; minimum readable height 340–420 px |
| Art fade | 45–65% of card height; strongest color away from primary copy |
| Shadow | `0 22px 42px -26px #4568c745`; contact shadow kept faint |
| Grain | Fixed low-opacity art overlay only; visibly subtle at native zoom |

## Composition anatomy

The triptych mode uses three tall cards on a pale canvas with equal widths and 24–40 px gaps. Each poster has a small original mark near the top, broad unoccupied color and bottom-anchored title/short detail. Keep headline baseline consistent despite different color areas.

The onboarding/dialog mode puts pastel atmosphere at the top, one symbolic object at the center of it, and white task copy below. For a launch card, roughly 45% is art and 55% copy/actions. Reference 03's stronger textured plane fits a launch; reference 12's pale top light fits a first-run tutorial. Pick one, not both mixed inside the same sequence.

## Component and texture recipe

Use `PosterCard palette="blue"|"violet"|"ice"` for bounded posters, `OnboardingCard` for a step, `FeatureCard` for a feature and `Dialog` for an actual modal. The kit's poster palette is an approximation with a contrast-conscious alternate dark-ink variant. `Orb appearance="accent"` can provide one central physical icon.

A spectral plane can be recreated with two large radial gradients at opposing corners over a linear pale base. Radius should exceed the small icon size, making a broad light source rather than a neon spotlight. Keep clear white at the bottom of an onboarding frame. A fine SVG noise tile adds grain; do not animate the noise. For a frosted glyph use a colored rear plate, translucent front, 1 px white edge and a limited shadow. Use source artwork rather than a page screenshot as a background.

## Page and UX recipe

Sequence: clear task hero → three specific feature posters → product preview on a white plane → concise setup explanation → final action. A first-run flow is welcome → one real choice → example result → completion. Show text step progress, preserve entered choices, support Back/Skip when the product permits it, and make the final button state an actual completion event. Launch dialogs need an accessible close action and honest availability/terms. Upgrade actions need real plan limits, prices and a visible decision exit.

## Responsive and motion

Triptychs become a two-column pair plus a full-width final card below 900 px, then a single column below 640 px. Avoid horizontal carousels unless browsing is actually useful and controls are explicit. Dialog art shrinks before copy does; cap modal width at 480–560 px and allow its content to scroll. Keep button targets at least kit-default 44 px.

Reveal a poster once with ≤12 px vertical travel and 560 ms easing; stagger by 70 ms, capped at 280 ms. A dialog opens in 200–260 ms with small opacity/translation, never a large zoom. Large color fields remain static by default. Reduced motion shows every card immediately; a user's decision is never held until an animation completes.

## Acceptance and exclusions

Accept: a readable solid copy region, consistent palettes, deliberate poster silhouettes and genuinely useful onboarding choices. Reject: white text on pale lavender without contrast treatment, random neon blobs, multiple active animations, huge blurred shadows or a decorative beta badge implying availability. Compare art/copy area and baseline first; improve gradients only after the text and flow work.
