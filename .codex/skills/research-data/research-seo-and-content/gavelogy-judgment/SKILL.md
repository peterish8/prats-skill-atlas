---
name: gavelogy-judgment
description: "Full pipeline for Gavelogy case law notes. Given an itemId (Convex content_items or structure_items ID), generates: (1) structured HTML notes in lex-note format, (2) flashcards JSON, (3) MCQ quiz questions, (4) PDF judgment connections. Pushes notes to the live-note preview (dev server), then saves everything to Convex. Trigger: /gavelogy-judgment"
trigger: /gavelogy-judgment
---

# /gavelogy-judgment

Full pipeline for a CLAT PG case law note. One command → notes + flashcards + quiz + PDF connections, all visible in the browser live preview before you hit Publish.

## Usage

```
/gavelogy-judgment <itemId>
/gavelogy-judgment <itemId> --only notes
/gavelogy-judgment <itemId> --only flashcards
/gavelogy-judgment <itemId> --only quiz
/gavelogy-judgment <itemId> --only connect
```

If no `--only` flag is given, run all four in sequence.

## Pre-flight

Before generating anything:

1. Read `references/note-html-format.md` to load the lex-note HTML structure and CSS classes.
2. Read `references/convex-api.md` to load the Convex HTTP API patterns.
3. Confirm the dev server is running at `http://localhost:3002`. If unreachable, warn the user before proceeding (notes can still be saved to Convex but live preview will fail).

## Step 1 — Fetch case data from Convex

```js
// POST to Convex HTTP API
const res = await fetch(`${CONVEX_URL}/api/query`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ path: 'temp:getNoteHtmlTemp', args: { itemId }, format: 'json' })
})
const { value } = await res.json()
// value = { html, title, pdfUrl }
```

Run this by writing a small Node.js script to `.local/tmp-fetch.mjs` and executing it, OR call the Convex HTTP API directly in Bash:

```bash
node -e "
const r = await fetch('${CONVEX_URL}/api/query', {
  method:'POST', headers:{'Content-Type':'application/json'},
  body: JSON.stringify({ path: 'temp:getNoteHtmlTemp', args: { itemId: '${ITEM_ID}' }, format: 'json' })
});
const d = await r.json(); console.log(JSON.stringify(d.value));
"
```

Extract: `title`, `pdfUrl`.

If `pdfUrl` is null, stop with: "No PDF attached to this item — upload a judgment PDF first via the Studio page."

## Step 2 — Extract PDF text

Use the existing script pipeline. Run:

```bash
node scripts/auto-connect.mjs <itemId>
```

This downloads the PDF, extracts text, calls AI, creates connections, and pushes to live preview. It handles all connection wiring. You do NOT need to re-implement PDF extraction for connections — let auto-connect.mjs handle Step 4 (connections).

For notes, flashcards, and quiz: read the PDF text yourself by running:

```bash
node -e "
// Node polyfill + pdfjs extraction
if (!Promise.withResolvers) {
  Promise.withResolvers = function() {
    let resolve, reject;
    const promise = new Promise((res,rej)=>{resolve=res;reject=rej});
    return {promise,resolve,reject};
  }
}
import('pdfjs-dist/build/pdf.mjs').then(async lib => {
  const workerSrc = new URL('./node_modules/pdfjs-dist/build/pdf.worker.mjs', 'file:///' + process.cwd().replace(/\\\\/g,'/') + '/').href;
  lib.GlobalWorkerOptions.workerSrc = workerSrc;
  const res = await fetch('http://localhost:3002/api/judgment/pdf-proxy?itemId=${ITEM_ID}', {
    headers: { 'x-admin-secret': '${ADMIN_SECRET}' }
  });
  const buf = await res.arrayBuffer();
  const pdf = await lib.getDocument({ data: new Uint8Array(buf), useSystemFonts: true }).promise;
  const parts = [];
  for (let i=1; i<=Math.min(pdf.numPages,80); i++) {
    const page = await pdf.getPage(i);
    const content = await page.getTextContent();
    parts.push('[Page ' + i + ']\n' + content.items.map(it=>it.str).join(' '));
  }
  console.log(parts.join('\n\n').slice(0, 20000));
});
" 2>/dev/null
```

Save the output as `pdfText` (first 20 000 chars is enough for notes generation).

## Step 3 — Generate Notes HTML

Read `references/note-html-format.md` for the exact structure and every CSS class. The system prompt text to use when calling AI is at `src/lib/prompts.ts` → `GAVELOGY_NOTES_SYSTEM_PROMPT`.

Generate the note as a single `<article class="lex-note" data-note-version="v1">` element.

**Required sections (in order):**
1. Case at a glance (FIRAO anatomy block — `lex-anatomy`)
2. Key legal ideas (concepts table — `lex-concept-table`, blockquote `lex-question`)
3. Main questions (numbered issues)
4. Issue-wise analysis (per-issue `<dl>` with petitioner / respondent / court / ratio)
5. Case brief (`lex-case-brief`)
6. Quick revision table (`lex-concept-table`)
7. Memory aid (mnemonic if useful)
8. Conclusion and CLAT Trap (`lex-exam-habit amber`)
9. Checkpoint (2 `gv-quiz` inline MCQs)
10. Match exercise (`gv-match-grid`)

**Rules:**
- Interactive quizzes: class `gv-quiz` with `data-correct="b"`. Radio `name` must be unique: `gv-q-<slug><N>`.
- Matching: `gv-match-grid` / `gv-match-col` / `gv-match-btn`. `data-match-id` must be unique.
- Language: plain English for a CLAT PG aspirant who has never read the case.
- Bold key terms with `<strong>`. Do NOT use em dashes — write "and" instead.
- Do NOT include `<span data-link-id>` tags — auto-connect.mjs injects those.
- Do NOT add `<script>` tags or `on*` event handlers.

