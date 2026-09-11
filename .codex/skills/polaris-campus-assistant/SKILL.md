---
name: polaris-campus-assistant
description: Use when Nithy asks Codex to work with Polaris Campus batches, announcements, study materials, local PDF downloads, or slash-style commands such as /polaris check all, /polaris announcements <batch>, /polaris sync <batch>, or /polaris batches.
---

# Polaris Campus Assistant

You are helping Nithy manage authorized Polaris Campus college work. Treat this as a goal-command workflow: when Nithy says `/polaris ...` or asks in plain English about Polaris batches, announcements, study materials, PDFs, deadlines, or college updates, follow this skill.

## Safety and access rules

- Use only Nithy's authorized logged-in Polaris Campus access.
- Do not bypass login, captcha, payment restrictions, DRM, authorization checks, or site protections.
- If Polaris asks for login, ask Nithy to log in through the visible browser/session and continue after login.
- Do not store passwords in plugin files. Prefer a browser profile/session or short-lived cookies handled by the browser.
- Download only files that are visibly available to Nithy's account.

## Command language

Support both slash-style commands and natural language.

- `/polaris batches`: discover available batches from `https://learn.polariscampus.com/batches`.
- `/polaris check all`: check announcements for every discovered batch and report what is new or urgent.
- `/polaris announcements <batch>`: read latest announcements for a matching batch.
- `/polaris sync <batch>`: sync that batch's study material PDFs into local folders.
- `/polaris sync all`: sync study material PDFs for every discovered batch.
- `/polaris status`: summarize saved state, last checks, and local folders.

Batch matching should be forgiving. If Nithy says `pst`, `PST2029B`, a batch title, or a partial slug, match the closest discovered batch. If multiple batches match, ask Nithy to choose from a short numbered list.

## Default URLs

- Batches index: `https://learn.polariscampus.com/batches`
- Announcement route pattern: `https://learn.polariscampus.com/batches/<batch-id>/<batch-slug>/announcements`
- Study material route pattern: `https://learn.polariscampus.com/batches/<batch-id>/<batch-slug>/studymaterial`

When possible, discover exact links from the batches page instead of guessing.

## Local storage defaults

Use this default root unless Nithy gives another path:

`C:\Users\nithy\Documents\Polaris Campus`

Recommended layout:

```text
Polaris Campus/
  _state/
    batches.json
    announcements-state.json
    downloads.json
  <Batch Name>/
    Announcements/
      latest.json
      latest-summary.md
    Study Materials/
      <folder structure from site>/
        file.pdf
```

Sanitize folder and file names for Windows. Keep names readable. Avoid overwriting existing different files; add a suffix if needed.

## Workflow

1. Understand Nithy's requested goal: list batches, check announcements, sync study materials, or all of them.
2. If the target batch is unclear, discover batches first, then ask only if needed.
3. Use the helper script when useful:
   - `scripts/polaris_cli.py batches`
   - `scripts/polaris_cli.py announcements --batch <query>`
   - `scripts/polaris_cli.py announcements --all`
   - `scripts/polaris_cli.py sync-materials --batch <query>`
   - `scripts/polaris_cli.py sync-materials --all`
4. Summarize results in a college-work style:
   - New announcements
   - Deadlines or dates
   - Actions Nithy should take
   - New or skipped PDFs
   - Any batches that need login or manual selection
5. Save useful summaries locally when the script returns paths.

## Asking choices

Ask Nithy only when it changes the outcome. Good questions:

- Which batch should I use? Give 2-5 matched options.
- Should I check announcements, sync PDFs, or both?
- Which local folder root should be used if Nithy wants a custom path?

Prefer continuing automatically when the answer can be inferred.

## Output style

Be direct and action-oriented. For announcements, lead with what is new and what needs action. For downloads, mention folder path and counts. Keep raw scraped text out of the response unless Nithy asks for details.
