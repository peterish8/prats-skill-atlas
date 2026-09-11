# Skill Atlas onboarding protocol

This protocol is the small front door to a large collection. The repository contains hundreds of packages, but a new user should receive only the few that fit their work.

## Agent behavior

When Claude, Codex, or another agent sees this repository for the first time:

1. Explain that the atlas is a source library and that setup is selective.
2. Read the catalog index and inspect the user's project files, not every full skill document.
3. Ask the discovery interview below. Ask all 12 questions together unless the user asks for a guided interview.
4. Convert the answers into a proposed skill plan. Each recommendation must include its exact package name, runtime availability, category, and reason.
5. Keep the initial plan narrow: normally 5 to 15 packages, plus at most 3 optional packages.
6. Show an explicit **not selected** section for plausible packages that are being left out to avoid context and runtime bloat.
7. Ask for approval using a clear choice: `install selected`, `edit the plan`, or `install everything`.
8. Only after approval, write a selection manifest and run the selection installer.
9. Summarize the result and load the selected skill instructions for the user's active task.

The agent must never silently run `install.ps1 -All`, `install.sh all`, or copy all three runtime trees during onboarding. Full installation is an explicit user choice, not the default.

## Discovery interview

Ask these 12 questions. The user may answer with short phrases or `skip` where a question does not apply.

1. What are you building or maintaining, and what is the repository or product called?
2. What is your role on this work: founder, product, design, frontend, backend, full-stack, mobile, data, security, DevOps, or something else?
3. What is the current phase: exploring, planning, implementing, debugging, reviewing, hardening, shipping, or maintaining?
4. Which languages, frameworks, runtimes, and package managers are in use?
5. Which frontend surfaces matter: web, React, Next.js, CSS, browser automation, desktop UI, game UI, or none?
6. Which backend and data surfaces matter: APIs, databases, auth, serverless, realtime, queues, analytics, or none?
7. Are mobile or native targets in scope: Expo, React Native, iOS, SwiftUI, Kotlin, Android, macOS, or none?
8. Which delivery systems are in scope: GitHub, CI/CD, Docker, Cloudflare, Vercel, AWS, release signing, or other platforms?
9. Which quality risks matter most right now: tests, accessibility, performance, security, privacy, observability, or documentation?
10. Which external tools or integrations do you actually use: Figma, Canva, MCP, Google services, Notion, Supabase, Convex, Firecrawl, or other tools?
11. Which agent runtimes should be installed: Claude, Codex, shared Agents, or a specific combination? Where should the packages be installed?
12. What should never be installed, and what would make this setup successful after the first session?

## How to choose packages

Use the answers and project evidence in this order. For end-to-end acquisition, activation, monetization, retention, or experimentation work, consider `product-growth-experimentation` first and let it route only the focused product-growth skills that are actually needed:

Select `reverse-skill-router` only for authorized reverse engineering, CTF, offline-sample, malware-analysis, or defensive-security work. Tell the user that it is a guarded adapter to a separate upstream checkout: passive R0 and bounded-local R1 actions can proceed within the approved task, while R2 and R3 commands require a clear yes/no permission immediately before the exact command is run. Never install or execute the upstream toolchain merely because this adapter was selected.

1. Exact task fit. A skill must help with the work the user is doing now.
2. Stack fit. Prefer skills that name the user's language, framework, platform, or workflow.
3. Runtime fit. Prefer packages available in the user's selected runtime tree.
4. Coverage. Add one planning or architecture skill only when the task needs it, then the smallest implementation and verification set.
5. Cost control. Avoid duplicate skills, broad role bundles, and unrelated integrations.

For each candidate, inspect its frontmatter and then its full `SKILL.md` only if it remains a serious candidate. The catalog is the fast index; it is not a substitute for reading an approved skill before using it.

### Recommended first-pass shape

For a typical software project, start with:

- 1 project-context or planning skill
- 1 architecture or implementation skill
- 1 stack-specific skill
- 1 testing or verification skill
- 0 to 2 delivery, design, security, or integration skills driven by the interview

This is a heuristic, not a license to install generic bundles.

## Selection manifest

After the user approves a plan, create a JSON file such as `.prats/selection.json`. Keep it reviewable and save the user's answers so the setup can be audited or repeated:

```json
{
  "schemaVersion": 1,
  "atlas": "prats-skill-atlas",
  "profileName": "nextjs-product-build",
  "targets": ["Claude", "Codex"],
  "answers": {
    "projectType": "web product",
    "phase": "implementation",
    "stack": ["TypeScript", "Next.js"],
    "excluded": ["iOS", "game development"]
  },
  "skills": [
    {
      "name": "frontend-design",
      "reason": "Needed for the product's web interface",
      "targets": ["Claude"]
    },
    {
      "name": "frontend-app-builder",
      "reason": "Matches the Next.js implementation workflow",
      "targets": ["Codex"]
    }
  ]
}
```

The `skills` array accepts exact catalog names. The selection installer ignores unknown names with a clear report, skips a package when it is unavailable in a requested runtime tree, and never deletes unrelated global skills.

## Install the approved selection

Windows PowerShell:

```powershell
.\install.ps1 -Manifest .\.prats\selection.json
```

Unix-like systems:

```bash
./install.sh selection ./.prats/selection.json
```

Use dry-run mode when the user wants to inspect the result first:

```powershell
.\install.ps1 -Manifest .\.prats\selection.json -DryRun
```

## Completion report

The agent should finish onboarding with:

- the approved profile name and the answers that shaped it;
- selected package names grouped by runtime;
- installed, unavailable, and skipped counts;
- packages intentionally left out;
- the exact command used and the next verification step;
- a reminder that the selection can be expanded later without reinstalling everything.
