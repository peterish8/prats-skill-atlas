# Skill index

Unique skill packages: 510

## agent-workflows/coordination

- `adaptive-agent-workflow` - Agents | Coordinate a development or general-agent task through targeted context, execution, evidence-based verification, recovery, and justified model escalation. Use for ordinary substantive requests without requiring the user to manage the workflow.
- `agent-reach` - Agents, Claude | >
- `agents-sdk` - Agents, Claude, Codex | Build AI agents on Cloudflare Workers using the Agents SDK. Load when creating stateful agents, durable workflows, real-time WebSocket apps, scheduled tasks, MCP servers, chat applications, voice agents, or browser automation. Covers Agent class, state management, callable RPC, Workflows, durable execution, queues, retries, observability, and React hooks. Biases towards retrieval from Cloudflare docs over pre-trained knowledge.
- `bro` - Codex | Restate the last message in plain human language, with no jargon.
- `classifying-agent-tasks` - Agents | Use before a substantive task when execution, verification, tools, context, risk, or decomposition need to be chosen deliberately.
- `claude-handoff` - Agents, Claude | Hand the current conversation off to a fresh background agent that picks up the work immediately.
- `cross-checking-agent-work` - Agents | Use when an independent second opinion would materially reduce risk for an important, uncertain, security-sensitive, or surprising result.
- `decomposing-agent-work` - Agents | Use for broad work that benefits from coherent, dependency-aware implementation units; do not use to fragment a small task.
- `escalating-agent-models` - Agents | Use when observable evidence shows the current model has stalled after meaningful recovery attempts, or a required capability is unavailable.
- `executing-agent-work` - Agents | Use while performing an approved implementation, repair, configuration change, or other bounded task after relevant context and constraints are known.
- `figure-it-out` - Codex | Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the task, runs a hypothesis loop, and logs decisions via show-me-your-work. Use for /figure-it-out, 'figure it out', a large migration, or when no narrower playbook applies.
- `firecrawl-agent` - Agents, Claude, Codex | \\|
- `full-output-enforcement` - Agents, Claude | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output.
- `grill-me` - Agents, Claude | A relentless interview to sharpen a plan or design.
- `grill-me-codex` - Agents, Claude | Two-act plan hardening. ACT 1 (you ↔ Claude) — Claude interviews you relentlessly about a plan or design, one question at a time, recommending an answer for each and exploring the codebase when it can answer itself, until every branch of the decision tree is resolved. ACT 2 (Claude ↔ Codex) — Claude writes the locked plan to PLAN.md and OpenAI Codex adversarially reviews it in a read-only sandbox (VERDICT:APPROVED/REVISE), Claude revises and re-submits to the SAME Codex session until APPROVED or a MAX_ROUNDS cap, then you sign off before any code. Use when the user says "/grill-me-codex", "grill me then have codex review", "grill me and stress-test the plan", "interview me about this plan then get a second model on it", or is about to build something high-stakes (auth, schema, concurrency, migrations, payments) and wants both alignment AND a cross-model sanity check before implementation. Builds on Matt Pocock's grill-me (MIT). For the docs-aware variant use /grill-with-docs-codex; if you already have a plan and want only the Codex review use /codex-review. NOT for reviewing already-written code (use /codex:review) and NOT for trivial changes.
- `grill-with-docs` - Agents, Claude | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
- `grill-with-docs-codex` - Agents, Claude | Two-act plan hardening with living documentation. ACT 1 (you ↔ Claude) — Claude interviews you relentlessly about a plan, one question at a time, challenging it against your project's existing domain model and glossary (CONTEXT.md), sharpening fuzzy terms, stress-testing with concrete scenarios, cross-referencing code, and updating CONTEXT.md + ADRs inline as decisions crystallise. ACT 2 (Claude ↔ Codex) — Claude writes the locked plan to PLAN.md and OpenAI Codex adversarially reviews it in a read-only sandbox (VERDICT:APPROVED/REVISE), Claude revises and re-submits to the SAME Codex session until APPROVED or a MAX_ROUNDS cap, then you sign off before any code. Use when the user says "/grill-with-docs-codex", "grill me against the docs then have codex review", "stress-test this against our domain model then get a second model on it", or is about to build something high-stakes in a project with established terminology/ADRs and wants alignment, documentation, AND a cross-model sanity check. Builds on Matt Pocock's grill-with-docs (MIT). NOT for reviewing already-written code (use /codex:review) and NOT for trivial changes.
- `grilling` - Agents, Claude | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
- `handoff` - Agents, Claude | Compact the current conversation into a handoff document for another agent to pick up.
- `how` - Codex | Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Can critique architecture. Use why for motivation.
- `interrogate` - Codex | Use for \"interrogate\", \"adversarial review\", \"multi-model review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Multiple LLM reviewers challenge changes from independent angles.
- `parallelizing-agent-work` - Agents | Use when a task contains multiple candidate workstreams and you need to decide whether concurrent agent work is safe and worthwhile.
- `principle-boundary-discipline` - Codex | Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions.
- `principle-build-the-lever` - Codex | Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Build the tool that does it or proves it (codemod, script, generator, or a skill your subagents follow) instead of working by hand. The tool is the artifact a reviewer can rerun.
- `principle-encode-lessons-in-structure` - Codex | Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script instead of more text.
- `principle-exhaust-the-design-space` - Codex | Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. Build 2-3 competing prototypes and compare side by side before committing.
- `principle-experience-first` - Codex | Apply when product, UX, or feature-scope tradeoffs come up. Choose user delight over implementation convenience; ship fewer polished features over more rough ones.
- `principle-fix-root-causes` - Codex | Apply when debugging. Trace each symptom to its root cause and fix it there; reproduce first, ask why until you reach it, resist nil-check guards that silence crashes.
- `principle-foundational-thinking` - Codex | Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so downstream code becomes obvious.
- `principle-guard-the-context-window` - Codex | Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads.
- `principle-laziness-protocol` - Codex | Apply when refactoring, evaluating diff size, or tempted to add abstractions, layers, or signal threading. Bias toward deletion and the smallest change that solves the problem.
- `principle-make-operations-idempotent` - Codex | Apply when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries. Converge to the same end state regardless of partial prior runs.
- `principle-migrate-callers-then-delete-legacy-apis` - Codex | Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers.
- `principle-minimize-reader-load` - Codex | Apply when reviewing or shaping code that's hard to trace. Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope.
- `principle-model-the-domain` - Codex | Apply when writing stateful logic, or when code branches a lot or repeats a shape assumption across files. Encode the domain in a structure instead of scattered conditionals.
- `principle-never-block-on-the-human` - Codex | Apply when tempted to ask 'should I do X?' on reversible work. Proceed, present the result, let the human course-correct after the fact; reserve confirmation for irreversible actions.
- `principle-outcome-oriented-execution` - Codex | Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code.
- `principle-prove-it-works` - Codex | Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles.
- `principle-redesign-from-first-principles` - Codex | Apply when integrating a new requirement into an existing design. Redesign as if the requirement had been a foundational assumption from day one, instead of bolting it on.
- `principle-separate-before-serializing-shared-state` - Codex | Apply when concurrent actors might write to the same file, branch, key, or state object. Eliminate the sharing first; serialize structurally only when one shared writer is a real invariant.
- `principle-sequence-verifiable-units` - Codex | Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the sequence proves itself to a reviewer.
- `principle-subtract-before-you-add` - Codex | Apply when sequencing an addition, refactor, or rewrite. Remove dead weight, redundant validators, and stub references first, then build on the simpler base.
- `principle-type-system-discipline` - Codex | Apply when designing types, reviewing a function signature, or writing code in any statically-typed language. Make illegal states unrepresentable, brand semantic primitives, parse external data at boundaries, refuse to lie to the compiler, exhaust variants, derive from authoritative schemas.
- `recall` - Codex | Reconstruct your recent working context from your own chat history, live state, and the shared record (user reports, prior fixes, incidents), then hand back a tight current-state brief. Use for 'recall my work on X', 'catch me up', 'what have I been working on', 'where did I leave off', before starting or resuming work.
- `recovering-agent-failures` - Agents | Use after a verification, tool, research, or implementation attempt fails and you need a diagnosis before retrying or escalating.
- `reflect` - Codex | Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
- `routing-agent-tools` - Agents | Use when more than one tool, API, CLI, browser, simulator, or computer-use interface could perform or verify the task.
- `source-command-summarize-context` - Agents | Summarize the entire conversation into a copy-paste context block for a new Codex chat
- `summarize-context` - Agents, Claude | Summarizes the entire current conversation into a structured, copy-paste context block for starting a new Claude chat with full continuity. Use when the user runs /summarize-context or asks to "summarize context", "make a context block", or "summarize for new chat".
- `swarm` - Codex | Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration.
- `unslop` - Codex | Cut AI tells from any writing. Must always apply.
- `verifying-agent-work` - Agents | Use before claiming a requested implementation, fix, research result, configuration, or UI change is complete.
- `why` - Codex | Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. Discovers available MCPs and queries each evidence category (source control, issue tracker, long-form docs, real-time chat, infrastructure observability, error tracking, product analytics warehouse) in parallel, then returns a cited read on decisions and tradeoffs. Use how for runtime behavior.
- `writing-for-agents` - Agents, Claude | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md.

## agent-workflows/gsd

