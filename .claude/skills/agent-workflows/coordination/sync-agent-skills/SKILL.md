---
name: sync-agent-skills
description: Quickly synchronize missing user-installed skills between Claude, Codex, shared Agents, and a Prats Skill Atlas checkout using bundled Python scripts. Use for sync skills, fast sync, catalog parity, or skills exclusive to one agent. Preserve existing versions and exclude bundled plugin/system catalogs.
---

# One-command skill sync

On invocation, execute the existing runner immediately. Do not rewrite a script, launch subagents, browse the web, or reinstall the collection. Routine local synchronization is authorized by the user's request.

From this skill's directory, run:

```sh
python scripts/run_sync.py
```

Use this skill's actual installation path as the command's working directory; it works from Claude, Codex, or shared Agents. Read the Atlas checkout's `AGENTS.md` before the first invocation in a session. This is collection maintenance, not first-time project onboarding.

## What the default command does

1. Locate Atlas using `--atlas-root`, `PRATS_SKILL_ATLAS`, a current-directory ancestor, `~/Documents/Codex/prats-skill-atlas`, or `~/prats-skill-atlas`, in that order. It never searches the whole drive, clones a repository, or contacts GitHub.
2. Inventory Claude user skills and Codex's effective union of direct Codex plus shared `.agents/skills`. Direct Codex wins for duplicate names. Respect `CLAUDE_CONFIG_DIR` and `CODEX_HOME`.
3. Preflight the missing packages, including public-export checks, before applying copies. Add Claude-only skills to Codex, Codex-only skills to Claude, Atlas-only names to missing local catalogs, and missing local packages to Atlas's Claude/Codex trees. Also export missing shared Agents packages to the Atlas Agents tree.
4. Preserve every existing package and same-name variant. Copy supporting scripts, references, assets and licenses; exclude caches, dependencies and generated output. Stop on publication-sensitive content instead of exposing it or weakening the checks.
5. Rebuild and validate stale Atlas metadata when needed, including its README count fields. Preserve unrelated working-tree edits. Already-synced runs skip category mapping and catalog rebuilds when metadata is current.
6. Verify final skill-name parity and save a private JSON report. Print before/after counts, additions, preserved variant count, and elapsed time.

Grok/Antigravity trees and bundled plugin/system skills are outside this Claude/Codex sync. Do not claim that every runtime has the same collection or that preserved versions are byte-identical.

## Optional modes

```sh
python scripts/run_sync.py --dry-run --list
python scripts/run_sync.py --atlas-root /path/to/prats-skill-atlas
python scripts/run_sync.py --local-only
python scripts/run_sync.py --refresh-catalog
```

Use preview only when requested; a normal invocation performs the sync. `--local-only` explicitly excludes Atlas. A missing or invalid Atlas checkout fails with configuration guidance rather than silently omitting it. The default private report is `LOCALAPPDATA/PratsSkillAtlas/last-sync.json`, or `~/.cache/PratsSkillAtlas/last-sync.json` when that variable is unavailable. Python 3.12+ is required; Atlas category/build steps require PowerShell 7 (`pwsh`).

`--claude-root`, `--codex-root`, `--agents-root`, and `--report` support explicit paths. Keep reports outside the public checkout. Supporting engines are [sync_atlas.py](scripts/sync_atlas.py) and [sync_skills.py](scripts/sync_skills.py); inspect them only for a concrete failure or requested change.

## Finish

Report sync status, counts added to each side, and the number of preserved variants in a few lines. Zero additions is a successful already-synced result. A nonzero exit means incomplete: diagnose the named failure, retain existing work, and never claim parity from a partial run.

The runner does not commit, push, deploy, modify this skill, or reconcile existing version differences. Perform separately requested Git publication only within the user's authorization and stage only relevant changes. Never include private reports, environment files, or unrelated website work in such a commit.
