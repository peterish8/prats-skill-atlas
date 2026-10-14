---
name: bug-bounty-report-writing
description: Write and quality-check evidence-first bug-bounty reports from verified, in-scope findings without inventing proof or impact.
---

# Bug-Bounty Report Writing

Use this skill when a security issue has been observed during authorized research and the user needs a finding record, triage-ready report, or submission draft.

## Evidence gate

Do not write a confirmed-vulnerability report from a suspicion, scanner output, changed status code, or unverified video. Before drafting, confirm that the exact target is in scope, the behavior is reproducible with researcher-controlled accounts/data, the security impact is real and demonstrated, the issue is not excluded, and the evidence is minimal, redacted, and sufficient for reproduction.

If any item is missing, label the record `IDEA`, `TESTING`, `NEEDS REVIEW`, or `FALSE POSITIVE` and state the missing proof.

## Report structure

Produce a concise report with:

1. **Title** — affected component + vulnerability + concrete impact.
2. **Target and scope confirmation** — exact URL, app, hostname, program, and matching scope entry.
3. **Severity suggestion** — Bugcrowd VRT baseline and a short impact-based rationale; never present it as guaranteed.
4. **Summary** — two to four sentences describing the defect and attacker outcome.
5. **Prerequisites** — authentication, role, account count, user interaction, and researcher-controlled setup.
6. **Steps to reproduce** — numbered, deterministic, minimal, and replayable.
7. **Request(s)** — only the relevant sanitized HTTP request or UI action; redact tokens and personal data.
8. **Response(s)** — only the relevant sanitized response and status; include stable evidence of unauthorized read/write/action.
9. **Expected behavior vs actual behavior** — explicit comparison.
10. **Security impact** — realistic attacker story, affected confidentiality/integrity/availability, scope, and limits.
11. **Evidence** — filenames for screenshots, recordings, logs, or proof-of-concept code; keep the smallest useful set.
12. **Accounts and data used** — identify Account A/B and synthetic object labels without secrets or unnecessary PII.
13. **Request count and safety** — number of requests, test window, and confirmation that no unrelated data or destructive action was used.
14. **Suggested remediation** — conceptual server-side fix, such as checking authorization against the authenticated principal and object on every request.
15. **Confidence and status** — `CONFIRMED`, `NEEDS REVIEW`, or another workspace status.

## Quality checks

Before presenting the draft:

- Re-run the exact reproduction steps from a clean state.
- Check every URL, parameter, role, and object ID for accuracy.
- Separate observed impact from possible downstream impact.
- Remove secrets, session cookies, passwords, real customer data, and unnecessary identifiers.
- Explain why the result is a security issue rather than intended product behavior.
- Mention excluded categories or duplicate uncertainty when relevant.
- Keep the proof short; a clear request/response comparison is usually better than a dramatic narrative.
- Do not include weaponized automation, persistence, evasion, or post-exploitation instructions.

## Workspace output

For a local record, write the finding under `programs/<program>/findings/<finding-name>.md`. For a submission draft, write under `programs/<program>/reports/`. Preserve original evidence and never overwrite it with redacted copies; create a separate sanitized artifact.

## References

- Read [references/report-quality.md](references/report-quality.md) for source-backed quality guidance and report links.
