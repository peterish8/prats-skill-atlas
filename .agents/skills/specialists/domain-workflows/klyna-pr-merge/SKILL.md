---
name: klyna-pr-merge
description: Verify that requested Klyna PR changes were correctly delivered, then approve and merge a green PR when the user explicitly asks to merge if it is good.
allowed-tools: Bash(git *) Bash(gh *) Bash(rg *) Bash(cargo *) Bash(powershell *)
---

# Klyna PR change verification and merge

Use this skill after Klyna review feedback has been implemented and committed to the same pull request. It is for requests such as "check the changes and merge if good." It is not for initial PR review or for writing the requested changes.

## Repository context

- Repository: `klynaio/klyna`.
- Checkout: `<USER_HOME>\Desktop\klynaorg\klyna`.
- Review account: `<GITHUB_USER>`.
- Base branch: latest `main`.
- Read `mvp/workflow.md` fully. Read any applicable `CLAUDE.md`; if none exists, use `CONTRIBUTING.md` and `AGENTS.md` when present.
- Use authenticated `gh` and local Git. Do not use Firecrawl for GitHub data and never expose credentials.

## Verify the follow-up, not merely the latest commit

1. Fetch `origin/main` and the PR head into a remote-tracking ref without checking out or changing the user's worktree.
2. Read the open PR's metadata, linked issues, latest head SHA, commits, changed files, reviews, inline comments, review threads, mergeability, and every CI check.
3. Identify every actionable review thread and formal change request that the current user previously made, normally authored by `<GITHUB_USER>`. Read the original requested behavior, its review commit, replies, and the full current diff from merge base to head.
4. Inspect the code and tests around each fix. Confirm each request is fixed by the current head, not just acknowledged in a reply. Review for any newly introduced correctness, contract, state, cancellation, persistence, or deterministic-test regression.
5. Run focused local tests when practical without disturbing the current worktree. Otherwise rely on the actual PR CI result and say that local tests were not run. Never claim a test passed without evidence.

Treat a change as incomplete when it only changes a test without proving the production behavior, it hides the original failure, it violates an issue acceptance criterion, or it leaves a related actionable review thread unanswered.

## Decide what happens next

### More changes are needed

Do not post a second review, resolve conversations, approve, merge, edit the PR, or alter the author branch. Report in chat only:

- PR URL and the specific unaddressed request or new finding;
- severity, changed file and exact PR-head line when applicable;
- the exact concise comment body that would be posted;
- current CI and mergeability.

Then stop and wait for the user to explicitly say to post those second-round changes. Do not infer that permission from a prior review request.

### The changes are good

Only continue automatically when the user explicitly asked to merge if the PR is good. Otherwise report the clean result and wait.

Before merging, require all of the following:

- PR is open, not draft, mergeable, and clean against current `main`;
- the linked issue acceptance criteria and the user's earlier review requests are satisfied;
- all required CI checks are completed successfully. Report advisory/non-blocking checks exactly as GitHub reports them;
- no unresolved actionable thread remains;
- the Klyna workflow's required approval is present. If the prior `<GITHUB_USER>` request-changes review is the only blocker and the PR author is someone else, submit one concise `APPROVE` review for the current head and resolve only the verified threads authored by `<GITHUB_USER>`.

Never approve a PR authored by `<GITHUB_USER>`. If that would leave the required independent approval missing, report the blocker instead of merging. Do not create duplicate approvals, replies, or comments. For GraphQL conversation resolution, first query and use the exact `reviewThread.id`; never guess an ID.

## Merge method

Use the user's requested distinction, even though the general workflow usually squash-merges:

- For a small cleanup or focused review correction, squash merge and delete the source branch: `gh pr merge <number> --squash --delete-branch`.
- For a larger integration/tie-up PR that genuinely spans multiple linked issues or coordinated modules, use a regular merge commit and delete the source branch: `gh pr merge <number> --merge --delete-branch`.

Do not decide "large" based only on line count. Use linked issues and coordinated scope. If the merge mode is genuinely unclear, report the evidence and ask the user before merging.

After the merge, verify the PR is `MERGED`, record the merge commit, confirm linked issues closed or their actual remaining state, and watch the `main` CI to completion when one is triggered. Report the PR URL, merge method, commit, issue state, and exact CI outcome.

