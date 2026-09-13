# Antigravity CLI routing

Use Antigravity as either the active orchestrator or a bounded worker. Do not create a nested committee by default: an Antigravity worker may spawn its own subagents only when the ticket explicitly grants a nested-agent budget.

## Refresh capability evidence

Before first use, and whenever the roster is stale, inspect rather than guess:

```text
agy --version
agy models
agy agents
agy --help
```

Record only model and agent slugs returned by the installed CLI. Availability and quota can change independently of the package version.

## Best-fit roles

- Fast model at medium effort: reconnaissance, codebase mapping, documentation lookup, test discovery, and mechanical transformations.
- Fast model at high effort: bounded debugging, implementation, or analysis before escalating to a more expensive model.
- Strong reasoning model at high effort: architecture, planning, integration advice, difficult debugging, or final review.
- A different available model family at high effort: independent critique of meaningful changes.
- A verified `gsd-*` specialist: use only when its name and scope match the worker ticket; the lead still evaluates its evidence.

These are routing defaults, not claims that one vendor is universally better. Prefer recorded user outcomes over the defaults.

## Safe headless dispatch

Use print mode for a bounded worker and request structured output when useful:

```text
agy -p "<worker ticket>" --sandbox --mode plan --model <verified-model-or-effort-variant> [--effort <compatible-level>] --agent <verified-agent> --output-format json --print-timeout <finite-duration>
```

Use the exact slug returned by `agy models`. When the slug already encodes an effort variant such as `-low`, `-medium`, or `-high`, do not also pass a conflicting `--effort`; AGY rejects that combination. Use `--effort` only with a compatible model selection verified by the current CLI. When explaining the rule, quote a slug from the current inventory or use a non-versioned placeholder—never fabricate a versioned model name as an example.

Use `--mode accept-edits` only for a write-enabled ticket with isolated ownership. Omit `--agent` when no listed specialist is a clear match. Inspect the JSON `status`, `response`, `error`, usage, denied actions, and artifacts; exit code zero does not prove every requested tool ran.

Never use `--dangerously-skip-permissions` as an orchestration convenience. Keep the sandbox on by default, grant only scoped permissions required by the ticket, and ask the user immediately before any risky action not already authorized.

## Native Antigravity features

Antigravity can run asynchronous subagents, inspect diffs and artifacts, and expose structured headless output. Treat `/boost` and paid teamwork modes as optional high-cost mechanisms: use them only when the task is genuinely complex and the roster permits the additional agent and quota cost.

Official references:

- https://antigravity.google/docs/skills
- https://antigravity.google/docs/cli/headless/
- https://antigravity.google/docs/cli/features/
