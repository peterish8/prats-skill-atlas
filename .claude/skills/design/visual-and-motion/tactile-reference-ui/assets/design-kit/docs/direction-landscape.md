# Landscape product

Primary references: [32](../references/32-corebit-landscape-product-cards.png), [33](../references/33-financial-autonomy-landscape-features.png), [34](../references/34-organize-pastel-product-triptych.png), [35](../references/35-lendro-split-product-hero.png), [36](../references/36-goodluca-cloud-learning-bento.png). Use `Theme direction="landscape"`; `ShowcaseCard` supplies colored art stages and `AmbientBackdrop kind="landscape"` uses the kit's original generated landscape asset. No reference photographs or branded screenshots are supplied as output assets.

## Visual contract

A real product fragment is the hero object. Landscape, sky or pastel air forms a backdrop; white product UI supplies crisp detail. The page remains restrained around the stage. Different card spans express the importance of each workflow rather than a generic decorative grid.

| Setting | Rebuild estimate / target |
|---|---|
| Canvas | White or warm `#fbf8f4`; copy near-black; optional blue accent `#233fad` |
| Stage palette | Sky `#c4e6f5`, lavender `#c4ccf1`, mint `#d8f1dd`, blue `#466ee8` |
| Hero headline | 48–72 px sans or 48–66 px serif, 1.04–1.15 line-height |
| Card radius | 16–28 px; embedded UI 10–16 px; product panels 12–20 px |
| Stage height | Feature 260–360 px; split hero 560–720 px at desktop |
| Product fragment | Approximately 60–80% stage width; crisp white plane, 1 px rim |
| Artifact shadow | `0 18px 34px -18px #26345450` plus faint contact edge |
| Tilt | Decorative fragments only, generally −6° to +6°; tables remain upright |
| Triptych gaps | 20–28 px; feature copy under art 12–20 px |
| Hero columns | 45–50% copy / 50–55% art; stage independently clips illustration |

## Choose one of four compositions

**Centered metric triptych (32):** plain nav, large serif statement, two actions and three scenes. Make the central scene 15–25% taller/wider than flanks. Each has one focused artifact, not an entire dashboard. This composition works when the metrics are genuinely relevant.

**Feature rail/triptych (33,34):** clear section heading, three stage cards and specific explanations. In 34 titles/explanations sit inside the upper area and artifacts rise from below; in 33 copy sits outside beneath the image. Choose one placement throughout the section. Do not mix alternating copy positions without a reason.

**Split hero (35):** substantial white copy column, left actions, tall right scene holding a genuine product screen. Low copy placement creates breathing room on a large desktop; reduce that gap on small/short screens. The product screen can crop inside an illustration frame, while the actual app remains separately usable.

**Learning bento (36):** one wide core workflow beside a small companion, then three secondary workflow cells and a wider deeper feature. Spans follow user priorities. Use shared stage palette, similar object depth and each cell's actual task.

## Components and artifact construction

Use `MarketingHero`, `SectionHeading`, `ShowcaseCard tone="meadow"|"blue"|"mint"|"lavender"`, `FileStack`, `MetricCard`, `Meter`, `Sparkline`, `Surface` and `Reveal`. A `ShowcaseCard` requires an art slot; fill it with a focused original product fragment. The supplied landscape is original generated artwork, not a copy of the reference photographs or a product claim. Approved original/stock imagery can replace it when its rights and crop are appropriate.

Build fragments from honest UI: a file list, a labeled form, a small bounded progress item or a compact comparison. A static screenshot should have relevant alt text; an art-only mini UI should be `aria-hidden` with the capability explained in card copy. Do not embed tiny real interactive controls inside a scaled preview. Use one real working example beside or after the decorative stage.

## Complete UX and states

Sequence: user recognizes job → sees relevant product artifact → understands features through distinct workflows → tries one usable example → sees setup/limits → takes final action. A landscape itself does not explain the product. Every fragment should map to a capability the host actually implements. Clearly label demonstration values; use real data and dates for claims about savings, verification, progress or payments.

A course/product flow includes loading, empty, selected, in-progress, success and recoverable failure states. A certificate state has an actual qualification/issuer explanation. A payment example does not capture sensitive payment information through a pretend client-side handler. Demo links resolve to a genuine sandbox or disclose their preview behavior.

## Responsive and motion

Below 900 px use two columns or split hero stacking; below 640 px preserve copy → action → product → features order and stack feature stages. A wide bento core card becomes one ordinary card; do not horizontally crop required text. Show one readable product fragment instead of shrinking a full desktop screen. If a rail is intended, add visible Previous/Next controls, focusable items and a clear position indicator.

Reveal card groups once with at most 70 ms increments and 280 ms total delay. Product art can settle ≤12 px on entry; leave text and controls immediately available. Hover tilt is optional and only on pointer devices, max 1–2°; omit it on meaningful charts/forms and for reduced motion. Avoid continuously floating product panels or cloud parallax.

## Acceptance and exclusions

Accept: an authentic product artifact, coherent stage palette, deliberate span hierarchy, crisp white UI and a usable next step. Reject: scenery-only cards, copied photos/device UI, unreadable screenshot miniatures, decorative certificates presented as verification, accidental overflow or fake savings/usage numbers. Inspect art at 100% and the actual working flow separately.
