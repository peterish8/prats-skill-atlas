# Gavelogy Note HTML Format Reference

The canonical format uses `lex-note` for the article wrapper and `lex-section` for sections. Interactive quizzes use `gv-quiz` / `gv-match-grid` classes. Both class families are in `src/styles/gavelogy-notes.css`.

## Full structure

```html
<article class="lex-note" data-note-version="v1">

  <header class="lex-note-header">
    <div class="lex-note-kicker">Case Law · Constitutional Law · Note 01</div>
    <h1>Case Title v. Respondent</h1>
    <p class="lex-note-deck"><em>One-line holding that tells students what this case decided and why it matters for CLAT PG.</em></p>
  </header>

  <!-- SECTION 1: Case Identification -->
  <section class="lex-section">
    <span class="lex-section-number">1</span>
    <h2>Case at a glance</h2>
    <div class="lex-anatomy">
      <article><b>F</b><h3>Material facts</h3><p>Facts that change the legal outcome only.</p></article>
      <article><b>I</b><h3>Issues</h3><p>Precise legal questions before the court.</p></article>
      <article><b>R</b><h3>Rules</h3><p>Provisions, doctrines, and precedents applied.</p></article>
      <article><b>A</b><h3>Application</h3><p>How the court applied the rules to the facts.</p></article>
      <article><b>O</b><h3>Order</h3><p>The court's operative directions and result.</p></article>
    </div>
    <aside class="lex-exam-habit"><strong>Exam focus</strong> Add the most-tested distinction or recurring trap.</aside>
  </section>

  <!-- SECTION 2: Core Legal Concepts -->
  <section class="lex-section">
    <span class="lex-section-number">2</span>
    <h2>Key legal ideas</h2>
    <p>Explain the central doctrine and why it governs this dispute.</p>
    <table class="lex-concept-table">
      <thead><tr><th>Concept</th><th>What it means</th><th>Exam angle</th></tr></thead>
      <tbody>
        <tr><td>Doctrine name</td><td>Plain-English explanation</td><td>Common trap or MCQ angle</td></tr>
      </tbody>
    </table>
    <blockquote class="lex-question">Quote the court's clearest statement of the principle here.</blockquote>
  </section>

  <!-- SECTION 3: Issues -->
  <section class="lex-section">
    <span class="lex-section-number">3</span>
    <h2>Main questions</h2>
    <ol>
      <li>Frame issue 1 as a precise legal question.</li>
      <li>Frame issue 2 as a precise legal question.</li>
    </ol>
  </section>

  <!-- SECTION 4: Issue-wise analysis (one sub-section per issue) -->
  <section class="lex-section">
    <span class="lex-section-number">4</span>
    <h2>Issue-wise analysis</h2>

    <h3>Issue 1: [Question]</h3>
    <dl>
      <dt>Petitioner</dt><dd>Arguments made.</dd>
      <dt>Respondent</dt><dd>Counter-arguments.</dd>
      <dt>Court</dt><dd>How the court resolved it and why.</dd>
      <dt>Ratio</dt><dd>The legal proposition necessary for this result.</dd>
    </dl>
    <aside class="lex-exam-habit"><strong>Key takeaway</strong> What students must remember from this issue.</aside>
  </section>

  <!-- SECTION 5: Case Brief (always include) -->
  <section class="lex-section">
    <span class="lex-section-number">5</span>
    <h2>Case brief</h2>
    <article class="lex-case-brief">
      <header><span>Case Brief</span><cite>Case Name v. Respondent, (Year) Citation</cite></header>
      <dl>
        <dt>Facts</dt><dd>Two or three sentences, legally relevant only.</dd>
        <dt>Issue</dt><dd>The exact legal question decided.</dd>
        <dt>Held</dt><dd>Holding and essential ratio.</dd>
        <dt>Study value</dt><dd>Why this case matters for the exam.</dd>
      </dl>
    </article>
  </section>

  <!-- SECTION 6: Quick Revision Table -->
  <section class="lex-section">
    <span class="lex-section-number">6</span>
    <h2>Quick revision table</h2>
    <table class="lex-concept-table">
      <thead><tr><th>Issue</th><th>Court's holding</th></tr></thead>
      <tbody>
        <tr><td>Issue 1</td><td>Holding 1</td></tr>
        <tr><td>Issue 2</td><td>Holding 2</td></tr>
      </tbody>
    </table>
  </section>

  <!-- SECTION 7: Mnemonic (only if genuinely useful) -->
  <section class="lex-section">
    <span class="lex-section-number">7</span>
    <h2>Memory aid</h2>
    <p><strong>ACRONYM:</strong> Explanation of what each letter stands for.</p>
  </section>

  <!-- SECTION 8: Conclusion + CLAT Trap -->
  <section class="lex-section">
    <span class="lex-section-number">8</span>
    <h2>Conclusion and CLAT trap</h2>
    <p>State the outcome and its broader legal impact.</p>
    <aside class="lex-exam-habit amber"><strong>CLAT Trap</strong> Common mistake: students often confuse X with Y. The court said Z.</aside>
  </section>

  <!-- SECTION 9: Checkpoint quiz (inline, no storage needed) -->
  <section class="lex-section">
    <span class="lex-section-number">9</span>
    <h2>Checkpoint</h2>

    <div class="gv-quiz" data-correct="b">
      <p class="gv-qtext">Question 1 testing the central holding.</p>
      <label><input type="radio" name="gv-q-c1a" value="a"> A. Wrong option.</label>
      <label><input type="radio" name="gv-q-c1a" value="b"> B. Correct option.</label>
      <label><input type="radio" name="gv-q-c1a" value="c"> C. Wrong option.</label>
      <label><input type="radio" name="gv-q-c1a" value="d"> D. Wrong option.</label>
      <div class="gv-quiz-actions">
        <button type="button">Check answer</button>
        <span class="gv-quiz-feedback" aria-live="polite"></span>
        <div class="gv-answer"><strong>B is correct.</strong> Explanation tied to the judgment.</div>
      </div>
    </div>

    <div class="gv-quiz" data-correct="c">
      <p class="gv-qtext">Question 2 testing a provision or procedural safeguard.</p>
      <label><input type="radio" name="gv-q-c1b" value="a"> A. Wrong option.</label>
      <label><input type="radio" name="gv-q-c1b" value="b"> B. Wrong option.</label>
      <label><input type="radio" name="gv-q-c1b" value="c"> C. Correct option.</label>
      <label><input type="radio" name="gv-q-c1b" value="d"> D. Wrong option.</label>
      <div class="gv-quiz-actions">
        <button type="button">Check answer</button>
        <span class="gv-quiz-feedback" aria-live="polite"></span>
        <div class="gv-answer"><strong>C is correct.</strong> Explanation.</div>
      </div>
    </div>
  </section>

  <!-- SECTION 10: Match exercise -->
  <section class="lex-section">
    <span class="lex-section-number">10</span>
    <h2>Match the concepts</h2>
    <p>Select a term, then select its correct description.</p>
    <div class="gv-match-grid" data-match-id="m-case01">
      <div class="gv-match-col">
        <button class="gv-match-btn" data-match-key="a">First legal term</button>
        <button class="gv-match-btn" data-match-key="b">Second legal term</button>
        <button class="gv-match-btn" data-match-key="c">Third legal term</button>
      </div>
      <div class="gv-match-col">
        <button class="gv-match-btn" data-match-val="b">Description of second term</button>
        <button class="gv-match-btn" data-match-val="c">Description of third term</button>
        <button class="gv-match-btn" data-match-val="a">Description of first term</button>
      </div>
    </div>
    <p class="gv-match-status">0 of 3 matched</p>
  </section>

</article>
```

