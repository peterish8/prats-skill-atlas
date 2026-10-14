# Motion and texture: a coherent physical scene

The attached images establish static materials and composition. All timings and choreography in this guide are authored implementation recommendations. Cinematic craft comes from a complete static frame, a grounded persistent object and one action that changes it; it does not mean adding a loop to every card.

## Scene contract

Before code, write: “The user does [task]. The persistent [product artifact] changes by [meaningful transformation]. [Light/material] supports it. [Control] confirms activation. The journey ends with [real outcome].” For a map maker the object can be a route, for a file tool a folder tray, for a learning tool a progress artifact. If an object does not clarify the task, use continuity of the content itself.

Compose five layers: quiet substrate → static light/perspective → grounded object → readable content/stable controls → temporary feedback. Match the chosen reference's silhouette, occupied/empty ratio, type width and art placement before tuning shadows. Prefer a specific original product fragment over a generic gradient orb when the reference demonstrates real UI.

## Timing and physical feedback

| Lane | Starting setting | State obligation |
|---|---|---|
| Logical acceptance | Immediate native activation | Record choice or start operation before decorative effects |
| Raised control press | 110 ms, about 2 px down; bottom edge/contact shadow reduces | Keep hit area/layout footprint stable |
| Hover | 150–180 ms, ≤1–2 px lift; only `(hover:hover)` and fine pointer | No hover-only information |
| Panel exit | 140–180 ms, ≤8–12 px away from its origin | Do not remove meaningful content before replacement is available |
| Panel arrival | 220–340 ms, ≤12–14 px, easing `cubic-bezier(.22,1,.36,1)` | Next input available independently of art completion |
| One-shot section reveal | Kit 560 ms; 70 ms stagger, maximum 280 ms | Above-fold content visible immediately |
| Ambient field | Static default; optional 18–24 s drift, ≤4–6 px | Pause control and system-motion handling |
| Success artifact | Optional one-shot 600–1200 ms settle/halo | Success text and next action available throughout |

`@tactile-ui/tokens` exports `motion` timings. The host owns actual task state, request cancellation and navigation. Do not concatenate a press, exit, arrival and showcase into a forced multi-second wait. Inspect activation-to-next-input readiness; durations alone are not performance evidence.

## Raised buttons and recessed fields

Raised buttons need a fine boundary, restrained top highlight, small bottom edge and short contact shadow. Pointer-down may press the face; click/native keyboard activation commits the action. Clear pressed appearance on pointer-up, leave, cancel and unmount. The input stays still on focus: strengthen its rim/focus outline instead of lifting the field. A loading action keeps its text footprint and exposes appropriate busy/disabled state.

Use library `Button`, `ActionLink`, `Field`, `TaskComposer`, `Switch`, `SegmentedControl` and `Tabs` for routine interactive controls. Navigation is an anchor; an operation is a button; a radio group is a mutually exclusive choice. Do not introduce plain unstyled buttons into an otherwise finished page, or restyle each component with unrelated physics. Selected state remains distinct without motion through outline, fill, visible label/check and native accessibility state.

## Choreograph one action

1. Validate and record logical input; reject a rapid duplicate with an operation identity or synchronous lock where needed.
2. Confirm at the initiating control through press/selected/pending text.
3. Change the same persistent object's pose/content to reflect state. Keep its instance stable where continuity matters.
4. Reveal the next relevant content while the object settles independently.
5. On Back/edit/cancel, cancel abandoned callbacks and restore a pose derived from current logical state. Do not replay completed construction milestones or repeat a backend write.

Visual success follows an actual successful operation. Animation completion is not the success signal. Visual replay never resubmits a form. Prefer existing CSS/native transitions for a small page; add an engine only when its state-continuity responsibility justifies it. Do not update framework app state every pointer frame merely for decoration.

## Normal, paused and reduced behavior are different

`MotionStage` scopes physical staging. Its `paused` control pauses ambient work while purposeful task feedback remains available. An OS reduced-motion preference removes travel, spin, overshoot and optional particles. Content, selection, progress and final logical state remain present. `AmbientBackdrop animated` is opt-in; static is its default. `Reveal` renders visible server HTML, only hides eligible below-viewport content after mount, reveals on keyboard focus and respects reduced motion. A blank first paint with `opacity:0` on all content is unacceptable.

