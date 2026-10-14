---
name: sync-agent-skills
description: Compare and synchronize global Claude Code and Codex skill catalogs. Use when asked to find missing skills between Claude and Codex or make both available across the two agents.
---

# Sync Claude and Codex skills

When this skill is invoked for a catalog comparison or sync, run the bundled helper with no arguments. It audits both catalogs and adds packages that are missing. The user does not need to approve this routine sync again.

The helper treats Claude's catalog as the skill folders under the Claude config directory. It treats Codex's effective catalog as the union of CODEX_HOME/skills and the shared .agents/skills folder, with CODEX_HOME taking precedence for duplicate names. It copies into a catalog only when that catalog cannot already load the skill.

The script preserves every existing skill folder and its local version. It never replaces or deletes existing files. It copies full missing skill packages, including scripts, references, and assets; it skips common installed runtime directories such as .venv, node_modules, and browser caches. If the same skill name has different SKILL.md content in both catalogs, it reports the difference and leaves both versions intact.

Run the helper from this skill's directory:

    python scripts/sync_skills.py

Use --dry-run when the user asks for a preview. Use --list with --dry-run when they ask which skill names would be added. The helper accepts --claude-root, --codex-root, and --agents-root for explicit catalog locations.

After a sync, report the before and after counts, which side received packages, any same-name SKILL.md differences that were preserved, and any runtime directories skipped. Do not describe skill names as synchronized if the final name sets do not match.

## Include an Atlas checkout when requested

When the user also requests synchronization with their Prats Skill Atlas repository, read that checkout's instructions and inspect its dirty state first. Run `python scripts/sync_atlas.py --atlas-root <checkout> --dry-run --report <private-report.json>` to preflight publication. This adds Atlas-only names to the local catalogs and missing local packages to the Atlas Claude/Codex trees, plus missing shared Agents packages. It preserves existing package variants. Preview reports do not change skill folders.

Then run the same command without `--dry-run` within the user's authorized scope. The helper excludes dependency caches, credentials, and generated output from public packages, checks secret-shaped strings, and verifies file hashes. Public documentation substitutes portable project-root placeholders for local paths. The Tactile source kit retains source assets and documents regeneration of excluded library builds.

The default local helper also has a Windows fallback when the host permits creating files but denies moving a staged directory. Neither helper overwrites an existing skill package.

After adding Atlas entries, run its organizer, catalog builder, and validator. Refresh README counts from the generated catalog. Review the task diff and report preserved same-name variants rather than claiming byte-identical catalogs. Publishing a commit or pushing requires the user's session authorization; requesting local sync alone does not authorize a public push. Never copy private reports or runtime payloads into the public repository.