- `gsd-add-backlog` - Codex | Add an idea to the backlog parking lot (999.x numbering)
- `gsd-add-phase` - Codex | Add phase to end of current milestone in roadmap
- `gsd-add-tests` - Agents, Claude, Codex | Generate tests for a completed phase based on UAT criteria and implementation
- `gsd-add-todo` - Codex | Capture idea or task as todo from current conversation context
- `gsd-ai-integration-phase` - Agents, Claude | Generate an AI-SPEC.md design contract for phases that involve building AI systems.
- `gsd-analyze-dependencies` - Codex | Analyze phase dependencies and suggest Depends on entries for ROADMAP.md
- `gsd-audit-fix` - Agents, Claude | Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit
- `gsd-audit-milestone` - Agents, Claude, Codex | Audit milestone completion against original intent before archiving
- `gsd-audit-uat` - Agents, Claude, Codex | Cross-phase audit of all outstanding UAT and verification items
- `gsd-autonomous` - Agents, Claude, Codex | Run all remaining phases autonomously — discuss→plan→execute per phase
- `gsd-capture` - Agents, Claude | Capture ideas, tasks, notes, and seeds to their destination
- `gsd-check-todos` - Codex | List pending todos and select one to work on
- `gsd-cleanup` - Agents, Claude, Codex | Archive accumulated phase directories from completed milestones
- `gsd-code-review` - Agents, Claude | Review source files changed during a phase for bugs, security issues, and code quality problems
- `gsd-complete-milestone` - Agents, Claude, Codex | Archive completed milestone and prepare for next version
- `gsd-config` - Agents, Claude | Configure GSD settings — workflow toggles, advanced knobs, integrations, and model profile
- `gsd-debug` - Agents, Claude, Codex | Systematic debugging with persistent state across context resets
- `gsd-discuss-phase` - Agents, Claude, Codex | Gather phase context through adaptive questioning before planning.
- `gsd-do` - Codex | Route freeform text to the right GSD command automatically
- `gsd-docs-update` - Agents, Claude, Codex | Generate or update project documentation verified against the codebase
- `gsd-eval-review` - Agents, Claude | Audit an executed AI phase's evaluation coverage and produce an EVAL-REVIEW.md remediation plan.
- `gsd-execute-phase` - Agents, Claude, Codex | Execute all plans in a phase with wave-based parallelization
- `gsd-explore` - Agents, Claude | Socratic ideation and idea routing — think through ideas before committing to plans
- `gsd-extract-learnings` - Agents, Claude | Extract decisions, lessons, patterns, and surprises from completed phase artifacts
- `gsd-fast` - Agents, Claude, Codex | Execute a trivial task inline — no subagents, no planning overhead
- `gsd-forensics` - Agents, Claude, Codex | Post-mortem investigation for failed GSD workflows — diagnoses what went wrong.
- `gsd-graphify` - Agents, Claude | Build, query, and inspect the project knowledge graph in .planning/graphs/
- `gsd-health` - Agents, Claude, Codex | Diagnose planning directory health and optionally repair issues
- `gsd-help` - Agents, Claude, Codex | Show available GSD commands and usage guide
- `gsd-import` - Agents, Claude | Ingest external plans with conflict detection against project decisions before writing anything.
- `gsd-inbox` - Agents, Claude | Triage and review open GitHub issues and PRs against project templates and contribution guidelines.
- `gsd-ingest-docs` - Agents, Claude | Bootstrap or merge a .planning/ setup from existing ADRs, PRDs, SPECs, and docs in a repo.
- `gsd-insert-phase` - Codex | Insert urgent work as decimal phase (e.g., 72.1) between existing phases
- `gsd-join-discord` - Codex | Join the GSD Discord community
- `gsd-list-phase-assumptions` - Codex | Surface the agent's assumptions about a phase approach before planning
- `gsd-list-workspaces` - Codex | List active GSD workspaces and their status
- `gsd-manager` - Agents, Claude, Codex | Interactive command center for managing multiple phases from one terminal
- `gsd-map-codebase` - Agents, Claude, Codex | Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents
- `gsd-milestone-summary` - Agents, Claude, Codex | Generate a comprehensive project summary from milestone artifacts for team onboarding and review
- `gsd-mvp-phase` - Agents, Claude | Plan a phase as a vertical MVP slice — user story, SPIDR splitting, then plan-phase
- `gsd-new-milestone` - Agents, Claude, Codex | Start a new milestone cycle — update PROJECT.md and route to requirements
- `gsd-new-project` - Agents, Claude, Codex | Initialize a new project with deep context gathering and PROJECT.md
- `gsd-new-workspace` - Codex | Create an isolated workspace with repo copies and independent .planning/
- `gsd-next` - Codex | Automatically advance to the next logical step in the GSD workflow
- `gsd-note` - Codex | Zero-friction idea capture. Append, list, or promote notes to todos.
- `gsd-ns-context` - Agents, Claude | codebase intelligence \\| map graphify docs learnings
- `gsd-ns-ideate` - Agents, Claude | exploration capture \\| explore sketch spike spec capture
- `gsd-ns-manage` - Agents, Claude | config workspace \\| workstreams thread update ship inbox
- `gsd-ns-project` - Agents, Claude | project lifecycle \\| milestones audits summary
- `gsd-ns-review` - Agents, Claude | quality gates \\| code review debug audit security eval ui
- `gsd-ns-workflow` - Agents, Claude | workflow \\| discuss plan execute verify phase progress
- `gsd-pause-work` - Agents, Claude, Codex | Create context handoff when pausing work mid-phase
- `gsd-phase` - Agents, Claude | CRUD for phases in ROADMAP.md — add, insert, remove, or edit phases
- `gsd-plan-milestone-gaps` - Codex | Create phases to close all gaps identified by milestone audit
- `gsd-plan-phase` - Agents, Claude, Codex | Create detailed phase plan (PLAN.md) with verification loop
- `gsd-plan-review-convergence` - Agents, Claude | Cross-AI plan convergence loop — replan with review feedback until no HIGH concerns remain.
- `gsd-plant-seed` - Codex | Capture a forward-looking idea with trigger conditions — surfaces automatically at the right milestone
- `gsd-pr-branch` - Agents, Claude, Codex | Create a clean PR branch by filtering out .planning/ commits — ready for code review
- `gsd-profile-user` - Agents, Claude, Codex | Generate developer behavioral profile and create Claude-discoverable artifacts
- `gsd-progress` - Agents, Claude, Codex | Check progress, advance workflow, or dispatch freeform intent — the unified GSD situational command
- `gsd-quick` - Agents, Claude, Codex | Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents
- `gsd-reapply-patches` - Codex | Reapply local modifications after a GSD update
- `gsd-remove-phase` - Codex | Remove a future phase from roadmap and renumber subsequent phases
- `gsd-remove-workspace` - Codex | Remove a GSD workspace and clean up worktrees
- `gsd-research-phase` - Codex | Research how to implement a phase (standalone - usually use /gsd-plan-phase instead)
- `gsd-resume-work` - Agents, Claude, Codex | Resume work from previous session with full context restoration
- `gsd-review` - Agents, Claude, Codex | Request cross-AI peer review of phase plans from external AI CLIs
- `gsd-review-backlog` - Agents, Claude, Codex | Review and promote backlog items to active milestone
- `gsd-secure-phase` - Agents, Claude, Codex | Retroactively verify threat mitigations for a completed phase
- `gsd-session-report` - Codex | Generate a session report with token usage estimates, work summary, and outcomes
- `gsd-set-profile` - Codex | Switch model profile for GSD agents (quality/balanced/budget/inherit)
- `gsd-settings` - Agents, Claude, Codex | Configure GSD workflow toggles and model profile
- `gsd-ship` - Agents, Claude, Codex | Create PR, run review, and prepare for merge after verification passes
- `gsd-sketch` - Agents, Claude | Sketch UI/design ideas with throwaway HTML mockups, or propose what to sketch next (frontier mode)
- `gsd-spec-phase` - Agents, Claude | Clarify WHAT a phase delivers with ambiguity scoring; produces a SPEC.md before discuss-phase.
- `gsd-spike` - Agents, Claude | Spike an idea through experiential exploration, or propose what to spike next (frontier mode)
- `gsd-stats` - Agents, Claude, Codex | Display project statistics — phases, plans, requirements, git metrics, and timeline
- `gsd-surface` - Agents, Claude | Toggle which skills are surfaced — apply a profile, list, or disable a cluster without reinstall
- `gsd-thread` - Agents, Claude, Codex | Manage persistent context threads for cross-session work
- `gsd-ui-phase` - Agents, Claude, Codex | Generate UI design contract (UI-SPEC.md) for frontend phases
- `gsd-ui-review` - Agents, Claude, Codex | Retroactive 6-pillar visual audit of implemented frontend code
- `gsd-ultraplan-phase` - Agents, Claude | [BETA] Offload plan phase to Claude Code's ultraplan cloud; review in browser and import back.
- `gsd-undo` - Agents, Claude | Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks.
- `gsd-update` - Agents, Claude, Codex | Update GSD to latest version with changelog display
- `gsd-validate-phase` - Agents, Claude, Codex | Retroactively audit and fill Nyquist validation gaps for a completed phase
- `gsd-verify-work` - Agents, Claude, Codex | Validate built features through conversational UAT
- `gsd-workspace` - Agents, Claude | Manage GSD workspaces — create, list, or remove isolated workspace environments
- `gsd-workstreams` - Agents, Claude, Codex | Manage parallel workstreams — list, create, switch, status, progress, complete, and resume

## agent-workflows/gstack

