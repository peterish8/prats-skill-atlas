---
name: gavelnews-editorial
description: Converts a raw newspaper article or website page into a complete GavelNews current-affairs piece for CLAT aspirants using article schema v2 (hero/story/law_decode/exam_radar/challenge/one_line_revision/sources + Visual Memory Card). Every output MUST pass a behuman pass before being considered done. Use when given a newspaper/news-site URL or pasted article and asked to turn it into GavelNews content, or when asked to update the gavel-news editorial pipeline.
---

# gavelnews-editorial

Turns one piece of raw current-affairs source material (a newspaper article, a court press release, a ministry notification, a news-site page) into one complete GavelNews piece under **article schema v2**: hero metadata, a casual "what happened" story block, a law-decode deep dive, exam radar, a fixed challenge quiz, a one-line revision, sources, and a Visual Memory Card. This is the content-generation half of the `gavel-news` engine repo's editorial pipeline; `gavel-news-web` only renders whatever this skill (or the human editor) produces.

**Mandatory dependency: this skill MUST invoke the `behuman` skill as its final step, every time, no exceptions.** Nothing produced here ships until it has passed `behuman`'s checklist. If you skip that step, the output is not done, no matter how complete the sections look.

New drafts use `schema_version=2` and populate **only** the v2 fields below. Do not dual-write the old v1 flat fields (`what_happened`, `why_it_matters`, etc.) for new stories.

## Who you're writing as

A senior law student explaining today's news to a junior who's prepping for CLAT UG/PG. Smart, patient, clear, a little informal. Not a newspaper editorial voice, not a coaching-institute voice, not a Wikipedia voice. If a sentence could appear in a press release or a corporate blog, it's wrong for this — rewrite it.

## Input

One of:
- A URL to a newspaper/legal-news article (fetch with the `defuddle` skill first to get clean text — don't use raw HTML)
- Pasted article text
- A court order/judgment excerpt or a ministry notification

## Pipeline

### Step 1 — Read the source once, fully, before writing anything

Identify: what actually happened (the concrete event), who did what, what law/provision/institution is involved, whether there's a judgment (and if so, what was held), and why a CLAT aspirant specifically would need to know this. If the source doesn't contain enough to answer these, say so — don't invent facts to fill gaps. Never write a knowledge-gap sentence dressed as analysis (e.g. "while specific details are limited, it likely..." — this is banned outright by `behuman`, and it's also just fabrication).

Do not invent case names, doctrine names, section numbers, or IPC→BNS mappings that the source does not support. If a v2 field cannot be filled honestly, leave it empty or omit it.

### Step 2 — Hero (`hero`)

Metadata for the card/header. Keep it factual.

- **`title`** — clear, specific, 8-15 words; not clickbait
- **`subtitle`** — one short line under the title (optional but preferred)
- **`category`** — one of: `constitutional-law` | `criminal-law` | `legal-current-affairs` | `bare-acts-update`
- **`subject`** — syllabus-facing label (e.g. "Criminal Law — Obscenity")
- **`exam`** — e.g. `CLAT UG/PG` or `Both`
- **`read_time`** — e.g. `6 min`
- **`difficulty`** — Easy | Medium | Hard (overall)
- **`importance`** — short label or 1-5 style signal if you use one
- **`date`** — edition / story date `YYYY-MM-DD`
- **`tags`** — short string list (provisions, doctrines, institutions)

Also set top-level `title` (and usually `category` / `exam_tags`) to match `hero` for the engine row.

### Step 3 — Story (`story`) — "What Happened?"

- **`heading`** — default `"What Happened?"` (product UI may add emoji; do not decorate prose with emoji)
- **`summary`** — explain the news like a senior to a junior. Casual. No legal jargon. **Maximum 150 words.**
- **`takeaway`** — exactly one sentence: "If you remember one thing..."

Word budget: summary ≤150 words. No padding.

### Step 4 — Law decode (`law_decode`) — "Decode the Law"

Write only what this story actually puts in play. Empty arrays/fields are better than invented filler.

- **`heading`** — default `"Decode the Law"`
- **`sections`** — `[{provision, explanation}]` — only Articles/Sections/Acts load-bearing here
- **`doctrines`** — `[{name, explanation}]` — only if the source or holding actually invokes one
- **`legal_tests`** — `[{name, rule}]` — the operative test the court or statute uses
- **`important_cases`** — `[{case, principle}]` — only cases already in the source material or clearly named in existing editorial content
- **`constitutional_link`** — `[{article, why}]` — only real Article links
- **`bns_mapping`** — `{ipc, bns}` — only when the story itself discusses IPC/BNS (or an old/new pair already stated). Never invent a BNS section number.
- **`dont_confuse`** — `[{confusion, reality}]` — 1-3 pairs students actually mix up *for this story*
- **`memory_trick`** — one short mnemonic or hook tied to *this* holding, not a generic slogan

