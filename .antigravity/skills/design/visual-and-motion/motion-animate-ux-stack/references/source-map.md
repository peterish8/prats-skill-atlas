# Source extraction and technical references

## Observed Polaris mechanisms

Source inspected on 2026-09-17, baseline `390fc6ff1c168e5b14229207c557974ad3f094a1`. Paths identify provenance, not dependencies required by this skill.

| Evidence | Mechanism | Design lesson |
| --- | --- | --- |
| `src/lib/motion.ts` | Ease roles; settle/rise springs; text lifts out; objects sink into light; delayed tile removal | Reuse a spatial and temporal language across different subjects |
| `components/scenery/glow-tile.tsx` | Perspective lanes meet near `(50,34)` in a normalized viewBox; quiet text region and lower light | A coherent stage origin relates graphic motion, light and object placement |
| `components/experience/experience.tsx` | Persistent hero poses; separate delayed advance/arrival guard; navigation cancels pending advance | Presentation continuity and interaction readiness are distinct contracts |
| `components/experience/fly-burst.tsx` | Eight seeded particles, control-to-object path, 500ms playback and 18ms stagger; owned Web Animations cancelled on cleanup | Make variation reproducible and causal; own each sequence's lifecycle |
| `components/scenery/cube-3d.tsx` | Logical cubie state committed per move; ordered transform queue; dynamic per-face shading | Physical continuity can require preserving a real model, not merely interpolating CSS |
| `components/experience/badge.tsx` | One fractional wheel center derives card transforms; gesture following and settle | A common motion parameter can keep a group spatially coherent |
| `src/app/globals.css` | Masked entrances, light layers, dimension changes, finale impact/reveal and reduced-motion alternatives | Reusable graphics need normal and alternative playback plus a rendering budget |

Observed source values are not universal recommendations. The choice hold is 360ms and the arrival guard 600ms; the old plan's under-400ms target is not established by those values. The eight-particle example's final staggered completion is 500 + 7 × 18 = 626ms, not 500ms for the whole group. The stage includes animated dimensions and shading, so comments describing every layer as compositor-only are not performance proof.

The earlier extraction included a public mobile journey through review/edit, a desktop opening and isolated badge PNG inspection. This extension re-read source and official guidance; it did not add a new full-motion browser recording, device performance pass, production submission or native-share test. The skill's proposed patterns and timing ranges are authored design guidance rather than measured engagement evidence.

## Primary technical references

- [Motion transition configuration](https://motion.dev/docs/react-transitions): check tween/spring controls, units and property-specific behavior against the installed version.
- [Motion shared-element and layout animation](https://motion.dev/docs/react-layout-animations): verify actual layout/shared-element support and constraints rather than inventing an API.
- [MDN Animation.cancel](https://developer.mozilla.org/en-US/docs/Web/API/Animation/cancel): cancellation lifecycle and finished-promise rejection.
- [web.dev animation performance](https://web.dev/articles/animations-guide): rendering cost and profiling guidance; no guarantee that a source snippet is smooth on every device.
- [W3C animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html): consider how nonessential triggered motion can be disabled.
- [W3C pause, stop, hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html): evaluate applicable automatically moving content and user controls.
- [W3C flash threshold guidance](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html): evaluate frequency, luminance and affected area; this skill does not certify a flash sequence from source alone.

These sources inform API, rendering and accessibility decisions. The creative principles and illustrative timelines are adapted craft guidance, not quotes from or standards prescribed by those documents.
