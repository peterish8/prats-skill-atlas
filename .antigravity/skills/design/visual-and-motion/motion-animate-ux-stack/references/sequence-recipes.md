# Sequence recipes and reusable motion roles

These are starting compositions, not mandatory numbers or measured Polaris timings. Implement only the pattern appropriate to the task.

## Role tokens

Define separate roles for direct acknowledgement, content exit, content arrival, object transformation, explanatory reveal, ambient motion and first-time signature. A useful first tuning pass might use:

| Role | Starting duration/behavior | Why |
| --- | --- | --- |
| Direct acknowledgement | Immediate state with roughly 80–140ms visual response | Make the user's action visible without a theatrical prelude |
| Small content exit | Roughly 120–180ms | Clear space briefly while preserving direction |
| Local content arrival | Roughly 180–320ms | Decelerate into a stable readable state |
| Major spatial transformation | Roughly 300–600ms, or an appropriate spring | Let an important relationship remain trackable |
| First-time signature | A deliberately paced optional sequence | Establish identity; provide skip/immediate reveal |
| Gesture following | Pointer-driven, no time tween behind the finger | Preserve direct control |
| Ambient motion | Slow, low-amplitude and pausable where applicable | Support a scene without repeatedly stealing attention |

Tune to frequency, travel, viewport and product tone. These ranges are authored heuristics, not accessibility standards or universal performance limits. A workflow with frequent actions can reasonably be quicker or static.

## 1. Action → object response → next content

Intent: make a local action visibly contribute to the next state without creating a forced wait.

Resting poses: the selected control remains recognizable; a persistent object shows the updated state; new content settles into the same action region.

Illustrative timeline, time measured from activation:

| Track | Start | Duration | Behavior | Gate useful input? |
| --- | ---: | ---: | --- | --- |
| Logical state / selected mark | 0ms | Immediate | Record once; selection visible | Prevent duplicate operation only |
| Control settle | 0ms | 120ms | Small internal material response | No |
| Persistent object | 30ms | 300ms | Meaningful transform toward new pose | Usually no |
| Decorative causal flight, if useful | 40ms | 360ms | Origin at control, destination at object | No |
| Old content departure | 110ms | 140ms | Lift/fade using local direction | Only while unsafe/invisible |
| New content arrival | 200ms | 180ms | Overlap is intentional; old content becomes inert | Input when readable/stable |

The graphical tail can continue beyond the readiness condition. Overlap must not leave two operable answer groups or block focus behind an invisible layer. The next action must not activate before users can perceive its target.

Reduced motion: immediate selected state and updated object; static or short fade for content; no travel/burst. Back/edit: restore previous selection, suppress completed-milestone replay. Cancel/navigation: discard the scheduled advance, preserve the correct operation state.

## 2. Shared object: overview → detail

Intent: teach that the detail belongs to the item the user selected.

Storyboard: selected thumbnail → expansion anchored to that thumbnail → final detail artwork → explanatory content. Preserve aspect ratio, identity and the subject's focal crop; do not stretch a photo or glyph to match the outer panel.

Separate outer geometry from inner artwork and content reveal. Use shared-element/layout support already present, or a measured FLIP transition. New captions can appear after enough space exists, while the main content remains available. Keep a stable final layout rather than making the animation itself own the page dimensions indefinitely.

Interruption: closing mid-expansion should retarget from the current visible pose. If the original thumbnail is gone, use a defined detail-exit pose/cut rather than flying to a stale coordinate. Resize: recompute geometry or choose a short resolved transition. Reduced motion: keep selected identity and direct overview/detail navigation without the spatial zoom.

## 3. Editorial hero and motion graphics

Intent: establish an idea with a graphic, then make its meaning readable.

Storyboard: quiet stage → focal graphic construction/arrival → meaningful transformation → phrase reveal → stable useful frame. Set the graphic and words in complementary regions; the brightest light should not erase the copy.

Choose one lead event: a route joins, a geometric mark assembles or an object unfolds. Introduce supporting linework, depth or a contained light response around that event. Reveal a whole phrase or a small word group rather than staggering a paragraph indefinitely. Time the complete reveal explicitly: last item start plus its duration, not the first word's timing alone.

Controls can remain visible and usable before the signature resolves. Skip sets all layers to their intended final poses and cancels obsolete work. Replay resets only presentation. Do not hijack native scrolling merely to make the scene resemble a film. For scroll-linked motion, define readable static states and what reversed/fast scroll means; do not assume scroll progress is elapsed time.

## 4. Explanatory diagram or data transformation

Intent: show a relationship that words alone would leave ambiguous.

Identify source, path, destination and conclusion. Reveal nodes/paths in causal order, then labels where they belong. Keep previously learned objects in place while introducing the new connection. Use animation to explain construction or a comparison, not to imply invented numerical precision.

A changing value should land on the actual value; avoid long number roulette. Provide the full semantic result without requiring playback. A hypothetical comparison must stay labelled hypothetical. Pause holds the explanation at a legible frame; reduced motion shows the completed relation.

## 5. Ambient loop and milestone punctuation

Ambient loops: use restrained travel/scale, matching loop seams and low contrast. Duplicate a seamless track only when the repeated artwork is truly equivalent; keep a single semantic label and accessible content. Pause owned loop work when appropriate, including custom render loops rather than only their CSS visibility.

Milestone punctuation: after confirmed success, a contained halo, object resolution or short showcase can give closure. Avoid repeating impacts or high-contrast strobes. The primary acknowledgement and next action should remain available. Replay is a visual operation and never reissues submission/payment/export delivery.

## Timing arithmetic

For a staggered sequence with N items, initial delay d, per-item stagger s and item duration u, the final item completes at d + (N - 1) × s + u. Cap the total when the text/item count grows; change grouping or remove stagger rather than retaining a hidden multi-second input delay.

For overlapping tracks, decorative completion is the maximum of each track's start + duration. Interaction readiness is a separate explicit predicate. For a stateful ordered physical sequence, the next transform may depend on the previous logical pose; independent opacity/light layers do not inherit that serialization requirement.