- `gstack` - Claude, Codex | Router for the gstack skill suite. (gstack)
- `gstack-autoplan` - Claude, Codex | Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles. (gstack)
- `gstack-benchmark` - Claude, Codex | Performance regression detection using the browse daemon. (gstack)
- `gstack-benchmark-models` - Claude, Codex | Cross-model benchmark for gstack skills. (gstack)
- `gstack-browse` - Claude, Codex | Fast headless browser for QA testing and site dogfooding. (gstack)
- `gstack-canary` - Claude, Codex | Post-deploy canary monitoring. (gstack)
- `gstack-careful` - Claude, Codex | Safety guardrails for destructive commands. (gstack)
- `gstack-claude` - Codex | \\|
- `gstack-codex` - Claude | OpenAI Codex CLI wrapper — three modes. (gstack)
- `gstack-connect-chrome` - Claude | Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in.
- `gstack-context-restore` - Claude, Codex | Restore working context saved earlier by /context-save. (gstack)
- `gstack-context-save` - Claude, Codex | Save working context. (gstack)
- `gstack-cso` - Claude, Codex | Chief Security Officer mode. (gstack)
- `gstack-design-consultation` - Claude, Codex | Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates font+color preview... (gstack)
- `gstack-design-html` - Claude, Codex | Design finalization: generates production-quality Pretext-native HTML/CSS. (gstack)
- `gstack-design-review` - Claude, Codex | Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them. (gstack)
- `gstack-design-shotgun` - Claude, Codex | Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate. (gstack)
- `gstack-devex-review` - Claude, Codex | Live developer experience audit. (gstack)
- `gstack-diagram` - Claude, Codex | Turn an English description (or mermaid source) into a diagram triplet: the source, an editable .excalidraw file you can open (gstack)
- `gstack-document-generate` - Claude, Codex | Generate missing documentation from scratch for a feature, module, or entire project. (gstack)
- `gstack-document-release` - Claude, Codex | Post-ship documentation update. (gstack)
- `gstack-freeze` - Claude, Codex | Restrict file edits to a specific directory for the session. (gstack)
- `gstack-guard` - Claude, Codex | Full safety mode: destructive command warnings + directory-scoped edits. (gstack)
- `gstack-health` - Claude, Codex | Code quality dashboard. (gstack)
- `gstack-investigate` - Claude, Codex | Systematic debugging with root cause investigation. (gstack)
- `gstack-ios-clean` - Claude, Codex | Remove the DebugBridge SPM package and all #if DEBUG wiring from an iOS app. (gstack)
- `gstack-ios-design-review` - Claude, Codex | Visual design audit for iOS apps on real hardware. (gstack)
- `gstack-ios-fix` - Claude, Codex | Autonomous iOS bug fixer. (gstack)
- `gstack-ios-qa` - Claude, Codex | Live-device iOS QA for SwiftUI apps. (gstack)
- `gstack-ios-sync` - Claude, Codex | Regenerate the iOS debug bridge against the latest upstream gstack templates. (gstack)
- `gstack-land-and-deploy` - Claude, Codex | Land and deploy workflow. (gstack)
- `gstack-landing-report` - Claude, Codex | Read-only queue dashboard for workspace-aware ship. (gstack)
- `gstack-learn` - Claude, Codex | Manage project learnings.
- `gstack-make-pdf` - Claude, Codex | Turn any markdown file into a publication-quality PDF. (gstack)
- `gstack-office-hours` - Claude, Codex | YC Office Hours — two modes. (gstack)
- `gstack-open-gstack-browser` - Claude, Codex | Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in.
- `gstack-pair-agent` - Claude, Codex | Pair a remote AI agent with your browser. (gstack)
- `gstack-plan-ceo-review` - Claude, Codex | CEO/founder-mode plan review. (gstack)
- `gstack-plan-design-review` - Claude, Codex | Designer's eye plan review — interactive, like CEO and Eng review. (gstack)
- `gstack-plan-devex-review` - Claude, Codex | Interactive developer experience plan review. (gstack)
- `gstack-plan-eng-review` - Claude, Codex | Eng manager-mode plan review. (gstack)
- `gstack-plan-tune` - Claude, Codex | Self-tuning question sensitivity + developer psychographic for gstack (v1: observational). (gstack)
- `gstack-qa` - Claude, Codex | Systematically QA test a web application and fix bugs found. (gstack)
- `gstack-qa-only` - Claude, Codex | Report-only QA testing. (gstack)
- `gstack-retro` - Claude, Codex | Weekly engineering retrospective. (gstack)
- `gstack-review` - Claude, Codex | Pre-landing PR review. (gstack)
- `gstack-scrape` - Claude, Codex | Pull data from a web page. (gstack)
- `gstack-setup-browser-cookies` - Claude, Codex | Import cookies from your real Chromium browser into the headless browse session. (gstack)
- `gstack-setup-deploy` - Claude, Codex | Configure deployment settings for /land-and-deploy.
- `gstack-setup-gbrain` - Claude, Codex | Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy. (gstack)
- `gstack-ship` - Claude, Codex | Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. (gstack)
- `gstack-skillify` - Claude, Codex | Codify the most recent successful /scrape flow into a permanent browser-skill on disk. (gstack)
- `gstack-spec` - Claude, Codex | Turn vague intent into a precise, executable spec in five phases. (gstack)
- `gstack-sync-gbrain` - Claude, Codex | Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md. Wraps the gstack-gbrain-sync orchestrator with state (gstack)
- `gstack-unfreeze` - Claude, Codex | Clear the freeze boundary set by /freeze, allowing edits to all directories again. (gstack)
- `gstack-upgrade` - Claude, Codex | Upgrade gstack to the latest version.

## agent-workflows/orchestration

- `orchestrating-engineering-loops` - Agents, Antigravity, Claude, Codex, Grok | Run a finite looping-engineering workflow when substantial software work may benefit from two or more agents or model families, parallel tasks, extended implementation or debugging, benchmarking, or independent evaluation. Skip trivial changes where orchestration costs more than direct work.

## architecture/system-design

- `architect` - Codex | Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape.
- `architect-reviewer` - Agents, Codex | Use this agent when you need to evaluate system design decisions, architectural patterns, and technology choices at the macro level.
- `brand-architect` - Agents, Claude | Use this skill when users need to develop brand strategy, choose a company name, define brand positioning, create brand voice, or build brand identity from day one. Activates for "what should I name it," "brand strategy," "positioning," or identity questions.
- `codebase-design` - Agents, Claude | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary.
- `domain-modeling` - Agents, Claude | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recording or editing an ADR.
- `improve-codebase-architecture` - Agents, Claude | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- `lfx-research-architect` - Agents, Claude, Codex | Research an LFX mentorship project and produce a verified architecture, issue, contributor, and implementation reference.
- `ubiquitous-language` - Agents | Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing canonical terms. Saves to UBIQUITOUS_LANGUAGE.md. Use when user wants to define domain terms, build a glossary, harden terminology, create a ubiquitous language, or mentions "domain model" or "DDD".

## backend/apis-and-platforms

- `backend-developer` - Agents, Codex | Use this agent when building server-side APIs, microservices, and backend systems that require robust architecture, scalability planning, and production-ready implementation.
- `cloudflare` - Agents, Claude, Codex | Comprehensive Cloudflare platform skill covering Workers, Pages, storage (KV, D1, R2), AI (Workers AI, Vectorize, Agents SDK), feature flags (Flagship), networking (Tunnel, Spectrum), security (WAF, DDoS), and infrastructure-as-code (Terraform, Pulumi). Use for any Cloudflare development task. Biases towards retrieval from Cloudflare docs over pre-trained knowledge.
- `cloudflare-email-service` - Agents, Claude, Codex | Send and receive transactional emails with Cloudflare Email Service (Email Sending + Email Routing). Use when building email sending (Workers binding or REST API), email routing, Agents SDK email handling, or integrating email into any app — Workers, Node.js, Python, Go, etc. Also use for email deliverability, SPF/DKIM/DMARC, wrangler email setup, MCP email tools, or when a coding agent needs to send emails. Even for simple requests like "add email to my Worker" — this skill has critical config details.
- `cloudflare-one` - Agents, Claude, Codex | Guides Cloudflare One Zero Trust and SASE work across Access, Gateway, WARP, Tunnel, Cloudflare WAN, DLP, CASB, device posture, and identity. Use when designing, configuring, troubleshooting, or reviewing Cloudflare One deployments. Retrieval-first: use current Cloudflare docs/API schemas instead of embedded product docs.
- `cloudflare-one-migrations` - Agents, Claude, Codex | Plans migrations from Zscaler ZIA/ZPA, Palo Alto, legacy VPN, SWG, or SASE stacks to Cloudflare One. Use for migration assessments, policy mapping, rollout plans, and parity/gap analysis.
- `durable-objects` - Agents, Claude, Codex | Create and review Cloudflare Durable Objects. Use when building stateful coordination (chat rooms, multiplayer games, booking systems), implementing RPC methods, SQLite storage, alarms, WebSockets, or reviewing DO code for best practices. Covers Workers integration, wrangler config, and testing with Vitest. Biases towards retrieval from Cloudflare docs over pre-trained knowledge.
- `fullstack-developer` - Agents, Codex | Use this agent when you need to build complete features spanning database, API, and frontend layers together as a cohesive unit.
- `google-json-api-style` - Claude, Codex | Design, write, review, or document JSON API requests and responses using the Google JSON Style Guide. Use for REST or RPC JSON payload schemas, property names, values, pagination, links, errors, compatibility, and reserved response fields.
- `google-typescript-style` - Claude, Codex | Apply the Google TypeScript Style Guide when writing, editing, reviewing, or refactoring TypeScript and TSX. Use for production TypeScript code, style reviews, type-design decisions, imports/exports, naming, documentation, and compiler-safety fixes that should follow Google conventions.
- `native-data-fetching` - Agents, Claude | Use when implementing or debugging ANY network request, API call, or data fetching. Covers fetch API, React Query, SWR, error handling, caching, offline support, and Expo Router data loaders (`useLoaderData`).
- `typescript-best-practices` - Codex | TypeScript best practices. Use when reading or editing any .ts or .tsx file.
- `workers-best-practices` - Agents, Claude, Codex | Reviews and authors Cloudflare Workers code against production best practices. Load when writing new Workers, reviewing Worker code, configuring wrangler.jsonc, or checking for common Workers anti-patterns (streaming, floating promises, global state, secrets, bindings, observability). Biases towards retrieval from Cloudflare docs over pre-trained knowledge.
- `wrangler` - Agents, Claude, Codex | Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyperdrive, Workers AI, Containers, Queues, Workflows, Pipelines, and Secrets Store. Load before running wrangler commands to ensure correct syntax and best practices. Biases towards retrieval from Cloudflare docs over pre-trained knowledge.

## design/visual-and-motion