## Critical rules

1. Wrapper: `<article class="lex-note" data-note-version="v1">` — always include `data-note-version`
2. Sections: `<section class="lex-section">` with `<span class="lex-section-number">N</span>` and `<h2>`
3. Quiz class: `gv-quiz` (not `lex-quiz`). Radio `name` must be unique per quiz — use `gv-q-<caseSlug><N>` pattern
4. Match class: `gv-match-grid`, `gv-match-col`, `gv-match-btn`. `data-match-id` must be unique per note — use `m-<caseSlug><N>`
5. No `<script>` tags. No inline `on*` event handlers. No invented CSS classes
6. No bracket format `[h2]...[/h2]` — HTML only
7. Do NOT add `<span data-link-id>` — auto-connect.mjs injects those after the fact
8. The AI system prompt lives at `src/lib/prompts.ts` → `GAVELOGY_NOTES_SYSTEM_PROMPT` — use it verbatim when calling the AI to generate notes
9. The actual AI call goes to `/api/ai-format` or `/api/ai-flashcards` in the Next.js app — or call the AI providers directly via `NVIDIA_API_KEY` / `GROQ_API_KEY`

## Available highlight spans (inline)

```html
<span class="hl-blue">ratio / holding</span>
<span class="hl-amber">warning / trap</span>
<span class="hl-green">positive / definition</span>
```

## Available callout asides

```html
<aside class="lex-exam-habit"><strong>Exam focus</strong> Text.</aside>
<aside class="lex-exam-habit amber"><strong>CLAT Trap</strong> Text.</aside>
<aside class="lex-exam-habit green"><strong>Exam tip</strong> Text.</aside>
```
