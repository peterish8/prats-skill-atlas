# Drop in the actual library

Use the tokens package and one framework adapter. The kit ships 37 typed components per adapter, self-hosted Manrope/Instrument Serif, original visual assets, scoped materials, physical controls and motion controller. It does not ship a product backend. Reading a direction and changing the Theme is insufficient: reproduce the page anatomy using the real compounds and authentic host content.

## Install from the portable bundle

This public package carries source, references, artwork, fonts, and licenses. Generated output is excluded. In `assets/design-kit`, run `npm ci`, `npm run build`, and `npm run pack:libs` to generate the local adapter tarballs before following installation commands. Follow the project's existing dependency-install authorization.


From the consuming application, install both local tarballs in one command so the adapter's tokens dependency resolves locally. Replace `<kit>` with the actual bundled `assets/design-kit` directory or a copied kit directory; these are placeholders, not executable paths.

```powershell
# React 19 consumer
npm install "<kit>/dist-packages/tactile-ui-tokens-0.1.0.tgz" "<kit>/dist-packages/tactile-ui-react-0.1.0.tgz"

# Svelte 5 / existing SvelteKit consumer
npm install "<kit>/dist-packages/tactile-ui-tokens-0.1.0.tgz" "<kit>/dist-packages/tactile-ui-svelte-0.1.0.tgz"
```

Do not run both framework commands for one application unless it intentionally uses both. Packages are local/private; do not substitute a public registry package of the same name. Preserve the consuming app's package manager/lockfile conventions. The adapter manifests declare actual peer ranges; do not silently upgrade the host.

To copy source/examples into a new local directory first:

```powershell
node "<kit>/scripts/copy-kit.mjs" --target "<project>/vendor/tactile-ui" --framework svelte --dry-run
node "<kit>/scripts/copy-kit.mjs" --target "<project>/vendor/tactile-ui" --framework svelte
```

The helper refuses an existing destination and reports what it copies. It leaves application/package.json untouched and prints the combined tarball install command. It is a copy helper, not a dependency installer or a production deployment. Use `--framework react` for the React install recommendation. A workspace can also consume the local packages after their builds; inspect the kit's actual scripts rather than inventing build commands.

## Styles, typography and page layout

Import `@tactile-ui/tokens/styles.css` once in the host's global layout/entry. The stylesheet imports marketing/cinematic layers and local font/assets URLs. Keep CSS and assets together; copying only styles.css breaks those imports. The stylesheet does not reset body margin or host typography outside Theme. Use the host's existing reset/layout intentionally.

Theme owns material variables, not routing or every page layout. Components own their internal anatomy. A page wrapper owns max width, grids, sections and the reference's characteristic whitespace. Shared [recipe CSS](examples/recipe.css) shows a deliberate meadow layout without replacing library controls. Override scoped `--tui-*` variables when fitting an established brand.

## Complete copyable pages

- [React MeadowPage.tsx](examples/MeadowPage.tsx): controlled task field, local outline result, actual library controls, paused atmosphere, visible product frame and process/help sections.
- [Svelte MeadowPage.svelte](examples/MeadowPage.svelte): the same behavior using Svelte 5 state/snippets and native `onclick`.
- [Companion layout CSS](examples/recipe.css): import next to either example.

These are runnable local demonstrations: they create a page-memory outline and explicitly disclose that reload clears it. They make no AI/provider call and do not save a project. Replace the local callback with the host's authorized service, preserve pending/error/cancel states and report actual results. The sample uses one h1, a concrete result and actionable Pause/Resume. Add original page content/imagery appropriate to the product rather than copying sample brand names everywhere.

## Slot mapping

React:

```tsx
<ShowcaseCard title="A focused workspace" description="Keep the next useful step in view."
  tone="mint" art={<DeviceFrame label="Example workspace"><FileStack title="Field notes"
    files={[{id:'notes',name:'Notes',detail:'Example folder',kind:'folder'}]}/></DeviceFrame>}/>
```

Svelte 5:

```svelte
<ShowcaseCard title="A focused workspace" description="Keep the next useful step in view." tone="mint">
  {#snippet art()}
    <DeviceFrame label="Example workspace">
      <FileStack title="Field notes" files={[{id:'notes',name:'Notes',detail:'Example folder',kind:'folder'}]}/>
    </DeviceFrame>
  {/snippet}
</ShowcaseCard>
```

Use named `art`, `footer` or `center` Snippets only where actual component types expose them. Child Snippets hold actions or ordinary content. React uses `onClick`/`onChange`; Svelte uses native `onclick`/`oninput` for HTML primitives. Controlled kit callbacks such as `onValueChange`, `onCheckedChange` and `onOpenChange` retain their explicit names in both frameworks.

## Framework and SSR details

React interactive components use hooks/client behavior; in a server-component host import them from a client boundary while keeping service secrets server-side. The CSS is one shared import. Stable IDs and deterministic art prevent hydration drift. Do not generate random positions per render.

The Svelte package contains preprocessed `.svelte` modules/types, with `types`/`svelte` exports and CSS side-effects preserved. [Official Svelte packaging guidance](https://svelte.dev/docs/kit/packaging) describes this structure. The bundled gallery uses pinned SvelteKit 3 configuration in `vite.config.ts` through `sveltekit({...})`; [the Vite integration reference](https://svelte.dev/docs/kit/@sveltejs-kit-vite) is its setup source. Existing Kit 2 consumers keep their own supported configuration; installing the component library does not require copying a gallery's framework config.

Reveal keeps server-rendered content visible and initializes enhancement after mount. MotionStage mounts a scoped controller and destroys listeners/frame work on teardown. `.tui-stage-object` opts a decorative object into that stage's physical pose; do not apply it to the whole page, form fields or data table. Ambient pause and OS reduced motion are separate. A beautiful static page must remain useful before browser enhancement.

## Adapting other directions with real compounds

Equilibrium uses contours + centered hero + ProcessCard triptych and an axis divider. Systems uses paths + split hero + real labeled setup form/product art. Prism uses ribs + white hero type + opaque cream editorial sheet. Atelier uses pixels or original subject-shaped scanlines + asymmetric copy/facts. Landscape uses split hero or a deliberate triptych with genuine DeviceFrame/ShowcaseCard artifacts. Citrus uses rounded chassis, limited lime MaterialObject/FrostedIcon and product stage. Read each direction's anatomy, not only its token row.

For routine actions use Button/ActionLink; for text input Field/TaskComposer; for boolean choice Switch; for single selection SegmentedControl; for panels Tabs; for help Accordion; for absence EmptyState; for pending Skeleton paired with text; for results InlineNotice. Custom page layout may use semantic HTML/CSS. Do not invent new props or replace all controls with unstyled elements because it is quicker.

Read [component contracts](component-recipes.md) and actual [React](../assets/design-kit/packages/react/src/index.tsx)/[Svelte](../assets/design-kit/packages/svelte/src/lib/index.ts) exports before extending. Validate a packed external consumer as well as workspace builds; inspect the rendered target page and one complete interaction. No production/backend/device claim follows from a successful component build.

