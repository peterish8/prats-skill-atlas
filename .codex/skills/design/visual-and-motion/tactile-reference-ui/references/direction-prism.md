# Refracted blue

Primary reference: [25](../assets/design-kit/references/25-kaiko-refracted-blue-editorial.png). Reference [26](../assets/design-kit/references/26-sequence-collect-airy-hero-small.png) is only a broad airy-light cue. Use `Theme direction="prism"` with `AmbientBackdrop kind="ribs"` for a decorative approximation.

## Visual contract

A saturated blue hero with fine vertical ribbing and a diagonal pale light band transitions into a spacious cream editorial plane. This direction is distinguished by full-page rhythm and material transition. It should not become a row of blue gradient cards.

| Setting | Rebuild estimate / target |
|---|---|
| Hero | Blue `#2c65ba` to cyan `#65b2c2`; pale cream diagonal band |
| Content plane | Warm cream `#fffbee` or kit surface; dark navy `#1d3d68` |
| Hero title | Desktop 72–100 px sans regular; mobile 42–56 px; 1–1.08 line-height |
| Rib spacing | 28–48 px at desktop; 1 px dark edge and 1 px light edge |
| Hero height | 620–800 px adjusted to real viewport/copy |
| Content overlap | Cream plane intrudes 64–104 px into hero; desktop gutter 20–40 px |
| Cream panel radius | 12–20 px top edge; interior sections mostly flat |
| Statement block | 32–44 px sans, width 680–800 px; small side label 12–14 px |
| Horizontal rules | 1 px pale blue-green, with ≥40 px surrounding space |
| Product focal orb | 160–240 px art; only one dominant abstract object |

## Composition anatomy

In the hero, small white corner brand/navigation leave a large central stage for a two-line promise. Blue is strong at the top; the diagonal cream/cyan band occupies the lower region. Fine ribs cross the color plane uniformly. Keep the headline on a sufficiently dark field; a bright band behind text needs an original layout adjustment or scrim.

The cream content sheet begins before the hero ends. Its first compact centered block explains the product and holds two pill actions. A horizontal rule separates a larger statement row: small identifying label left, generous editorial paragraph right. Another large section introduces the product and its core jobs around a central illustration. At mobile widths this must turn into an ordered reading flow rather than four crowded corners.

## Components and refraction recipe

Use `SiteHeader`, `MarketingHero`, `AmbientBackdrop kind="ribs"`, `SectionHeading`, `ActionLink`, `Surface depth="flat"` and one `Orb appearance="iridescent"` as a simplified focal object. Use an original illustration if detailed surface refraction is essential; a CSS orb is an approximation, not a replica of the source sphere.

Build a ribbed plane from a broad blue/cyan/cream gradient and a repeated vertical overlay with a thin shadow/highlight pair. The apparent refraction comes from slight light/dark contrast at each rib, not a costly animated blur per strip. A diagonal pale band is a separate broad gradient positioned under the ribs. Keep the decorative hero layer clipped and `pointer-events:none`. The cream sheet is opaque: do not apply glass/transparency to body copy.

## Complete narrative and UX

Sequence: supported human/product promise → specific explanation/actions → statement explaining the problem and approach → concrete product jobs → real output demonstration → research/support evidence → final action. Product jobs should name outcomes the user recognizes. A research link goes to actual material; a discovery/demo link goes to a usable flow. Medical/security/compliance claims require their own evidence and should not be copied from the reference.

A request action needs real form pending/success/error states. Long editorial sections use clear headings and anchors. Supporting proof shows provenance/date and distinguishes demonstration from shipped capability. The art is a tone choice; it cannot justify claims that a system is safe, compliant or effective.

## Responsive and motion

At 900 px reduce title toward 64 px and shorten the blue stage. Below 640 px put navigation into a disclosure, keep title 42–50 px, reduce cream overlap to 28–40 px, stack label/statement and use a single ordered column of product jobs. Focal art sits between introduction and jobs or beside one job, never squeezing all labels around it. Content sheet padding remains 24 px.

Static ribbing is the default and closest evidence-supported state. If motion is requested, one broad light band may drift ≤4 px over 20–24 seconds; no per-rib animation, shimmer or flashing. Editorial blocks reveal once with ≤12 px travel. Reduced motion shows the final static refraction and complete content. Do not pin giant hero text while scrolling through essential explanations.

## Acceptance and exclusions

Accept: a readable blue hero, precise rib texture, opaque cream plane and spacious editorial transitions. Reject: multiple glowing cards, dark body text over a translucent blue field, endless light sweeps, small crowded four-corner jobs or reproducing reference claims. Check the hero with maximum light behind the title, not only the prettiest frame.

