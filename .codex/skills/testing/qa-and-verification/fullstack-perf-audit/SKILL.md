---
name: fullstack-perf-audit
description: >
  Self-bootstrapping production audit of a web app or website — bug hunt plus
  load-speed and runtime-performance analysis. Phase 0 makes you build your own
  repo context (stack, entry points, live URL, pain-point signals) before
  auditing, so nothing needs to be filled in by the user. Use when the user says
  "audit this app/site", "why is my site slow", "production audit", "performance
  audit", "find bugs and perf issues", "debug + speed up this codebase", or
  invokes /fullstack-perf-audit. Report first, fixes only on go-ahead.
---

# Full-stack debug + performance audit

## Role

You are a senior full-stack engineer doing a paid production audit. You have full
read access to the repository and a terminal. Do not ask the user questions —
investigate the codebase yourself and only surface findings + fixes.

## Mission

Work the 4 phases below **in order**. Do not skip ahead. Use actual tools — grep,
read files, run the build, check bundle output, search the web when unsure. Never
guess.

---

## Phase 0 — Self-discovery (build your own context first)

Before anything else, inspect the repo and determine, from real evidence (files,
configs, lockfile, git remote/readme) — not assumptions:

- Stack: framework(s), language, styling, state management, DB/backend, hosting
- Entry points and routing structure
- Live URL if discoverable (readme, `package.json` `"homepage"`, deploy config,
  `vercel.json` / `vercel.ts` / `netlify.toml`, env files) — note if none found
- Repo root / monorepo structure (single app vs multiple packages)
- Pain points implied by the code itself: TODO/FIXME/HACK comments, disabled
  tests, commented-out optimizations, recent commit messages mentioning "fix",
  "slow", "bug", "perf" (check `git log --oneline -30`)

Write this out explicitly as a short **CONTEXT block** (Stack / Entry points /
Live URL / Pain-point signals found). This is the context a human would normally
have had to hand you — you just built it yourself. Use it to steer Phases 1–3
(e.g. skip backend-query checks if there's no backend; prioritize areas near
recent "fix"/"slow" commits).

---

## Phase 1 — Map the codebase (deepen the Phase 0 context)

1. Walk the directory tree and build a mental model: routing, data layer, state
   management, build config, API/backend calls, third-party SDKs.
2. Identify the render path for the 2–3 heaviest / most-visited pages.
3. Check `package.json` / lockfile for bloated, duplicate, or outdated deps
   (anything with a known lighter alternative — e.g. moment.js → date-fns).
4. Note the build tool config (`next.config`, `vite.config`, webpack) — flag
   missing optimizations (no image domains config, no compression, source maps
   shipped to prod, etc).

**Output:** a short architecture summary + a prioritized list of suspects before
you touch anything.

---

## Phase 2 — Bug hunt (correctness first, not style)

Search for real, exploitable/breaking bugs, not lint nitpicks:

- Race conditions (unawaited async, stale closures in `useEffect`/hooks,
  double-fetch on mount, missing cleanup/aborts)
- Null/undefined access on async data before it resolves
- Off-by-one / boundary errors in loops, pagination, array slicing
- Memory leaks: uncleared intervals/listeners/subscriptions
- Incorrect memoization (missing deps, or memoizing something that should re-run)
  causing stale UI or wasted recompute
- N+1 query patterns (a loop that calls DB/API per item instead of batching)
- Error boundary / try-catch gaps that let failures fail silently
- Type mismatches TypeScript is currently allowing via `any` / `as`
- Security-adjacent correctness bugs: unvalidated input reaching a query, missing
  auth checks on an API route, secrets in the client bundle

For every bug: **file:line**, root cause in 1–2 sentences, minimal diff to fix,
and how you verified it (e.g. "confirmed via grep — no cleanup function in this
useEffect").

---

## Phase 3 — Performance: load speed + runtime efficiency

### A) Loading / network (LCP, TTFB, bundle size)

- Run the production build and read the actual bundle output/stats. Flag the top
  5 largest chunks and why they're that big.
- Code-splitting gaps: heavy components/libs loaded eagerly that could be
  dynamic-imported (`next/dynamic`, `React.lazy`)
- Images: correct format/sizing/lazy-loading (`next/image` or equivalent used
  properly; no unoptimized full-res images shipped)
- Fonts: preloaded/subset vs render-blocking
- Unnecessary client-side JS for content that could be server-rendered or static
- Waterfall requests that could be parallelized or batched
- Caching: HTTP cache headers, CDN usage, missing memoization of expensive server
  calls, no revalidation strategy

### B) Runtime / algorithmic efficiency (LLD + DSA lens)

For every hot path (render loop, search/filter/sort on data, list rendering,
state updates):

- State the current time/space complexity (e.g. "O(n²) — nested `.find()` inside
  a `.map()` over the same array")
- Propose the optimal data structure/algorithm for the access pattern (swap array
  `.find()` lookups for a `Map`/`Set` index built once; debounce/throttle
  high-frequency handlers; virtualize long lists with windowing instead of
  rendering all DOM nodes; use a min-heap instead of re-sorting on every update)
- Flag unnecessary re-renders: components re-rendering on unrelated state changes,
  missing `key` causing full remounts, prop drilling causing cascade re-renders
  where context/selector-based state would isolate it
- Flag redundant recomputation: expensive derived values recalculated every render
  instead of memoized

### C) Backend / data layer (if applicable)

- Missing indexes for the actual query patterns being run
- Over-fetching (selecting full documents/rows when only a few fields are used)
- Sequential awaits that could run in parallel (`Promise.all`)

---

## Research step (whenever you're unsure)

If you hit a library/framework-specific question you're not 100% sure of — current
best practice, a deprecated API, a known perf bug in a dependency version you find
in the lockfile — search the web for the current docs or changelog before
proposing a fix. Don't guess at library behavior.

---

## Output format

1. **Architecture summary** (5–10 lines)
2. **Bug list** — ranked by severity (breaks prod > silent data corruption >
   UX-visible > edge case), each with file:line + fix
3. **Performance findings** — ranked by expected impact on load time / runtime,
   each with: current complexity/behavior → proposed fix → expected gain
4. **Prioritized action list** — top 5 changes to make first, in order, with the
   reasoning for that order (effort vs impact)

Then, **with the user's go-ahead**, implement the top 5 fixes directly in the
codebase, one at a time, re-running the build/tests after each to confirm nothing
broke.

---

## Repeat runs

Once the codebase is known, the user can say "skip Phase 0, use this context: …"
and paste the CONTEXT block from a previous run. Honor that and start at Phase 1.
