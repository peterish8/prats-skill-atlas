# Verification, recovery, and stopping

## Progressive verification

Use the cheapest reliable feedback first, then broaden in proportion to impact:

1. parser or syntax check;
2. formatter and lint;
3. type or schema validation;
4. focused unit tests;
5. affected subsystem tests;
6. integration or contract tests;
7. architecture and static checks;
8. broader regression suite;
9. UI, device, deployed-service, end-to-end, or expensive benchmark checks.

Build output does not prove browser behavior, device behavior, live integrations, accessibility, security, or deployment. Report each evidence boundary honestly.

## Builder and evaluator

The builder may self-review, but cannot be the sole judge for meaningful changes. The lead must inspect the actual diff and deterministic evidence. Use a distinct reviewer when risk, subjectivity, or independent challenge justifies the cost.

## Failure taxonomy

Classify before retrying:

- requirement misunderstanding;
- implementation defect;
- architecture issue;
- test or benchmark defect;
- environment or external-service issue;
- missing tool or authority;
- bad decomposition or overlapping ownership;
- insufficient context;
- performance regression;
- worker capability limit.

Choose a response supported by that class: targeted feedback, new evidence, different worker, lead investigation, architecture decision, contract correction, or harness improvement. Do not send the same unchanged task to the same worker a third time.

## Benchmark integrity

Record the baseline, environment, corpus, correctness, aggregation method, repeated runs, failed runs, median and tail values when relevant, resource use, and confidence limits when available. Change one important variable at a time.

Never report only the best run, remove hard cases, weaken correctness, change the benchmark to hit the target, hard-code answers, or invent cost, token, latency, or quality measurements. Distinguish capability evaluation from regression evaluation.

## Stop conditions

- **Success:** acceptance criteria and applicable verification pass.
- **Diminishing returns:** expected value of another iteration is below its cost or merge risk.
- **External limit:** a service, device, credential, or unavailable tool blocks local proof.
- **Budget limit:** agreed time, token, cost, concurrency, or retry budget is reached.
- **Judgment required:** product, design, risk, or tradeoff choice belongs to the user.
- **Unrealistic target:** evidence shows the target cannot be met safely without violating higher-priority requirements.
- **Blocked or unsafe:** authority, scope, or safe execution is missing.

Every failed iteration must produce information. Stop rather than repeating a path that no longer has a justified chance of changing the result.
