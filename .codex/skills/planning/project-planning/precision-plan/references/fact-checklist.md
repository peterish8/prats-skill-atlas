# Fact sweep

Answer each from the code (file and line) before writing tasks. Skip a question only when it
cannot apply, and say why in the notes.

## Build and test wiring

1. How does each app reach shared code? Direct import, path alias, a generated copy, a build
   step? If copies are generated, which script, which list of files, and which test fails on a
   stale copy? Can shared files live in subfolders, or must they be flat?
2. What does each test script actually run? Globs or an explicit file list? Does a new test file
   need registering somewhere to run at all?
3. Which commands are the quality gates (typecheck, lint, test, build), and which workspace runs
   which?
4. Are there separate packages with their own lockfile or install step (a mobile app, a worker)?
5. How are environment flags read on the server and on the client? What may be public?

## Request and data limits

6. Request body size limit on the API.
7. Batch caps on existing write endpoints (ops per request, items per call).
8. Rate-limit buckets by path, and their numbers.
9. Timeouts on outbound calls; the helper the repo uses for them.
10. The database's rules: document size, array limits, index naming, transaction limits,
    batch-and-reschedule pattern, what may not run inside a query.

## Auth and identity

11. How each layer authenticates (user tokens, server secrets, guest sessions) and how routes
    tell a guest from an account.
12. The existing ports and adapters (store interfaces with memory and real implementations).
13. Existing id formats and validators (playlist ids, codes, refs) that new ids must pass.

## Product surface

14. How routes are declared and parsed on the client; how a new view is rendered.
15. Design tokens and motion rules; the components to reuse for sheets, rows, buttons.
16. Mobile: navigation library, deep-link scheme, whether app links are configured.
17. Deployment routing: rewrites, well-known paths, anything order-sensitive.
18. Privacy page and data export: where stored data is disclosed, how erase reaches each table,
    how a policy version change is presented to users.

## Reuse before building

19. Is there already a helper for what the plan needs (identity, splitting names, codes,
    caching, retries, workers)? Are there duplicates that disagree?
20. Is there an existing worker, sheet, list row, or similar feature to copy the pattern from?

## Third parties

21. Quotas, terms and access rules of every external service the plan touches (checked against
    current docs, cited).
22. File and payload formats from a real sample, never from memory.