After generating the HTML, push it to the live preview:

```bash
curl -s -X POST http://localhost:3002/api/dev/live-note/<itemId> \
  -H "Content-Type: application/json" \
  -d '{"html": "<ESCAPED_HTML_HERE>"}'
```

Use a Node.js one-liner to avoid shell escaping issues:

```js
// Write to .local/notes/<itemId>.html directly — the SSE watcher picks it up
fs.writeFileSync('.local/notes/' + itemId + '.html', html, 'utf-8')
```

Then save to Convex:

```bash
node -e "
const html = require('fs').readFileSync('.local/notes/${ITEM_ID}.html','utf-8');
const r = await fetch('${CONVEX_URL}/api/mutation', {
  method:'POST', headers:{'Content-Type':'application/json'},
  body: JSON.stringify({ path:'temp:updateNoteHtmlTemp', args:{ itemId:'${ITEM_ID}', html }, format:'json' })
});
console.log(await r.json());
"
```

Tell the user: "Notes pushed to live preview — check http://localhost:3002/admin/notes/edit/<itemId>"

## Step 4 — Generate Flashcards

Generate 8-12 flashcards from the case. Format:

```json
[
  {
    "front": "What did the Court hold about internet shutdowns in Anuradha Bhasin?",
    "back": "Internet shutdowns must be temporary, published, proportionate, and reviewed every 7 working days under the Telecom Suspension Rules, 2017.",
    "tag": "holding"
  }
]
```

Tags: `"holding"` | `"provision"` | `"doctrine"` | `"fact"` | `"trap"`

Save as `flashcardsJson = JSON.stringify(flashcards)`.

## Step 5 — Generate Quiz Questions

Generate 5 MCQ questions. Each must have exactly 4 options (A/B/C/D), one correct answer, and a 1-2 sentence explanation.

Format for Convex (use this exact shape):

```json
[
  {
    "question_text": "Which articles did the Court invoke to protect internet use?",
    "options": [
      "Articles 14 and 21",
      "Articles 19(1)(a) and 19(1)(g)",
      "Articles 32 and 226",
      "Articles 19(1)(a) and 21"
    ],
    "correct_answer": "B",
    "explanation": "The Court held that speech and trade through the internet fall under Articles 19(1)(a) and 19(1)(g) respectively."
  }
]
```

Questions must test:
1. The precise legal holding
2. A provision/statute cited
3. A procedural safeguard
4. A CLAT trap (common wrong answer)
5. A fact from the case

## Step 6 — Save Flashcards + Quiz to Convex

Use `temp:seedMasterJudgmentNote` to save notes + flashcards + quiz in one mutation:

```bash
node -e "
const html = require('fs').readFileSync('.local/notes/${ITEM_ID}.html','utf-8');
const body = {
  path: 'temp:seedMasterJudgmentNote',
  args: {
    itemId: '${ITEM_ID}',
    contentHtml: html,
    flashcardsJson: JSON.stringify(FLASHCARDS_ARRAY),
    quizTitle: 'CASE_TITLE Quiz',
    quizQuestions: QUIZ_QUESTIONS_ARRAY,
    activateCourse: true
  },
  format: 'json'
};
const r = await fetch('${CONVEX_URL}/api/mutation', {
  method:'POST', headers:{'Content-Type':'application/json'},
  body: JSON.stringify(body)
});
console.log(JSON.stringify((await r.json()).value));
"
```

## Step 7 — Run Connections (auto-connect.mjs)

```bash
node scripts/auto-connect.mjs <itemId>
```

This runs the full pipeline: downloads PDF, extracts text, calls AI to find connections, inserts `pdf_highlights` or `note_pdf_links` records, injects `<span data-link-id>` into the notes HTML, pushes to live preview, saves to Convex.

If it exits with errors, report them clearly. The most common failures:
- NVIDIA 404: falls back to Groq automatically
- `PDF text not found`: AI returned a phrase not verbatim in the PDF — this is OK, other connections still save
- `Note is empty`: notes weren't saved yet — run Steps 3-6 first

## Step 8 — Final Report

After all steps, print a clean summary:

```
✅  <Case Title> — fully generated

  Notes     : <N> sections, <chars> chars → live preview + Convex
  Flashcards: <N> cards saved
  Quiz      : <N> questions saved
  Connections: <N> PDF links created, <N> spans injected

  Preview: http://localhost:3002/admin/notes/edit/<itemId>
  Action : review in browser → click Publish when happy
```

## Environment Variables

Read from `.env.local` in the project root:
- `NEXT_PUBLIC_CONVEX_URL` — Convex HTTP API base URL
- `ADMIN_API_SECRET` — x-admin-secret header for PDF proxy
- `NVIDIA_API_KEY`, `GROQ_API_KEY` — AI providers (auto-connect.mjs uses these)

To read them in Node.js:
```js
const env = {}
require('fs').readFileSync('.env.local','utf-8').split('\n').forEach(line => {
  const m = line.match(/^([A-Z0-9_]+)=(.*)$/)
  if (m) env[m[1]] = m[2].replace(/^["']|["']$/g,'')
})
```

## What NOT to do

- Do NOT write `[h2]...[/h2]` bracket format — use HTML only.
- Do NOT add `<span data-link-id>` tags manually — auto-connect.mjs injects them.
- Do NOT publish to Convex without telling the user first (they should review in the browser).
- Do NOT skip the Case Checkpoints section at the end of the notes — it is required for the student quiz UI.
- Do NOT use em dashes (—) in the note text — write "and" or reword the sentence.
