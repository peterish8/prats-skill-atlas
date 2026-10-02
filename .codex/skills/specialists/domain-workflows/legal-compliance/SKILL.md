---
name: legal-compliance
description: Legal and privacy compliance audit plus fixes for an app or website. This skill should be used when the user asks whether their product can "get sued", wants a viral legal claim fact-checked, asks "what do we need legally", "is this compliant", "privacy policy / terms / GDPR / DPDP / COPPA / DMCA", wants a compliance checklist for a codebase, or wants the fixes built (policy pages, consent at sign-up, delete-my-account, data export, retention cron, takedown and report flow, open-source licence). It verifies the rules with live web search, reads the codebase to see what actually applies, produces a short tickable checklist ordered by deadline, then implements the items the user picks.
---

# Legal compliance: audit, checklist, fixes

Turn "can we get sued?" into three things: a fact check, a checklist the user can read in two
minutes, and working code for the items they choose.

This is engineering help, not legal advice. Say so once, plainly, in the first answer and on the
checklist. Recommend a lawyer for the items that are legal judgement rather than code (licensing,
the final wording of policies).

## Ground rules

- **Verify, do not recall.** Penalty amounts, deadlines and thresholds change yearly. Search for
  each rule relied on (Firecrawl search if available, otherwise any web search) and prefer
  primary sources: regulator sites, the statute, the gazette, official docs. Mark anything not
  confirmed in this run as "from general knowledge, confirm before relying on it".
- **Read the code before judging.** A rule only matters if the product does the thing. Most
  viral lists are true in general and irrelevant to the codebase in front of you.
- **Maximum is not typical.** "Up to X per violation" is a ceiling. State who can enforce it
  (a regulator, or any private person) and whether courts actually award it.
- **Jurisdiction first.** Ask or infer where the operator is based and where users are. The
  operator's home law applies today; foreign law applies only for users there.
- **Never invent facts about the operator.** Legal name, address, grievance contact, minimum
  age and retention periods are decisions. Use clearly empty constants and make pages say
  "not published yet"; never ship a made-up name or address.
- **State the biggest risk even when unasked.** If the product's core activity is the exposure
  (unlicensed content, scraping, a third party's private API), say it first. Do not help hide
  it; describe it and the honest options.
- **Free and open source change less than people hope.** Free does not exempt a public service
  from privacy law or copyright. Open-source tooling does not license the content it fetches.

## Workflow

### 1. Scope

Establish in one or two questions at most (infer the rest from the repo):
where the operator is based, whether the product is a website, a mobile app or both, whether it
charges money, and whether it is or will be open source.

### 2. Inventory the codebase

Read `references/code-inventory.md` and run its searches. Produce a private table of facts:
what personal data is stored, where sign-in happens, third parties contacted from the client,
analytics and replay, email, payments, user uploads and public content, existing policy pages,
account deletion, and licences. Cite `file:line` for every finding.

### 3. Verify the rules

Read `references/rules.md` for the baseline by jurisdiction and the search queries that confirm
each rule. Run the searches in parallel. For a pasted claim list (a video, a thread), check each
claim: figure, statute, who enforces, and the condition the claim leaves out.

### 4. Answer in this shape

1. One paragraph: is it true, and how much applies to this product.
2. A fact-check table: claim, verdict (True / Misleading / Half true / False), what is actually true.
3. What applies to this codebase, with file links, and what does not.
4. The risk the list missed, if there is one.
5. Ordered next steps.

### 5. The checklist

When the user asks for a plan or checklist, read `references/checklist-format.md` and produce
one. Publish it as a private page when an artifact tool is available, otherwise write it as a
markdown file in the repo. Phases are ordered by deadline; every item is tagged Add, Change or
Decide, says why in one or two sentences, and names the file. Keep it readable by a non-lawyer.

### 6. Let the user choose

The page's ticks are local to their browser. Ask which items to build, or have them paste the
list back. Do not start a 20-item build on a guess.

### 7. Build what they picked

Read `references/implementation-patterns.md` and adapt each pattern to the repo's own
conventions (its store seams, contract docs, test style, commit rules). Order of work:

1. One shared constants file for what the policies promise (policy version, minimum age,
   retention days, operator details, paths).
2. Data model: consent record, last-active marker, any new table.
3. Server: consent, export, delete, report endpoints; honour the personalisation switch.
4. Client: policy pages, sign-in consent step, settings links and controls, report link.
5. Scheduled retention sweep and its one-off backfill.
6. Docs: breach plan, grievance handling, contract docs, README, LICENSE, CREDITS.
7. Run the project's own typecheck, lint and tests. Report what passed and what was not run.

### 8. Hand over

List what was built, what still needs a human decision (operator details, the lawyer review,
licensing), and any deploy step that does not happen by itself (schema deploy, running the
backfill, rotating a leaked key, rewriting git history).

## Things that need confirmation before doing

Rewriting git history, force-pushing, deleting data, publishing policy pages to production,
registering anything with a government body, and sending any email. Ask first, every time.
