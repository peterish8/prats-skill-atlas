---
name: measurable-performance-engineering
description: Find and fix performance problems in websites, apps, APIs, and other software using representative workloads, repeatable measurements, and profiling evidence. Use when asked to diagnose, improve, or prevent performance regressions; show a dark HTML plan and wait for approval before implementation changes.
---

# Measurable Performance Engineering

Improve a user-visible outcome by measuring a representative journey, finding the dominant cost from evidence, and changing one focused slice at a time. Reading code can explain a result; it cannot replace a measurement.

## Required workflow

1. **Choose one journey or workload.** Translate the reported slowness into a start event, an end event, and a realistic input. Prefer high-impact journeys using available usage data. Keep the first slice narrow.
2. **Inventory evidence before proposing a fix.** Inspect existing telemetry, benchmarks, traces, profiler output, logs, and relevant code. Check whether the metric spans the full user-visible journey and separates client, network, and server time where useful. Do not treat a convenient sub-span as the user's full wait.
3. **Check whether the baseline is trustworthy.** Record the workload, environment, commit, run procedure, sample count, variation, and metric. Repeat noisy measurements. A deterministic proxy such as instruction count is useful only after showing that it tracks a user-relevant wall-clock outcome. Discard or repair a flaky benchmark that rewards the wrong behavior.
4. **Select the bottleneck from evidence.** Rank candidate slices by expected user impact, strength of evidence, implementation risk, and ongoing complexity. State what the profile or trace shows; label unverified explanations as hypotheses. Do not optimize unrelated code or pursue a tiny gain whose maintenance cost is larger.
5. **Present a reviewable plan before changing implementation.** Populate the supplied performance-plan HTML with the journey, measured baseline (or the fact that it is missing), evidence, proposed single slice, target, guardrails, risks, and a like-for-like verification procedure. Save a task-specific copy as a standalone HTML file and open it for the user. Keep it self-contained and readable in a browser without network access.
6. **Wait for explicit user approval.** Do not edit application source, add instrumentation or benchmark code, change build/CI configuration, or deploy before the user approves the plan. A request to “make it faster” is not approval to skip this review step. If evidence is too weak to name a defensible optimization, present a measurement-only plan first. After that is approved and measurements are collected, present a new optimization plan and wait again.
7. **Implement only the approved slice.** Preserve existing behavior and project contracts. If new evidence requires a materially different scope, stop and present an updated plan for approval.
8. **Measure the same workload again.** Hold environment, inputs, and measurement boundaries constant. Compare baseline and result with the same statistics; report uncertainty and correctness guardrails. Do not claim a gain when the difference is within measurement noise. Run the relevant existing checks needed to establish the requested outcome; avoid unrelated test suites.
9. **Leave a useful regression control when justified.** Propose a stable benchmark or CI threshold only if it is repeatable and correlates with the real user outcome. Prefer an evidence-backed threshold that tightens as results improve. Do not add a noisy gate just to have one.

## Missing or sensitive data

Read [references/measurement-data.md](references/measurement-data.md) when deciding what to collect. Use what the repository and user already provide; do not invent telemetry, thresholds, devices, or results. If key evidence is absent, put the gap and the smallest useful measurement setup in the HTML plan. Ask for access or missing context only when it blocks a useful next step. Treat production traces, account data, and paid profiling services as sensitive or potentially costly; use them only when the user has authorized that access.

## Plan artifact

Use [assets/performance-plan.html](assets/performance-plan.html) as the visual starting point. Replace every double-bracket placeholder, remove sections that do not apply, and clearly label estimates, hypotheses, unknowns, and measured facts. Default to a task-specific file under the repository's existing planning/artifact convention; if none exists, put it in a clearly named workspace artifact folder. Link or open the rendered file so the user can review the actual plan before implementation begins.

The plan should answer in plain language:

- What is slow, for whom, and in which repeatable journey?
- What was measured, in what environment, and how reliable is it?
- What evidence points to the proposed bottleneck?
- What is the smallest proposed change, and what is explicitly outside this slice?
- What result would count as success, and what behavior must not regress?
- How will the before/after comparison be repeated?
- What approval is needed before implementation?
