# One independent reviewer

Read when work qualifies for the single reviewer. This is a prompt/evidence contract, not a request to install another model. All review stays inside the one-distinct-subagent task ceiling.

## Dispatch

Prefer a fresh minimally primed context when available. Same-model review is allowed; different-model access is optional. Disclose limited context isolation where relevant.

Supply the actual spec, repo rules, task-owned diff/new files, baseline, affected consumers, and check results. Use exact paths instead of dumping the whole repo/conversation. Do not omit inconvenient evidence or suggest the verdict.

Freeze the implementation during review. Reviewer may inspect source/run safe local checks, and create artifacts only in its assigned disposable scratch directory. It may not modify production code, task tests, configuration, live data, or the skill. Inspect tests for paid/live side effects before execution.

## Prompt template

```text
Independently review this change against the supplied requirements.
You are the only subagent permitted for the entire task. Do not delegate,
spawn agents, invoke multi-agent workflows, or request another model.

Ownership: review and artifacts in [scratch path] only. You are not alone
in the codebase. Preserve existing edits. Do not fix production code or
change the author's tests/configuration. Do not mutate live services,
install packages, or expose sensitive content.

Inputs:
- Outcome/acceptance: [contract/path].
- Product/repo rules: [paths or bounded excerpts].
- Task baseline and actual diff/new files: [details].
- Relevant sources/consumers: [paths].
- Check results and baseline failures: [evidence].

Inspect the entire task diff and sufficient context. Use the repository
index when available. Stay inside this change's blast radius.

Check requirements, real-boundary validation/auth/ownership, persistence,
async failure paths, affected consumers/docs/config, complexity, test
strength, and whether verification/readiness claims are supported.

Each material finding needs severity, location, violated requirement,
concrete trigger, expected/actual outcome, evidence, and smallest fix.
Label untested suspicions as candidates. Keep style preferences separate.

Return PASS / CHANGES REQUIRED / INSUFFICIENT EVIDENCE, examined scope,
material findings, and checks actually run. PASS means no material issue
found in this review, not whole-system certification or human approval.
Do not invent findings to appear thorough.
```

## Triage

| Class | Meaning | Main-agent action |
| --- | --- | --- |
| Critical | Unauthorized action/exposure or serious data corruption/loss | Reproduce safely, fix and boundary test; otherwise remain blocked |
| Significant | Broken requirement/integration or likely regression | Validate trigger, fix and regression check |
| Minor material | Concrete localized defect with limited impact | Fix within scope when practical; disclose unresolved effect |
| Optional | Preference/future improvement without contract violation | Do not make a gate or expand scope |
| Candidate | Concern without adequate evidence | Investigate within budget; retain uncertainty if unproven |

Impact/reachability determine severity. Check false positives against the contract. Green tests do not automatically refute a finding; reviewer confidence does not establish it.

## Recheck

The main agent repairs and reruns affected checks. Reuse the same reviewer for at most one follow-up on fixes/consumers, within the two repair-cycle budget. Supply updated diff/evidence and retain the original findings.

If an earlier reviewer cannot resume, do not spawn a replacement: self-review and report the independent-review gap. No tool may create nested assistants under another name.
