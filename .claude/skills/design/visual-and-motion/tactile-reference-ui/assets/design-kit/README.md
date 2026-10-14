# Tactile UI reference kit

A reusable skill and original component library derived from 36 supplied visual references. This standalone design kit is separate from the FinanceAPI application roadmap. It preserves the previous six component directions and adds six page compositions.

## Start

Use `$tactile-reference-ui` in a new coding chat. The installed skill includes its visual guides, original reference images, component source, compiled libraries, galleries, and local package tarballs. The repository copy is [skill/tactile-reference-ui/SKILL.md](skill/tactile-reference-ui/SKILL.md).

```sh
npm ci
npm run check
npm run build
npm run dev:react
# Or, in another terminal:
npm run dev:svelte
```

React gallery: http://127.0.0.1:5181. SvelteKit gallery: http://127.0.0.1:5182. Galleries show original compositions and explicitly illustrative product content.

## Use in another application

After building, `npm run pack:libs` writes three local packages into `dist-packages`. Install tokens plus the chosen framework package in the same command; the framework package depends on tokens.

```sh
npm install /path/to/dist-packages/tactile-ui-tokens-0.1.0.tgz /path/to/dist-packages/tactile-ui-react-0.1.0.tgz
# Svelte / SvelteKit:
npm install /path/to/dist-packages/tactile-ui-tokens-0.1.0.tgz /path/to/dist-packages/tactile-ui-svelte-0.1.0.tgz
```

Import `@tactile-ui/tokens/styles.css` once. Wrap components in `Theme` with a direction. Use React 19 or Svelte 5; a JavaScript application can consume the compiled exports, with TypeScript definitions available. The Svelte library is independent of SvelteKit route APIs.

```jsx
import '@tactile-ui/tokens/styles.css';
import { Theme, MarketingHero, ActionLink } from '@tactile-ui/react';

export default function Landing() {
  return <Theme direction="meadow">
    <MarketingHero title="A little room for your next idea." description="Your actual product benefit, in plain language.">
      <ActionLink href="/start">Start a project</ActionLink>
    </MarketingHero>
  </Theme>;
}
```

For portable source, preview a safe copy with `node scripts/copy-kit.mjs --target ../vendor/tactile-ui --framework svelte --dry-run`, then remove `--dry-run`. It refuses an existing destination and leaves the application's dependency manifest untouched. See [framework recipes](docs/framework-guide.md) for complete examples.

## Directions

| Existing component language | New page compositions |
|---|---|
| Porcelain desk | Meadow light |
| Spectral atmosphere | Lime equilibrium |
| Warm editorial | Mint infrastructure |
| Citrus playground | Refracted blue |
| Precision signal | Pixel atelier |
| Connected canvas | Landscape product |

Read [the visual catalogue](docs/reference-catalogue.md), choose one direction, then use its composition and component recipes. The skill routes to the appropriate documents without loading every direction.

The 37 matching framework components include controls, dialogs/tabs, cards, charts, file stacks, maps, headers, heroes, task composers, device frames, process cards, material objects, notices, empty/loading states, accordions, segmented controls, avatar stacks and motion stages. Shared styles ship original landscape and iridescent artwork plus unmodified OFL Manrope/Instrument Serif fonts. No external font service, remote image request or animation-engine dependency is required. The [asset provenance](packages/tokens/assets/PROVENANCE.md) records generated prompts, font revisions and license files.

## Packaging and scope

`npm run bundle:skill` refreshes the local and installed skill from canonical documentation, libraries and reference assets. Screenshots are study references, not licensed production assets; keep their brands and unproven metrics out of shipped content. Libraries remain local private packages and have not been published to npm. No FinanceAPI implementation, provider integration or deployment is included.

Actual check and rendered-browser results are recorded in [VERIFICATION.md](VERIFICATION.md) after verification.
