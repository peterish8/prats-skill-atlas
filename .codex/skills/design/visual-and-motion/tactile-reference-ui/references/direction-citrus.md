# Citrus playground

Primary references: [14](../assets/design-kit/references/14-citrus-playful-widget-bento.png), [29](../assets/design-kit/references/29-lime-blockchain-orbit-bento.png), [30](../assets/design-kit/references/30-neopay-lime-device-stage.png), [31](../assets/design-kit/references/31-green-frosted-icon-process.png). Reference 18 contributes a pale iridescent curved detail. Use `Theme direction="citrus"`.

## Visual contract

Generous rounded geometry, bright lime/yellow gel and crisp dark type live inside a mostly white chassis. The newer references extend a widget language into a full page: orbital art, a device/product stage and a construction method for green frosted icons. Decorative lime is not a success status.

| Setting | Rebuild estimate / target |
|---|---|
| Canvas / surfaces | `#efefeb` / white; ink near `#17371e` or `#202327` |
| Functional accent | Dark green `#29632c`; bright art lime `#b1ff88` and yellow `#f4ed77` |
| Radius | 36 px card; 18 px control; outer chassis 40–56 px; orbital discs circular |
| Hero type | 44–68 px sans, regular/500, −.04 em; widget numeric text 32–48 px |
| Outer frame | 1 px white edge + faint gray line; broad soft ground shadow |
| Gel button | Lime/yellow gradient, pale rim, dark text, contact shadow ≤4 px |
| Orbital art | 3–4 large offset discs; brightest at top-left; 15–25% clipping at frame edge |
| Frosted icon | Rear plate rotated about −12°; front upright; ≥20% translucent white at lower edge |
| Bento gap | 20–28 px; genuine controls remain at least 44 px high |

## Three complete compositions

**Widget desk:** a wide utility capsule at the top, two equal central cards, then a small square action beside a wide note. Give different spans according to function. Use one large number and one instruction per widget. Keep neon material to the key affordance and one object.

**Orbital launch:** plain top navigation, broad rounded hero containing art at upper-right and copy at lower-left, then three aligned summary cells. Hold the text clear of the disc diagonal. A registration/status pill sits just above the heading. Summary cells have a tiny category label, a grounded fact and consistent icon/avatar scale. Use genuine figures or transparent demonstration labels.

**Product stage:** centered dark pill navigation, medium centered heading, two actions, broad desktop artifact cropped at its illustration frame and smaller mobile artifact in front. The white upper field dissolves into lime behind the product. Reproduce the relationship using actual product UI, not a screenshot of the entire reference including outer ghost lettering.

## Components and texture

Use `Surface`, `MarketingHero`, `ActionLink`, `MetricCard`, `FeatureCard`, `FrostedIcon` and `Orb`. `FrostedIcon` is an original decorative SVG abstraction of reference 31; it is not a chart. Its three bars do not encode real data. For custom icon families, use the same two-layer construction and a simple glyph: colored rear plate, translucent front plane, 1 px white rim, shallow highlight and diffuse ground shadow. Keep three coherent icons rather than mixing unrelated 3D render styles.

The circular lime objects in 29 can be an original SVG made from ellipses and clipped pale line glyphs. Use a fixed art layout with no random DOM-position generation; deterministic coordinates support SSR. The library supplies material primitives, not branded coins or device mockups.

## UX, responsive and motion

A friendly product page should make the first action obvious: hero invitation → real product example → features → setup/limits → final action. A booking widget needs a real duration choice, available times, pending state and a successful reservation detail. A file card needs a specific open/create action and a recoverable empty state. A mobile/desktop preview must be labeled as illustrative when it is not an interactive app.

Below 900 px let orbital art occupy a separate upper or lower zone; below 640 px stack copy first, art second and summary cells vertically. Device preview uses one readable screen instead of two overlapping tiny screens. Widgets reflow to one column while preserving function order. Do not scale entire mini UI to make it fit.

If requested, let decorative discs drift a maximum 4–6 px over 18–24 seconds; default static. Controls press ≤1 px over 110 ms, hover ≤1 px over 180 ms. Do not bounce every card or rotate the device with pointer position. Reduced motion disables drift and positional transitions. All controls still have visible state text.

## Acceptance and exclusions

Accept: white chassis, strong dark text, one coherent lime gel family, bounded original objects and specific tasks. Reject: fluorescent full-page copy backgrounds, lime used as automatic approval, excessive pill controls, copied wallet/user-count claims, financial balances invented for aesthetic reasons or instructions copied from the tutorial image. The photographed/editor framing is excluded from the live layout.

