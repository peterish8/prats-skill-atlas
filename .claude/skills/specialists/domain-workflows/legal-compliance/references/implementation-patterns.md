# Implementation patterns

Adapt each to the repo's own seams and rules. Read its architecture and contract docs first;
where a contract document exists, update it before the code.

## One source for what the policies promise

A single shared constants file that the web app, the mobile app, the API and scheduled jobs all
import:

- `POLICY_VERSION` (the effective date), `MINIMUM_AGE`, retention periods in days.
- `OPERATOR = { name, address, grievanceOfficer, email }`, left empty until the user supplies
  them, with a helper that says whether they are published. Pages show "not published yet"
  while empty.
- Paths of the policy pages, report reasons, field length limits.

The policy text reads the numbers from here, so the page and the behaviour cannot drift.

## Policy pages

Three pages reachable without signing in: privacy, terms, copyright and complaints.

- **Privacy**: what is collected (match the inventory exactly), why, who processes it (every
  third party found), how long it is kept (the retention constants), the rights and how to use
  them (link to the export and delete controls), children, the complaints contact, the right to
  go to the regulator, and the policy version.
- **Terms**: minimum age, acceptable use for anything users can write or upload, ownership of
  uploads, no guarantee for a free service, governing law.
- **Copyright and complaints**: the grievance officer, what a notice must contain, the promised
  response times, and the report link.

Link them from settings, the sign-in step, any public page a signed-out visitor can reach, and
the mobile About screen. Correct any existing privacy text that is no longer true.

## Consent at sign-in

- Above the sign-in button: two lines on what the account stores, links to the policies, and an
  unticked checkbox ("I am 18 or older and agree"). The button stays disabled until ticked.
- With OAuth redirects the page reloads, so remember the tick locally and send it to the
  server after sign-in completes.
- Server: an authenticated endpoint that stores `{ policyVersion, at }` on the profile, with the
  time taken from the server clock. Reject a version that is not the current one.
- Show the recorded consent in the account panel. When the policy version moves on, ask again.

## Delete my account

- One authenticated endpoint; the client confirms in its own UI before calling it.
- Enumerate every table keyed by the user, including ones other features own (sync rows,
  devices, presence, sessions, share links) and uploaded files. Delete the profile and sign-in
  sessions in the first pass so the account stops working at once.
- Large accounts exceed one transaction: delete a bounded batch per table, then schedule the
  same job again until nothing is left. Make it safe to repeat.
- Delete the identity record in the auth provider's tables last.
- Guard against resurrection: if a still-valid session token arrives after deletion, do not
  silently create a fresh empty profile for it.
- Afterwards the client signs out and returns to the signed-out state.

## Download my data

An authenticated endpoint returning one JSON document: profile, settings, consent, what was
learned (taste, history), the library, share links and registered devices. The client saves it
as a file. Cap page counts and say so in the payload when it was truncated.

## Withdraw consent: a real personalisation switch

A server-side setting, enforced on the server so every client obeys it. When off: stop
recording history and taste, stop using them for recommendations, and erase what was already
learned at the moment it is switched off. A switch that only hides UI is not withdrawal.

## Retention sweep

- Add a `lastActiveAt` marker written on every profile write, and an index on it (with the
  guest or account flag first when the periods differ).
- A daily scheduled job erases profiles older than the stated period, a small bounded number
  per run, rescheduling itself when the batch was full. It reuses the delete-account routine.
- Rows written before the marker existed have none: make the sweep skip them (range from a
  value greater than zero) and ship a one-off paged backfill that derives the marker from data
  already there. Tell the user to run it after deploying.
- A user who is active but causes no writes (personalisation off) must still count as active:
  bump the marker from the API at most once every few days when it is stale.
- Watch the cost: never scan the whole table daily; use the index.

## Report and takedown for public content

- A "Report" control on every public user-made page, open to signed-out visitors.
- A public, rate-limited endpoint storing reason, optional details and optional contact in a
  reports table, capped per item.
- Internal commands for the officer: list open reports, take an item down (and its uploaded
  file), dismiss. Document them in a short grievance-handling doc with the response times.

## Third-party requests

Self-host fonts (in Next.js, `next/font` downloads at build time). Keep session replay off
unless there is consent, and write that rule into the project's contributor rules so it stays off.

## Open source

- `LICENSE` at the root and a `license` field in each package manifest. Choose by what the
  code already contains: ported GPL code means GPL. Fetch the canonical licence text rather
  than typing it (`gh api licenses/gpl-3.0 --jq .body`).
- `CREDITS.md` naming every project code was taken or ported from, with its licence.
- Remove files the licence cannot cover (proprietary fonts, copied assets). Removing them from
  history means rewriting it: confirm with the user first.
- README: what the project is, that it is unaffiliated, and a contact for rightsholders.

## Operations docs

- **Breach plan**: one page. Who decides, contain, assess what leaked, notify affected people
  in plain language and the regulator, record what happened.
- **Grievance handling**: where reports arrive, the response clock, the takedown commands.

## Verification

Add tests in the repo's own style for: consent stored and returned, export shape, delete
removes everything and is repeatable, report accepted for a live link and refused for a dead
one, the personalisation switch stopping writes. Run typecheck, lint and tests and report the
results as they are.
