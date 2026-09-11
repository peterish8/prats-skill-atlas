# Authorized Research Methodology and Sources

## High-signal, low-risk heuristics

Use these as questions, not as a scan list:

1. **Ownership check:** after Account A creates Object A and Account B creates Object B, does the server reject Account A when one object identifier is replaced with Object B's identifier? Use one controlled request and stop if unrelated data appears.
2. **Role check:** if a normal user can see a privileged action in a client bundle or UI state, does the server reject the action for that user's session? Test only a harmless, researcher-owned object.
3. **Workflow check:** can a researcher-owned action be repeated, reordered, resumed after expiry, or used after revocation when the normal flow says it should not be possible?
4. **Client/server check:** does hiding or disabling a control actually correspond to server-side authorization, validation, and state checks?
5. **API surface check:** from legitimate traffic, document methods, content types, parameters, object identifiers, and response fields. Test one low-impact method or field change at a time.
6. **Impact check:** distinguish a visible oddity from confidentiality, integrity, or availability impact. A response change alone is not a finding.

## Source-backed guidance

- [OWASP WSTG introduction](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/00-Introduction_and_Objectives/) — organize testing around information gathering, authentication, authorization, business logic, client-side, and API testing.
- [OWASP WSTG API BOLA](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/12-API_Testing/02-API_Broken_Object_Level_Authorization) — use object-level authorization checks and controlled identifiers.
- [OWASP WSTG authorization schema](https://wstg.owasp.org/v4.2/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema/) — compare horizontal and vertical access with separate sessions.
- [PortSwigger access control](https://portswigger.net/web-security/access-control) — distinguish horizontal, vertical, and context-dependent authorization.
- [PortSwigger API testing](https://portswigger.net/web-security/api-testing) — map endpoints from legitimate application traffic and pay attention to methods, content types, parameters, and documentation.
- [PortSwigger business logic examples](https://portswigger.net/web-security/logic-flaws/examples) — test assumptions about sequence and state only with controlled data and minimal requests.
- [PortSwigger access-control workflow](https://portswigger.net/burp/documentation/desktop/testing-workflow/vulnerabilities/access-controls) — use Repeater-style comparisons for access-control hypotheses.
- [Bugcrowd VRT](https://www.bugcrowd.com/products/vulnerability-rating-taxonomy/) — use the VRT as a baseline classification, not a guaranteed final severity.

## User-provided video sources

These links were supplied by the user as learning material. The current web fetch was throttled, so exact titles/transcripts were not verified. Do not attribute specific claims to them until the user provides a transcript or the videos can be reviewed:

- https://www.youtube.com/watch?v=JPwRoFDv4eI
- https://www.youtube.com/watch?v=1F0mEkfxlaM&t=194s
