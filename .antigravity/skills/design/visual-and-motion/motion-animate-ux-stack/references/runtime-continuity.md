# Runtime continuity, ownership and interruption

## Property ownership

Create a motion ownership map before mixing engines. One component/engine should own a property's current value at a time. Separate wrappers are often useful:

```text
scene placement wrapper     position / shared-element geometry
  object wrapper            object pose / semantic transformation
    visual body             artwork / material / local deformation
  shadow                    grounding aligned to object pose
```

If idle sway and an active transform both write the same `transform`, compose them deliberately or pause one. Independent translate/scale/rotate properties can help, but do not assume they remove all transform-order and engine interactions.

Choose CSS transitions/keyframes for simple reusable states, Web Animations for fixed sequences needing playback/cancel handles, the current state/gesture engine for springs and shared elements, SVG for paths/masks, and custom frame work for a real physical/model requirement. Verify syntax against the installed version. Avoid adding a heavy renderer for an effect already expressible in the current stack.

## Continuity contracts

- Pose continuity: no visible position/scale/orientation jump on retargeting.
- Velocity continuity: a spring or gesture can carry current velocity where supported and appropriate. A tween restarted from the current pose can still have a velocity discontinuity.
- Identity continuity: stable object/content ID, focal crop and material. A shared key alone does not guarantee a convincing shared object.
- Semantic continuity: restored, completed and pending states retain their meaning even when visual travel is skipped.

For a FLIP-style layout transition: capture the old bounds, commit the final layout, capture new bounds, apply the inverse translate/scale from old to new, and animate that inverse back to identity. Measure in a consistent coordinate system and choose transform origin intentionally. Keep text/inner artwork from unwanted scale distortion. Handle zero-size/removed items with a defined fallback. Scale/rotation/scrolling ancestors and interrupted measurements can make naive viewport-bound calculations insufficient.

For shape morphing, compatible point topology and correspondence matter. An incompatible shape should use masking/occlusion/crossfade or a different authored transition. Do not morph numeric values blindly and call it continuity.

## Operation policy

| Operation kind | Useful policy | Caution |
| --- | --- | --- |
| Cosmetic selection/hover transition | Replace or retarget to the latest state | Keep the selected semantic state correct |
| Gesture-followed object | Follow current input; settle on release/cancel | Avoid a lagging tween and stale release velocity |
| Ordered physical transformation | Queue only what must preserve the model, or reconcile to a known final pose | Dropping an intermediate move can corrupt logical state |
| Navigation/Back | Cancel stale delayed navigation; resolve to requested scene | A previous callback must not advance the new scene |
| External write | Operation state owns success, not animation completion | Visual replay or cancellation must not duplicate/cancel a server write implicitly |

Set a bounded backlog policy. Accelerating an unbounded queue can still leave the display far behind the chosen item. Reconcile state deliberately when collapsing work; do not assume skipping rotation also applies its logical transformation.

## Cancellation example: presentation only

This dependency-free browser example manages a replaceable presentation transition. It does not own a backend operation. The caller owns stable visible start/final values and loading markers; it must not hide essential content solely because an animation object exists.

```js
function createTransitionOwner(element) {
  let generation = 0;
  let active = null;

  return {
    async play(keyframes, options, onComplete) {
      const mine = ++generation;
      const previous = active;
      active = null;
      previous?.cancel();
      const animation = element.animate(keyframes, options);
      active = animation;
      try {
        await animation.finished;
        if (mine !== generation || active !== animation) return false;
        // Commit final caller-owned styles/classes before dropping the effect.
        onComplete();
        if (mine === generation && active === animation) active = null;
        animation.cancel();
        return true;
      } catch (error) {
        if (error?.name === "AbortError") return false;
        if (mine === generation && active === animation) active = null;
        animation.cancel();
        throw error;
      }
    },
    cancel() {
      ++generation;
      const previous = active;
      active = null;
      previous?.cancel();
    },
  };
}
```

Cancellation prevents stale completion, but this helper alone does not guarantee pose continuity. Before replacement, sample the current visible values and use them as the new start frame, or use an engine with current-pose retargeting. The old effect is cancelled only after those values are captured. Do not indiscriminately cancel every animation on the element; other owners may exist.

`Animation.cancel()` can reject a pending `finished` promise; handle that path rather than allowing an unhandled rejection. In custom rendering, retain frame IDs, timer IDs and an ownership/generation token. On unmount, navigation or preference changes, cancel owned work and ensure pending waiters have a defined resolution. An `alive` guard prevents stale updates but does not itself cancel a scheduled frame.

## Reduced motion, pause, skip and replay

Use a static pose contract plus engine-specific alternatives. Reduced motion should remove unnecessary travel, rotation, parallax, spring overshoot, particle flights and prolonged stagger while retaining the user's progress and result. A brief fade is a choice, not a universally safe substitute for every person or scene.

Pause is separate from reduced motion: freeze applicable ambient work and keep task interaction available. Hidden-tab handling is separate again; choose whether to resume, finish at the correct pose or restart an optional ambient loop. Avoid an accumulated catch-up burst when a tab becomes visible.

Skip commits the intended presentation endpoint and cancels obsolete tasks. Replay restarts only the visual sequence with its appropriate initial presentation pose. Neither should reset answers, payment state or server persistence unless the product explicitly defines that action.

Keep text as one accessible phrase. Mark decorative clones/layers hidden from assistive technology; during presence overlap make departing interactive content inert/unavailable and move focus to the useful arrival at its defined readiness point. Do not announce every animation frame or letter.

## Rendering and review

Prefer transform/opacity for frequent updates. They can still produce expensive compositing or excessive layers; large transformed scenes are not automatically free. Layout dimensions, masks, filter/shadow changes, large gradients and custom lighting need profiling on the actual scene. Use `will-change` selectively rather than promoting every layer indefinitely.

Inspect the busiest overlap, not just an idle loop. At 60Hz a frame period is about 16.7ms; that is not a full JavaScript allowance because rendering and other work share it, and other displays differ. Measure input readiness, missed frames and long tasks in the target environment. Simplify decorative layers first. Distinguish source review, browser profiling and real-device evidence.
