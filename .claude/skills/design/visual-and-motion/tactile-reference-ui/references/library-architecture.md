# Library architecture and extension contract

The kit is reusable source and packaged components for React and Svelte. It is not a FinanceAPI application or a remotely published npm package. Use one framework adapter plus shared tokens/style package; do not introduce React into the SvelteKit product to consume the React adapter.

## Four layers

| Layer | Ownership | Examples |
|---|---|---|
| Foundations | Stable direction names, semantic tones, spacing/material/motion | tokens, scoped CSS, Direction, Atmosphere, motion |
| Primitives | One native semantic element with consistent visual physics | Button, ActionLink, Field, Switch, Badge, Surface |
| Compounds | Small reusable structure with explicit typed state/slots | Tabs, Dialog, TaskComposer, SiteHeader, Accordion, SegmentedControl |
| Product recipes | Page composition and host-owned behavior | creation hero, showcase, integration section, workspace |

Keep implementations in focused framework modules and export through one stable barrel. Shared visual rules live in tokens CSS rather than duplicate adapter styles. Directions alter material/composition but do not alter state ownership or business meaning. Consumer overrides stay in a named wrapper and documented custom properties/classes.

## API and state ownership

Required inputs have typed props; optional variants have explicit defaults. Export common types. Use native attributes where supported, forward meaningful labels and keep props equivalent across adapters. React uses ReactNode slots; Svelte uses named/child Snippets. Do not fabricate pseudo-props such as `onGenerate` or `asChild`: inspect actual exported source/types and examples.

Controlled components receive current value plus change callback. The parent owns durable truth, filtering, network requests, cancellation and authorization. Components may own presentation state such as a disclosure or one-shot reveal; they cannot silently call a business API. Avoid competing sources of truth. React's [state sharing guidance](https://react.dev/learn/sharing-state-between-components) describes a common parent coordinating state.

Illustration APIs describe art, not data models: `MaterialObject kind="coin"` has no balance, `FrostedIcon` has no financial values, `DeviceFrame` is not a device simulator, `IntegrationMap` has no credentials. Host data stays outside decorative rendering.

## Document variants and states through examples

Give each component a realistic default, alternate variant, narrow viewport and actual state transitions. Forms need focus, invalid, disabled, pending and completion examples; compounds need keyboard/selection examples; narrative components need long copy and missing-art cases. Render genuine content, not only label matrices.

The galleries and checks are the current demonstration surface; they are not Storybook. Future Storybook adapters can expose typed props/slots through args/Controls without changing semantics. [Storybook args](https://storybook.js.org/docs/writing-stories/args) and [Controls](https://storybook.js.org/docs/essentials/controls) document the pattern. Do not claim it is installed or verified unless that work occurred.

## CSS and rendering boundaries

Import shared CSS once. Styles are scoped under kit classes/Theme; the package does not reset the host or request external font services. It loads bundled Manrope/Instrument Serif through relative local asset URLs; keep assets and licenses with the CSS. Use supported product semantics. Decorative layers are pointer-inert and not focus targets. SSR uses deterministic markup/IDs/coordinates; browser behavior begins after mount and cleans up observers/listeners/frame work.

Package React as ESM/types and Svelte as preprocessed `.svelte` modules/types through `svelte-package`. Preserve types/svelte exports and CSS side-effects so tree-shaking does not strip shared styles. [Svelte packaging guidance](https://svelte.dev/docs/kit/packaging) supports this distribution structure. Actual manifests own versions/exports.

## Extend deliberately

Add a component for a repeated distinct semantic/material pattern that existing composition cannot express cleanly. Prefer a focused compound over one Card with dozens of switches. Keep business reports, tenancy, fetching and promises in the host. Match static art quality before motion.

When changing shared behavior, update both adapters, types, examples and meaningful verification. A new selection control needs keyboard/focus/state checks; a color change does not need a wording-matching test. Verify a packed external consumer to catch hidden workspace paths. API parity/build do not establish visual equivalence: inspect both rendered examples.

Sources above were retrieved/verified during this work on 2026-10-12. They support technical conventions, not claims about retention, fidelity, compliance or production performance.

