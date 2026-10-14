---
name: website-bug-finder
description: Audit a website codebase and local runtime for reproducible, high-impact product and security bugs, with strict P1 evidence gates and reusable reports.
---

# Website Bug Finder

Use this skill when the user asks to find bugs in a website, frontend, web app, or web repository. It covers static source review, dependency/configuration checks, local browser validation, and product-workflow defects. It does not authorize testing a third-party live target.

## Boundaries

- Treat a local repository, a user-owned deployment, or an explicitly authorized test target as in scope. If live target ownership, hostname scope, account identity, or testing rules are unclear, do not probe it.
- Default to read-only review. Do not fix code, deploy, submit reports, contact maintainers, or mutate external systems unless separately requested.
- For uploaded files, test data, and browser payloads, use only synthetic data or researcher-controlled objects. Stop on unrelated data, instability, rate-limit warnings, or destructive behavior.
- Never call a bug P1 from a pattern alone. Require a concrete attacker/user-controlled source, reachable sink or broken control, observable impact, and a reproducible proof.

## Workflow

1. **Inventory the application.** Identify the framework, entrypoints, package manager, build/dev scripts, routes, API calls, auth/session model, storage, upload/conversion flows, third-party scripts, and deployment configuration. Record important unknowns instead of assuming a backend exists.
2. **Run the release gate early.** Install with the repository’s lockfile when possible, run the declared build, typecheck, lint, and tests, and request the app’s root URL and documented entrypoints. A build failure or root-route 404 is a product/release finding even when it is not a security vulnerability.
3. **Map trust boundaries.** For every user-controlled source—URL, query/hash, form field, filename, file content, imported document, API response, postMessage, local storage, or third-party script—trace transformations to DOM, navigation, download, parser, network, filesystem, or code-execution sinks.
4. **Review security controls.** Check authorization at every sensitive operation, server-side validation, output encoding, CSRF/session behavior, SSRF restrictions, safe file handling, dependency versions, secrets, CORS, security headers, and third-party script integrity. For static client-only apps, explicitly state which server-side classes cannot be validated.
5. **Review product workflows.** Exercise the primary user paths and edge states: first load, empty state, invalid input, cancel/reset, repeated action, large input, malformed input, mobile viewport, refresh, and direct navigation. Prefer one controlled mutation at a time.
6. **Validate candidates.** Reproduce each candidate with a minimal local browser or test command. Capture exact URL/route, input, action, expected behavior, observed behavior, console/network errors, and source line(s). Use harmless proof payloads for XSS and never exfiltrate data.
7. **Classify conservatively.** Use project policy when supplied. Otherwise, for security findings use `P0=critical`, `P1=high`, `P2=medium`, `P3=low`; for product defects use `P1` only for release blockers or broken core journeys. Downgrade local/self-only findings and generic hardening observations.
8. **Report coverage and gaps.** Separate verified findings, plausible candidates needing more validation, false positives, and blocked checks. State exactly what was not tested, especially live authentication, cross-account authorization, deployment headers, and production-only integrations.

## P1 bar

A security P1 requires all of: an in-scope realistic attacker, a reachable exploit path, major confidentiality/integrity/availability impact, and reproducible evidence. Examples include meaningful authz bypass, account takeover, high-impact SSRF, sensitive arbitrary file read/write, code execution, or severe cross-tenant exposure. A raw `innerHTML`, missing CSP, outdated package, open redirect, startup console error, or self-only filename XSS is not P1 without a demonstrated major impact path.

For each finding include:

- ID, priority, title, status (`verified`, `candidate`, or `blocked`)
- affected file and line(s), entrypoint/source, control, sink, and concrete impact
- exact reproduction steps and expected versus observed result
- validation evidence and environment
- why the priority is justified, or why it is explicitly downgraded
- remediation direction without claiming an untested fix

## Tooling guidance

Prefer `rg`/`rg --files` for source discovery. Use the project’s own scripts first. For browser checks, use a controlled local browser and collect page errors, request failures, and DOM state. Useful static searches include:

```text
innerHTML|outerHTML|insertAdjacentHTML|document.write|eval\(|Function\(
location\.|window.open|postMessage|src=|href=|fetch\(|FileReader|URL.createObjectURL
localStorage|sessionStorage|indexedDB|password|token|secret|api[_-]?key
```

Do not treat a successful build as proof of runtime correctness, and do not treat static evidence as proof of exploitability when a runtime precondition is missing.

## Supporting reference

Read [references/prompt-pack.md](references/prompt-pack.md) when constructing an LLM-assisted audit prompt or when the user asks for reusable bug-finding prompts. It contains source-backed prompt templates and links to OWASP and PortSwigger guidance.
