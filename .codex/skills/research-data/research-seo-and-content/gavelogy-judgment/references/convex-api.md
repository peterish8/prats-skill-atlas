# Convex HTTP API Reference for Gavelogy

Base URL is `NEXT_PUBLIC_CONVEX_URL` from `.env.local` (e.g. `https://wary-perch-979.convex.cloud`).

All calls are `POST` with `Content-Type: application/json`.

## Read note data

```js
// Returns: { html, title, pdfUrl }
POST ${CONVEX_URL}/api/query
{
  "path": "temp:getNoteHtmlTemp",
  "args": { "itemId": "<itemId>" },
  "format": "json"
}
```

## Save HTML notes only

```js
POST ${CONVEX_URL}/api/mutation
{
  "path": "temp:updateNoteHtmlTemp",
  "args": { "itemId": "<itemId>", "html": "<html string>" },
  "format": "json"
}
// Returns: { value: { ok: true } }
```

## Save notes + flashcards + quiz in one call

```js
POST ${CONVEX_URL}/api/mutation
{
  "path": "temp:seedMasterJudgmentNote",
  "args": {
    "itemId": "<itemId>",
    "contentHtml": "<full article HTML>",
    "flashcardsJson": "[{\"front\":\"...\",\"back\":\"...\",\"tag\":\"holding\"}]",
    "quizTitle": "Anuradha Bhasin Quiz",
    "quizQuestions": [
      {
        "question_text": "Which articles did the Court invoke?",
        "options": ["Art 14 & 21", "Art 19(1)(a) & 19(1)(g)", "Art 32 & 226", "Art 19(1)(a) & 21"],
        "correct_answer": "B",
        "explanation": "The Court held speech and trade through the internet fall under 19(1)(a) and 19(1)(g)."
      }
    ],
    "activateCourse": true
  },
  "format": "json"
}
// Returns: { value: { ok, itemId, table, title, courseId, hasPdf, quizId, noteChars, quizCount } }
```

### Flashcards JSON format (string-encoded array)

Each flashcard object:
```json
{
  "front": "Question or prompt on front of card",
  "back": "Answer — precise, cite-able, exam-ready",
  "tag": "holding"
}
```
Allowed tags: `"holding"` | `"provision"` | `"doctrine"` | `"fact"` | `"trap"`

Minimum 8 cards, maximum 15. Cover: 2 holdings, 2 provisions, 2 doctrines, 1 fact, 1+ trap.

### Quiz questions format (array of objects)

```json
{
  "question_text": "Full question text ending with a question mark?",
  "options": ["A. option", "B. option", "C. option", "D. option"],
  "correct_answer": "B",
  "explanation": "1-2 sentence explanation citing the judgment."
}
```

- Exactly 4 options in the `options` array (values are the full strings with letter prefix)
- `correct_answer` is the letter only: `"A"`, `"B"`, `"C"`, or `"D"`
- Minimum 5 questions: 1 holding, 1 provision, 1 procedural safeguard, 1 CLAT trap, 1 fact

## Add a single PDF connection

```js
POST ${CONVEX_URL}/api/mutation
{
  "path": "temp:insertNotePdfLinkTemp",
  "args": {
    "itemId": "<itemId>",
    "link_id": "kebab-case-anchor-id",
    "pdf_page": 3,
    "x": 72.5,
    "y": 400.0,
    "width": 400.0,
    "height": 12.0,
    "label": "yellow|Verbatim PDF text matched"
  },
  "format": "json"
}
```

- `link_id` must match the `data-link-id` attribute in the corresponding `<span>` in the notes HTML
- `x`, `y`, `width`, `height` are in PDF points (pt), y-origin bottom-left
- `label` format: `"<color>|<text>"` where color is one of: `yellow`, `blue`, `green`, `orange`, `red`

## Node.js helper to read .env.local

```js
const env = {}
require('fs').readFileSync('.env.local','utf-8').split('\n').forEach(line => {
  const m = line.match(/^([A-Z0-9_]+)=(.*)$/)
  if (m) env[m[1]] = m[2].replace(/^["']|["']$/g,'')
})
const CONVEX_URL = env.NEXT_PUBLIC_CONVEX_URL
```

## Call AI directly (notes / flashcards / quiz generation)

Use NVIDIA first, fall back to Groq. Both are OpenAI-compatible:

```js
async function callAI(messages, maxTokens = 8000) {
  const providers = [
    { url: 'https://integrate.api.nvidia.com/v1', key: env.NVIDIA_API_KEY, model: 'mistralai/mistral-small-3.1-24b-instruct' },
    { url: 'https://api.groq.com/openai/v1', key: env.GROQ_API_KEY, model: 'llama-3.3-70b-versatile' },
  ]
  for (const p of providers) {
    try {
      const r = await fetch(`${p.url}/chat/completions`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${p.key}` },
        body: JSON.stringify({ model: p.model, messages, max_tokens: maxTokens, temperature: 0.3 })
      })
      if (!r.ok) continue
      const d = await r.json()
      return d.choices[0].message.content
    } catch {}
  }
  throw new Error('All AI providers failed')
}
```