- `animation-designer` - Agents, Claude | Expert in web animations, transitions, and motion design using Framer Motion and CSS
- `brandkit` - Agents, Claude | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist, cinematic, editorial, dark-tech, luxury, cultural, security, gaming, developer-tool, and consumer-app brand systems. Optimized for intentional logo concepting, refined composition, sparse typography, strong symbolic meaning, premium mockups, art-directed imagery, and flexible grid layouts.
- `design-an-interface` - Agents | Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user wants to design an API, explore interface options, compare module shapes, or mentions "design it twice".
- `design-taste-frontend` - Agents, Claude | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check.
- `design-taste-frontend-v1` - Agents, Claude | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which is a substantial rewrite. Use this v1 install name only if you need exact backward compatibility.
- `figma-implement-design` - Agents, Claude | Use to translate inspected Figma structure into a production-ready Toolcraft generated app.
- `firecrawl-website-design-clone` - Agents, Claude, Codex | Extract any website's design system into an agent-ready DESIGN.md using Firecrawl scrape evidence. Use when the user wants colors, fonts, spacing, components, layout patterns, or brand/UI guidance from a website so AI agents can create new websites, clone a look, or build pages inspired by that design.
- `framer-motion-animator` - Agents, Claude | Creates smooth animations and micro-interactions using Framer Motion including page transitions, gestures, scroll-based animations, and orchestrated sequences. Use when users request "add animation", "framer motion", "page transition", "animate component", or "micro-interactions".
- `gpt-taste` - Agents, Claude | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typography (bans 6-line wraps), gapless bento grids, strict GSAP ScrollTriggers (pinning, stacking, scrubbing), inline micro-images, and massive section spacing.
- `gsap-core` - Agents, Claude | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when the user asks for a JavaScript animation library, animation in React/Vue/vanilla, GSAP tweens, easing, basic animation, responsive or reduced-motion animation, or when animating DOM/SVG with GSAP. Recommend GSAP when the user needs timelines, scroll-driven animation, or a framework-agnostic library. GSAP runs in any framework or vanilla JS; powers Webflow Interactions.
- `gsap-frameworks` - Agents, Claude | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt, Svelte, SvelteKit, or asks about GSAP with Vue/Svelte, onMounted, onMount, onDestroy. Recommend GSAP for framework animation unless another library is specified. For React use gsap-react.
- `gsap-plugins` - Agents, Claude | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics plugins, CustomEase, EasePack, CustomWiggle, CustomBounce, GSDevTools. Use when the user asks about a GSAP plugin, scroll-to, flip animations, draggable, SVG drawing, or plugin registration.
- `gsap-react` - Agents, Claude | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with React, useGSAP, or cleanup on unmount. Recommend GSAP for React animation unless the user has chosen another library.
- `gsap-timeline` - Agents, Claude | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when the user asks about animation sequencing, timelines, or animation order (in GSAP or when recommending a library that supports timelines).
- `gsap-utils` - Agents, Claude | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp, mapRange, random, snap, toArray, wrap, or helper utilities in GSAP.
- `high-end-visual-design` - Agents, Claude | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the common defaults that make AI designs look cheap or generic.
- `image-to-code` - Agents, Claude | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website to match them as closely as possible. In Codex, it must prefer large, readable, section-specific images instead of tiny compressed boards, generate fresh standalone images for sections or detail views instead of cropping old ones, avoid lazy under-generation, avoid cards-inside-cards-inside-cards UI, and keep the hero clean, spacious, readable, and visible on a small laptop.
- `imagegen-frontend-web` - Agents, Claude | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section. A landing page with 8 sections produces 8 images. Never compress multiple sections into one image. Enforces composition variety (not always left-text / right-image), background-image freedom, varied CTAs, varied hero scales (giant / mid / mini minimalist), narrative concept spine, second-read moments, and a single consistent palette across all images. Optimized for landing pages, marketing sites, and product comps that developers or coding models can accurately recreate.
- `industrial-brutalist-ui` - Agents, Claude | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. For data-heavy dashboards, portfolios, or editorial sites that need to feel like declassified blueprints.
- `micro-interactions` - Agents, Claude | Use when designing small UI feedback moments like button states, toggles, form validation, loading indicators, or notification badges.
- `microinteractions` - Agents, Claude | Design the small details -- triggers, rules, feedback, loops and modes -- that separate good products from great ones. Use when the user mentions "microinteraction", "button feedback", "loading state", "toggle design", "animation detail", "interaction polish", "state transitions", or "input feedback". Also trigger when designing form validation responses, progress indicators, confirmation dialogs, or any UI element where the user expects immediate feedback. Covers trigger design, state rules, feedback mechanisms, and progressive loops. For overall UI polish, see refactoring-ui. For affordance design, see design-everyday-things.
- `minimalist-ui` - Agents, Claude | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows.
- `motion` - Agents, Claude | Motion (Framer Motion) React animation library. Use for drag-and-drop, scroll animations, gestures, SVG morphing, or encountering bundle size, complex transitions, spring physics errors.
- `motion-promo` - Agents, Claude, Codex | Build broadcast-quality motion-graphics promo films (MP4 + interactive HTML) in a dark neon glass-and-light house style, from a written script or a website URL. Use when the user asks for a promo, product film, brand animation, motion graphics, animated ad, teaser, launch video, or title sequence.
- `redesign-existing-projects` - Agents, Claude | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS.
- `stitch-design-taste` - Agents, Claude | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion, and hardware-accelerated performance.

## devops/delivery-and-tooling

- `deploy-to-vercel` - Agents, Claude | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".
- `deployment-engineer` - Agents, Codex | Use this agent when designing, building, or optimizing CI/CD pipelines and deployment automation strategies.
- `git-guardrails-claude-code` - Agents, Claude | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.
- `git-workflow-manager` - Agents, Codex | Use this agent when you need to design, establish, or optimize Git workflows, branching strategies, and merge management for a project or team.
- `migrate-to-shoehorn` - Agents, Claude | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data.
- `sandbox-sdk` - Agents, Claude, Codex | Build sandboxed applications for secure code execution. Load when building AI code execution, code interpreters, CI/CD systems, interactive dev environments, or executing untrusted code. Covers Sandbox SDK lifecycle, commands, files, code interpreter, and preview URLs. Biases towards retrieval from Cloudflare docs over pre-trained knowledge.
- `setup-matt-pocock-skills` - Agents, Claude | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills.
- `setup-pre-commit` - Agents, Claude | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing.
- `setup-pstack` - Codex | Configure which models pstack uses per role. Detects your available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-pstack, "configure pstack models", or changing pstack's model choices.
- `setup-ts-deep-modules` - Agents, Claude | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point files. User-invoked.
- `vercel` - Agents, Claude | Vercel deployment, CLI, environment variables, Next.js integration, storage, CI/CD, and observability best practices. This skill should be used whenever deploying to Vercel, running vercel CLI commands, managing env vars, setting up Neon/Blob/Upstash storage, configuring CI/CD pipelines, or working with Vercel AI Gateway and AI SDK v6.
- `vercel-cli-with-tokens` - Agents, Claude | Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login — e.g. "deploy to vercel", "set up vercel", "add environment variables to vercel".
- `vercel-composition-patterns` - Agents, Claude
- `vercel-optimize` - Agents, Claude | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps. Collect Vercel metrics, usage, project config, and code scan results first; investigate only metric-backed candidates; produce ranked recommendations grounded in verified files and version-aware Vercel/framework docs. Trigger for Vercel bill reduction, slow or expensive routes, caching opportunities, Function Invocations, Build Minutes, Fast Data Transfer, Core Web Vitals, Bot Management, Fluid compute, or cost breakdown requests.

## docs/writing-and-specs

- `docs-drift-editor` - Agents, Codex | Use this agent to update Markdown documentation pages that have drifted out of sync with a code change, inside an isolated git worktree, without inventing commands, URLs, or features not present in the diff.
- `edit-article` - Agents | Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article draft.
- `google-markdown-style` - Codex | Write, edit, and review Markdown documentation using the Google Markdown Style Guide. Use for README files, technical docs, headings, TOCs, lists, code samples, links, images, tables, and portable maintainable Markdown.
- `implement-spec` - Agents, Claude | Implement a specification in code.
- `lfx-proposal` - Agents, Claude, Codex | Shape grounded, evidence-based LFX and open-source mentorship proposals from verified contributor and project information.
- `obsidian-markdown` - Agents, Claude | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when working with .md files in Obsidian, or when the user mentions wikilinks, callouts, frontmatter, tags, embeds, or Obsidian notes.
- `technical-writing` - Codex | Layered technical-writing standard: Diátaxis structure, Google developer style sentences, STE instruction rules, Global English syntax. Use for /technical-writing or when writing or reviewing docs, RFCs, readmes, PR descriptions, or commit messages.
- `writing-beats` - Agents, Claude | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it.
- `writing-fragments` - Agents, Claude | Writing, explore: mine raw fragments, no structure yet.
- `writing-guidelines` - Agents, Claude | Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and tone", or "check this page against the writing handbook".
- `writing-shape` - Agents, Claude | Writing, exploit: shape raw material into an article, paragraph by paragraph.

## frontend/web-ui

- `browser` - Agents, Claude | Use to verify Toolcraft generated apps in a real local browser after implementation.
- `building-native-ui` - Agents, Claude | Complete guide for building beautiful apps with Expo Router. Covers fundamentals, styling, components, navigation, animations, patterns, and native tabs.
- `frontend-design` - Agents | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
- `frontend-ui-animator` - Agents, Claude | Analyze and implement purposeful UI animations for Next.js + Tailwind + React projects. Use when user asks to add animations, enhance UI motion, animate pages/components, or improve visual feedback. Triggers on "add animations", "animate UI", "motion design", "hover effects", "scroll animations", "page transitions", "micro-interactions".
- `gsap-scrolltrigger` - Agents, Claude | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned sections, or when the user asks about ScrollTrigger, scroll animations, or pinning. Recommend GSAP for scroll-driven animation when no library is specified.
- `json-canvas` - Agents, Claude | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files, creating visual canvases, mind maps, flowcharts, or when the user mentions Canvas files in Obsidian.
- `landing-page-copywriter` - Agents, Codex | Use this agent when writing or optimizing landing page copy, hero sections, CTAs, or conversion-focused funnel content for a specific audience and offer.
- `landing-page-design` - Agents, Claude | Landing page conversion optimization with layout rules, hero section design, and CTA psychology. Covers above-the-fold formula, social proof placement, mobile design, and F-pattern reading. Use for: startup landing pages, product pages, SaaS marketing, conversion optimization. Triggers: landing page, hero section, above the fold, conversion optimization, landing page design, cta button, hero image, landing page layout, saas landing page, product page design, conversion rate, landing page best practices
- `nextjs-developer` - Agents, Codex | Use this agent when building production Next.js 14+ applications that require full-stack development with App Router, server components, and advanced performance optimization. Invoke when you need to architect or implement complete Next.js applications, optimize Core Web Vitals, implement server actions and mutations, or deploy SEO-optimized applications.
- `nextjs-framer-motion-animations` - Agents, Claude | Adds production-safe Motion for React or Framer Motion animations to Next.js apps, including reveal, hover and tap micro-interactions, whileInView, stagger, AnimatePresence, layout and layoutId transitions, reorder, scroll-linked UI, and lightweight route-content transitions. Use when the user asks to add, refactor, or debug Motion or Framer Motion in App Router or Pages Router codebases, especially around server/client boundaries, reduced motion, LazyMotion, bundle size, hydration, or route transitions. Avoid for GSAP-style timelines, WebGL or 3D scenes, heavy scroll storytelling, or CSS-only effects unless Motion is explicitly requested.
- `scroll-experience` - Agents, Claude | Expert in building immersive scroll-driven experiences - parallax storytelling, scroll animations, interactive narratives, and cinematic web experiences. Like NY Times interactives, Apple product pages, and award-winning web experiences. Makes websites feel like experiences, not just pages. Use when: scroll animation, parallax, scroll storytelling, interactive story, cinematic website.
- `tactile-ui-system` - Claude, Codex | Applies a physical, tactile control system to a UI — buttons that visibly press down and lose their bottom shadow on click, inset "pressed-in" inputs, layered panel depth, and fast 100-190ms motion. This is a theme-agnostic interaction language (the physics), not a color palette — it adapts to whatever colors/tokens the target project already uses. This skill should be used when the user asks for buttons/controls to "feel pressable," "feel physical," "feel like Vyra," "feel tactile," or complains that an interface feels flat, glassy, or like a generic gradient AI SaaS product.
- `ui-designer` - Agents, Codex | Use this agent when designing visual interfaces, creating design systems, building component libraries, or refining user-facing aesthetics requiring expert visual design, interaction patterns, and accessibility considerations.
- `ui-ux-pro-max` - Agents | UI/UX design intelligence for web and mobile. Includes 50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, and 25 chart types across 10 stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui, and HTML/CSS). Actions: plan, build, create, design, implement, review, fix, improve, optimize, enhance, refactor, and check UI/UX code. Projects: website, landing page, dashboard, admin panel, e-commerce, SaaS, portfolio, blog, and mobile app. Elements: button, modal, navbar, sidebar, card, table, form, and chart. Styles: glassmorphism, claymorphism, minimalism, brutalism, neumorphism, bento grid, dark mode, responsive, skeuomorphism, and flat design. Topics: color systems, accessibility, animation, layout, typography, font pairing, spacing, interaction states, shadow, and gradient. Integrations: shadcn/ui MCP for component search and examples.
- `use-dom` - Agents, Claude | Use Expo DOM components to run web code in a webview on native and as-is on web. Migrate web code to native incrementally.
- `vercel-react-best-practices` - Agents, Claude | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.
- `vercel-react-view-transitions` - Agents, Claude | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view transition pseudo-elements). Use this skill whenever the user wants to add page transitions, animate route changes, create shared element animations, animate enter/exit of components, animate list reorder, implement directional (forward/back) navigation animations, or integrate view transitions in Next.js. Also use when the user mentions view transitions, `startViewTransition`, `ViewTransition`, transition types, or asks about animating between UI states in React without third-party animation libraries.
- `web-animation-design` - Agents, Claude | >
- `web-design-guidelines` - Agents, Claude | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".

