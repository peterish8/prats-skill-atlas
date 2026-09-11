# Website Bug-Finder Prompt Pack

These prompts are designed to force evidence, scope discipline, and severity calibration. Replace bracketed values; do not give an assistant a suspected answer if the goal is independent discovery.

## Full local website audit

```text
Audit [REPO_PATH] as an authorized local code review. First identify the framework, entrypoints, build/test commands, routes, APIs, auth/session/storage model, uploads/converters, third-party scripts, and deployment assumptions. Then trace every attacker- or user-controlled source to dangerous sinks and missing controls. Run the declared checks and a local browser smoke test. Report only reproducible findings with file:line evidence, source, sink/control, impact, reproduction, confidence, and priority. Separate verified findings from candidates and blocked checks. Do not modify code or access external targets.
```

## P1 security gate

```text
Review this codebase only for security issues that could defensibly be P1/high or P0/critical. For each candidate prove: realistic in-scope attacker, reachable entrypoint, controllable input, missing/bypassed control, concrete impact, and minimal reproduction. Reject generic hardening advice, theoretical supply-chain risk, self-only impact, and findings that require privileged access. If no candidate meets the bar, say “No verified P1/P0 findings” and list lower-severity evidence separately.
```

## DOM XSS dataflow review

```text
Trace untrusted data from URL/query/hash, form fields, filenames, uploaded document contents, imported archives, postMessage, storage, and third-party responses to HTML, attribute, URL, CSS, script, and navigation sinks. For every path, identify the exact source and sink lines, encoding context, browser reachability, and a harmless local proof. Distinguish reflected/stored/DOM XSS, self-XSS, and file-triggered XSS. Do not report a sink without a controllable source and impact path.
```

## Core workflow/release audit

```text
Test the website’s primary journey plus first load, root route, direct entrypoint, empty state, invalid input, cancel/reset, repeated action, malformed/large input, refresh, and mobile viewport. Compare expected behavior from the UI copy and scripts with actual behavior. Record any build failure, 404, uncaught exception, dead button, data loss, stuck loading state, or incorrect output with exact steps and severity. Keep security and ordinary correctness findings separate.
```

## API/authz review when a backend exists

```text
Map legitimate requests before testing. For each object or privileged action, compare researcher-controlled Account A and Account B with one changed identifier or role variable at a time. Verify server-side authorization, object ownership, state/expiry/revocation, accepted fields, and response scope. Stop after unexpected unrelated data. Report only a reproducible BOLA/BFLA, privilege escalation, state-change bypass, or sensitive overexposure with the request/response evidence redacted.
```

## Evidence-first report reviewer

```text
Review these proposed findings as a skeptical security triager. For each one, check scope, reachable source, sink/control, reproduction, counterevidence, attacker position, impact, and whether the priority follows the stated policy. Mark unsupported claims as candidate or false positive. Do not strengthen wording beyond the evidence and do not invent affected users or exploitability.
```

## Source-backed method

The workflow follows the OWASP Web Security Testing Guide’s risk-based coverage of information gathering, authentication, authorization, input validation, client-side testing, and reporting, plus OWASP Secure Code Review’s source-to-sink and business-logic review guidance. DOM XSS validation follows OWASP’s DOM sink/source approach. Access-control review uses OWASP and PortSwigger’s horizontal/vertical authorization distinction.

- OWASP WSTG: https://owasp.org/www-project-web-security-testing-guide/latest/
- OWASP WSTG introduction: https://wstg.owasp.org/latest/2-Introduction/
- OWASP Secure Code Review Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html
- OWASP DOM XSS testing: https://wstg.owasp.org/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting/
- PortSwigger XSS: https://portswigger.net/web-security/cross-site-scripting
- PortSwigger access control: https://portswigger.net/web-security/access-control
- PortSwigger API testing: https://portswigger.net/web-security/api-testing
