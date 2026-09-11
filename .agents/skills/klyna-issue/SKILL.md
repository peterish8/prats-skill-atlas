---
name: klyna-issue
description: Solve a Klyna GitHub issue end to end using the repository workflow, tests, DCO commits, fork push, and a ready pull request.
allowed-tools: Bash(git *) Bash(gh *) Bash(rg *) Bash(cargo *) Bash(powershell *)
---

# Klyna issue workflow

Use this skill when the user gives a Klyna issue number or URL and asks to solve it, follow the workflow, push it, or create a PR.

## Fixed repository conventions

- Repository: `klynaio/klyna`.
- Intended checkout: `<USER_HOME>\Desktop\klynaorg\klyna`. Do not use the older Documents checkout.
- GitHub account and PR head owner: `<GITHUB_USER>`.
- DCO email: `<EMAIL>`.
- Upstream remote is normally `origin`; push work branches to the `fork` remote and open a cross-repository PR with head `<GITHUB_USER>:<branch>`.
- The base branch is `main`, never `master`.
- Use a ready PR, never a draft. Do not merge unless the user explicitly asks.

## Required instructions and issue context

Before editing:

1. Confirm the checkout, current branch, remotes, GitHub authentication, and clean worktree. If unrelated local changes exist, stop and report them instead of overwriting them.
2. Run `git pull` for the current tracked branch. Stop and report any pull failure or conflict before changing branches or starting issue work.
3. Read `mvp/workflow.md` completely. Read root and relevant nested `CLAUDE.md` files completely if present. If no `CLAUDE.md` exists, say so briefly and use `CONTRIBUTING.md`, `AGENTS.md`, and the workflow as the available repository instructions.
4. Fetch the latest `origin/main` and base the work on it. Never begin implementation from a stale base.
5. Read the issue with `gh issue view`, including its body, comments, labels, assignees, dependencies, and linked pull requests. Inspect the project board item and assign the issue to `<GITHUB_USER>`; move it to `In Progress` before coding.
6. Inspect the relevant modules, tests, CI configuration, and neighboring implementations before writing code. Do not use Firecrawl for private GitHub repository context; use authenticated `gh` commands and local Git data.

## Token-efficient execution

Use the `caveman` skill at the level that fits the issue after the initial repository and issue inspection:

- `lite` for cross-module, ambiguous, security-sensitive, or stateful work where compressed phrasing could hide an important dependency or decision.
- `full` for a normal contained Klyna issue. This is the default.
- `ultra` only for a clearly mechanical, low-risk change with a narrow acceptance criterion and an established local pattern.

Choose the lowest-detail level that preserves correct reasoning. Caveman changes communication and token use only: it never permits skipping issue context, code inspection, acceptance criteria, tests, verification gates, or final diff review. Use normal clear language for irreversible actions, commands the user must run, commit messages, PR titles/bodies, review comments, and security-sensitive explanations.

## Branch and identity

Derive one lowercase branch from the issue title using the workflow format:

`<type>/<issue-number>-<short-kebab-slug>`

Use `feat`, `fix`, `test`, `chore`, `docs`, or `refactor` as appropriate. Keep it under 50 characters and do not put an email address in the branch name. The GitHub owner is `<GITHUB_USER>`; the DCO identity must use `<EMAIL>`.

When the branch name is materially ambiguous, show the proposed name and ask before creating it. Otherwise create it from the fetched latest `main`, never from another feature branch.

Before committing, verify `git config user.email`. If it is not `<EMAIL>`, use the repository-local Git identity or an equivalent commit-scoped configuration so `git commit -s` produces the requested DCO signoff. Do not expose credentials or tokens in output.

## Implementation

- Implement the complete issue acceptance criteria, not a stub or placeholder.
- Preserve unrelated work and the existing product/code shape.
- Follow surrounding naming, error handling, comments, serialization, and test patterns.
- Add or update deterministic tests in the same PR. Mock external agents and network calls; never add real provider calls to the test suite.
- Keep one issue per branch and one logical task per commit unless the repository workflow requires otherwise.