Word budget: tight. Prefer short explanations over bare-act dumps.

### Step 5 — Exam radar (`exam_radar`) — "Exam Radar"

- **`heading`** — default `"Exam Radar"`
- **`why_exam`** — one paragraph: why this is exam-worthy (current affairs / static law / recent judgment / policy / constitutional principle). Distinct from the story summary.
- **`examiner_focus`** — list of concrete points an examiner would probe
- **`pyq_connection`** — MANDATORY VERIFICATION, not a recollection:
  - If `search_pyqs` is connected, call it with 2-3 phrasings before concluding no match.
  - If not connected, query `engine.pyq.search_pyqs` against `data/pyq-core.sqlite` directly.
  - Real match only: cite exam, year, question number, and what it tests. Never a vague "recurring theme" sentence.
  - No real match → leave empty (and do not invent a keyword either).
- **`probability`** — integer 1-5
- **`difficulty`** — object preferably `{UG, PG, Judiciary}` with Easy|Medium|Hard values when known; a single string is acceptable only if you cannot honestly split

### Step 6 — Challenge (`challenge`) — fixed quiz, authored once

- **`heading`** — default `"Challenge Yourself"`
- **`mcqs`** — 3-5 questions, mixed types (`factual` / `conceptual` / `application` — and related labels like passage/static_law/inference if useful)

Each MCQ:
```
{
  question: string,
  type: string,
  options: { A: string, B: string, C: string, D: string },
  answer: "A" | "B" | "C" | "D",
  explanation: string  // why correct is right AND why the strongest wrong option fails
}
```

No filler options. Every wrong option should be a plausible trap.

### Step 7 — One-line revision (`one_line_revision`)

- **`heading`** — default `"One Line Revision"`
- **`line`** — the single sentence you want the student to remember walking away

### Step 8 — Sources (`sources`)

v2 object shape (not the old array of `{name,url,type}` alone):

```
sources:
  primary: <main source name/url/label>
  secondary: <list or string of supporting sources>
```

You may put structured objects inside `primary`/`secondary` if helpful (`{name, url, type}`), but keep the top-level keys exactly `primary` and `secondary`. Always include at least one real source. Types when nested: `newspaper` | `official` | `legal_website` | `statute`.

### Step 9 — Visual Memory Card (`visual_memory_card`)

A short **ASCII tree** stored as plain TEXT (not JSON). Structure:

```
THIS CASE / TOPIC
       │
  [Provision / Test]
       │
  Requires [X]
       │
  [Doctrine / Test name]
       │
  NOT [common misconception]
       │
  [Leading case] ([Year])   # only if real
       │
  [Old law] → [New law]     # only if real IPC/BNS (or equivalent) pair
```

Keep it scannable. No invented case or section on the card.

### Step 10 — MANDATORY: run the behuman pass

Before this piece is done, explicitly invoke the `behuman` skill against the full generated text (every prose field: summary, takeaway, explanations, memory_trick, why_exam, MCQ explanations, one_line_revision, etc.). Run its self-check checklist literally:

1. Zero hits on its banned-vocabulary list — check every section
2. Zero em dashes
3. No reflexive rule-of-three lists
4. No elegant-variation synonym-cycling on legal terms — use the same term consistently
5. Every fact-bearing sentence specific to *this* story, not generic filler that could paste into any other current-affairs piece
6. Read it out loud in your head — does it sound like a senior law student talking, or like a press release?

If any section fails, rewrite that section — don't ship it with a note that it "could be improved."

## Output shape

Produce a single JSON object matching the engine's v2 `save_story_draft` / `update_story` payload:

```
{
  title,
  schema_version: 2,
  hero: { ... },
  story: { heading, summary, takeaway },
  law_decode: { ... },
  exam_radar: { ... },
  challenge: { heading, mcqs: [...] },
  one_line_revision: { heading, line },
  sources: { primary, secondary },
  visual_memory_card: "<ascii tree>",
  category,
  exam_tags,
  decision,
  decision_reason,
  pyq_question_ids  // only verified IDs
}
```

Field names must match `engine/editorial.py` / the MCP tool schema. Do not invent divergent names.

## What NOT to do

- Do not generate the quiz dynamically at read time — author it once and store it.
- Do not add a "Challenges and Future Outlook" style closing section.
- Do not pad any block to hit a word count.
- Do not invent doctrines, legal tests, case citations, or BNS section numbers.
- Do not invent a PYQ connection without running `search_pyqs` (or querying `data/pyq-core.sqlite`) first.
- Do not dual-write v1 fields for new schema_version=2 stories.
- Do not use em dashes, banned AI vocabulary, or "landmark judgment" / "watershed moment" puffery.
- Do not skip Step 10. An article that reads clean to you but hasn't been checked against `behuman`'s explicit list is not done.