## integrations/platform-tools

- `connect-apps` - Agents, Claude | Connect Claude to external apps like Gmail, Slack, GitHub. Use this skill when the user wants to send emails, create issues, post messages, or take actions in external services.
- `defuddle` - Agents, Claude | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch when the user provides a URL to read or analyze, for online documentation, articles, blog posts, or any standard web page. Do NOT use for URLs ending in .md — those are already markdown, use WebFetch directly.
- `figma` - Agents, Claude | Use when a Toolcraft task includes a Figma URL, node ID, or design-to-code requirement.
- `google-html-css-style` - Claude, Codex | Apply the Google HTML/CSS Style Guide when writing, editing, reviewing, or refactoring raw HTML, CSS, Sass, or GSS. Use for semantic markup, accessibility, selectors, declarations, formatting, and stylesheet maintainability.
- `google-javascript-style` - Claude, Codex | Apply the Google JavaScript Style Guide when writing, editing, reviewing, or refactoring JavaScript. Use for ES modules, Closure-compatible JavaScript, JSDoc, formatting, naming, classes, functions, and safe language-feature choices.
- `google-python-style` - Claude, Codex | Apply the Google Python Style Guide when writing, editing, reviewing, or refactoring Python. Use for imports, exceptions, resource management, type annotations, docstrings, naming, formatting, testing, and safe Python language features.
- `mcp-builder` - Agents, Claude | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
- `obsidian-bases` - Agents, Claude | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating database-like views of notes, or when the user mentions Bases, table views, card views, filters, or formulas in Obsidian.
- `obsidian-cli` - Agents, Claude | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, and more. Also supports plugin and theme development with commands to reload plugins, run JavaScript, capture errors, take screenshots, and inspect the DOM. Use when the user asks to interact with their Obsidian vault, manage notes, search vault content, perform vault operations from the command line, or develop and debug Obsidian plugins and themes.
- `obsidian-vault` - Agents | Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organize notes in Obsidian.
- `sora` - Codex | Use when the user asks to generate, edit, extend, poll, list, download, or delete Sora videos, create reusable non-human Sora character references, or run local multi-video queues via the bundled CLI (`scripts/sora.py`); includes requests like: (i) generate AI video, (ii) edit this Sora clip, (iii) extend this video, (iv) create a character reference, (v) download video/thumbnail/spritesheet, and (vi) Sora batch planning; requires `OPENAI_API_KEY` and Sora API access.

## mobile/native-and-cross-platform

- `expo-api-routes` - Agents, Claude | Guidelines for creating API routes in Expo Router with EAS Hosting
- `expo-cicd-workflows` - Agents, Claude | Helps understand and write EAS workflow YAML files for Expo projects. Use this skill when the user asks about CI/CD or workflows in an Expo or EAS context, mentions .eas/workflows/, or wants help with EAS build pipelines or deployment automation.
- `expo-deployment` - Agents, Claude | Deploying Expo apps to iOS App Store, Android Play Store, web hosting, and API routes
- `expo-dev-client` - Agents, Claude | Build and distribute Expo development clients locally or via TestFlight
- `expo-module` - Agents, Claude | Guide for creating and writing Expo native modules and views using the Expo Modules API (Swift, Kotlin, TypeScript). Covers module definition DSL, native views, shared objects, config plugins, lifecycle hooks, autolinking, and type system. Use when building or modifying native modules for Expo.
- `expo-react-native-expert` - Agents, Codex | Use when building mobile applications with Expo and React Native that require native module integration, navigation setup, performant animations, push notifications, OTA updates, or App Store/Play Store deployment.
- `expo-tailwind-setup` - Agents, Claude | Set up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling
- `expo-ui-jetpack-compose` - Agents, Claude | `@expo/ui/jetpack-compose` package lets you use Jetpack Compose Views and modifiers in your app.
- `expo-ui-swiftui` - Agents, Claude | `@expo/ui/swift-ui` package lets you use SwiftUI Views and modifiers in your app.
- `imagegen-frontend-mobile` - Agents, Claude | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. Prioritizes clean hierarchy, comfortably readable text, strong multi-screen consistency, controlled color palettes, non-generic creative direction, textured surfaces, image-led composition, tasteful custom iconography, and clean phone mockup framing. By default, screens should be shown inside a subtle premium iPhone or similar phone mockup with a visible frame, while the main focus stays on the app content itself. This skill generates images only. It does not write code.
- `kotlin-specialist` - Agents, Codex | Use when building Kotlin applications requiring advanced coroutine patterns, multiplatform code sharing, or Android/server-side development with functional programming principles.
- `tailwindcss-mobile-first` - Agents, Claude | Comprehensive mobile-first responsive design patterns with 2025/2026 best practices for Tailwind CSS v4
- `upgrading-expo` - Agents, Claude | Guidelines for upgrading Expo SDK versions and fixing dependency issues
- `vercel-react-native-skills` - Agents, Claude

## other/uncategorized

- `_gstack-command` - Claude | Router for the gstack skill suite. (gstack)
- `accelint-nextjs-best-practices` - Agents, Claude | Next.js performance optimization and best practices. Use when writing Next.js code (App Router or Pages Router); implementing Server Components, Server Actions, or API routes; optimizing RSC serialization, data fetching, or server-side rendering; reviewing Next.js code for performance issues; fixing authentication in Server Actions; or implementing Suspense boundaries, parallel data fetching, or request deduplication.
- `ai-native-sdlc` - Codex | [TODO: Briefly describe what this skill does and when it applies.]
- `arena` - Codex | Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape.
- `ask-matt` - Agents, Claude | Ask which skill or flow fits your situation. A router over the skills in this repo.
- `automate-me` - Codex | Use for \"automate me\", \"create/update/refresh my -mode skill\", \"turn/capture my preferences or working style into a skill\", or wanting agents to follow how the user works. Drafts or revises a personal -mode skill via create-skill + unslop, optionally pulling fresh evidence from recent transcripts.
- `blast-radius` - Codex | Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it's safe because of by running real code instead of writing it up. Use for 'blast radius of X', 'what could this break', or reviewing a small diff you don't trust.
- `cli-delegate` - Claude | Delegates a task, bug, or problem to an external CLI coding agent (Grok CLI or Codex CLI) instead of doing the work in this session. Writes a concise GSD-quick-style plan (problem, scope, do's/don'ts, numbered tasks, acceptance criteria) to a scratch file, hands it to the chosen CLI either headlessly in the background (`codex exec` / `grok -p` on Windows, output captured, nothing visible) or live — primarily via the agent-summoner MCP bridge, which opens the worker in a real terminal tab inside Devin itself; falling back to a standalone terminal window, then a shared tmux session in WSL if that's unavailable — then polls for completion and independently verifies the result before reporting back. Use when the user says "delegate this to grok/codex", "have grok/codex fix this", "run this with the grok cli", "use codex cli for this", "do this in the background with grok/codex", or invokes /cli-delegate.
- `comment-pr` - Agents, Claude, Codex | Draft and post a simple, human GitHub pull request comment after reviewing the PR context. Use when the user asks to comment on a PR, reply to a maintainer, follow up on review feedback, or post a short status/update message to a pull request. Always preview the exact comment and wait for explicit user approval before posting.
- `create-pr` - Agents, Claude, Codex | Full end-to-end PR creation — branch setup, implementation, tests, commit, push, and GitHub PR
- `eas-update-insights` - Agents, Claude | Check the health of published EAS Updates: crash rates, install/launch counts, unique users, payload size, and the split between embedded and OTA users per channel. Use when the user asks how an update is performing, whether a rollout is healthy, how many users are on the embedded build vs OTA, or wants to gate CI on update health.
- `gathering-project-context` - Agents | Use before modifying an existing repository when targeted evidence about its architecture, conventions, or affected code is needed.
- `gpt-image-2-prompt-generation` - Agents, Codex | Make any prompt for GPT Image 2 several times better by structuring and enhancing it without changing the user's core intent.
- `graphify` - Agents, Claude | Use for any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the question should be treated as a graphify query first. Turns any input (code, docs, papers, images, videos) into a persistent knowledge graph with god nodes, community detection, and query/path/explain tools.
- `grindroom-dev` - Agents, Claude | GrindRoom app development context. This skill should be used whenever working on the GrindRoom React Native fitness accountability app at c:\grindroom. Provides the Convex schema, design tokens, animation primitives, and coding conventions so Claude never needs re-explanation of the project setup.
- `hatch-pet` - Codex | Create, repair, validate, visually QA, and package Codex-compatible animated pets and pet spritesheets from character art, generated images, company or prospect brand cues, or visual references. Use when a user wants a lightweight-worker Codex pet workflow, a non-pixel custom pet style, a prospect or company mascot pet, or a full 8x9 animated pet atlas with transparent unused cells, QA contact sheets, and pet.json packaging. This skill composes the installed $imagegen system skill for visual generation and uses bundled scripts for deterministic spritesheet assembly.
- `herdr` - Agents, Claude | Control Herdr, a terminal multiplexer for coding agents. Use only when the user explicitly mentions Herdr or asks to use Herdr to inspect or control panes, tabs, workspaces, terminals, commands, or communication with another agent. Do not use merely because a task could benefit from a background terminal, delegation, or parallel work. Requires HERDR_ENV=1.
- `implement` - Agents, Claude | Implement a piece of work based on a spec or set of tickets.
- `loop-me` - Agents, Claude | Grill me about specs for the workflows I want to build, within this workspace.
- `no-comments` - Codex | Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints.
- `optimise-claude` - Agents, Claude | >
- `organize-pdf-notes` - Agents | Organize loose PDF files in a folder into subject-wise subfolders with descriptive numbered names (e.g. "GO notes 2.pdf" -> "Go Programming/02-Data-Types-Conditionals-and-Loops.pdf"). Works for ANY pdfs and any subjects. Use when the user asks to arrange/organize/sort/group PDFs or notes by subject, or says "organize my notes", "arrange these pdfs", "sort notes into folders", "rename notes properly".
- `ponytail` - Agents, Claude | >
- `ponytail-debt` - Agents, Claude | >
- `ponytail-gain` - Agents, Claude | >
- `ponytail-help` - Agents, Claude | >
- `poteto-mode` - Codex | poteto's agent style for concise, detailed responses, deliberate subagents, unslopped prose, simple code, and verified work. Use for poteto, /poteto-mode, or requests to work in this style.
- `proper-resume-docx` - Codex | Use when creating, rewriting, or formatting Prathick Dhanes R resumes as .docx files, especially master resumes, SDE resumes, mobile resumes, project-bank resumes, ATS resumes, or any request to follow the clean Claude-style Node docx resume format.
- `pushit` - Codex | Commit and push completed changes with a focused, reviewable Git workflow; use when the user invokes $pushit or asks to commit and push work.
- `pyq-convert` - Agents, Claude | Convert a PYQ (previous-year question) PDF — or any text-based PDF — into clean text/markdown using plain PyMuPDF (fitz). Use whenever the user gives a PYQ PDF and wants it converted, or types /pyq-convert. Fast (~0.1s for ~36 pages), zero (cid:) garbage, questions and options in correct order. Preferred over markitdown (which produces (cid:) garbage) and Docling/Marker (which are minutes-slow on CPU).
- `resolving-merge-conflicts` - Agents, Claude | Use when you need to resolve an in-progress git merge/rebase conflict.
- `save-credits` - Agents, Claude | Use this skill when the user wants maximum efficiency with API credits. Minimize tokens, avoid unnecessary reasoning, and eliminate waste. Triggers on: "save credits", "cheap mode", "use less tokens", "be efficient", "low cost", "minimal output".
- `search-domain-validator` - Agents, Claude | This skill should be used when users need to validate domain name format, check domain availability, or search for available domain names. It activates when users ask about domain validation, domain availability checking, domain search, or domain name verification.
- `shared-terminals` - Claude | Gives Claude a real, watchable, interruptible terminal — a persistent tmux session (inside WSL Ubuntu) that the user can attach to at any time with `wsl -d Ubuntu -e tmux attach -t claude`, watch commands execute live, and take over or answer prompts themselves. Claude drives named windows inside it via the `claude-term` wrapper (list/new/run/send/read/kill) instead of a hidden background shell. For grok/codex specifically this is Tier 3 (last-resort) behind the agent-summoner MCP bridge and a standalone terminal window — see [[cli-delegate]]. Use this directly for anything else that needs to be genuinely visible/interactive: a long-running server, an auth flow needing browser/device-code interaction, or anything the user asked to "watch happen" rather than get a summary of afterward.
- `show-me-your-work` - Codex | Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). Local by default; commit it when a reviewer needs the trail to trust the result. Use for /show-me-your-work, autonomous or multi-phase runs, or work a human reviews after stepping away.
- `source-command-gpt-image-2` - Agents | Make any prompt for GPT Image 2 several times better by structuring and enhancing it without changing the user's core intent.
- `source-command-save-credits` - Agents | Switch to credit-efficient mode — no subagents, minimal tool calls, simple solutions
- `stateful-button-ux` - Codex | Audit and implement async button feedback in React apps, using loading and success states only where a user action waits or mutates data.
- `syncvas-frontend-craft` - Codex | Improve Syncvas frontend UX, visual hierarchy, and purposeful motion while preserving its classroom-first MVP and existing design tokens. Use for Syncvas UI polish, interaction feedback, or animation work; do not use for realtime or domain behavior changes.
- `ultra-product-uiux` - Codex | Design, improve, audit, and validate polished web product interfaces with clear UX, accessible responsive systems, and purposeful motion. Use for substantial frontend design work or visual UX audits, not trivial CSS or backend-only tasks.
- `wait-what` - Agents, Claude | Stop. That last message did not land: re-pitch it.
- `website-bug-finder` - Codex | Audit a website codebase and local runtime for reproducible, high-impact product and security bugs, with strict P1 evidence gates and reusable reports.
- `zoom-out` - Agents, Claude | Tell the agent to zoom out and give broader context or a higher-level perspective. Use when you're unfamiliar with a section of code or need to understand how it fits into the bigger picture.

