# Measurement data for a performance investigation

Collect only what is needed to make a repeatable comparison. Start with existing project data and mark missing values as unknown; do not fill gaps with guesses. The HTML plan must distinguish measurements, estimates, hypotheses, and unknowns.

## Minimum useful setup

| Input | What to capture | Why it matters |
|---|---|---|
| Journey or workload | User action, start boundary, successful end boundary, representative input and size | Keeps the benchmark tied to the time the user actually waits |
| User outcome | Wall-clock duration, frame smoothness, throughput, memory, CPU, startup time, or another directly relevant measure | Prevents optimizing a convenient but irrelevant proxy |
| Environment | Commit/build, OS, browser/runtime, device or machine class, network/backend conditions, cache state, and other conditions that materially affect the result | Makes before/after runs comparable |
| Baseline | Value and unit, statistic used, number of runs, spread/noise, date, and exact run procedure | Shows both current performance and confidence in the result |
| Evidence | Existing trace, profile, telemetry, logs, benchmark output, and the exact hot span/resource | Connects a candidate fix to an observed cost |
| Success and guardrails | Desired outcome or target, correctness requirements, and any CPU/memory/battery/network or compatibility limits | Defines a win without allowing quality regressions |

There is no universal sample count or acceptable latency. Repeat enough times to understand variation for this workload and environment. Report the statistic that matches the decision (for example median for a typical run, or a tail percentile for a tail-latency problem) and say when the sample is too small to support it.

## Useful extras

- Production journey frequency and distribution, anonymized where needed.
- p50/p95/p99 or other tail data when the complaint concerns outliers.
- Cold-start versus warm-cache runs, low-end versus high-end hardware, and realistic network conditions.
- A profiler or trace with attribution across UI, runtime, network, storage, and server work.
- Existing performance budgets, release gates, related incidents, and known benchmark flakiness.
- Dataset size and shape, concurrency, and throughput if the workload is not a single-user journey.
- A user-provided screen recording or reproduction steps when visual jank or interaction delay is involved.

## If evidence is missing

Do not call a code path the cause based on appearance alone. Write down the narrowest measurement needed to distinguish plausible causes. First use existing read-only tools and instrumentation. If new app instrumentation or benchmark code is necessary, include it in a measurement-only HTML plan and wait for approval before adding it. Re-measure the real journey after instrumentation; only then propose an optimization.

Do not run production load, alter production telemetry, incur paid profiling costs, or access restricted user data without explicit authorization.

## Copyable intake record

Adapt this record to the project. Leave unknowns null and explain why they are unavailable.

    case:
      project:
      reported_symptom:
      journey:
      start_event:
      end_event:
      representative_workload:
      target_population_or_device:
      environment:
        commit_or_build:
        platform_and_version:
        device_or_machine:
        runtime_or_browser:
        network_and_backend:
        cache_or_start_state:
      baseline:
        metric:
        unit:
        statistic:
        value:
        sample_count:
        variation_or_confidence:
        captured_at:
        run_procedure:
      evidence:
        telemetry:
        trace_or_profile:
        logs_or_benchmark:
        suspected_hot_span:
      goal:
      correctness_guardrails:
      resource_guardrails:
      measurement_gaps:
      approval_status: pending
