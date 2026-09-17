# Implementation recipes

Adapt these contracts to the target framework; pseudocode is intentionally not a drop-in library API.

## A. Record first, animate independently

```text
onActivate(choice, origin):
  if activation is duplicate or belongs to an obsolete scene: return
  previous = current answer
  record answer(choice)                 # synchronous local acceptance
  mark transition owned by current scene
  render selected state                # also works with animation disabled
  if choice changed and normal motion: emit bounded feedback(origin, hero)
  if milestone not played: record milestone; request hero transform
  request next content after short confirmation

onNextContentReady():
  enable current controls
  focus current heading or task control according to journey

onBackOrSceneAbandoned():
  cancel pending navigation callbacks
  clear locks and stale pressed state
  preserve answers and completed milestone ledger
```

Use a synchronous lock/ref or an equivalent event gate as well as visual disabled state; render updates alone may not prevent rapid duplicate activation. Associate scheduled callbacks with a scene identity. Use transition-completion events or current readiness when feasible; a fixed guard alone can drift from the actual entrance.

Reduced motion shortens decorative delays too. Re-selecting the same answer can proceed without another burst. Editing should return to its origin and update the existing visual representation rather than adding construction steps again.

## B. Separate the motion budget

| Lane | Purpose | Budget decision |
| --- | --- | --- |
| Logical acceptance | Store the intended local choice | Immediate; never after a spring |
| Tactile confirmation | Make activation visible | Short press and one settle |
| Scene replacement | Orient the user | Overlapped with feedback; faster for repeated tasks |
| Persistent-object change | Show meaningful construction | Can finish beyond scene replacement |
| Ambient motion | Establish atmosphere | Quiet, pausable and independent of task readiness |
| Success spectacle | Mark a real result | Optional, once; never gates access to result |

Measure activation-to-next-input readiness rather than summing all animation durations. An “instant recorded answer” can coexist with an unnecessarily slow UI; inspect both.

## C. Choose an engine by responsibility

| Work | Usually appropriate | Avoid |
| --- | --- | --- |
| Fixed word/card entrance | CSS keyframes, existing utility classes | Per-frame app-state updates |
| Seeded particles | Web Animations or existing animation engine | New random field every render |
| Presence and shared object pose | Current declarative animation engine | Remounting persistent artwork on each step |
| Pointer following | One motion value or direct render value | React/setState on every pointer movement |
| Physical state model and lighting | Carefully scoped custom frame loop | Repainting unrelated page state |
| Simple product with a few transitions | CSS and native events | Adding a large stack to animate two buttons |

CSS and Web Animations can allow compositor execution for suitable properties. Engine choice alone does not guarantee it. Profile paint/layout, long tasks and input under the actual overlap of mounting and motion. Use temporary layer hints sparingly.

## D. Product object continuity

Keep logical state independent of animated pose. Interpolate from the current rendered pose toward the newest target. If an operation must queue, preserve order and bound stale visual backlog; do not show a completed selector with the hero indefinitely catching up.

For physical simulations like the source cube, commit state only at a mathematically matching turn boundary. For simple progress artwork, derive the final appearance directly from current task state. On reload or reduced motion, render that final appearance immediately.

Animation completion must never be the database success signal. Visual replay must never invoke the write again.

## E. Arced picker with bounded momentum

Reference mapping, where `o = itemIndex − fractionalCenter`:

```text
x       = o * 116px
y       = min(o², 4) * 16px − 6px * max(0, 1 − |o|)
rotate  = clamp(o, −2, 2) * 6deg
rotateY = clamp(o, −2, 2) * −12deg
scale   = 1.04 − min(|o|, 2) * .14
opacity = clamp(2.6 − |o|, 0, 1)
z       = 100 − round(|o| * 10)
```

Keep near cards opaque; darken side cards with a separate overlay instead of making the product look ghosted. These values belong to a compact optional picker and should be retuned for different card sizes.

Follow horizontal drag at 1:1 distance. The source activates drag after about 6px horizontal movement, uses .3 edge resistance, estimates velocity from a few recent samples and limits carry to two cards. In a new implementation, also distinguish horizontal intent from vertical movement and release pointer capture cleanly.

On pointer cancel, settle to the nearest valid item without treating the interrupted gesture as a fresh flick. Suppress the trailing click after a drag so it cannot choose a different card. Arrow buttons, arrow keys and current-selection semantics provide the same task without a gesture. Reduce physical travel in reduced-motion mode.

## F. Reveals and reading

Mask each visual word with overflow hidden; animate its child from roughly 110% below the baseline. Keep the complete phrase accessible once, and mark the segmented decorative spans hidden from assistive technology. Remove leftover transforms after a one-shot entrance so later layouts are not trapped in unexpected stacking contexts.

A tap-to-reveal shortcut is useful, but provide a keyboard-operable equivalent when a meaningful amount of content is withheld. Do not make text appear in a way that prevents selection, copying or reading at the user's own pace. Long paragraphs generally need less segmentation.

## G. Loading, success and useful artifacts

Use a static initial visual contract before fonts/assets arrive. A bounded wait or fallback prevents a loading animation from withholding the whole app. Optional opening sequences play once and remain skippable.

For exported artwork, build from the same logical data and palette as the preview. Inspect the actual PNG/PDF, including long names, longest labels and low-size viewing. A CSS 3D object may need a separate deterministic renderer, as Polaris does for its 1080×1350 canvas PNG. Do not assume screenshotting the DOM preserves the intended lighting.

Precompute a shareable file when possible. Call native share from direct user activation; slow awaited rendering can lose that activation, especially on Safari. Keep visible Save and copy-link alternatives, treat share cancellation as neutral, and describe where the download lands when useful. A platform may reject a combined file/text/URL payload: test real targets rather than claiming a universal share shape.

## H. Motion alternatives and teardown

Maintain an inventory of CSS loops, Web Animations, library transitions, requestAnimationFrame, timer-driven algorithms and haptics. For each, define normal, pause, reduced-motion and unmount behavior. Cancel animations and frame/timer work on abandonment. If a visual state must survive interruption, restore its logical final pose.

An ambient pause is different from reduced motion. Pause should freeze loops without disabling the person's intentional actions; reduced motion should remove physical travel even for user-triggered transitions. Persist a pause preference only if appropriate to the product's existing settings model.

## Technical sources

These support implementation guidance, not claims that motion increases retention:

- Prefer transform and opacity and inspect rendering cost: [web.dev animation guide](https://web.dev/articles/animations-guide).
- `MotionConfig` respects system preferences for supported Motion animations; custom behavior needs explicit handling: [Motion accessibility guide](https://motion.dev/docs/react-accessibility).
- Provide control for qualifying moving/auto-updating content: [W3C Pause, Stop, Hide guidance](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html).
