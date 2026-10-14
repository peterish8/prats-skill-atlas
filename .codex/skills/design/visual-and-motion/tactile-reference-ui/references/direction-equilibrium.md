# Lime equilibrium

Primary reference: [23](../assets/design-kit/references/23-axion-equilibrium-landing.png). Use `Theme direction="equilibrium"`; `AmbientBackdrop kind="contours"` gives a bounded rule field. The reference uses predominantly vertical lines; a generic rainbow gradient loses its defining structure.

## Visual contract

A lime-tinted line canopy, a centered serif axis and exceptionally generous vertical rhythm lead into almost flat process tiles. Institutional confidence comes from restraint and exact alignment. This direction differs from citrus: geometry is disciplined, corners smaller inside the page, actions sober and objects mostly linear.

| Setting | Rebuild estimate / target |
|---|---|
| Canvas / ink | White / near-black `#191c17` |
| Accent / field | Dark olive `#38451c`; pale lime `#dbffa3` fading to white |
| Outer page frame | 36–48 px radius only if an actual framed application needs it |
| Inner cards | 4–8 px radius; flat pale lavender-gray and one lime tile |
| Hero heading | Desktop 64–88 px serif; mobile 42–54 px; regular / 1.05–1.15 |
| Central axis | Headline 620–740 px wide; explanation 520–620 px |
| Canopy rules | 1 px, spaced about 24–44 px at production scale; varied lengths |
| Hero vertical rhythm | Nav → canopy → heading → copy → actions; 28–48 px local gaps |
| Transition rule | One centered 1 px rule, about 80–140 px high |
| Process triptych | 3 equal 240–320 px cards with 20–28 px gaps |

## Composition anatomy

Start with a compact centered nav floating over the lime field. Let the vertical rules occupy the top 35–45% of the visible hero and fade before the main heading. The heading sits lower than a conventional hero and anchors the white region. Place a concise paragraph and two actions under it. The main action is dark rectangular/soft-square; the secondary can be a text link with a thin underline.

A narrow centered vertical rule then leads to a brief editorial introduction, a broader section heading and three sequential process cards. Each card has a sparse line illustration near the top, a short serif verb near the bottom and two to four lines of specific explanation. One card can use lime while the others use a quiet neutral. This makes process structure legible without a forest of shadows.

## Components and line recipe

Use `SiteHeader`, `AmbientBackdrop`, `MarketingHero`, `ActionLink`, `SectionHeading`, `Surface depth="flat"` and `ShowcaseCard` where actual preview art is needed. A custom process tile is simpler than a product showcase: its art should be an original SVG of separated lines, aligned strokes or transfer arrows. Keep every stroke 1–1.25 px and limited to one visual family.

Build the canopy as a deterministic SVG or repeating-linear-gradient with a white mask toward the bottom. Alternate line groups with varied start/end positions; do not randomize per render. The section divider is CSS on an art wrapper, hidden from assistive technology. Avoid making the entire page a card on a gray board merely to replicate the presentation screenshot.

## Complete page and UX

Sequence: clear proposition → one action → process explanation → supported mechanism/product detail → specific evidence/FAQ → final access/contact route. If access is gated, state what the request means and what happens next. An access form needs labeled email/org fields, actual pending/sent/error states and a realistic response expectation. Process tiles explain transformations and constraints rather than repeating vague benefits.

For a working institutional app, keep the serif in section titles while using signal-like clear forms/tables in the task area. Supply definitions, scope and source dates for any displayed risk/financial statements. The direction itself does not establish a service's regulatory or economic safety.

## Responsive and motion

Below 900 px make nav width flexible and shorten the line canopy. Below 640 px shorten hero whitespace, keep the title at 42–48 px when possible and stack process cards with numbered text. The central axis remains; secondary actions wrap without becoming squeezed. The transitional rule can shorten to 48–64 px.

Use a single fade/12 px reveal for the process section. The canopy is static; an optional very slow opacity variation should be omitted when unnecessary. Do not animate lines repeatedly falling like rain or draw transfer arrows as fake live activity. Reduced motion renders complete process art at once.

## Acceptance and exclusions

Accept: a long but purposeful axis, genuine serif hierarchy, thin line field and flat disciplined process cards. Reject: citrus gel controls, many floating orbs, giant radii on every element, too many credibility badges or unsupported claims that risk is balanced. Make the main action reachable at normal viewport height without an artificial wait.

