# Observed Polaris UI and motion patterns

Extracted on 2026-09-17 from source commit `390fc6ff1c168e5b14229207c557974ad3f094a1`. Paths below are provenance within the original app, not dependencies required to use this skill. These are implementation facts and adaptation judgments, not measured effects on engagement.

## Composition and material

| Observed implementation | Source | Transferable decision |
| --- | --- | --- |
| Near-black textured canvas; warm cream text; charcoal surfaces; gold selection/focus | `src/app/globals.css`, `:root`, `.stage-canvas` | Set a quiet tonal hierarchy before using spectacle |
| One black rounded stage, warm light from below, five perspective lanes converging near `(50,34)` | `src/components/scenery/glow-tile.tsx` | Give scenery a shared spatial origin |
| A dark radial pool behind upper text, light concentrated below | `.glow-tile-light`, `.glow-tile-shade` | Reserve the quiet region for reading |
| Scene stage changes from rounded tile to full-bleed light | `.experience-tile`, `.glow-tile`, `data-wide` | Change immersion at meaningful transitions, not each hover |
| Raised cream pill CTA, recessed keycaps, fine card border, 2px edge | `.btn-primary`, `.answer-card`, `.keycap` | Physical material cues can make simple controls feel finished |
| Glossy object faces, black plastic gaps, top/front/right lighting, contact shadow | `cube-3d.tsx`, `.sticker3d`, `pyraminx.tsx` | Coherent material makes the hero feel like an object instead of an icon |

Reference values, only when a similar warm dark system is wanted:

```text
canvas       #0a0a0a
well         #0c0c0d
surfaces     #161618 → #1f1f22 → #2c2c30
main text    #fffaeb
muted text   #a1a1a8
faint text   #8b8b92
accent       #ffcc3f
accent deep  #f99707
control/card/dock radii 12 / 16 / 32px
primary CTA radius     pill
```

Body and ordinary UI use Geist; move notation uses mono styling where appropriate; the personal badge name uses the wide Unbounded display face. “Early supporter” remains semibold gold in the ordinary application font. Transfer the hierarchy of ordinary/control/display typography, not the exact typefaces.

## Scene grammar

`experience.tsx` owns the journey; `tiles.tsx` owns scene-specific artwork.

| Phase | Visual event | Why adapt it |
| --- | --- | --- |
| Boot | Dark first paint, small breathing status glow, bounded font readiness wait | Avoid showing a half-styled performance or a dead page |
| Splash | Bottom light, spring Pyraminx entrance, letters, rule, tag; skippable and once per tab | A first-time signature can establish identity if it does not gate utility |
| Open | Large “60s” count, floating glossy Pyraminx, quiet embers, reachable CTA | One promise and one focal object |
| Who | Opening Pyraminx transforms into a smaller story pose without remounting | Continuity is more memorable than unrelated illustrations |
| Spark | Dated counts; bars temporarily illustrate the goal and swap ranks | Demonstrate a change instead of describing it with extra copy |
| Vision | A rank destination and a concrete gap | Give the comparison a clear conclusion |
| CS | A real `R U R′ U′` sequence highlights its current notation | Couple explanatory text and physical behavior |
| Questions | Same 3D cube, each step contributes a predefined move slice | Turn actions into visible cumulative construction |
| Review | Cube remains, shifts pose; readable editable summary | Lower spectacle while accuracy matters |
| Success | Finished pattern showcased, one reveal burst; thank-you controls available | Acknowledge actual success, then celebrate |
| Badge | Name, chosen pattern, live cube and arced picker | Put the result under user control |
| Finale | Learn, compete, grow, personal contribution, return to the vision | Vary the visual argument while preserving its world |
| End | Full-bleed light, rings, sticker stream and animated “Happy cubing”; pause and replay | A richer optional ending is appropriate after the required task |

The ranking illustration marks its future arrangement as “Goal.” Its synthetic destination is an illustration, not a live statistic. Do not transplant its number or aspiration as evidence about another product.

## Actual timing and physics

These values are observed in code. They are tuning references, not universal performance targets.

