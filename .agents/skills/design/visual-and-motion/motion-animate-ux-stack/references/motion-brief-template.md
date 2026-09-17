# Motion brief, storyboard and review template

Use only the sections needed for the request. A focused transition can be one complete contract rather than a full-product storyboard.

## Intent and scope

- Mode: existing implementation / prototype / planning only.
- Surface, user trigger and intended meaning.
- Existing brand, navigation and useful behavior to preserve.
- Inspected source/rendered states and unresolved old-plan differences.
- Existing motion engine and actual property owners.

## Temporal storyboard

| Beat | Pose and focal subject | Meaning | Supporting graphics | Useful action available |
| --- | --- | --- | --- | --- |
| Initial | | | | |
| Acknowledgement | | | | |
| Transformation | | | | |
| Arrival | | | | |
| Settled | | | | |

Write the spatial grammar: origin/destination, coordinate space, pivot, depth, light, persistent object and entry/exit direction. State when a deliberate cut replaces a continuous transform.

## Sequence contract

| Track/property | Owner | Start/trigger | Duration or settle rule | Easing/physical model | Overlap dependency | Completion meaning |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

- Named reusable tokens with explicit units.
- Useful-input readiness predicate and budget.
- Total decorative tail and complete stagger duration.
- Current-pose retargeting or defined cut policy.
- Queue/drop/reconcile behavior for rapid changes.
- Normal, reduced, paused and skipped endpoint behavior.
- Navigation, reversal, resize, hidden-tab and teardown policy.

## Acceptance criteria

Write observable outcomes relevant to the task. Examples:

- A mid-transition reversal begins from the visible pose without teleporting.
- A departing panel cannot accept an accidental second operation during presence overlap.
- A long translated title does not extend stagger into a prolonged hidden wait.
- Resize keeps causal flights anchored to the intended elements or replaces them cleanly.
- Skip lands all layers at the correct final presentation state without replaying a backend action.
- Reduced motion communicates the same result without object travel or spin.
- The primary phrase is announced once; decorative duplicates are not focus targets.
- Ambient pause stops its owned render work while the next task remains usable.

## Review evidence

Inspect first/last/impact frames, full-speed playback and the busiest overlap. Test relevant rapid input, reversal, cancel, Back, resize, focus, preference changes and resource limits. Record source review, runtime assertions, visual playback, profiling and real-device results separately. Flash-related risk requires actual rendered-output assessment; do not certify it from a keyframe count alone.

For planning only, deliver the contract and untested acceptance criteria without scaffolding. For code/prototypes, deliver the scoped working result and exact verification boundaries. A readable final frame and honest interruption behavior matter more than the number of effects.
