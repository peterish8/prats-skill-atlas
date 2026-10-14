# Pixel atelier

Primary references: [27](../references/27-cyan-pixel-design-studio.png) and [28](../references/28-cargo-scanline-logistics-hero.png). Use `Theme direction="atelier"`; choose `AmbientBackdrop kind="pixels"` or `kind="scanlines"`, not both in one hero.

## Visual contract

Precise monochrome copy sits against one graphic cyan/indigo field. Asymmetry, restrained navigation and crafted texture give the page character. Reference 27 uses soft squares and sans type; 28 uses a subject-shaped horizontal line mask and serif type. Preserve these as two coherent modes of one graphic direction.

| Setting | Rebuild estimate / target |
|---|---|
| Canvas / ink | White/soft gray / `#151719` |
| Pixel light | Cyan `#92def0` to blue `#39a9e0`, white fade above |
| Scanline art | Indigo-blue `#675bef` on very pale gray |
| Heading | Studio 48–72 px sans; logistics 44–62 px serif; mobile 34–44 px |
| Pixel cells | 28–56 px square at desktop; low per-cell alpha variation |
| Scanline spacing | 4–7 px, line thickness 1.5–2 px; fixed static silhouette |
| Outer panel | 16–24 px radius in studio; 0–4 px in technical scanline mode |
| Actions | Dark pill in studio; near-square 4–8 px rectangle in logistics |
| Layout | Copy left 5–6 columns; facts/art right; artwork fills lower third to half |
| Shadow | Small black action contact shadow; panel ambient shadow nearly invisible |

## Mode A: cyan studio

Use a restrained top bar, a large open region, then lower-left headline/description/action and two short right-side service facts. Cyan squares build toward the bottom of the panel and fade into the white copy region. Content is asymmetric but balanced: align facts to the headline block, not randomly to the window. External transparent sculptures and creator portrait in the screenshot are presentation artifacts; they are not required UI.

## Mode B: technical scanline

Use a slim mono-like nav, modest left serif headline and compact actions. Fill the lower-right with an original silhouette related to the product, built from horizontal indigo strokes. The shape matters: plain full-frame stripes will not convey cargo, architecture or a technical object. A halftone scene may sit behind a presentation panel, but a working page normally uses the white plane directly to avoid ornamental outer framing.

## Components and texture implementation

Use `SiteHeader`, `MarketingHero align="split"`, `ActionLink`, `SectionHeading`, `MetricCard` for genuinely supported service facts, `AmbientBackdrop kind="pixels"|"scanlines"`, and `Surface depth="flat"`. The generic scanlines backdrop is a texture approximation; for subject-shaped art, supply an original SVG in the hero art slot.

Pixels are a fixed grid of translucent squares over a large cyan gradient, with a white top fade. Choose a deterministic opacity pattern, not random styles during server rendering. A mask can shape the bottom edge into a broad basin. Scanline silhouettes use a vector outline or mask plus repeating horizontal strokes; a simple static SVG pattern is sufficient and resolution independent. Avoid hundreds of animated DOM cells. Very subtle fixed grain can soften the pixel field; the source image does not show animated noise.

## Complete page and task flow

Sequence: specific service/product promise → evidence of actual work/product → scoped deliverables/features → process/limits → real pricing or contact route → final action. Service facts such as turnaround or unlimited requests require clear definitions; omit them when unsupported. A portfolio/project card shows real artifact, responsibility and date. A technical page shows one understandable workflow, not decorative logistics claims.

A contact path includes labeled form fields, send status, failure recovery and what the user should expect after sending. A pricing page exposes scope and constraints before booking. Fact cards are not clickable unless they have a destination and clear affordance. Nav links resolve to actual sections/routes; no dead menu items.

## Responsive and motion

Below 900 px lower excessive blank space and bring facts beneath the main copy. Below 640 px choose copy → action → art → facts order; art height 220–320 px with an independent clip. If using a subject silhouette, preserve recognizable contours through a simpler crop; do not shrink it until lines flicker. Keep responsive text outside the masked region.

Use a short content reveal only. Pixel/scanline art is static; no flickering scan, VHS distortion, continuous shimmer, cursor tracking or moving halftone. Hover on a real work link can lift its preview ≤2 px. Reduced motion leaves texture and copy fully visible.

## Acceptance and exclusions

Accept: one graphic mode, strong monochrome hierarchy, meaningful original silhouette or cyan basin, controlled asymmetry and real service detail. Reject: both texture modes on one hero, random pixel confetti, cloned creator marks, huge dead whitespace on a phone or tiny techno navigation. The page should retain its structure when the art is temporarily disabled.