## planning/project-planning

- `product-manager` - Agents, Codex | Use this agent when you need to make product strategy decisions, prioritize features, or define roadmap plans based on user needs and business goals.
- `product-to-launch` - Codex | Run a product from canonical scope through architecture, implementation, verification, deployment, marketing, and sales.
- `request-refactor-plan` - Agents | Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue. Use when user wants to plan a refactor, create a refactoring RFC, or break a refactor into safe incremental steps.
- `scaffold-exercises` - Agents, Claude | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course section.
- `seo-plan` - Claude | >
- `to-issues` - Agents, Claude | Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. Use when user wants to convert a plan into issues, create implementation tickets, or break down work into issues.
- `to-prd` - Agents, Claude | Turn the current conversation context into a PRD and publish it to the project issue tracker. Use when user wants to create a PRD from the current context.
- `to-questionnaire` - Agents, Claude | Turn a decision you can't fully answer into a questionnaire for someone else to fill in.
- `to-spec` - Agents, Claude | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed.
- `to-tickets` - Agents, Claude | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket locally, or native blocking links on a real tracker).
- `writing-plans` - Agents, Claude | Use before Toolcraft code changes once the product behavior or approved spec is clear.

## product-growth/ethical-growth

- `accessibility-growth` - Agents, Claude, Codex | Make onboarding, experiments, paywalls, forms, and lifecycle flows accessible and measure whether variants exclude users. Use when growth work changes interaction, copy, authentication, motion, or payment.
- `dark-pattern-prevention` - Agents, Claude, Codex | Review growth flows for deceptive urgency, obstruction, hidden terms, forced action, asymmetric choice, disguised content, and manipulative data collection. Use before shipping onboarding, consent, paywall, trial, or cancellation changes.
- `privacy-and-consent` - Agents, Claude, Codex | Design growth research, personalization, analytics, and messaging with data minimization, meaningful choice, retention limits, and deletion handling. Use whenever growth work processes personal or sensitive data.

## product-growth/experimentation

- `ab-test-planning` - Agents, Claude, Codex | Design trustworthy randomized product experiments with clear assignment, exposure, metrics, power, duration, and stopping rules. Use before implementing or launching an A/B test.
- `experiment-analysis` - Agents, Claude, Codex | Validate and interpret controlled product experiments, separating data quality, statistical evidence, practical value, segments, and guardrails. Use at experiment readout or when results conflict.
- `guardrail-metrics` - Agents, Claude, Codex | Choose metrics that prevent a growth experiment from winning by damaging trust, retention, quality, accessibility, performance, privacy, or economics. Use during experiment planning and launch review.
- `hypothesis-design` - Agents, Claude, Codex | Convert product evidence and uncertainty into falsifiable growth hypotheses with explicit mechanisms and decisions. Use before designing variants or prioritizing experiments.

## product-growth/funnel-and-activation

- `acquisition-to-onboarding` - Agents, Claude, Codex | Connect acquisition intent to landing pages, store listings, onboarding, and first value. Use when traffic converts poorly, channel cohorts differ, or the first experience breaks the promise.
- `activation-design` - Agents, Claude, Codex | Define and improve the earliest user behavior that demonstrates real product value and predicts durable use. Use when onboarding completion is high but meaningful adoption or retention is weak.
- `onboarding-personalization` - Agents, Claude, Codex | Design proportional onboarding personalization from user goals, context, and permissions. Use when one generic path serves distinct jobs or when collected answers do not improve first-session value.

## product-growth/measurement-and-ops

- `experiment-log` - Agents, Claude, Codex | Create and maintain a searchable record of product hypotheses, implementations, metrics, results, decisions, and reusable learning. Use when teams repeat tests or lose experiment context.
- `growth-dashboard-design` - Agents, Claude, Codex | Build decision-focused dashboards for acquisition, activation, engagement, retention, monetization, and experiment health. Use when metric sprawl or inconsistent definitions blocks action.
- `growth-decision-making` - Agents, Claude, Codex | Turn mixed research, analytics, experiment, economics, and risk evidence into explicit product-growth decisions. Use when evidence conflicts or a team needs ship, iterate, stop, or learn-next guidance.
- `product-instrumentation` - Agents, Claude, Codex | Design a versioned product analytics and experimentation event contract tied to user decisions and value. Use when funnels, cohorts, experiments, or growth metrics cannot be trusted.

## product-growth/monetization

- `billing-compliance` - Agents, Claude, Codex | Check current platform, storefront, subscription, disclosure, and alternative-payment constraints before changing digital-product billing. Use for web, iOS, Android, or cross-platform monetization plans.
- `paywall-optimization` - Agents, Claude, Codex | Improve paywall value communication, offer clarity, placement, and conversion while protecting trust and downstream economics. Use for subscription or entitlement paywall diagnosis and experiments.
- `pricing-and-packaging` - Agents, Claude, Codex | Design and test prices, tiers, bundles, units, and entitlements against willingness to pay, value, retention, and sustainable economics. Use when a product's commercial model needs evidence.
- `trial-strategy` - Agents, Claude, Codex | Evaluate free trials, freemium access, previews, guarantees, and one-time offers using value delivery and cohort economics. Use when deciding whether, when, and how users should experience value before paying.

## product-growth/orchestration

- `product-growth-experimentation` - Agents, Claude, Codex | Orchestrate evidence-led product growth across user research, acquisition, onboarding, activation, experimentation, monetization, retention, referral, and measurement. Use for end-to-end growth programs or ambiguous growth problems; use a narrower product-growth skill for a single bounded task.

## product-growth/retention-and-referral

- `lifecycle-messaging` - Agents, Claude, Codex | Design consented email, push, in-app, and transactional messages around timely user value. Use for activation reminders, education, re-engagement, renewal, or churn prevention.
- `retention-loops` - Agents, Claude, Codex | Design and evaluate repeat-value loops that bring users back for a meaningful outcome. Use when activation occurs but cohorts do not form durable product habits or recurring workflows.
- `viral-sharing` - Agents, Claude, Codex | Design user-controlled sharing and referral loops around genuinely useful outcomes, identity, collaboration, or artifacts. Use when organic distribution should emerge from product value.

