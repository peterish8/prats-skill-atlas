# Prats Skill Forge

An organized, cloneable collection of global skills mirrored from Claude and Codex environments.

This repository keeps the three runtime-compatible trees intact:

```text
.claude/skills/<skill-name>/SKILL.md
.codex/skills/<skill-name>/SKILL.md
.agents/skills/<skill-name>/SKILL.md
```

The runtime trees stay flat because Claude and Codex discover skills directly under `skills/<skill-name>`. For browsing, the generated catalog groups every unique skill into practical categories such as frontend, backend, mobile, security, testing, design, documentation, integrations, and agent workflows.

## Install

Clone the repository, then run the installer for the roots you want:

### Windows PowerShell

```powershell
git clone https://github.com/<GITHUB_USER>/prats-skill-forge.git
cd prats-skill-forge
.\install.ps1 -All
```

You can install only one runtime tree:

```powershell
.\install.ps1 -Claude
.\install.ps1 -Codex
.\install.ps1 -Agents
```

### macOS/Linux/WSL

```bash
git clone https://github.com/<GITHUB_USER>/prats-skill-forge.git
cd prats-skill-forge
./install.sh all
```

The installers are copy-only: they create missing directories and overwrite same-named skill packages, but never delete unrelated local skills.

## Browse the catalog

- [`catalog/skills.md`](catalog/skills.md) — human-readable categorized index
- [`catalog/skills.json`](catalog/skills.json) — machine-readable index
- [`catalog/categories/`](catalog/categories/) — one focused page per category
- [`catalog/README.md`](catalog/README.md) — category and source rules

Regenerate the catalog after adding or removing skills:

```powershell
.\scripts\build-catalog.ps1
```

Validate all three runtime trees:

```powershell
.\scripts\validate.ps1
```

## Source policy

This is a local skill mirror and packaging project. Generated dependencies and machine-specific artifacts are intentionally excluded: `node_modules`, `.venv`, Playwright browser binaries, `dist`, `.git`, bytecode, native binaries, and similar build output. The skill instructions, source, scripts, references, and assets are retained where practical.

Individual skill packages may have their own authorship and license terms. See [`NOTICE.md`](NOTICE.md) before redistributing or modifying a specific package.

## Updating the mirror

1. Sync the three source trees into the matching repository trees.
2. Run `scripts/build-catalog.ps1`.
3. Run `scripts/validate.ps1`.
4. Review the diff and secret-scan results before pushing.

The repository intentionally does not delete destination-only skills during synchronization.
