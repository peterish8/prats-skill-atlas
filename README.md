# Prats Skill Atlas

<p align="center">
  <img src="./assets/prats-skill-atlas-hero.svg" alt="Prats Skill Atlas, a cinematic map of skills for Claude, Codex, and shared agents" width="100%">
</p>

<p align="center">
  <strong>A navigable constellation of global skills for Claude, Codex, and shared agents.</strong><br>
  Clone once. Install everywhere. Keep the runtime clean.
</p>

<p align="center">
  <a href="https://github.com/peterish8/prats-skill-atlas"><img src="https://img.shields.io/badge/483_unique_skills-36d9ff?style=flat-square&labelColor=0b1017" alt="483 unique skills"></a>
  <a href="https://github.com/peterish8/prats-skill-atlas/tree/main/.claude"><img src="https://img.shields.io/badge/Claude-ready-f4b860?style=flat-square&labelColor=0b1017" alt="Claude ready"></a>
  <a href="https://github.com/peterish8/prats-skill-atlas/tree/main/.codex"><img src="https://img.shields.io/badge/Codex-ready-36d9ff?style=flat-square&labelColor=0b1017" alt="Codex ready"></a>
  <a href="https://github.com/peterish8/prats-skill-atlas/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-b9c2cc?style=flat-square&labelColor=0b1017" alt="MIT license"></a>
</p>

<p align="center">
  <img src="./assets/atlas-network.svg" alt="Connected categories in the Prats Skill Atlas" width="100%">
</p>

## The idea

Skill collections grow like galaxies: useful stars arrive from different systems, then become hard to find. **Prats Skill Atlas** gives that collection a clear map.

This public repository packages the global skill trees from Claude, Codex, and shared agents into one cloneable home. The source layout is organized for humans. The installers flatten it back to the runtime layout each tool expects.

## What is inside

| Runtime tree | Packages | Purpose |
| --- | ---: | --- |
| [`.claude/skills`](.claude/skills) | 352 | Claude-compatible skill packages |
| [`.codex/skills`](.codex/skills) | 252 | Codex-compatible skill packages |
| [`.agents/skills`](.agents/skills) | 307 | Shared agent skill packages |
| **Unique skill names** | **483** | Deduplicated collection across all trees |

Every package keeps its own `SKILL.md`, references, scripts, and practical assets where they are safe to redistribute. Categories and subcategories make the collection easy to scan:

- `planning/project-planning`
- `architecture/system-design`
- `frontend/web-ui`
- `backend/apis-and-platforms`
- `design/visual-and-motion`
- `agent-workflows/coordination`
- `security/appsec-and-privacy`
- `testing/qa-and-verification`
- `devops/delivery-and-tooling`
- `docs/writing-and-specs`
- `research-data/research-seo-and-content`
- `integrations/platform-tools`
- `mobile/native-and-cross-platform`
- `specialists/domain-workflows`
- `tools-utilities/general-purpose`

See the complete map in [`catalog/skills.md`](catalog/skills.md).

## Install the atlas

### Windows PowerShell

```powershell
git clone https://github.com/peterish8/prats-skill-atlas.git
cd prats-skill-atlas
.\install.ps1 -All
```

Install only the runtime tree you need:

```powershell
.\install.ps1 -Claude
.\install.ps1 -Codex
.\install.ps1 -Agents
```

### macOS, Linux, or WSL

```bash
git clone https://github.com/peterish8/prats-skill-atlas.git
cd prats-skill-atlas
./install.sh all
```

The installers are copy-only. They create missing directories and overwrite same-named packages, but never delete unrelated local skills.

## The repository map

```text
prats-skill-atlas/
|-- .claude/skills/<category>/<subcategory>/<skill-name>/SKILL.md
|-- .codex/skills/<category>/<subcategory>/<skill-name>/SKILL.md
|-- .agents/skills/<category>/<subcategory>/<skill-name>/SKILL.md
|-- assets/
|   |-- prats-skill-atlas-hero.svg
|   `-- atlas-network.svg
|-- catalog/
|   |-- skills.json
|   |-- skills.md
|   `-- categories/<category>--<subcategory>.md
|-- scripts/
|   |-- build-catalog.ps1
|   |-- organize-runtime-trees.ps1
|   `-- validate.ps1
|-- install.ps1
|-- install.sh
`-- NOTICE.md
```

The category folders are the browsing layer. `install.ps1` and `install.sh` intentionally flatten packages into the user runtime roots, so Claude and Codex continue to discover skills by package name.

## Catalog and maintenance

- [`catalog/skills.md`](catalog/skills.md): human-readable index of every package
- [`catalog/skills.json`](catalog/skills.json): machine-readable package metadata
- [`catalog/categories/`](catalog/categories/): focused pages for each category
- [`catalog/README.md`](catalog/README.md): category rules and source notes

After adding or syncing packages:

```powershell
.\scripts\organize-runtime-trees.ps1
.\scripts\build-catalog.ps1
.\scripts\validate.ps1
```

The organizer applies deterministic name-based rules to new flat packages. The catalog records the actual category path. Validation checks all three runtime trees and every required `SKILL.md`.

## Motion, with a quiet fallback

The atlas artwork is built as inline-friendly SVG, not a screenshot. Orbit lines, signal pulses, and constellation points animate in browsers that support SVG motion. The moving layers are marked with `.motion` and disappear when `prefers-reduced-motion: reduce` is enabled. The labels and hierarchy remain readable in the still frame.

## Source and license notes

This is a local skill mirror and packaging project. Generated dependencies and machine-specific artifacts are intentionally excluded, including `node_modules`, `.venv`, Playwright browser binaries, `dist`, `.git`, bytecode, native binaries, and similar build output.

Individual skill packages may have their own authorship and license terms. Read [`NOTICE.md`](NOTICE.md) before redistributing or modifying a specific package.

## Make it yours

Fork the atlas, add your own skill constellation, regenerate the catalog, and keep the runtime roots clean. If you build a useful category or compatibility improvement, open a pull request with the validation output included.