## Verification gates

Run and fix failures before committing:

```text
cargo fmt --all --check
cargo test --workspace --locked
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo build --workspace --locked
```

Run documentation checks when the changed Rust API or docs warrant them:

```text
RUSTDOCFLAGS="-D warnings" cargo doc --workspace --no-deps --locked
```

Also run `git diff --check`, inspect the final diff, and check changed files for TODOs, debug prints, commented-out code, secrets, and unrelated edits. State exactly what passed and what was unavailable, including ignored real-provider tests.

## Mandatory self-review before push

After the implementation and first verification pass, commit the issue work locally but do **not**
push yet. Treat the issue body and its acceptance criteria as the spec, and review the branch
against the fetched base with `git diff origin/main...HEAD` plus the commit list.

Load and apply both of these review rubrics as a read-only pre-push gate:

- `<USER_HOME>\.agents\skills\review\SKILL.md` for separate standards and spec/acceptance-criteria review.
- `<USER_HOME>\.agents\skills\klyna-review\SKILL.md` for Klyna's contract-focused review method.

At this stage there is no PR to comment on. Do not call GitHub's review API, approve anything, or
write a draft review. Use the rubrics to inspect the local branch as if reviewing someone else's
PR. When available and useful, add a read-only specialist review for the risk in the change (for
example persistence/state, cancellation/process execution, input validation, or security). Do not
load unrelated review skills just to inflate the process.

The self-review must cover the full changed diff, affected callers, and the issue's acceptance
criteria. For Klyna runtime, health, driver, state, spec, or CLI changes, explicitly challenge:

- event lifecycle ordering, append-only persistence, serialization compatibility, and schema migration;
- every error path after a durable intent event, including retry and terminal transitions;
- cancellation, handle ownership, timeout, resource cleanup, and real-driver versus mock behavior;
- replay/resume at each durable crash boundary, including token/accounting correctness;
- overflow, numeric thresholds, deterministic ordering, and untrusted spec/input validation;
- deterministic regression tests that would fail on the bug being guarded against.

Fix every valid blocker or meaningful correctness/test-coverage finding before pushing. Re-run the
targeted tests and all verification gates after the last code change, commit the correction with
the same DCO rules, then repeat this self-review against `origin/main`. Continue until the review
has no unresolved valid findings. If a finding is genuinely ambiguous, conflicts with the issue
scope, or requires a product decision, stop and ask the user rather than pushing a known gap.

Before pushing, inspect the final diff one more time and retain concise evidence for the handoff:
base SHA, review scopes used, findings fixed (or a clean result), and exact verification commands.
Do not claim the code is perfect; report the evidence-backed clean review result.

## Commit, push, and PR

Stage only confirmed paths. Never use `git add -A` or `git add .`. Commit with a one-line imperative message under 72 characters:

```text
git commit -s -m "<imperative message>"
```

Run the mandatory self-review above after the initial local commit. If it produces a corrective
commit, repeat the review and verification before the first push.

Push to the fork:

```text
git push -u fork <branch>
```

Before opening the PR, compare the branch with `origin/main` and confirm the diff is exactly the issue work. Check recent merged PR titles and use the exact issue title for the PR title when that matches the repository convention. Open a ready PR:

```text
gh pr create --repo klynaio/klyna --base main --head <GITHUB_USER>:<branch> --title "<issue title>" --body "... Closes #<issue number> ..."
```

The body must contain `Closes #<issue number>`, describe the behavior and tests in plain human prose, and contain no DCO signoff, AI/tool mention, or draft marker. Request exactly one reviewer from the other two contributors, choosing the neighboring code owner according to `mvp/workflow.md`. Do not request the PR author or yourself.

After creation, verify the PR is open and not draft, the head/base are correct, the issue is linked, the requested reviewer is present, the project item is `Ready For Review`, and the worktree is clean. Report the PR URL, branch, commit, reviewer, project status, and precise verification results. Stop before merge.

