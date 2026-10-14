# Mint infrastructure

Primary reference: [24](../assets/design-kit/references/24-sydecar-mint-infrastructure-heroes.png), which presents two alternative heroes. Use `Theme direction="systems"` and `AmbientBackdrop kind="paths"`. The paths illustrate a system; they do not indicate actual money transfers or live connections.

## Visual contract

A readable left aligned task/proposition is set against mint light and a disciplined schematic or isometric art field. Dark green actions create a stable functional anchor. The art expresses orchestration; the copy and form remain the primary interaction.

| Setting | Rebuild estimate / target |
|---|---|
| Substrate | Warm white; optional pale mint `#e7fff0`, pink `#f9edf0`, icy blue `#e8f8fa` |
| Ink / accent | Near-black/green; primary `#093e34`, white action text |
| Hero heading | 52–72 px sans, regular/500, −.045 em; 1.04–1.12 line-height |
| Copy width | 520–680 px heading; 400–520 px explanation |
| Grid | Copy 5–6 columns; art 6–7 of twelve; generous overlap only in background |
| Path | 1 px muted mint, orthogonal rounded turns; 8–14 px corner radius |
| Diagram nodes | Small white/cream chips; restrained 1 px edge; no heavy glow |
| Form group | 440–560 px combined row, ≥52 px high; button dark green |
| Card radius | 12–20 px; schematic cluster 6–10 px; illustrated platform edges crisp |
| Spacing | 24–32 px within copy; 80–120 px section separation |

## Two hero modes

**Schematic mode:** white nav spans the top. The background paths stretch around the frame; a few small labeled clusters indicate input, coordination and output. Place copy on the lower-left or mid-left quiet region, with one bounded proof/context label above and a form below. Keep paths out of the copy block or lower their opacity enough that the paragraph stays solid.

**Isometric mode:** copy/action on the left, one original isometric platform/object on the right with a sparse grid beneath it. A mint/lime light field supports the illustration. Do not use both modes as two consecutive heroes: choose based on whether relationship or product object is the stronger story. A system explanation can appear later as a small supporting section.

## Component and art recipe

Use `SiteHeader`, `MarketingHero align="split"`, `AmbientBackdrop kind="paths"`, `Field`, `Button`, `SectionHeading`, `IntegrationMap` and `ShowcaseCard tone="mint"`. The backdrop is decorative; `IntegrationMap` supplies readable nodes when relationships matter. Its nodes are illustrative and have no authentication behavior.

An original isometric object uses three consistent faces with a common 30°-like projection: pale top, mid-tone left, dark green right. Draw white edge lines sparingly. A broad shallow ground plane has a light grid and one diffuse shadow beneath the base. Use an approved SVG/illustration if the actual product calls for it; the kit does not contain the reference's hand/coin rendering. Avoid dollar glyphs if the product has no reason to imply finance.

## Complete journey and states

Sequence: product proposition → request/create input → concrete example of orchestration → supported outputs → implementation/setup detail → FAQ/limits → final action. If the hero uses email, explain why it is requested and connect it to a real endpoint. Form success includes a human-readable next step; errors preserve the address; loading gives one clear label. A contact form cannot quietly subscribe or authorize external integrations.

A working orchestration screen adds readable input validation, stage status, partial result, cancellation and retry states. Use textual labels for connection/currentness/permission, not just mint node glows. Any statistics above the headline need real source/date/scope; omit them when unavailable.

## Responsive and motion

Below 900 px stack hero copy before art; reduce path clusters to three or four. Below 640 px form input and action stack if necessary, with labels fully visible. Schematic nodes become a named list if they carry meaning. Cropped paths can remain decorative. A mobile isometric scene becomes a smaller single object with no grid clutter.

Reveal the copy immediately, then below-fold examples once. If an active path pulse is useful, use it only for a real operation and end it when complete; otherwise static. No cursor-driven parallax over the form. Reduced motion removes all pulses and movement while leaving actual process text visible.

## Acceptance and exclusions

Accept: dark green functional controls, airy mint/pink/cool substrate, explicit system relation and one hero mode. Reject: faint copy on circuits, interchangeable generic blobs, repeated dollar icons, unsupported speed/cost facts or decorative transfer motion suggesting a live service. All key actions must work without the background art.