| Moment | Observed values | Location |
| --- | --- | --- |
| Press | 110ms; translateY 2px; hard edge disappears | CSS tokens and control states |
| Hover | 150ms, only under `(hover: hover)` | CSS |
| Ease out/in/in-out | `[.22,1,.36,1]` / `[.4,0,1,1]` / `[.65,0,.35,1]` | `src/lib/motion.ts` |
| Rise spring | stiffness 170, damping 22, mass .9 | `SPRING_RISE` |
| Settle spring token | stiffness 500, damping 32 | `SPRING_SETTLE`; token availability does not prove every control uses it |
| Spatial scene exit | .34s | `SCENE_EXIT_S`, `EXIT_DOWN` |
| Text exit | .24s, y −18 | `EXIT_UP` |
| Dock text | enter .34s, y +16; exit .16s, y −12 | `textSwap` |
| Panel | enter .26s, y +14; exit .14s, y −12 | `panelSwap` |
| Choice selection hold | 360ms before advance | `EXIT_DELAY_MS` |
| Arrival guard | 600ms after advance | `ARRIVE_MS`, `arrivingUntil` |
| Step cube turn | 300ms per move; double turns longer | `TURN_MS`, cube queue |
| Choice flight | 8 fixed bits, 500ms each, 18ms stagger | `fly-burst.tsx` |
| Question card entrance | .3s; delay `.06 + index*.04` | `Stagger`, `.enter-rise-12` |
| Story word reveal | .42s duration; .018s or .012s stagger | `ChapterDock`, `SplitWords` |
| One-shot object showcase | 1700ms | `OUTRO.SHOWCASE` |
| Pattern wheel | spacing 116px; spring 260/30/.9 | `badge.tsx` |
| Pattern cube change | inverse old sequence + new sequence, simplified; 55–140ms per move | `patterns.ts`, `choosePattern` |
| Cube ambient sway | 9s alternating; camera X −27°, Y −38° | CSS |
| Algorithm marquee | measured content groups, about 28px/s | `AlgorithmTicker` |
| Stage morph | 760ms dimensions/radius/masks; panel property 520ms | CSS |

The original motion plan suggested next-question readiness under roughly 400ms. Current code instead has a 360ms hold and a 600ms arrival guard, plus overlapping visual effects. Do not claim the plan's latency target is measured or met. A multi-move hero animation also need not finish before the next task begins.

The shiny progress implementation animates width with a spring (190/13/.8), five small edge sparkles, a shine sweep and a rolling count. Its label reports the actual question count; the fill reserves visual space for submission and reaches full after success. If adapting this, separate task progress semantics from decorative fill and never imply a saved result before confirmation.

## Persistent cube mechanics

The cube has 26 visible cubies and 156 face nodes, not a spinning bitmap. Each cubie stores integer position and orientation, and stickers stay attached to local faces. A move selects one layer, animates its transform, then commits the rotated coordinates and matrix at the boundary. The final frame and committed pose agree.

`PATTERN_BY_STEP` contributes 18 predefined moves across eight steps, ending in “cube in a cube in a cube.” `turnedSteps` prevents revisits from adding moves. The final pattern is not determined by whether the person chose an enthusiastic or neutral answer: step completion drives it. The badge picker separately chooses among eight patterns.

Generalize as:

```text
logical product state → deterministic visual state
milestone ledger     → which construction effects have played
visual queue         → ordered transformations, independent of persistence
```

For a plant, map or assembled playlist, this can be much simpler than a 3D simulation. Correct state continuity matters more than geometric complexity.

## Responsive extraction

Mobile is the base; larger layouts recompose the same experience.

- Base mobile width cap: 460px; 461–599px use available width.
- 600–899px: centered tablet composition, stage capped near 460px and panel near 520px.
- 900px+: hero left, working panel right; badge mode becomes a centered vertical stage and picker.
- Question stage yields height to the actual answer count; five choices receive more room.
- Short choice screens below 620px height allow page scrolling.
- Name/email fields move to an upper stage card on phones with a lower Continue action; the cube occupies the intervening area.
- Mobile review uses a bounded scrolling list with a visible cue and a reachable submit action.
- Safe-area padding and small/dynamic viewport units are used selectively; do not assume one viewport unit solves all keyboard behavior.

Choose a scroll owner per state. Native page scrolling serves long narrative and badge content; contained review scrolling is a specific exception. Do not copy a fixed full-height shell onto a content-heavy app.

## What not to universalize

Old planning docs prescribe a blue/navy palette, no pill controls and a light SVG hero. The current code uses gold/cream, pill CTAs and the CSS 3D cube. Current source is the evidence for this extraction.

Some dimension, mask and shading animation is deliberately expensive relative to simple transforms. Source comments describing compositor playback are an implementation intention, not a device benchmark. The global reduced-motion setting also does not cover every custom effect automatically.

No dwell-time, replay-rate, completion-rate or retention results were established during extraction. Treat “satisfying,” “curious” and “memorable” as design goals to validate with users.
