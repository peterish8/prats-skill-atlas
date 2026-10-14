# Meadow light

Primary reference: [22](../references/22-pampam-meadow-map-hero.png). Reference [26](../references/26-sequence-collect-airy-hero-small.png) confirms airy centered typography but is only 235×147. Use `Theme direction="meadow"`; `AmbientBackdrop kind="meadow"` approximates botanical light without copying the source photograph.

## Visual contract

An organic green light field dissolves into a clean white task plane. A restrained serif headline and a small central creation invitation are the focus. Preserve this narrower, gentler composition; do not enlarge the input into a dashboard or fill the white lower half with a wall of cards.

| Setting | Rebuild estimate / target |
|---|---|
| Canvas / ink | White/soft warm white; near-black `#1b211b` or kit text |
| Functional accent | Dark moss `#273e2c`; art sage `#b5d38f`, pale cream and icy blue |
| Headline | Desktop 56–80 px, mobile 38–50 px serif; regular; 1.02–1.1 line-height |
| Text width | Hero headline 9–13 characters per line; explanation 38–50 characters |
| Hero height | Approximately 640–760 px at full desktop; never force tall height on short screens |
| Atmosphere | Upper 45–60%; white fade complete by primary task/result area |
| Navigation | Plain corner brand / few links / compact sign-in, 64–80 px high |
| Task row | 420–560 px width, 52–60 px height; solid white field with 1 px edge |
| Alternate routes | Three equal small tiles, 12–16 px gap, 10–14 px radius |
| Depth | Almost flat; task field receives faint contact shadow only |

## Composition anatomy

Navigation stays sparse at the top. Place the headline on the central axis with substantial whitespace above, a two-line maximum explanation below, a concrete creation input/action and a tidy alternate import row. Put a real proof or discovery section below with enough space to separate it from the initial task. The screenshot's title uses a dramatic line break; reproduce the scale through width and font metrics rather than forcing identical copy breaks.

The backdrop is a large decorative plane, not a blurred image behind the input. Its strongest sage light sits toward the upper-left/right edges, with cream at the center and cool light toward the lower perimeter. The input remains solid. If an approved botanical asset is available, crop it loosely and fade it into white; otherwise use the library approximation. Do not lift the exact source site background as an output asset.

## Components and texture recipe

Use `SiteHeader`, `MarketingHero align="center"`, `AmbientBackdrop`, `Field`, `Button` for creation and `ActionLink` for navigation/import routes. The kit does not supply a magic prompt box or import handlers: compose a real form. A field label can be visually compact but must remain explicit; placeholder text is an example, not its label. Imported tiles can be simple anchors or buttons with original small icons.

A custom organic field uses three broad radial color layers plus an opaque white fade on the bottom. Add subtle diagonal translucent leaf-like ellipses only in the top layer if required; keep them outside the content column. No grain is necessary. A tiny serif/italic proof introducer works only when actual proof follows, not invented logos.

## Complete task UX

Sequence: visitor understands one thing they can create → enters a real input or selects import → sees validating/loading state → receives first useful result → can edit, save or recover. Pending action retains the input and changes text to the actual stage; do not just spin indefinitely. An invalid input shows a specific correction beside the field. Import choices disclose accepted formats and failures. Empty initial state gives one concrete example; successful state moves to the product outcome rather than leaving the user in a beautiful hero.

## Responsive and motion

At 640 px the central column uses the full available width within 20–24 px gutters. Task action may stack below the field; import routes use three compact tiles or a vertical list if labels are long. Header links become an explicit disclosure. At shorter desktop heights, reduce top whitespace rather than clipping the action.

Default atmosphere is static. Optional drift moves the large light plane ≤4 px over 20–24 seconds with no flicker; it cannot animate the text. Reveal below-the-fold proof once; the primary input is visible immediately. Reduced motion removes all drift/reveal translation. Never use scroll hijacking or a cursor trail.

## Acceptance and exclusions

Accept: calm upper light, a clear central task, serif/sans contrast, quiet white space and usable alternate entry routes. Reject: extra dashboard metrics, a large neon blob, input over textured foliage, many competing CTA buttons, logos masquerading as proof or precise claims about image26's unreadable microdetail.
