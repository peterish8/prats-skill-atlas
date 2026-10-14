# Warm editorial

Primary references: [08](../references/08-growth-story-analytics-card.png), [13](../references/13-cyan-research-feature-card.png), [16](../references/16-editorial-integration-feature-cards.png). Use `Theme direction="editorial"`.

## Visual contract

Large confident typography leads. One warm physical accent supplies a focal point. White/off-white panels, editorial pacing and restrained linework make this suitable for stories, studios or a carefully evidenced product narrative. A warm chart or badge must not invent a success claim.

| Setting | Rebuild estimate / target |
|---|---|
| Substrate | `#f4f1ed`; near-white content plane |
| Ink / muted | `#202327` / `#606770`; do not use pale gray on essential phrases |
| Warm action | `#bd4808`; art can use orange `#ff840e` and gold `#ffc565` |
| Large card radius | 32 px; narrative cards can reach 40 px; editorial technical cards 12–18 px |
| Hero heading | 52–80 px sans or 48–72 px serif; line-height 1.02–1.14 |
| Body | 16–18 px / 1.55; readable width 48–66 characters |
| Narrative width | 740–980 px; content sections 1120–1200 px |
| Badge | 12–14 px text; 1 px warm rim; tight faint warm contact shadow |
| Ambient shadow | `0 16px 30px -22px #66361a45`; shadows mostly on one medallion or annotation |

## Composition anatomy

Reference 08's story mode is a generous statement card above a separate sparse illustration card. Use an eyebrow/pill, a three-line maximum headline and a visually quieter optional continuation. Beneath it place one artifact with spacious axes and an annotation aligned to its relevant datum. This is effective only when the story is concrete.

Reference 16's service mode uses two equal cards with modest serif headings and tidy technical miniatures below. Keep it straight, structured and easy to compare. The heading creates editorial character; the connected artwork creates specificity. Reference 13 contributes a warm medallion over a cyan/white window; use it as one feature illustration, not a competing third palette for the whole page.

## Components and custom detail

Use `SectionHeading`, `FeatureCard`, `Badge`, `Surface`, `Sparkline` and `IntegrationMap`. `Orb appearance="accent"` in editorial provides a warm medallion. `Sparkline` handles chart coordinates; the host must supply actual values, dates, scale interpretation and textual detail. Build a raised annotation as a small white pill with a narrow warm under-rim and 10–18 px shadow blur; avoid glowing every number.

Use a serif heading only on title/section text when the content invites reading. Keep body, tables, form labels and navigation sans. The serif should have regular weight and enough line-height to retain its rhythm. A marked gray continuation still needs legible contrast; it is lower emphasis, not hidden meaning. Grid lines are 1 px, faint and limited to an art or chart region.

## Page and UX recipe

Sequence: specific narrative hero → artifact or result showing the claim → two service/feature cards → process explanation → genuine proof with date and context → relevant action. A case study includes what changed, over what period and what the figure measures. If numbers are illustrative, label them as demonstration data beside the chart. If there is no proof, use a product artifact rather than a fictitious success story.

A service decision page offers scope, deliverables, turnaround definition, constraints and a real contact/booking route. Include a sent/failed state for a form, preserve text on failure and confirm the next expected step. Use one main action per stage; a case study link is navigation and should use `ActionLink`.

## Responsive and motion

Headline size uses `clamp(36px, 5.5vw, 76px)` and a width that creates similar readable lines without hard breaks. At 640 px stack story/technical cards, shrink decoration and retain 20–24 px content padding. Real charts reflow labels and include a data summary/table; do not scale the whole chart with tiny text.

Warm medallion hover is optional and only if interactive. Reveal the artifact once; a chart may draw on first presentation only when it still shows complete values immediately for reduced motion. Never count up money, fabricated success metrics or hide the outcome behind an entrance. A narrow highlight can fade in after content, within the 280 ms maximum stagger.

## Acceptance and exclusions

Accept: one typography idea, generous readable statements, a supporting artifact and restrained orange/gold object detail. Reject: badge/counter clutter, oversized fake proof numbers, every noun highlighted, thin unreadable body text or turning the editorial layout into a generic metric dashboard. The evidence and action should remain clear with all warm art removed.