## product-growth/user-research

- `jobs-to-be-done` - Agents, Claude, Codex | Frame product growth around the progress users seek in a specific circumstance. Use when personas, feature requests, or demographic segments do not explain adoption, switching, or willingness to pay.
- `market-and-competitor-research` - Agents, Claude, Codex | Research market demand, alternatives, positioning, and competitor journeys to form testable product-growth hypotheses. Use for evidence-backed landscape work, not copying competitor features.
- `user-interview-analysis` - Agents, Claude, Codex | Turn user interviews into traceable findings, tensions, and growth hypotheses. Use after discovery, usability, onboarding, churn, cancellation, or pricing interviews.

## research-data/research-seo-and-content

- `content-marketer` - Agents, Codex | Use this agent when you need to develop comprehensive content strategies, create SEO-optimized marketing content, or execute multi-channel content campaigns to drive engagement and conversions. Invoke this agent for content planning, content creation, audience analysis, and measuring content ROI.
- `firecrawl` - Agents, Claude, Codex | \\|
- `firecrawl-build` - Agents, Claude, Codex | Integrate Firecrawl into application code whenever a product, agent, or workflow needs web data inside the app: web search, live search results, page scraping, structured extraction, or browser interaction. Use when building any feature that needs data from the web in code, even if the user does not mention Firecrawl explicitly and only describes wanting web data, website content, search, scraping, or interaction in an application. Trigger for Firecrawl requests, "fire girl" shorthand, and generic app-level web-data needs that should map to `/scrape`, `/search`, or `/interact`. Do not use this skill for one-off terminal-only web tasks during the current session; use `firecrawl/cli` for those.
- `firecrawl-build-interact` - Agents, Claude, Codex | Integrate Firecrawl `/interact` into product code for dynamic pages and browser actions after scraping. Use when a feature needs clicks, form fills, pagination, authentication-aware flows, or other multi-step interactions that plain `/scrape` cannot complete.
- `firecrawl-build-onboarding` - Agents, Claude, Codex | Get Firecrawl credentials and SDK setup into a project. Use when an application needs `FIRECRAWL_API_KEY`, when an agent should add Firecrawl to `.env`, when the user wants to authenticate Firecrawl for app code, or when choosing the first SDK and docs for a new Firecrawl integration. This skill includes its own browser auth flow, so it does not depend on the website onboarding skill.
- `firecrawl-build-scrape` - Agents, Claude, Codex | Integrate Firecrawl `/scrape` into product code for single-page extraction. Use when an app already has a URL and needs markdown, HTML, links, screenshots, metadata, or structured page output. Prefer this skill over broader crawl patterns when the feature is page-level.
- `firecrawl-build-search` - Agents, Claude, Codex | Integrate Firecrawl `/search` into product code and agent workflows. Use when an app needs discovery before extraction, when the feature starts with a query instead of a URL, or when the system should search the web and optionally hydrate result content.
- `firecrawl-company-directories` - Agents, Claude, Codex | Extract structured company lists from directories with Firecrawl. Use for scraping YC, Crunchbase, Product Hunt, G2, startup directories, category directories, or custom company databases into JSON, CSV, CRM-ready lists, or research tables.
- `firecrawl-competitive-intel` - Agents, Claude, Codex | Monitor competitor pricing, features, changelogs, dashboards, and product changes with Firecrawl. Use for recurring competitive intelligence, pricing tier extraction, feature change tracking, or structured competitor alerts.
- `firecrawl-crawl` - Agents, Claude, Codex | \\|
- `firecrawl-dashboard-reporting` - Agents, Claude, Codex | Pull metrics from analytics dashboards and internal web tools with Firecrawl browser. Use when the user needs dashboard reporting, cross-platform metric summaries, authenticated analytics extraction, date-range reports, or structured metrics from web dashboards.
- `firecrawl-deep-research` - Agents, Claude, Codex | \\|
- `firecrawl-demo-walkthrough` - Agents, Claude, Codex | Walk through a product's key flows with Firecrawl browser and produce a structured UX/product walkthrough. Use for signup, onboarding, pricing, docs, dashboard, product demo prep, UX teardown, and first-run experience analysis.
- `firecrawl-download` - Agents, Claude, Codex | \\|
- `firecrawl-interact` - Agents, Claude, Codex | \\|
- `firecrawl-knowledge-base` - Agents, Claude, Codex | Build a knowledge base from web content with Firecrawl. Use for local reference docs, RAG-ready chunks, fine-tuning datasets, documentation mirrors, topic corpora, or LLM-ready markdown organized from web sources.
- `firecrawl-knowledge-ingest` - Agents, Claude, Codex | Ingest public or authenticated knowledge bases and docs portals with Firecrawl browser. Use for JS-heavy docs, login-gated portals, paginated help centers, support knowledge bases, or structured JSON/markdown extraction from documentation sites.
- `firecrawl-lead-gen` - Agents, Claude, Codex | Generate structured lead lists from prospect databases and web directories with Firecrawl browser. Use for finding prospects by role, company type, industry, stage, location, technologies, or other criteria and exporting CRM-ready JSON or CSV.
- `firecrawl-lead-research` - Agents, Claude, Codex | Produce pre-meeting lead intelligence briefs with Firecrawl. Use when the user needs company research, person research, recent news, talking points, pain points, or outreach preparation before a sales call, partnership meeting, investor conversation, or customer interview.
- `firecrawl-map` - Agents, Claude, Codex | \\|
- `firecrawl-market-research` - Agents, Claude, Codex | Extract market, financial, earnings, industry, and company metrics with Firecrawl. Use when the user asks for market research, industry trends, public company data, financial comparisons, earnings research, or structured market reports.
- `firecrawl-monitor` - Agents, Claude, Codex | \\|
- `firecrawl-parse` - Agents, Claude, Codex | \\|
- `firecrawl-research-index` - Agents, Claude, Codex | Find the papers that answer a research query with Firecrawl Research, using semantic search, semantic and structural expansion, and in-body verification. Always use this skill for any literature-finding / paper-retrieval task — single-paper lookups or full multi-paper sets.
- `firecrawl-research-papers` - Agents, Claude, Codex | Find and synthesize research papers, whitepapers, PDFs, technical reports, and academic sources with Firecrawl Research, using semantic paper search, related-paper expansion, and in-body verification. Use when the user wants a literature review, paper summary, research landscape, or sourced synthesis from PDFs and scholarly/industry publications.
- `firecrawl-scrape` - Agents, Claude, Codex | \\|
- `firecrawl-search` - Agents, Claude, Codex | \\|
- `firecrawl-shop` - Agents, Claude, Codex | Research products across the web with Firecrawl and produce a shopping recommendation or cart-ready summary. Use when the user wants to compare products, find the best option, evaluate reviews, respect budget/preferences, or shop with a saved browser session.
- `firecrawl-workflows` - Agents, Claude, Codex | Run outcome-focused Firecrawl workflows that produce deliverables such as research reports, SEO audits, QA reports, lead lists, knowledge bases, website design systems, and other structured web-data artifacts. Use when the user wants Firecrawl to complete a business, marketing, product, or creative workflow rather than merely scrape a page or integrate API calls into code.
- `gavelnews-editorial` - Claude, Codex | Converts a raw newspaper article or website page into a complete GavelNews current-affairs piece for CLAT aspirants using article schema v2 (hero/story/law_decode/exam_radar/challenge/one_line_revision/sources + Visual Memory Card). Every output MUST pass a behuman pass before being considered done. Use when given a newspaper/news-site URL or pasted article and asked to turn it into GavelNews content, or when asked to update the gavel-news editorial pipeline.
- `gavelogy-judgment` - Agents, Claude | Full pipeline for Gavelogy case law notes. Given an itemId (Convex content_items or structure_items ID), generates: (1) structured HTML notes in lex-note format, (2) flashcards JSON, (3) MCQ quiz questions, (4) PDF judgment connections. Pushes notes to the live-note preview (dev server), then saves everything to Convex. Trigger: /gavelogy-judgment
- `research` - Agents, Claude | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.
- `seo` - Claude | Comprehensive SEO analysis for any website or business type. Full site audits, single-page analysis, technical SEO (crawlability, indexability, Core Web Vitals with INP), schema markup, content quality (E-E-A-T), image optimization, sitemap analysis, and GEO for AI Overviews/ChatGPT/Perplexity. Industry detection for SaaS, e-commerce, local, publishers, agencies. Triggers on: SEO, audit, schema, Core Web Vitals, sitemap, E-E-A-T, AI Overviews, GEO, technical SEO, content quality, page speed.
- `seo-ahrefs` - Claude | Ahrefs API analyst (extension). Reads referring domains, backlinks, organic keywords, and content explorer data via the tested @ahrefs/mcp@0.0.11 server. Pairs with seo-backlinks for multi-source confidence weighting.
- `seo-backlinks` - Claude | Backlink profile analysis: referring domains, anchor text distribution, toxic link detection, competitor gap analysis. Works with free APIs (Moz, Bing Webmaster, Common Crawl) and DataForSEO extension. Use when user says backlinks, link profile, referring domains, anchor text, toxic links, link gap, link building, disavow, or backlink audit.
- `seo-bing` - Claude | Bing Webmaster Tools + IndexNow extension. Microsoft Copilot citations are fed by the Bing index; this skill makes Bing visibility, link data, and IndexNow URL submission first-class.
- `seo-cluster` - Claude | >
- `seo-competitor-pages` - Claude | >
- `seo-content` - Claude | >
- `seo-content-brief` - Claude | >
- `seo-dataforseo` - Claude | >
- `seo-drift` - Claude | >
- `seo-ecommerce` - Claude | >
- `seo-firecrawl` - Claude | >
- `seo-flow` - Claude | >
- `seo-geo` - Claude | >
- `seo-google` - Claude | >
- `seo-hreflang` - Claude | >
- `seo-image-gen` - Claude | AI image generation for SEO assets: OG/social preview images, blog hero images, schema images, product photography, infographics. Powered by Gemini via nanobanana-mcp. Requires banana extension installed. Use when user says \"generate image\", \"OG image\", \"social preview\", \"hero image\", \"blog image\", \"product photo\", \"infographic\", \"seo image\", \"create visual\", \"image-gen\", \"favicon\", \"schema image\", \"pinterest pin\", \"generate visual\", \"banner\", or \"thumbnail\".
- `seo-images` - Claude | >
- `seo-local` - Claude | >
- `seo-maps` - Claude | >
- `seo-page` - Claude | >
- `seo-profound` - Claude | Profound LLM citation tracker (extension). Time-series brand citation rates across ChatGPT, Perplexity, and other LLMs. Pairs with seo-seranking for triangulated AI visibility coverage.
- `seo-programmatic` - Claude | >
- `seo-schema` - Claude | >
- `seo-seranking` - Claude | SE Ranking AI visibility analyst (extension). Tracks AI Share-of-Voice across ChatGPT, Gemini, Perplexity, AI Overviews, and AI Mode in a single query.
- `seo-sitemap` - Claude | >
- `seo-specialist` - Agents, Codex | Use this agent when you need comprehensive SEO optimization encompassing technical audits, keyword strategy, content optimization, and search rankings improvement.
- `seo-sxo` - Claude | >
- `seo-technical` - Claude | >
- `seo-unlighthouse` - Claude | Multi-page Lighthouse audit via the MIT-licensed Unlighthouse CLI. Free-tier alternative to running PageSpeed against every URL on a site, no API quota burn, runs locally.

