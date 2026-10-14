---
name: authorized-bug-bounty-research
description: Run authorized bug-bounty research with explicit scope gates, passive-first mapping, low-volume hypotheses, and controlled evidence.
---

# Authorized Bug-Bounty Research

Use this skill only when the user is researching a named, authorized bug-bounty or vulnerability-disclosure program. The goal is a reproducible, in-scope security finding—not the largest scan or the most dramatic claim.

## Hard authorization gate

Before any request, mutation, script, or active probe:

1. Read the program brief and extract exact in-scope targets, exclusions, testing rules, account requirements, rate limits, and disclosure terms.
2. Match the exact hostname, app, API, or endpoint to an explicit in-scope entry. A subdomain, redirect, JavaScript reference, certificate, DNS result, API response, or parent wildcard does not grant permission.
3. Confirm the action is allowed, the account/data is controlled by the researcher, and the expected request count is proportionate.
4. If scope, authorization, identity, or impact is unclear, classify the target as `UNCLEAR — DO NOT TEST` and stop.

Never infer permission from technical reachability. Do not continue after seeing another user's data, a rate-limit warning, account lockout, service instability, or an unexpected destructive effect.

## Operating workflow

### 1. Intake and scope record

Create or update one program folder with `scope.md`, `rules.md`, `targets.txt`, `notes.md`, and evidence folders. Record the source URL and date checked. Treat a copied brief as provisional until the live brief is checked for changes.

### 2. Passive understanding first

Use the visible application, normal user flows, public documentation, browser DevTools, and an intercepting proxy to map features and legitimate requests. Record the feature, exact endpoint, method, authentication, roles, object identifiers, parameters, response fields, ownership, state transitions, potential security question, and testing status.

Do not turn passive discovery into permission to probe newly found infrastructure.

### 3. Choose one high-signal hypothesis

Prefer hypotheses testable with the researcher's own accounts and objects:

- Horizontal authorization: Account A must not read or change Account B's object.
- Vertical authorization: a lower-privilege role must not perform a higher-privilege action.
- Server-side enforcement: a hidden or disabled UI action must still be denied by the server.
- Business logic: an action must not work twice, out of order, after expiry, or after access is revoked.
- API exposure or mass assignment: the response/request must not expose or accept fields beyond the user's authority.
- Session or account-linking mistakes: a token, invitation, reset, or link must not cross accounts or states.

Change one variable at a time. For two-account testing, use one object created by each account and make one controlled comparison. Never enumerate identifiers after a single authorization failure or success.

### 4. Explain before testing

For a beginner, explain what is being checked, why it could be unsafe, secure behavior, the exact request or UI action, the one changed value, and what result would indicate a bug versus a secure denial.

### 5. Execute minimally

Prefer manual or semi-manual work: browser DevTools, Burp Repeater, curl, or a small PowerShell/Python helper. Default to one request at a time, low concurrency, bounded timeouts, and minimal test data. Do not run broad discovery, brute force, credential attacks, denial-of-service tests, mass account creation, large downloads, or aggressive fuzzing unless the program explicitly permits a narrowly configured test.

If a helper is needed, place it under the program's `scripts/` folder. It must require a non-empty explicit target, print the hostname, enforce a request limit and timeout, log redacted activity, and stop on unexpected responses.

### 6. Record and classify

Log timestamp, program, target, scope match, endpoint, request, expected result, observed result, request count, impact, and next safe step. Redact cookies, bearer tokens, passwords, personal data, and unrelated identifiers.

Use `IDEA`, `TESTING`, `CONFIRMED`, `FALSE POSITIVE`, `NEEDS REVIEW`, or `REPORTED`. Do not call something a vulnerability without scope confirmation, reproducibility, and real security impact.

When a finding is confirmed, hand off to `bug-bounty-report-writing`. The report skill must use only observed evidence and must not invent exploitability, severity, affected users, or remediation certainty.

## Safety boundary

This skill does not authorize testing. Program rules and explicit target scope control every action. It must stop rather than broaden scope, access unrelated data, evade defenses, impair availability, or perform post-exploitation.

## References

- Read [references/methodology.md](references/methodology.md) for source-backed test heuristics and learning links.
