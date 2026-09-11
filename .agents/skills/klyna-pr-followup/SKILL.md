---
name: klyna-pr-followup
description: Address requested changes on an existing Klyna pull request by fixing review feedback on the same branch, testing it, and pushing the update to that PR.
allowed-tools: Bash(git *) Bash(gh *) Bash(rg *) Bash(cargo *) Bash(powershell *)
---

# Klyna PR follow-up

Use this skill when the user pastes a Klyna PR URL or number and asks to fix reviewer comments, address requested changes, update the PR, or push a revision.

## Fixed repository conventions

- Repository: `klynaio/klyna`.
- Intended checkout: `<USER_HOME>\Desktop\klynaorg\klyna`. Do not use the old Documents checkout.
- GitHub account and fork owner: `<GITHUB_USER>`.
- DCO email: `<EMAIL>`.
- The base branch is `main`. The normal upstream remote is `origin`; the user's work branches are pushed to `fork`.
- This is an existing-PR workflow. Never create a new branch, new PR, or draft PR. Never merge unless the user explicitly asks.

## Read the request before changing code

1. Confirm the supplied PR is open and identify its author, head repository/branch, base branch, latest head SHA, linked issue, CI state, reviews, review comments, and conversation threads.
2. Confirm the PR is authored by `<GITHUB_USER>` or that the user explicitly has authority to push to its head branch. If not, stop and explain that the source branch is not theirs to modify.
3. Read every actionable review request, including inline comments, replies, and formal `REQUEST_CHANGES` reviews. Use the current head and avoid re-solving comments that are already resolved or no longer apply.
4. Read `mvp/workflow.md` completely. Read root and relevant nested `CLAUDE.md` files if they exist. If no `CLAUDE.md` exists, state that briefly and use `CONTRIBUTING.md`, `AGENTS.md`, and the workflow instead.
5. Fetch latest `origin/main` for context and fetch the PR head. Do not rebase, merge `main`, force-push, or replace the PR branch unless the user explicitly asks. The review fix must stay on the existing PR branch.

## Safely enter the PR branch

- Check the current worktree first. If it contains unrelated changes, stop rather than overwriting or mixing them into the PR.
- Check out the existing head branch or create only a local tracking branch for that already-existing remote branch. Do not derive a new feature branch.
- Fast-forward only when the local branch is behind the remote PR head. If it has unpushed commits or diverged, stop and report the exact state.
- Verify that `HEAD` matches the PR head SHA before editing.

## Implement reviewer feedback

- Translate each valid request into a concrete code/test change. Re-read the surrounding implementation and callers so the correction addresses the cause, not just the highlighted line.
- Follow the issue acceptance criteria and preserve the PR's intended scope. If a comment asks for work outside the issue or conflicts with the repo contract, explain the conflict and ask the user before expanding scope.
- Add or update deterministic tests for the regression or missing behavior requested by the reviewer. Do not add real API/provider calls to the suite.
- Keep a short checklist of each actionable comment and its corresponding change. Do not claim a comment is addressed until the changed code and test prove it.

## Verification and commit

Run the relevant targeted test first, then the Klyna workflow gates before pushing:

```text
cargo fmt --all --check
cargo test --workspace --locked
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo build --workspace --locked
git diff --check
```

Run warnings-as-errors docs when the revision changes a public Rust API or its documentation. Inspect the final diff and check only the edited files for TODOs, debug prints, commented-out code, secrets, and unrelated changes.

Stage only confirmed files, never `git add -A` or `git add .`. Verify that the repository-local Git identity uses `<EMAIL>`, then commit with a one-line imperative message and DCO signoff:

```text
git commit -s -m "<imperative follow-up message>"
```

Push the same existing branch to the PR head remote, normally:

```text
git push fork <existing-branch>
```

Never force-push unless the user explicitly authorizes it after seeing why it is required.

## Hand back the updated PR

After push, verify the PR still has the same number and correct head branch, the new commit is visible, and CI has started or passed. Report:

- each review request and the specific change/test that addressed it;
- commit SHA and branch pushed;
- exact local verification results and current GitHub CI status;
- any remaining unresolved or out-of-scope comment.

Do not resolve a reviewer conversation, add a reply, request re-review, approve, or merge unless the user explicitly asks. If the user asks to reply, write a short factual response tied to each exact thread and post it only after showing the exact text for approval.