A CSS or animation-library preference does not automatically stop custom frame loops, timers, Web Animations or haptics. Inventory every engine and clean it up on unmount/abandonment. Ambient loops should also stop work when the document is hidden. A pause preference can be held in local product state; do not silently add account persistence.

The OS preference communicates a wish to minimize nonessential animation; large scaling/panning can trigger discomfort. [MDN reduced-motion guidance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) supports this preference handling. Interaction-triggered nonessential motion should be disableable; WAI also distinguishes automatic motion from user-initiated motion. [WAI interaction animation guidance](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html). These are implementation principles, not a claim of full kit or consuming-site compliance.

## Texture construction recipes

### Porcelain relief

White/pale face + 1 px top rim + short contact shadow + broad ambient shadow. Starting stack: `inset 0 1px 0 #fff, 0 2px 3px #19233207, 0 14px 30px -20px #19233245`. Recessed tray: slightly darker fill plus `inset 1px 2px 4px #1923320c`. These cues share a light direction. White glow alone washes out the boundary.

### Spectral atmosphere

Two broad radial fields at opposing corners over a pale linear base. Keep brightest areas outside the copy column. Fade to solid white copy. Optional grain is fixed SVG turbulence at low opacity inside art. Do not animate noise or apply `backdrop-filter` to all cards; retain a solid fallback.

### Meadow light

Broad sage/cream/icy-blue pools near the upper perimeter; opaque white fade over the lower 45%. Optional translucent leaf-like curves remain clipped and decorative. The input has opaque white fill and a visible border. A generic green glow directly behind the title misses reference 22's organic edge framing.

### Equilibrium rule canopy

Deterministic vertical strokes with varied lengths; production spacing about 24–44 px and stroke 1 px, under a lime-to-white fade. One SVG or CSS pattern suffices. Match reference 23's long descent and lower centered title; do not substitute random dots.

### Infrastructure paths

Original SVG routes use 1 px mint strokes, right-angle turns softened by small radii and sparse nodes. Leave a copy safe zone. Meaningful nodes also have readable names/statuses. An animated route is appropriate only for an actual current process.

### Refracted ribs

Broad blue/cyan base with a diagonal cream light region; overlay repeating vertical shadow/highlight pairs. Each rib is a fine material edge, not a separate blurred DOM strip. Keep static or move a single parent layer modestly. The cream sheet below is opaque and receives no refraction overlay.

### Pixel basin

Cyan gradient under a deterministic grid of translucent squares, stronger toward the bottom; white fade removes the top edge behind text. Fixed coordinate/opacity data avoids SSR mismatch. No flicker, random rerender or thousands of tile nodes. SVG/pseudo-elements can represent the field efficiently.

### Subject-shaped scanlines

An original recognizable silhouette is used as an SVG mask or clip. Repeating horizontal 1.5–2 px indigo strokes spaced 4–7 px supply texture. A full rectangle of stripes is only the generic backdrop: supply subject-specific art when fidelity requires it. Keep static to avoid moiré/shimmer.

### Green frosted glyph

Reference 31 transfers as: green rear rounded plate rotated about −12° → upright translucent pale front → simple pale line/bar glyph → white edges → diffuse contact/ground shadow. `FrostedIcon` supplies an original SVG abstraction. Its bars are decoration, not a metric. Do not blur its adjacent label.

### Landscape product stage

Approved imagery or original abstract hill/sky fills the stage. A focused crisp white product fragment sits above with a thin rim and coherent shadow. Landscape stays behind the artifact. `ShowcaseCard` supplies tonal stages; `DeviceFrame` stages original product content. Neither replaces the host's interaction.

## Runtime cost and verification

Prefer transform/opacity for frequent motion, but do not claim smoothness or compositor-only execution from names. Blur, gradients, SVG filters and large layers still cost paint. Keep layer count small, avoid permanent `will-change` everywhere and profile the actual overlap of mounting/input/motion when required. Inspect mobile 390×844, smaller/shorter viewport, desktop, rapid clicks, pointer cancellation, keyboard focus, Back/edit, loading/failure/success, ambient pause and reduced motion. A desktop resize does not prove keyboard-open device behavior.

Sources: supplied captures and the invoked cinematic-ui-motion skill's physical-control/state-continuity recipes. Recommendations were adapted to the light/pastel directions; no Polaris palette, cube or brand is required.

