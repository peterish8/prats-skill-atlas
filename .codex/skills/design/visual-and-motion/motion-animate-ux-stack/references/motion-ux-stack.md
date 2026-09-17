# Motion, animation and UX technology stack

Verified from the source `package.json`, `package-lock.json` and implementation on 2026-09-17, baseline `390fc6ff1c168e5b14229207c557974ad3f094a1`. Versions below are locked checkout versions; deployed bundle parity was not established. Native browser APIs have no npm package version here.

## Verified reference implementation foundation

| Technology | Locked version | Role |
| --- | --- | --- |
| Next.js App Router | 16.3.5 | Application shell, route rendering and client component boundaries |
| React / React DOM | 19.2.8 | State, refs, component identity and lifecycle ownership |
| TypeScript | 5.9.3 | Typed scene, pose, timing, object and interaction contracts |
| Tailwind CSS | 4.3.3 | Styling/build layer alongside extensive handwritten CSS; not the animation engine |
| Motion for React, npm package `motion` | 13.4.0 | State animation, presence, springs and gesture-linked values; manifest range is `^13.4.0` |

The actual import is `motion/react`. Some older project prose calls this Framer Motion; this checkout depends on `motion`, not a separately declared `framer-motion` package.

## Motion and UX responsibilities across the stack

| Layer | What the website uses it for | Source |
| --- | --- | --- |
| Motion for React | `AnimatePresence` entry/exit ownership; `m` components; spring/object pose changes; `useMotionValue` and `useTransform` for the arced pattern wheel; imperative `animate` where needed | `experience.tsx`, `tiles.tsx`, `badge.tsx`, `glow-tile.tsx` |
| CSS animations, transitions and CSS 3D | Word/shape entrances, ambient bob/sway/shine, light pulses and finale layers; perspective and `preserve-3d` for cubies; masks; registered custom properties for selected stage geometry/fades | `src/app/globals.css`, `scenery/cube-3d.tsx` |
| Native Web Animations API | `Element.animate()` keyframe sequences for causal particles, fixed reveal/burst work and field feedback; cancellable animation handles and shared per-segment easing | `fly-burst.tsx`, `tiles.tsx`, `liquid-progress.tsx`, `survey-docks.tsx` |
| Native SVG | Perspective lanes, Pyraminx/vector scenery, isometric pattern thumbnails, ornaments and icons; motion comes from the surrounding CSS/Motion/keyframes rather than an SVG-only animation package | `glow-tile.tsx`, `pyraminx.tsx`, `badge.tsx` |
| Custom JavaScript with `requestAnimationFrame` | True cube layer turns, rotation matrices, logical cubie commits and dynamic sticker/face shading; distinct from a simple whole-object spin | `scenery/cube-3d.tsx` |

The cube is a CSS 3D DOM object with a custom logical model and frame updates. Its material/geometry is not a canvas-rendered cube. HTML Canvas 2D is used separately in `lib/badge-image.ts` to render a static 1080×1350 PNG, not to drive the live cube animation.

## Motion configuration and shared contract

- `LazyMotion features={domAnimation} strict` and `m` components configure the current Motion feature bundle in `experience.tsx`. This is implementation evidence, not a measured bundle-size guarantee.
- `MotionConfig reducedMotion="user"` and `useReducedMotion()` supply Motion-side preference handling; CSS also has `prefers-reduced-motion`. Custom frame work and browser animations require their own alternatives/cleanup.
- `src/lib/motion.ts` supplies easing arrays, spring roles, CSS easing conversion, per-keyframe segment easing, entry delays and named sequence offsets. Some durations remain local; the presence of a token file does not prove every component uses centralized timing.
- Pointer events and derived motion values drive the picker. `ResizeObserver` measures relevant content/container dimensions, including the algorithm ticker. Fonts come through `next/font`; `document.fonts.ready` is used in readiness/output paths.

## Choosing a stack for another product

Choose by behavior, not branding. A static planning brief needs no installed animation engine. A small interactive site may need CSS and native keyframes alone. A React app with shared-element scenes and gesture settling may benefit from its existing declarative motion engine. Add custom model-driven rendering only when the object or explanation requires it. Do not present these exact versions as mandatory for a new project.

## How to transfer the architecture

Keep the target's existing engine when it can express the motion contract. Divide work by behavior: reusable CSS states, controlled fixed keyframes, declarative scene/gesture transitions and model-driven transforms. Use a shared coordinate/timing language and single property ownership across those layers. Adding every technology from this source is unnecessary for a small transition or a planning-only request.

Profile the actual overlap on the target device. Browser-native animation, CSS 3D, SVG and transform/opacity are tools, not automatic evidence of smooth playback. Convex owns survey persistence; it is outside the motion rendering stack.
