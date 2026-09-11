# Prats Skill Atlas agent contract

This repository is an installable skill atlas, not a request to load every skill into the current context.

## Mandatory onboarding

When a user gives you this repository or asks you to set it up:

1. Read [`ONBOARDING.md`](ONBOARDING.md) and [`catalog/skills.json`](catalog/skills.json).
2. Inventory the user's project and inspect the catalog metadata before choosing skills.
3. Ask the 12 onboarding questions in `ONBOARDING.md` in one concise message. Do not install anything before the user answers and approves the selection plan.
4. Recommend a small set of skills by exact package name, with one reason per skill. Prefer 5 to 15 skills for a first pass.
5. Show what is intentionally not being installed. Never use `-All` for onboarding unless the user explicitly requests the full collection.
6. After approval, create a selection manifest and run `install.ps1 -Manifest <path>` on Windows or the documented equivalent on Unix-like systems.
7. Report selected, unavailable, skipped, and installed skills separately. Re-read only the selected `SKILL.md` files for the active task.

## Selection rules

- Use `catalog/skills.json` as the complete index of names, categories, runtime availability, and descriptions.
- Match skills to the user's project, stack, current phase, and requested task. Do not install a whole category just because one skill matched.
- Prefer a shared skill only when it exists in the requested runtime tree. If a Claude-only or Codex-only package is needed, say so explicitly.
- Treat user answers, repository evidence, and skill metadata as separate evidence. Mark uncertainty instead of guessing.
- Keep the user's existing global skills. The selection installer is additive and does not delete unrelated packages.

## Repository maintenance

Runtime packages live at `.claude/skills/<category>/<subcategory>/<skill>/SKILL.md`, `.codex/skills/...`, and `.agents/skills/...`. Run these after changing the collection:

```powershell
.\scripts\organize-runtime-trees.ps1
.\scripts\build-catalog.ps1
.\scripts\validate.ps1
```

Do not commit secrets, dependency caches, build output, or machine-specific paths. Preserve package-level attribution and license files.
