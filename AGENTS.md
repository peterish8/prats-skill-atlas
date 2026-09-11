# Repository guidance

## Purpose

This repository packages global skills for Claude, Codex, and the shared agent catalog.

## Layout contract

- Keep `.claude/skills`, `.codex/skills`, and `.agents/skills` flat.
- A runtime skill is a direct child directory containing `SKILL.md`.
- Put organization and discovery metadata under `catalog/`; do not nest runtime skill directories into categories.
- Keep source-specific supporting files inside their skill package.

## Sync and safety

- Synchronization is copy-only. Never delete destination-only skills automatically.
- Exclude dependency/build artifacts such as `node_modules`, `.venv`, `ms-playwright`, `dist`, `.git`, bytecode, and native binaries.
- Run `scripts/build-catalog.ps1` and `scripts/validate.ps1` after changes.
- Scan for credentials before a public push.
- Preserve each package's local license and attribution files.
