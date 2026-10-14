# Connected canvas

Primary references: [05](../references/05-integration-flow-soft-gradient.png), [07](../references/07-secure-knowledge-base-card.png), [09](../references/09-project-workflow-neumorphic-map.png), [10](../references/10-cloud-drive-floating-panel.png), [16](../references/16-editorial-integration-feature-cards.png), [17](../references/17-ai-model-connected-chat-miniature.png), [20](../references/20-retainer-connected-bento-section.png), [21](../references/21-automation-connector-landing-section.png). Use `Theme direction="connected"`.

## Visual contract

Relationships are the composition. A center connects to a few named peripheral nodes; the material makes each node tangible and the labels make the relationship useful. Keep fine paths behind objects and anchor the network to a concrete product outcome.

| Setting | Rebuild estimate / target |
|---|---|
| Canvas | Pale gray `#f0f2f4` or white; restrained cyan/lavender edge light |
| Ink / accent | `#202327` / blue `#286ac1` |
| Node radius | 12–16 px; large group/card 22–36 px |
| Hub | 72–110 px decorative object or wide 180–240 px pill |
| Peripheral object | 40–64 px icon; capsule minimum 120×44 px |
| Connectors | 1–1.5 px stroke, corners 16–32 px radius, one style per group |
| Heading | Hero 40–64 px, feature 22–30 px; body 15–17 px |
| Map extent | 680–1060 px for explanatory marketing art |
| Depth | Selected hub strongest contact/ambient shadow; satellites one depth lower |
| Diagram text | Always outside or over solid node fill; never underneath a path |

## Composition anatomy

The simple invitation mode in 21 has mirrored curves from four peripheral nodes per side converging around a centered message/action. Its power comes from empty space, not node count. The richer section in 20 makes this relationship explicit and then routes downward into three feature outputs. The workflow in 09 is a branching path with named stages and selection. The miniature in 17 confirms only a model-row → workspace relation; inspect the larger references for material and type.

Choose hub-and-spoke when the product connects independent services, a directional path when there are stages, and a matrix when services are selected equally. Do not use a circular orbit to represent a sequential workflow. Essential relationships need an ordered textual version and meaningful labels; an art-only connector graph can be hidden from assistive technology.

## Components and relationship recipe

`IntegrationMap` renders a modest static hub/spoke relationship with named side nodes. Its `MapNode` contract has `id`, `label`, optional `detail` and `symbol`; it does not authenticate services, expose selection callbacks or compute a workflow graph. Use `FileStack`, `FeatureCard`, `Shield`, `Orb`, `Surface` and `SectionHeading` for artifacts and feature outputs.

Custom paths should be one original deterministic SVG, under the object layer and clipped within the art boundary. Use fixed viewBox geometry for decorative relationships; for a live graph derive paths from real layout or use a dedicated accessible graph implementation. Rounded orthogonal connectors work with porcelain; large mirrored curves work with the airy invitation. Avoid dotted, dashed and solid lines mixed without a meaning legend.

## Complete page and integration UX

Sequence: specific integration promise → labeled relationship → three concrete outputs → actual supported-provider list → connection/setup explanation → action. A real integration journey is select service → explain requested scope → authorize through approved mechanism → confirm connected account and permissions → test/import → show outcome. Provide disconnected, authorizing, connected, expired, permission denied and retry states. A decorative node is not a Connect button. Do not claim support for a pictured vendor unless the host implements it.

A workflow product needs stage status, a selected step with details, cancellation/recovery information and a clear next user action. Completed/blocked states use text and shape alongside color. A pipeline diagram cannot substitute for progress or error information.

## Responsive and motion

At narrow widths put the center first and side nodes into a one/two-column labeled list. Hide only the ornamental connector SVG; preserve every meaningful relationship in text. In three-feature sections stack output cards while keeping connector-to-output semantics through heading/copy. Do not make a phone horizontally scroll a decorative graph.

If motion is used, reveal the hub once, then paths in one short pass, then satellites; total delay ≤280 ms and duration ≤560 ms. A subtle path pulse belongs only to an actual active transfer, with adjacent text and a stop state. Do not continuously orbit, flash dots or animate fake data flow. Reduced motion keeps paths static, nodes visible and actual transfer status readable.

## Acceptance and exclusions

Accept: one relationship type, few named nodes, understated paths, coherent object depth and real supported outputs. Reject: spaghetti graphs, paths crossing copy, repeated brand logos without availability, hover-only integration details or low-contrast nodes disguised as disabled controls. Removing the diagram should leave a understandable textual explanation.
