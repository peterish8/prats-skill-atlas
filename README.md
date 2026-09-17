# Prats Skill Atlas

<p align="center">
  <img src="./assets/prats-skill-atlas-hero.svg" alt="Prats Skill Atlas, a cinematic map of skills for Claude, Codex, Grok, Antigravity, and shared agents" width="100%">
</p>

<p align="center">
  <strong>A navigable constellation of global skills for Claude, Codex, Grok, Antigravity, and shared agents.</strong><br>
  Clone once. Install everywhere. Keep the runtime clean.
</p>

<p align="center">
  <a href="https://github.com/peterish8/prats-skill-atlas"><img src="https://img.shields.io/badge/512_unique_skills-36d9ff?style=flat-square&labelColor=0b1017" alt="512 unique skills"></a>
  <a href="https://github.com/peterish8/prats-skill-atlas/tree/main/.claude"><img src="https://img.shields.io/badge/Claude-ready-f4b860?style=flat-square&labelColor=0b1017" alt="Claude ready"></a>
  <a href="https://github.com/peterish8/prats-skill-atlas/tree/main/.codex"><img src="https://img.shields.io/badge/Codex-ready-36d9ff?style=flat-square&labelColor=0b1017" alt="Codex ready"></a>
  <a href="https://github.com/peterish8/prats-skill-atlas/tree/main/.grok"><img src="https://img.shields.io/badge/Grok-ready-c084fc?style=flat-square&labelColor=0b1017" alt="Grok ready"></a>
  <a href="https://github.com/peterish8/prats-skill-atlas/tree/main/.antigravity"><img src="https://img.shields.io/badge/Antigravity-ready-8ab4f8?style=flat-square&labelColor=0b1017" alt="Antigravity ready"></a>
  <a href="https://github.com/peterish8/prats-skill-atlas/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-b9c2cc?style=flat-square&labelColor=0b1017" alt="MIT license"></a>
</p>

<p align="center">
  <img src="./assets/atlas-network.svg" alt="Connected categories in the Prats Skill Atlas" width="100%">
</p>

## The idea

Skill collections grow like galaxies: useful stars arrive from different systems, then become hard to find. **Prats Skill Atlas** gives that collection a clear map.

This public repository packages global skill trees for Claude, Codex, Grok, Antigravity, and shared agents into one cloneable home. The source layout is organized for humans. The installers flatten it back to the runtime layout each tool expects.

## First-time setup

Hand this repository to Claude, Codex, Grok, or Antigravity and the root agent instructions will route the conversation through [`ONBOARDING.md`](ONBOARDING.md). The agent inventories your project, asks 12 focused questions, proposes a small skill plan, shows what it is leaving out, and waits for approval before installing anything.

The default is selective setup. Your friend does not need to explain this workflow manually, and no one gets the full atlas unless they explicitly choose it.

> **Have two or more AI agents or model families?** The onboarding agent must ask, then strongly recommend the flagship [`agent-loop`](.agents/skills/agent-workflows/orchestration/agent-loop/SKILL.md) skill for substantial engineering. It asks once which runtimes, models, reasoning levels, budgets, and permissions you have, saves the confirmed roster, and updates only corrected preferences later.

## What is inside

| Runtime tree | Packages | Purpose |
| --- | ---: | --- |
| [`.claude/skills`](.claude/skills) | 381 | Claude-compatible skill packages |
| [`.codex/skills`](.codex/skills) | 281 | Codex-compatible skill packages |
| [`.grok/skills`](.grok/skills) | 3 | Grok-compatible skill packages |
| [`.antigravity/skills`](.antigravity/skills) | 3 | Antigravity-compatible source packages; installer targets `~/.gemini/config/skills` |
| [`.agents/skills`](.agents/skills) | 336 | Shared agent skill packages |
| **Unique skill names** | **512** | Deduplicated collection across all trees |

Every package keeps its own `SKILL.md`, references, scripts, and practical assets where they are safe to redistribute. Categories and subcategories make the collection easy to scan:

- `planning/project-planning`
- `product-growth/{user-research,funnel-and-activation,experimentation,monetization,retention-and-referral,measurement-and-ops,ethical-growth,orchestration}`
- `architecture/system-design`
- `frontend/web-ui`
- `backend/apis-and-platforms`
- `design/{visual-and-motion,experience-and-behavior}`
- `agent-workflows/{coordination,orchestration}`
- `security/{appsec-and-privacy,reverse-engineering}`
- `testing/qa-and-verification`
- `devops/delivery-and-tooling`
- `docs/writing-and-specs`
- `research-data/research-seo-and-content`
- `integrations/platform-tools`
- `mobile/native-and-cross-platform`
- `specialists/domain-workflows`
- `tools-utilities/general-purpose`

See the complete map in [`catalog/skills.md`](catalog/skills.md).

## Cinematic UI and curious UX

Two portable skills translate the Polaris Cubing Club experience into existing apps, prototypes, or planning-only specifications. They preserve the target product's brand and working features while adapting the staging, tactile feedback, meaningful progress and personalized completion to its own purpose.

| Skill | Category | Responsibility |
| --- | --- | --- |
| [`cinematic-ui-motion`](.agents/skills/design/visual-and-motion/cinematic-ui-motion/SKILL.md) | `design/visual-and-motion` | Composition, material depth, hero objects, gesture feedback, scene choreography, responsive and reduced-motion behavior |
| [`curiosity-driven-ux`](.agents/skills/design/experience-and-behavior/curiosity-driven-ux/SKILL.md) | `design/experience-and-behavior` | Narrative, low-effort choices, meaningful progress, agency, personalization and satisfying completion |

Both packages include their own references and agent metadata and are available in Claude, Codex, Grok, Antigravity and shared Agents. Behavioral principles are included in the UX skill. They do not require the original survey, a cube, a dark theme, React or a specific animation library; engagement and retention effects remain hypotheses until measured in the target product.

Use the [`cinematic experience selection`](examples/cinematic-experience-selection.example.json) to install only these two skills across all five supported atlas runtimes:

```powershell
.\install.ps1 -Manifest .\examples\cinematic-experience-selection.example.json
```

Example request: "Use cinematic-ui-motion and curiosity-driven-ux on this existing app. Preserve its brand and features; make its main journey tactile, curious and satisfying. Implement and verify the changes." For an idea or specification, add "Planning only; produce the journey, storyboard, motion timeline, state contracts and acceptance criteria."

## Product Growth system

The Atlas includes a source-backed Product Growth system with 25 independently installable skills. The orchestrator selects only the focused skills needed for the current decision:

```text
product-growth/
|-- user-research/                 3 skills
|-- funnel-and-activation/         3 skills
|-- experimentation/               4 skills
|-- monetization/                  4 skills
|-- retention-and-referral/        3 skills
|-- measurement-and-ops/           4 skills
|-- ethical-growth/                 3 skills
`-- orchestration/
    `-- product-growth-experimentation
```

It covers the complete loop from user evidence and acquisition intent through activation, trustworthy A/B tests, pricing and paywalls, retention, referral, instrumentation, decisions, privacy, accessibility, and dark-pattern prevention. Start with [`product-growth-experimentation`](.agents/skills/product-growth/orchestration/product-growth-experimentation/SKILL.md) for an end-to-end problem or choose a narrower package directly.

A minimal cross-runtime manifest is available at [`examples/product-growth-selection.example.json`](examples/product-growth-selection.example.json).

## Guarded reverse-security router

