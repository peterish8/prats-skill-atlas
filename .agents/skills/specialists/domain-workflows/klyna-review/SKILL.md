---
name: klyna-review
description: Review a Klyna pull request against main and its issue, then prepare exact GitHub inline comments, an approval, or a clean LGTM using the repository review style.
allowed-tools: Bash(git *) Bash(gh *) Bash(rg *) Bash(cargo *) Bash(powershell *)
---

# Klyna pull request review

Use this skill when the user supplies a Klyna PR number or URL and asks for a proper review, line comments, suggestions, approval, or LGTM.

## Review context

- Repository: `klynaio/klyna`.
- Intended checkout: `<USER_HOME>\Desktop\klynaorg\klyna`.
- Review account: `<GITHUB_USER>`.
- Base branch: latest `main`.
- Read `mvp/workflow.md` completely and read root or relevant nested `CLAUDE.md` files if present. If no `CLAUDE.md` exists, use `CONTRIBUTING.md`, `AGENTS.md`, and the workflow.
- Use authenticated `gh` for GitHub data. Do not use Firecrawl or expose GitHub credentials.

## Inspect before judging

1. Fetch the latest base and the PR head without replacing the user's current worktree, for example with `git fetch origin main refs/pull/<number>/head:refs/remotes/origin/pr-<number>`.
2. Read the full PR metadata: title, body, author, state, draft status, commits, changed files, existing comments, reviews, requested reviewers, and CI checks.
3. Read the linked issue and its acceptance criteria, dependencies, and relevant PRD/workflow sections. If the PR is closed or merged, report that before considering a comment.
4. Review the three-dot diff against the merge base and inspect enough surrounding code, tests, schemas, and callers to understand behavior. Use exact changed-file line numbers from the PR head.
5. Run relevant local tests or verification when practical. Otherwise report the actual GitHub CI result and do not claim local commands were run. Never invent a failure, test result, maintainer request, or project fact.

## What to review

Prioritize correctness over style. Follow `mvp/workflow.md`: look for contract violations, missing acceptance criteria, incorrect state transitions, data loss, silent error swallowing, concurrency or cancellation bugs, security issues, and missing deterministic tests. Skip formatting and naming nits handled by fmt, clippy, or CI. Separate:

- blocker or change-request findings that can make the PR wrong or unsafe;
- non-blocking suggestions that improve maintainability or test coverage;
- no-findings approval when the implementation and tests satisfy the issue.

Check for the kinds of failures that appeared in this repository's reviews: a state append that violates the store's required lifecycle, an error propagated with `?` after a WAL intent without recording a failure event, a dropped run handle that prevents cancellation, a test that hides a required production precondition, and an implementation that only works with a mock while the real interface cannot run. Use these as review prompts, not automatic findings; verify each one against the current diff and docs.

## Inline comment style

When a finding is tied to code, post it as a GitHub pull-request review comment attached to the exact changed line, not as a general issue comment. Use the right side of the PR diff, the PR head commit SHA, and the changed file path. Keep the range tight.

Write like a careful teammate:

- start with `Blocker:` or a concise priority when severity warrants it;
- explain the concrete behavior, impact, and why the current code causes it;
- point to the relevant contract or acceptance criterion;
- suggest the smallest direction for a fix and a test;
- use one short paragraph or a few readable paragraphs;
- do not use generic praise, corporate wording, AI/tool mentions, fake certainty, or style nits.

Example shape:

```text
Blocker: the intent event is written before this call, but this error path returns without recording the matching failure. A real startup or I/O error leaves the run looking active and bypasses the retry path. Please persist the failure before returning and add a driver-error test.
```

## Posting policy and API

Reviewing is read-only until the exact proposed action is clear. Before posting any external review, show the user the PR URL, finding severity, file and line, exact comment body, and whether the review will be `COMMENT`, `REQUEST_CHANGES`, or `APPROVE`. Ask for approval unless the user already explicitly approved the exact prepared review in the current turn. Never post a draft review accidentally.

After approval, use the GitHub pull-request review endpoint so comments render inline:

```text
gh api repos/klynaio/klyna/pulls/<number>/reviews --method POST --input -
```

The JSON payload must include the PR head `commit_id`, a review `event`, an optional overall body, and a `comments` array. Each inline comment must include `path`, `line`, `side: "RIGHT"`, and `body`. One review can contain multiple inline comments. Verify afterward with `gh api repos/klynaio/klyna/pulls/<number>/comments` and report the discussion URLs.

Use `REQUEST_CHANGES` only for verified blocking findings and only when the user asks for a formal requested-changes review or approves that event. Use `COMMENT` for suggestions or a review that should not change the PR state. If there are no findings, prepare a concise approval or LGTM that states what was checked. Do not approve a PR authored by `<GITHUB_USER>`; explain that GitHub disallows self-approval and use a comment if the user wants one.

If the PR has existing valid review comments, do not duplicate them. Review the current diff and add only new, actionable findings. If CI is still running, say so; do not treat an absent check result as green. Never merge or edit the PR branch while reviewing.

