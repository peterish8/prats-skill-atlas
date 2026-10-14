# Visual foundations

The common quality across these references is controlled hierarchy: a legible white or cream plane, substantial unoccupied space, one visual field, an object with convincing edges and a clear next action. Their cleanliness comes from proportion and material continuity. Adding a gradient to a standard dashboard does not reproduce it.

## What the images establish

These are static screenshots, cropped presentations and design studies. The catalogue records observable anatomy separately from recommended implementation. No exact source font, original motion curve, small-screen layout or conversion benefit can be identified from a capture. Image 26 is only 235×147; use it to infer a broad airy composition. Image 17 is also a small miniature. Image 19 repeats image 10 and is retained as a separate user submission, not an additional design direction. Outer gray boards, creator handles, photographed hands, watermarks and device perspective are presentation framing, not web UI to reproduce.

## Build the page in five layers

1. **Task:** Decide what the visitor understands and does first. Write real headings, actions, evidence and empty states before decorating. One hero CTA leads to one meaningful next step.
2. **Composition:** Set the content width, alignment axis, relative art area and section rhythm. Compare the silhouette to the chosen reference before inspecting tiny shadows.
3. **Material:** Establish page substrate, surfaces, borders and depth. Components in the same plane share one light direction and one shadow family.
4. **Atmosphere:** Add a bounded field, texture or original illustration. Leave a quiet region behind text; maintain a solid fallback.
5. **Interaction:** Connect controls to genuine behavior. Add brief motion that explains the transition; keep the initial render and reduced-motion view complete.

## Shared implementation baseline

| Property | Working range | Why it matters |
|---|---|---|
| Desktop content width | 1080–1240 px; editorial text 680–860 px | Avoid stretched paragraphs and thin artifacts |
| Page gutters | `clamp(20px, 4vw, 64px)` | Preserve breathing room across viewports |
| General body copy | 15–18 px, line-height 1.45–1.65 | Reference miniatures are not permission for unreadable live text |
| App labels | 13–14 px; secondary metadata 12–13 px | Keep density without using near invisible labels |
| Heading tracking | Sans −.025 to −.055 em; serif −.015 to −.035 em | Shape large type without crushing punctuation |
| Control height | At least 44 px in kit defaults | Small screenshot buttons must scale to usable controls |
| Spacing rhythm | 4,8,12,16,24,32,48,64,96,128 px | Repetition keeps complex compositions calm |
| Neutral surface border | 1 px, visible against adjacent plane | Shadows alone cannot define all controls |
| Art to text separation | 24–48 px; hero overlap only in art layer | Avoid text competing with ornamental objects |
| Section rhythm | 64–128 px; denser app sections 24–40 px | Marketing and working screens need different density |

These are starting settings; each direction adjusts them. The package CSS uses `--tui-bg`, `--tui-surface`, `--tui-text`, `--tui-muted`, `--tui-border`, `--tui-accent`, `--tui-on-accent`, `--tui-soft`, `--tui-halo`, `--tui-radius`, `--tui-control-radius`, `--tui-gap`, `--tui-shadow`, `--tui-float`, `--tui-font`. Override them within a named wrapper, not on `:root`, when adapting an existing application. Import `@tactile-ui/tokens/styles.css` once.

## Typography with an actual decision

The kit makes no external font requests. It bundles self-hosted Manrope and Instrument Serif with license/provenance files. These are deliberate substitute choices, not identified original screenshot fonts. Keep the supplied assets/CSS together so the local font URLs resolve. The host may override the font variables with its own licensed faces; system sans and Georgia remain fallbacks. Use at most one heading face and one body face, and two to three weights. Match approximate width and line break before chasing a font name.

Large headings should wrap through a constrained `max-inline-size`, not forced `<br>` elements that break a narrow phone. Mark a deliberate accent phrase with a span while keeping the entire heading meaningful. Numbers use tabular figures when aligned in rows; decorative posters do not need numerical display faces. Preserve content hierarchy with one page h1, section h2 and card h3. Artwork never substitutes for the heading.

## Material grammar

White relief uses a faint light edge plus a small contact shadow plus a wide low-opacity shadow. A recessed tray uses a very subtle inner shadow and a visibly different fill. Keep depth ordinal: page plane → card → small object. Do not give every row floating depth. Glass requires a colored substrate, a translucent front and an actual edge; blurring an empty white rectangle is insufficient.

Colorful texture belongs in the artwork and hero plane, not behind dense tables, validation errors or multi-line body copy. Grain should be barely visible at 100% zoom. Hairline connectors should survive standard contrast viewing but remain secondary to labels. Consistent 1–1.5 px line icons work well with quiet materials; use original/simple symbols and avoid importing a reference brand mark.

## Preserve the host product

Read the host's design contract and component library first. Adapt the chosen direction to the existing semantics, routes, statuses and accessible patterns. This standalone kit does not alter FinanceAPI's accepted SvelteKit/Convex architecture or its claim/calculation/coverage rules. In a financial workflow, decorative green cannot imply a verified finding and a pretty chart cannot supply invented data. Retain sources, periods, units, uncertainties and all real states.
