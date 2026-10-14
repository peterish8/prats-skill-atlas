# Component contracts and composition recipes

Both adapters export 37 components. Shared semantics/materials live in `@tactile-ui/tokens`; React slots use ReactNode, Svelte slots use Snippet. Read actual source/types before using an unfamiliar prop. The component API deliberately does not include business providers, persistence or automatic proof claims.

## Actual public inventory

| Component | Required inputs | Optional/defaults and responsibility |
|---|---|---|
| Theme | children/content | `direction='porcelain'`; scoped div, native attributes |
| Surface | content as needed | `depth='raised'`: flat/raised/recessed/floating; `texture='none'`: none/dots/grain/lines |
| Button | visible children/label | `variant='primary'`: primary/secondary/ghost/danger; `loading=false`; native button props; default type=button |
| ActionLink | href, visible children | variant primary/secondary/ghost; native anchor props; navigation rather than operation |
| Badge | visible children | tone neutral/info/success/warning/danger; text is meaningful, dot decorative |
| Field | label | native input props, hint?, error?; host owns value/validation |
| Switch | checked, onCheckedChange(boolean), label | native button props except conflicting handler/state; controlled switch |
| Tabs | items, value, onValueChange(id), label | items `{id,label,content}`; roving keyboard tab behavior; host controls current value |
| MetricCard | label, value | detail?, note?, children; Surface props; value is an already formatted string |
| Orb | none | appearance neutral/accent/iridescent; decorative small physical object |
| FeatureCard | title, description | art?, footer?; Surface props; h3 and art/copy zones |
| Sparkline | values(number[]), label | decorative chart coordinates plus accessible chart title; host owns dates/units/context |
| IntegrationMap | nodes, title | detail?, center?; nodes `{id,label,detail?,symbol?}`; static relationship, no authentication |
| FileStack | title, files | files `{id,name,detail,kind?:folder|document}`; read-only visual list/stack |
| Meter | label, value, max, valueText | clamps numerical range; host supplies actual meaning/text |
| Dialog | open, onOpenChange(boolean), title, children | native modal lifecycle; caller owns triggering operation/state |
| PosterCard | title, description | palette blue/violet/ice; symbol?; bounded atmosphere poster |
| Shield | none | decorative original SVG security object; no security certification |
| OnboardingCard | title, description, step, steps, onContinue | art?, continueLabel='Continue'; host owns sequence/back/skip/durable progress |
| SiteHeader | brand, homeHref, items | items `{label,href}`; action? `{label,href}`; native mobile disclosure |
| AmbientBackdrop | kind | meadow/contours/paths/ribs/pixels/scanlines/landscape; animated=false; decorative bounded layer |
| MarketingHero | title, description | eyebrow?, align=center/split, art?, children/actions; owns page h1 |
| SectionHeading | title | eyebrow?, description?, align=start/center; owns h2 |
| ShowcaseCard | title, description, art | tone meadow/blue/mint/lavender; owns h3; authentic product preview goes in art |
| FrostedIcon | none | decorative green layered icon; bars do not encode real values |
| Reveal | children | delay=0, clamped to 0–280 ms; visible SSR, one-shot below-fold enhancement |
| MotionStage | children | paused=false, intensity=.6 bounded 0–1; owns scoped browser motion controller |
| TaskComposer | label, value, onValueChange(string), onSubmit(trimmedString) | submitLabel='Create outline', placeholder?, hint?, error?, loading=false, disabled=false, maxLength=1000 |
| ProcessCard | title, description, mark | mark scatter/align/transfer; step?; fine-line process explanation, h3 |
| DeviceFrame | label, children | variant=desktop/phone; visible figure caption; actual foreground content |
| MaterialObject | kind | orb/coin/sun/certificate; decorative original sculpture |
| Accordion | items | items `{id,title,content}`; label?; native details/summary |
| SegmentedControl | label, value, options, onValueChange(string) | options `{value,label,disabled?}`; native mutually exclusive radio group |
| InlineNotice | title, children | tone neutral/info/success/warning/danger; caller owns announcements |
| EmptyState | title, description | art?, children/actions; explain the actual absence and one next step |
| AvatarStack | items | items `{id,name,initials}`, max=4; names exposed in accessible list; no profile fetching |
| Skeleton | none | lines=3, bounded 1–12; aria-hidden; host supplies visible/accessible loading label |

Most new components support `className`; native-attribute primitives in Svelte support native `class` (including Svelte ClassValue) and React uses `className`. This does not mean every compound forwards arbitrary HTML props. Exact package types are authoritative. `InlineNotice` is a visible note; put a changing result inside a host `role='status'`/live region only when an announcement is appropriate. Avoid making every note an assertive alert.

