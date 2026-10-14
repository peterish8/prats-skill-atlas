# Porcelain desk

Primary references: [07](../assets/design-kit/references/07-secure-knowledge-base-card.png), [09](../assets/design-kit/references/09-project-workflow-neumorphic-map.png), [10](../assets/design-kit/references/10-cloud-drive-floating-panel.png), [15](../assets/design-kit/references/15-porcelain-orbit-learning-card.png), [18](../assets/design-kit/references/18-iridescent-sun-switch-detail.png); 19 repeats 10. Use `Theme direction="porcelain"`.

## Visual contract

A quiet pale desk supports readable white objects. Elevation is reserved for selected objects and frontmost panels. The reference's low contrast is suitable for peripheral art; essential labels and controls need stronger edges and ink.

| Setting | Rebuild estimate / target |
|---|---|
| Substrate | `#f1f2f3`; card `#fdfdfd`; ink `#202327`; muted `#606770` |
| Accent | Blue `#3967d8`; keep it to selected item, action and meaningful progress |
| Card radius | 24 px; larger illustrative chassis 36–48 px |
| Small object radius | 12–20 px; circular orbital centers remain circular |
| Heading | App 24–32 px, feature 28–40 px; sans 500–620; −.035 em |
| Relief | White 1 px inner top edge; contact `0 2px 3px #19233207`; ambient `0 14px 30px -20px #19233245` |
| Floating object | Ambient `0 22px 42px -20px #19233240`; use once per cluster |
| Connector | 1 px pale gray/blue, behind nodes, curved orthogonal turns |
| Content spacing | Card 24–32 px; inter-card 20–24 px; marketing sections 80–104 px |

## Composition anatomy

For a feature page, use a centered plain navigation, a short left aligned introduction, then a broad three-column feature section. Each feature uses an upper illustration occupying 55–65% and lower copy occupying 35–45%. The main illustration has one saturated object at the center, four to six pale peripheral objects and quiet connectors. Match the rim/contact shadow before adding glow.

For a file workspace, use a plain header with breadcrumb, search and a relevant creation action; below, a clear list or grid occupies the center. A contextual detail panel can take 28–34% of the width. Illustration stacks are demonstration art only. Real lists should not be tilted, cropped or faded to imply peripheral depth.

## Components and material recipe

Use `Surface depth="raised"` for stable cards, `depth="recessed"` for trays and `depth="floating"` for a selected detail panel. Combine `FileStack` with three to six real file items; its layers are decorative and the text remains readable. `Shield` is a decorative center for a feature explaining supported security controls, not a certification badge. `IntegrationMap` is appropriate for a relationship; `Orb appearance="neutral"` for a relief object and `appearance="iridescent"` for one subtle sun-like detail.

Build custom relief art with a `position:relative` frame, a white front plane, a 1 px light edge and two distinct shadows. A front plane can have two offset pale backing planes 8 px and 16 px above, narrowing by 10 px each side. Limit stacks to three layers. Keep the same downward light direction for every object. A pale rim around a feature card is 8–12 px, not an enormous shadow.

## Page and UX recipe

Sequence: hero describing one actual task → feature pair showing a concrete artifact → connected source/workflow section → short evidence or support block → final task action. A working app sequence is file selection → detail inspection → explicit action → status confirmation. Provide a clear no-files state with one creation/import route, a loading label, a recoverable load error, selected file text and permission explanation. Put substantive eligibility/privacy notices in visible copy, not inside a clipped tray footer.

## Responsive and motion

Below 900 px use two columns; below 640 px use one. Recompose orbital art to one center and up to four satellites; use a text list for an actual network. Detail panels become inline regions or an accessible dialog. Preserve a 20 px gutter and 16 px body text. A hovered actionable raised surface may lift 1–2 px for 180 ms; a non-interactive card stays still. Switch changes use a short thumb translation. Selected file state changes immediately; do not animate every row into place. Reduced motion keeps all relief static.

## Acceptance and exclusions

Accept: clear white planes, one deliberate accent, coherent shadow direction, crisp selectable controls and actual file/status meaning. Reject: invisible borders, decorative dots carrying meaning alone, a shadow on every label, a huge floating hero orb without a purpose, or using the screenshot's faded copy on essential content. Test the page in grayscale and at 200% zoom; selection and content structure must remain obvious.