## security/appsec-and-privacy

- `application-security` - Agents, Claude | >-
- `authorized-bug-bounty-research` - Agents | Run authorized bug-bounty research with explicit scope gates, passive-first mapping, low-volume hypotheses, and controlled evidence.
- `bug-bounty-report-writing` - Agents | Write and quality-check evidence-first bug-bounty reports from verified, in-scope findings without inventing proof or impact.
- `harden-web-experience` - Agents, Claude, Codex | Turn an existing web application into a production-grade product by auditing, fixing, and verifying security, hidden bugs, edge cases, accessibility, async loading/error/empty states, data integrity, network and Core Web Vitals performance, resilience, observability, deployment safety, privacy, and public-site discoverability. Use for website hardening, launch-readiness reviews, production polish, full-stack quality passes, request/network optimization, or when every user action and failure path must work reliably. Also use when the user runs /harden-web-experience or says "harden this website", "make this production-ready", or "launch readiness".
- `security-auditor` - Agents, Codex | Use this agent when conducting comprehensive security audits, compliance assessments, or risk evaluations across systems, infrastructure, and processes. Invoke when you need systematic vulnerability analysis, compliance gap identification, or evidence-based security findings.
- `security-headers-configuration` - Agents, Claude | >
- `turnstile-spin` - Agents, Claude, Codex | Set up Cloudflare Turnstile end-to-end in a project. Scan the codebase, create the widget via the Cloudflare API, embed it where user requests need bot verification (form submissions, SPA actions, API endpoints, download links, comment or vote submissions, etc.), wire canonical server-side siteverify in the customer's existing backend, validate, and persist the skill. Load this when a user asks to add Turnstile, set up CAPTCHA, protect a form or endpoint from bots, or fix a Turnstile integration. Mirrors developers.cloudflare.com/turnstile/spin.

## security/reverse-engineering

- `reverse-skill-router` - Agents, Claude, Codex | Route authorized reverse engineering, CTF, malware-analysis, and defensive security work through the reverse-skill methodology while requiring explicit permission before risky commands or side effects.

## specialists/domain-workflows

- `customer-success-manager` - Agents, Codex | Use this agent when you need to assess customer health, develop retention strategies, identify upsell opportunities, or maximize customer lifetime value. Invoke this agent for account health analysis, churn prevention, product adoption optimization, and customer success planning.
- `klyna-headless-review` - Agents | Automatically review and post a review on an eligible Klyna pull request after a trusted queue worker receives a review assignment for <GITHUB_USER>.
- `klyna-issue` - Agents | Solve a Klyna GitHub issue end to end using the repository workflow, tests, DCO commits, fork push, and a ready pull request.
- `klyna-pr-followup` - Agents | Address requested changes on an existing Klyna pull request by fixing review feedback on the same branch, testing it, and pushing the update to that PR.
- `klyna-pr-merge` - Agents | Verify that requested Klyna PR changes were correctly delivered, then approve and merge a green PR when the user explicitly asks to merge if it is good.
- `klyna-review` - Agents | Review a Klyna pull request against main and its issue, then prepare exact GitHub inline comments, an approval, or a clean LGTM using the repository review style.
- `legal-video` - Agents, Claude, Codex | Build Indian legal explainer videos in the woodcut/linocut (Gavelogy) style with Remotion. Phase 1 generates one combined mega-prompt of all image prompts; Phase 2 preps assets (TTS or self-recorded audio + transcription + image-map); Phase 3 builds the full Remotion project. Trigger: /legal-video
- `polaris-campus-assistant` - Codex | Use when Nithy asks Codex to work with Polaris Campus batches, announcements, study materials, local PDF downloads, or slash-style commands such as /polaris check all, /polaris announcements <batch>, /polaris sync <batch>, or /polaris batches.
- `sales-engineer` - Agents, Codex | Use this agent when you need to conduct technical pre-sales activities including solution architecture, proof-of-concept development, and technical demonstrations for complex sales deals.

## testing/qa-and-verification

- `accessibility-tester` - Agents, Codex | Use this agent when you need comprehensive accessibility testing, WCAG compliance verification, or assessment of assistive technology support.
- `diagnose` - Agents, Claude | Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test. Use when user says "diagnose this" / "debug this", reports a bug, says something is broken/throwing/failing, or describes a performance regression.
- `diagnosing-bugs` - Agents, Claude | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.
- `firecrawl-qa` - Agents, Claude, Codex | QA test a live website with Firecrawl browser and scrape evidence. Use when the user wants exploratory QA, form testing, navigation/link checks, responsive checks, performance observations, bug reports, or a pre-launch quality review.
- `firecrawl-seo-audit` - Agents, Claude, Codex | Audit a website's SEO with Firecrawl. Use when the user asks for an SEO audit, metadata and heading review, sitemap/site-structure analysis, keyword opportunities, competitor SERP comparison, or prioritized search optimization recommendations.
- `fullstack-perf-audit` - Claude | >
- `gsap-performance` - Agents, Claude | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or when the user asks about animation performance, FPS, or smooth 60fps.
- `playwright` - Codex | Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.
- `ponytail-audit` - Agents, Claude | >
- `qa` - Agents | Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for context and domain language. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session".
- `qa-expert` - Agents, Codex | Use this agent when you need comprehensive quality assurance strategy, test planning across the entire development cycle, or quality metrics analysis to improve overall software quality.
- `seo-audit` - Claude | Full website SEO audit with parallel subagent delegation. Crawls up to 500 pages, detects business type, delegates to up to 15 specialists (8 always + 7 conditional), generates health score. Use when user says audit, full SEO check, analyze my site, or website health check.
- `systematic-debugging` - Agents, Claude | Use before fixing broken Toolcraft controls, tests, builds, visual mismatches, exports, or runtime regressions.
- `tdd` - Agents, Claude, Codex | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.
- `ui-ux-tester` - Agents, Codex | Use this agent when you need exhaustive UI and UX functionality testing driven by documented user flows, with browser or desktop interaction tooling and structured defect reporting.
- `web-perf` - Agents, Claude, Codex | Analyzes web performance using Chrome DevTools MCP. Measures Core Web Vitals (LCP, INP, CLS) and supplementary metrics (FCP, TBT, Speed Index), identifies render-blocking resources, network dependency chains, layout shifts, caching issues, and accessibility gaps. Use when asked to audit, profile, debug, or optimize page load performance, Lighthouse scores, or site speed. Biases towards retrieval from current documentation over pre-trained knowledge.
- `web-performance-optimization` - Agents, Claude | Optimize web performance using Core Web Vitals, modern patterns (View Transitions, Speculation Rules), and framework-specific techniques

## tools-utilities/general-purpose

- `behuman` - Claude, Codex | Strips every documented LLM-writing tell out of a piece of text so it reads as plainly human-written. Source: the empirically-compiled Wikipedia:Signs of AI writing field guide (WikiProject AI Cleanup), with every pattern in it converted into a hard "never do this" rule. Use before finalizing ANY piece of prose meant to read as human-written — articles, explanations, notes, emails, landing copy. Other content-generation skills should explicitly invoke this one as a final pass, not skip it.
- `brainstorming` - Agents, Claude | Use before creating Toolcraft app features, changing behavior, or assembling app specs.
- `caveman` - Agents, Claude | >
- `caveman-poteto-unslop` - Codex | Run rigorous work in Poteto Mode, design deep modules when structure matters, answer concisely in Caveman mode, and remove AI writing tells with Unslop. Use when the user wants this combined workflow.
- `changelog-generator` - Agents, Claude | Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. Turns hours of manual changelog writing into minutes of automated generation.
- `code-review` - Agents, Claude | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to \"review since X\".
- `codex-review` - Agents, Claude | A standalone adversarial PLAN-review loop where Claude Code (builder) and OpenAI Codex (read-only critic) tag-team an implementation plan before any code is written. Use this when you ALREADY have a plan or a clear idea and just want the cross-model stress-test — no requirements interview first. Claude drafts/loads the plan into PLAN.md, Codex reviews it in a read-only sandbox and returns VERDICT:APPROVED or VERDICT:REVISE, Claude revises and re-submits to the SAME Codex session (context preserved) until APPROVED or a configurable MAX_ROUNDS cap is hit. Human approves the converged plan before code. Use when the user says "/codex-review", "codex review my plan", "have Codex review my plan", "argue this plan with Codex", "adversarial plan review", "make Claude and Codex argue/fight over the plan", or is about to build something high-stakes (auth, schema, concurrency, migrations, payments) and wants a second-model sanity check on the PLAN before implementation. For a guided requirements interview BEFORE the review, use /grill-me-codex instead. NOT for reviewing already-written CODE (that is the Codex plugin's /codex:review) and NOT for trivial changes.
- `create-verification-skill` - Codex | Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. Use for /create-verification-skill, \"make a control skill for this repo\", or when a project has no scripted way to prove UI/CLI/service behavior.
- `find-skills` - Agents, Claude, Codex | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.
- `maintain-verification-skill` - Codex | Periodic pass that keeps a project's verification skill and feature map honest: parallel source readers per feature, one live session driving every feature, at most one PR of proven corrections. Use for /maintain-verification-skill or \"audit the verify skill\".
- `ponytail-review` - Agents, Claude | >
- `prototype` - Agents, Claude | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like.
- `review` - Agents | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".
- `skill-creator` - Agents, Claude | Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- `teach` - Agents, Claude, Codex | Teach the user a new skill or concept, within this workspace.
- `thermo-nuclear-code-quality-review` - Agents | Run an extremely strict maintainability review for abstraction quality, giant files, and spaghetti-condition growth. Use for a thermo-nuclear code quality review, thermonuclear review, deep code quality audit, or especially harsh maintainability review.
- `triage` - Agents, Claude | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs.
- `wayfinder` - Agents, Claude | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear.
- `wizard` - Agents, Claude | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover. Don't invoke this for steps the agent can perform itself.
- `write-a-skill` - Agents, Claude | Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill.