## Recipe: a task-first hero

Use `Theme` → `MotionStage` → positioned isolated hero wrapper → `AmbientBackdrop` → `SiteHeader` and `MarketingHero`. Put `TaskComposer` in the hero's child action area, not a plain unstyled input/button. The backdrop is absolute: its wrapper needs `position:relative; isolation:isolate; overflow:hidden` and an intentional height. Do not render it as an ordinary flow item and expect a hero to appear.

The parent owns input, pending, error and result. `onSubmit` receives the trimmed value; synchronously set loading/request identity before starting asynchronous work. The component's same-turn submit lock is not a server idempotency guarantee. `maxLength` is a UI bound, not backend validation. On failure preserve the value and show a precise error. Success reveals a useful artifact immediately; optional motion is independent.

Use one h1. A second MarketingHero is a second page-title owner; use SectionHeading for later sections. Use anchors for alternate imports that navigate, buttons for file pickers/actions, and actual accepted formats/permission copy. Library controls share physical styles; custom task components should compose these primitives rather than invent unrelated appearances.

## Recipe: a precise process triptych

`SectionHeading align='center'` followed by three `ProcessCard`s: scatter for separation, align for organization, transfer for delivery. The mark is visual metaphor, while title/description carries the actual process. Use a CSS three-column grid with `minmax(0,1fr)`, 20–28 px gap and one-column recomposition below 640–760 px. Do not give sequential process steps inconsistent decorative media or fake progress. For live stages, add genuine status text through Badge/InlineNotice and host state.

## Recipe: a product staged in open air

`ShowcaseCard` art contains `DeviceFrame label='…'`, a FileStack, a focused MetricCard or a small original product fragment. The caption states what the example is. Keep copy outside scaled/rotated art. A cropped device illustration should be non-interactive; place a real interaction elsewhere. Three examples should demonstrate different tasks, not repeat the same generic graph in different colors.

Use `.tui-stage-object` only on a decorative wrapper inside MotionStage when scoped motion is intended. Do not attach it to all form inputs, tables or primary copy. `MaterialObject` creates original bounded art; it does not provide a clickable object, a balance or certificate status. Pair it with meaningful copy, and replace it with authentic product art when that better matches the reference.

## Recipe: a connected section that explains a real relation

Use IntegrationMap with stable IDs, readable labels and genuine supported services/tasks. Follow it with FeatureCard/ShowcaseCard outputs. It splits nodes between two sides and has a static center; it is not an arbitrary graph editor. On phones the relationship becomes a named list and ornamental paths hide. For a real Connect action, use a separate Button and host-owned authorization/pending/error flow; avoid clickable decorative nodes with no exposed button semantics.

## Recipe: a working analytical surface

Use SectionHeading, date/scope controls from the host, a prioritized MetricCard group, Sparkline/Meter where semantically appropriate, and a real semantic table. Display amounts as correctly formatted strings; this library does no financial arithmetic. Tables need actual column headings, sorting state, units, pagination and row/detail behavior from the product. SegmentedControl changes a genuine mutually exclusive filter; Tabs switches labeled content panels. An empty filtered result uses EmptyState with Clear filters; an empty organization uses Create/import. Those are different states.

## Recipe: settings, help and outcomes

Switch toggles a true boolean immediately in parent state. SegmentedControl holds one of several values; do not model a multi-select with it. Accordion exposes useful FAQ/setup explanations through native disclosure, with answer content available in the document. Dialog is appropriate for a focused decision that must interrupt the page; an InlineNotice is suitable for contextual explanation. A destructive action uses a clearly labeled Button variant=danger and host safeguards appropriate to its consequences.

Skeleton is decorative while the parent renders loading text and sets busy state on the relevant region. AvatarStack shows actual people; it cannot be social-proof decoration with fictitious user counts. EmptyState includes cause/context and a real next action. Provide long-name/long-label examples; do not truncate essential terms to maintain a pretty card.

## Composition scope and omissions

The kit supplies material-aware primitives and compounds. It deliberately has no universal financial dashboard, checkout engine, provider authentication, tenant model or data router. Host CSS owns page-level widths and layouts where no dedicated compound exists. Source [React barrel](../packages/react/src/index.tsx), [Svelte barrel](../packages/svelte/src/lib/index.ts) and [shared styles](../packages/tokens/styles.css) are the actual APIs; use these files and the runnable examples together.