[`reverse-skill-router`](.agents/skills/security/reverse-engineering/reverse-skill-router/SKILL.md) adapts the upstream [`zhaoxuya520/reverse-skill`](https://github.com/zhaoxuya520/reverse-skill) router for authorized reverse engineering, CTF, malware analysis, and defensive security work. Its explicit R0–R3 command policy allows passive and bounded local work while requiring a clear yes/no permission immediately before risky commands, network activity, tool installation, dynamic execution, device changes, exploitation, or destructive actions.

The Atlas carries the lightweight guarded adapter and upstream provenance, not three copies of the upstream executable and payload corpus. A pinned shared checkout can serve Claude, Codex, and Agents without silently executing its bootstrap scripts. Use the [`reverse-skill` selection example](examples/reverse-skill-selection.example.json) to install only this adapter.

## Flagship: Looping Engineering Orchestrator

[`agent-loop`](.agents/skills/agent-workflows/orchestration/agent-loop/SKILL.md) is the Atlas's primary engineering-control skill. Claude leads inside Claude, Codex inside Codex, Grok inside Grok, and Antigravity inside `agy`; other confirmed systems become bounded workers. If access to two or more agents or model families is unknown, the skill must ask. Its compulsory first-use interview records the model and reasoning effort for orchestration, routine work, difficult work, and independent review, then saves the approved roster so setup is not repeated.

The skill delegates only when parallelism, specialization, context savings, or independent review outweigh coordination cost. It uses bounded worker contracts, single-writer ownership, isolated worktrees, deterministic verification, failure classification, benchmark integrity, and finite stopping conditions. Start with the [`multi-agent selection example`](examples/multi-agent-orchestration-selection.example.json).

| Loop role | Recommended starting point |
| --- | --- |
| Orchestrator, architect, final integrator | strongest reliable available model at high reasoning |
| Routine implementation | balanced coding model at medium reasoning |
| Fast scouting or mechanical work | fastest/lower-cost capable model at medium reasoning |
| Bounded difficult worker | fast/lower-cost model at high reasoning, then escalate only with evidence |
| Independent reviewer | a different capable model family at high reasoning when risk warrants it |

These defaults are recommendations, not permanent rankings. The skill must inspect the user's actual `Claude`, `Codex`, `Grok`, `agy`, local-model, or API inventory and accept corrections once. For Antigravity, it refreshes `agy models` and `agy agents`, keeps `--sandbox` on for bounded headless workers, and never uses `--dangerously-skip-permissions` as a shortcut.

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
.\install.ps1 -Grok
.\install.ps1 -Antigravity
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
|-- .grok/skills/<category>/<subcategory>/<skill-name>/SKILL.md
|-- .antigravity/skills/<category>/<subcategory>/<skill-name>/SKILL.md
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

The category folders are the browsing layer. `install.ps1` and `install.sh` intentionally flatten packages into the user runtime roots, so Claude, Codex, Grok, Antigravity, and shared agents continue to discover skills by package name.

For an approved selection, the agent creates a reviewable `.prats/selection.json` manifest and installs only those exact package names:

```powershell
.\install.ps1 -Manifest .\.prats\selection.json
```

## Catalog and maintenance

- [`catalog/skills.md`](catalog/skills.md): human-readable index of every package
- [`catalog/skills.json`](catalog/skills.json): machine-readable package metadata
- [`catalog/categories/`](catalog/categories/): focused pages for each category
- [`catalog/README.md`](catalog/README.md): category rules and source notes
- [`ONBOARDING.md`](ONBOARDING.md): the 12-question interview and selection contract

After adding or syncing packages:

```powershell
.\scripts\organize-runtime-trees.ps1
.\scripts\build-catalog.ps1
.\scripts\validate.ps1
```

The organizer applies deterministic name-based rules to new flat packages. The catalog records the actual category path. Validation checks all five runtime trees and every required `SKILL.md`.

## Motion, with a quiet fallback

The atlas artwork is built as inline-friendly SVG, not a screenshot. Orbit lines, signal pulses, and constellation points animate in browsers that support SVG motion. The moving layers are marked with `.motion` and disappear when `prefers-reduced-motion: reduce` is enabled. The labels and hierarchy remain readable in the still frame.

## Source and license notes

This is a local skill mirror and packaging project. Generated dependencies and machine-specific artifacts are intentionally excluded, including `node_modules`, `.venv`, Playwright browser binaries, `dist`, `.git`, bytecode, native binaries, and similar build output.

Individual skill packages may have their own authorship and license terms. Read [`NOTICE.md`](NOTICE.md) before redistributing or modifying a specific package.

## Make it yours

Fork the atlas, add your own skill constellation, regenerate the catalog, and keep the runtime roots clean. If you build a useful category or compatibility improvement, open a pull request with the validation output included.
