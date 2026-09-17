# Motion-design principles and spatial grammar

These are craft decisions for interactive motion graphics. The implementation invariants at the end are firm; visual magnitudes and timing are adaptable.

## Composition over time

| Principle | What it means in an interface | Decision to make |
| --- | --- | --- |
| Intent | Motion communicates a change or supports a deliberate expressive moment | Name the effect's job and what the final pose means |
| Staging | Attention has a clear subject at each beat | Let one major change lead; lower contrast/movement elsewhere |
| Hierarchy | The most important event reads first | Order focal subject, explanation, then supporting detail |
| Readable poses | Important meaning survives paused playback | Inspect initial, impact, transformation and final frames |
| Timing and spacing | Duration sets total time; spacing/easing distributes travel through that time | Tune distance and acceleration together, not duration alone |
| Rhythm | Changes and holds form a deliberate cadence | Alternate expressive and quiet beats; give new information time to read |
| Anticipation | A small preparation explains a larger movement | Reserve it for a meaningful reveal; acknowledge input immediately |
| Follow-through | Secondary material settles after the main action | Let a label, shadow or trail finish independently of interaction readiness |
| Overlapping action | Related layers do not all start or stop together | Offset support enough to show causality without producing a slow chain |
| Arcs | Curved travel can communicate direction and material character | Choose an arc that connects actual anchors; straight travel is valid for precision |
| Weight | Acceleration, resistance and settle imply material | Match behavior to an object or product tone instead of bouncing every element |
| Elasticity | A brief deformation suggests a flexible object | Deform an internal graphic, not readable text or a moving hit target |
| Restraint and exaggeration | Selected exaggeration clarifies an event | Amplify one meaningful dimension, then return to a calm resting pose |
| Continuity | Identity, direction and relationships persist across states | Keep anchors, depth and orientation coherent; choose a deliberate cut when needed |
| Secondary action | A supporting movement strengthens the primary one | Remove any particle or glow that competes with the event it explains |
| Loop closure | Repeated motion reconnects without a visible jump | Match end/start pose and speed, or conceal the seam intentionally |

Classic animation concepts are adapted here, not blindly imposed. A precise data interface may favor direct cuts and quiet fades; an identity scene may use arcs and exaggeration. “More cinematic” does not mean “more movement.”

## Easing is behavior

- Ease-out is a useful arrival/acknowledgement choice: early movement followed by controlled deceleration.
- Ease-in can support departure: begin gently and accelerate out of the current scene. Do not delay recognition of a user action waiting for that departure.
- Ease-in-out suits an autonomous travel between resting poses; it can feel detached when applied to direct pointer tracking.
- Linear progress represents constant visual speed along a parameter; it does not guarantee constant distance per second along an arbitrary curve.
- Springs suit gesture settling or elastic objects. Stiffness, damping, mass and initial velocity interact; a higher stiffness value is not by itself a complete “faster” preset. Use the engine's model and inspect the actual settle.

A duration-controlled tween and a physically tuned spring have different contracts. Do not promise an exact millisecond finish for an unrestricted spring or combine incompatible spring controls without checking the installed engine. Match different properties intentionally: opacity need not inherit the physical bounce of position.

## Spatial grammar

Specify an origin, destination, pivot, plane and light direction. A graphic may rise from a lower portal while its text lifts away; that is a coherent grammar when reused deliberately. A different product may grow route lines from a map node or pull album artwork from a list row.

Keep motion relative to measured containers/anchors, not a convenient viewport guess. Choose normalized or local coordinates when a composition must resize. Define what happens if the anchor moves mid-flight: retarget, finish a measured snapshot, or replace the decorative effect. Avoid mixing viewport coordinates with an absolute layer positioned inside another container.

Use depth to explain relationships: near elements can overlap distant ones; scale and parallax should agree with perspective. Lights and contact shadows follow the object's intended grounding. If the style is flat or deliberately nonphysical, keep that alternative language consistent instead of introducing isolated realistic effects.

## Graphic families

- Typography: reveal complete words/phrases through a mask; retain natural line breaks and a single accessible phrase. Use character animation primarily for short identity type.
- Shapes: preserve topology and compatible point order for a genuine morph; otherwise use composition, masking or a controlled cut. Explain state with shape rather than only color.
- Lines/diagrams: draw a path in the direction of the relationship, then reveal the connected label. A partial path is a construction cue, not proof a data operation is partially done.
- Particles: use bounded seeded variations in size, path and delay; travel should connect the action to the result. Keep bursts outside essential text and hit regions.
- Light: change a restrained layer's visibility or transform before choosing large animated filters. A short emphasis should return to the resting hierarchy.
- 3D: preserve object orientation and logical state; shape faces, occlusion and shading should agree with the turn. Rotate a meaningful object rather than the whole reading surface.

## Implementation invariants

Record the operation independently of decoration. Never show confirmed completion before confirmation. Do not let two engines fight over one property. Do not replay an external write on visual replay. Define cancellation, skip and reduced-motion final states. Preserve readable content, focus and reachable controls at each usable state. These rules do not impose a palette, a cube, particle count or animation library.
