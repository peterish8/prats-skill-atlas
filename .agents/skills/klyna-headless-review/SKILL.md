---
name: klyna-headless-review
description: Automatically review and post a review on an eligible Klyna pull request after a trusted queue worker receives a review assignment for <GITHUB_USER>.
allowed-tools: Bash(git *) Bash(gh *) Bash(rg *) Bash(cargo *) Bash(powershell *)
---

# Klyna headless pull-request review

Use this skill only for a queue worker processing a verified GitHub `review_requested` event for `klynaio/klyna`. This is the autonomous counterpart to `klyna-review`; do not use it for interactive, ad-hoc PR reviews.

## Eligibility and authorization

Automatic posting is explicitly authorized for an eligible event. Before inspecting or posting, verify all of the following from GitHub's current PR metadata:

- The PR is open and is not a draft.
- `<GITHUB_USER>` is currently a requested reviewer.
- The author is not `<GITHUB_USER>`.
- The event's PR number and head SHA still match the queued job.
- `<GITHUB_USER>` has not already submitted a review for that same head SHA.

If any check fails, stop without posting. Report the reason to the queue worker. Never merge, edit the PR branch, remove reviewers, or modify repository settings.

## Review context

- Repository: `klynaio/klyna`.
- Intended checkout: `C:\\Users\\nithy\\Desktop\\klynaorg\\klyna`.
- Review account: `<GITHUB_USER>`.
- Base branch: latest `main`.
- Use authenticated `gh` for GitHub data. Do not expose GitHub credentials.

Read `mvp/workflow.md` completely and read root or relevant nested `CLAUDE.md` files if present. If no `CLAUDE.md` exists, read `CONTRIBUTING.md`, `AGENTS.md`, and the workflow.

## Inspect before judging

1. Fetch the latest base and PR head without replacing a user's current worktree, for example with `git fetch origin main refs/pull/<number>/head:refs/remotes/origin/pr-<number>`.
2. Read full PR metadata: title, body, author, state, draft status, commits, changed files, existing comments, reviews, requested reviewers, and CI checks.
3. Read the linked issue and its acceptance criteria, dependencies, and relevant PRD/workflow sections.
4. Review the three-dot diff against the merge base. Inspect enough surrounding code, tests, schemas, and callers to understand actual behavior. Use exact changed-file line numbers from the PR head.
5. Run relevant local verification when practical. Otherwise report the actual GitHub CI result. Never invent a failure, test result, maintainer request, or project fact.

Prioritize correctness over style. Check for contract violations, missing acceptance criteria, incorrect state transitions, data loss, silent error swallowing, concurrency or cancellation bugs, security issues, and missing deterministic tests. Skip formatting and naming nits handled by fmt, clippy, or CI.

Treat these as prompts, not automatic findings: a state append that violates the store lifecycle, an error returned after a WAL intent without a matching failure event, a dropped run handle that prevents cancellation, a test hiding a required production precondition, or an implementation that works only with a mock while the real interface cannot run.

## Automatic posting policy

Post exactly one non-duplicate GitHub PR review after the review is complete:

- Use `REQUEST_CHANGES` only for verified blocking findings.
- Use `COMMENT` when there are only non-blocking suggestions, when required CI is pending or failed, or when review readiness is otherwise uncertain.
- Use `APPROVE` only when there are no actionable findings and all required CI checks have passed.

For code findings, attach inline comments to exact changed lines on the right side of the PR diff using the PR head commit SHA. Each comment must explain the concrete behavior and impact, cite the relevant contract or acceptance criterion, and give the smallest useful fix/test direction. Do not mention AI, tools, or this automation.

Use the pull-request review endpoint:

```text
gh api repos/klynaio/klyna/pulls/<number>/reviews --method POST --input -
```

The payload must contain `commit_id`, `event`, any concise overall body, and an inline `comments` array where appropriate. Each inline comment requires `path`, `line`, `side: "RIGHT"`, and `body`.

Verify the posted review with GitHub afterward. Report the PR URL, event used, each posted finding with its file/line, CI status, and the review/comment URLs to the queue worker. If posting fails, do not retry blindly: first re-read the PR head SHA and existing reviews to avoid posting a stale or duplicate review.

