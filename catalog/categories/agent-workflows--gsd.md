# agent-workflows/gsd

Skills in this category: 88

| Skill | Available in | Description |
| --- | --- | --- |
| `gsd-add-backlog` | Codex | Add an idea to the backlog parking lot (999.x numbering) |
| `gsd-add-phase` | Codex | Add phase to end of current milestone in roadmap |
| `gsd-add-tests` | Agents, Claude, Codex | Generate tests for a completed phase based on UAT criteria and implementation |
| `gsd-add-todo` | Codex | Capture idea or task as todo from current conversation context |
| `gsd-ai-integration-phase` | Agents, Claude | Generate an AI-SPEC.md design contract for phases that involve building AI systems. |
| `gsd-analyze-dependencies` | Codex | Analyze phase dependencies and suggest Depends on entries for ROADMAP.md |
| `gsd-audit-fix` | Agents, Claude | Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit |
| `gsd-audit-milestone` | Agents, Claude, Codex | Audit milestone completion against original intent before archiving |
| `gsd-audit-uat` | Agents, Claude, Codex | Cross-phase audit of all outstanding UAT and verification items |
| `gsd-autonomous` | Agents, Claude, Codex | Run all remaining phases autonomously — discuss→plan→execute per phase |
| `gsd-capture` | Agents, Claude | Capture ideas, tasks, notes, and seeds to their destination |
| `gsd-check-todos` | Codex | List pending todos and select one to work on |
| `gsd-cleanup` | Agents, Claude, Codex | Archive accumulated phase directories from completed milestones |
| `gsd-code-review` | Agents, Claude | Review source files changed during a phase for bugs, security issues, and code quality problems |
| `gsd-complete-milestone` | Agents, Claude, Codex | Archive completed milestone and prepare for next version |
| `gsd-config` | Agents, Claude | Configure GSD settings — workflow toggles, advanced knobs, integrations, and model profile |
| `gsd-debug` | Agents, Claude, Codex | Systematic debugging with persistent state across context resets |
| `gsd-discuss-phase` | Agents, Claude, Codex | Gather phase context through adaptive questioning before planning. |
| `gsd-do` | Codex | Route freeform text to the right GSD command automatically |
| `gsd-docs-update` | Agents, Claude, Codex | Generate or update project documentation verified against the codebase |
| `gsd-eval-review` | Agents, Claude | Audit an executed AI phase's evaluation coverage and produce an EVAL-REVIEW.md remediation plan. |
| `gsd-execute-phase` | Agents, Claude, Codex | Execute all plans in a phase with wave-based parallelization |
| `gsd-explore` | Agents, Claude | Socratic ideation and idea routing — think through ideas before committing to plans |
| `gsd-extract-learnings` | Agents, Claude | Extract decisions, lessons, patterns, and surprises from completed phase artifacts |
| `gsd-fast` | Agents, Claude, Codex | Execute a trivial task inline — no subagents, no planning overhead |
| `gsd-forensics` | Agents, Claude, Codex | Post-mortem investigation for failed GSD workflows — diagnoses what went wrong. |
| `gsd-graphify` | Agents, Claude | Build, query, and inspect the project knowledge graph in .planning/graphs/ |
| `gsd-health` | Agents, Claude, Codex | Diagnose planning directory health and optionally repair issues |
| `gsd-help` | Agents, Claude, Codex | Show available GSD commands and usage guide |
| `gsd-import` | Agents, Claude | Ingest external plans with conflict detection against project decisions before writing anything. |
| `gsd-inbox` | Agents, Claude | Triage and review open GitHub issues and PRs against project templates and contribution guidelines. |
| `gsd-ingest-docs` | Agents, Claude | Bootstrap or merge a .planning/ setup from existing ADRs, PRDs, SPECs, and docs in a repo. |
| `gsd-insert-phase` | Codex | Insert urgent work as decimal phase (e.g., 72.1) between existing phases |
| `gsd-join-discord` | Codex | Join the GSD Discord community |
| `gsd-list-phase-assumptions` | Codex | Surface the agent's assumptions about a phase approach before planning |
| `gsd-list-workspaces` | Codex | List active GSD workspaces and their status |
| `gsd-manager` | Agents, Claude, Codex | Interactive command center for managing multiple phases from one terminal |
| `gsd-map-codebase` | Agents, Claude, Codex | Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents |
| `gsd-milestone-summary` | Agents, Claude, Codex | Generate a comprehensive project summary from milestone artifacts for team onboarding and review |
| `gsd-mvp-phase` | Agents, Claude | Plan a phase as a vertical MVP slice — user story, SPIDR splitting, then plan-phase |
| `gsd-new-milestone` | Agents, Claude, Codex | Start a new milestone cycle — update PROJECT.md and route to requirements |
| `gsd-new-project` | Agents, Claude, Codex | Initialize a new project with deep context gathering and PROJECT.md |
| `gsd-new-workspace` | Codex | Create an isolated workspace with repo copies and independent .planning/ |
| `gsd-next` | Codex | Automatically advance to the next logical step in the GSD workflow |
| `gsd-note` | Codex | Zero-friction idea capture. Append, list, or promote notes to todos. |
| `gsd-ns-context` | Agents, Claude | codebase intelligence \\| map graphify docs learnings |
| `gsd-ns-ideate` | Agents, Claude | exploration capture \\| explore sketch spike spec capture |
| `gsd-ns-manage` | Agents, Claude | config workspace \\| workstreams thread update ship inbox |
| `gsd-ns-project` | Agents, Claude | project lifecycle \\| milestones audits summary |
| `gsd-ns-review` | Agents, Claude | quality gates \\| code review debug audit security eval ui |
| `gsd-ns-workflow` | Agents, Claude | workflow \\| discuss plan execute verify phase progress |
| `gsd-pause-work` | Agents, Claude, Codex | Create context handoff when pausing work mid-phase |
| `gsd-phase` | Agents, Claude | CRUD for phases in ROADMAP.md — add, insert, remove, or edit phases |
| `gsd-plan-milestone-gaps` | Codex | Create phases to close all gaps identified by milestone audit |
| `gsd-plan-phase` | Agents, Claude, Codex | Create detailed phase plan (PLAN.md) with verification loop |
| `gsd-plan-review-convergence` | Agents, Claude | Cross-AI plan convergence loop — replan with review feedback until no HIGH concerns remain. |
| `gsd-plant-seed` | Codex | Capture a forward-looking idea with trigger conditions — surfaces automatically at the right milestone |
| `gsd-pr-branch` | Agents, Claude, Codex | Create a clean PR branch by filtering out .planning/ commits — ready for code review |
| `gsd-profile-user` | Agents, Claude, Codex | Generate developer behavioral profile and create Claude-discoverable artifacts |
| `gsd-progress` | Agents, Claude, Codex | Check progress, advance workflow, or dispatch freeform intent — the unified GSD situational command |
| `gsd-quick` | Agents, Claude, Codex | Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents |
| `gsd-reapply-patches` | Codex | Reapply local modifications after a GSD update |
| `gsd-remove-phase` | Codex | Remove a future phase from roadmap and renumber subsequent phases |
| `gsd-remove-workspace` | Codex | Remove a GSD workspace and clean up worktrees |
| `gsd-research-phase` | Codex | Research how to implement a phase (standalone - usually use /gsd-plan-phase instead) |
| `gsd-resume-work` | Agents, Claude, Codex | Resume work from previous session with full context restoration |
| `gsd-review` | Agents, Claude, Codex | Request cross-AI peer review of phase plans from external AI CLIs |
| `gsd-review-backlog` | Agents, Claude, Codex | Review and promote backlog items to active milestone |
| `gsd-secure-phase` | Agents, Claude, Codex | Retroactively verify threat mitigations for a completed phase |
| `gsd-session-report` | Codex | Generate a session report with token usage estimates, work summary, and outcomes |
| `gsd-set-profile` | Codex | Switch model profile for GSD agents (quality/balanced/budget/inherit) |
| `gsd-settings` | Agents, Claude, Codex | Configure GSD workflow toggles and model profile |
| `gsd-ship` | Agents, Claude, Codex | Create PR, run review, and prepare for merge after verification passes |
| `gsd-sketch` | Agents, Claude | Sketch UI/design ideas with throwaway HTML mockups, or propose what to sketch next (frontier mode) |
| `gsd-spec-phase` | Agents, Claude | Clarify WHAT a phase delivers with ambiguity scoring; produces a SPEC.md before discuss-phase. |
| `gsd-spike` | Agents, Claude | Spike an idea through experiential exploration, or propose what to spike next (frontier mode) |
| `gsd-stats` | Agents, Claude, Codex | Display project statistics — phases, plans, requirements, git metrics, and timeline |
| `gsd-surface` | Agents, Claude | Toggle which skills are surfaced — apply a profile, list, or disable a cluster without reinstall |
| `gsd-thread` | Agents, Claude, Codex | Manage persistent context threads for cross-session work |
| `gsd-ui-phase` | Agents, Claude, Codex | Generate UI design contract (UI-SPEC.md) for frontend phases |
| `gsd-ui-review` | Agents, Claude, Codex | Retroactive 6-pillar visual audit of implemented frontend code |
| `gsd-ultraplan-phase` | Agents, Claude | [BETA] Offload plan phase to Claude Code's ultraplan cloud; review in browser and import back. |
| `gsd-undo` | Agents, Claude | Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks. |
| `gsd-update` | Agents, Claude, Codex | Update GSD to latest version with changelog display |
| `gsd-validate-phase` | Agents, Claude, Codex | Retroactively audit and fill Nyquist validation gaps for a completed phase |
| `gsd-verify-work` | Agents, Claude, Codex | Validate built features through conversational UAT |
| `gsd-workspace` | Agents, Claude | Manage GSD workspaces — create, list, or remove isolated workspace environments |
| `gsd-workstreams` | Agents, Claude, Codex | Manage parallel workstreams — list, create, switch, status, progress, complete, and resume |
