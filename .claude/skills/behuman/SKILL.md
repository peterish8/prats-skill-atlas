---
name: behuman
description: Strips every documented LLM-writing tell out of a piece of text so it reads as plainly human-written. Source: the empirically-compiled Wikipedia:Signs of AI writing field guide (WikiProject AI Cleanup), with every pattern in it converted into a hard "never do this" rule. Use before finalizing ANY piece of prose meant to read as human-written — articles, explanations, notes, emails, landing copy. Other content-generation skills should explicitly invoke this one as a final pass, not skip it.
---

# behuman

This skill exists because LLM output has an identifiable "voice" — a fingerprint made of specific words, sentence shapes, and structural habits that show up regardless of topic. None of these individually proves AI authorship, but stacked together they're the single strongest tell there is. This skill turns the full Wikipedia:Signs of AI writing catalogue into a permanent, non-negotiable checklist for anything you write.

**Rule zero:** these are not stylistic suggestions to weigh against other priorities. Treat every rule below as a hard constraint on the output, the same way you'd treat a syntax error. If a draft violates one, rewrite the sentence — don't just note the violation.

## 1. Banned vocabulary

Never use these words/phrases. Not "use sparingly" — never, in any register, unless quoting a source verbatim.

**The core AI-vocabulary list** (co-occurrence of 2+ of these in one piece is close to a guaranteed tell):
`delve`, `boasts` (meaning "has"), `crucial`, `pivotal`, `intricate` / `intricacies`, `tapestry` (abstract sense), `testament`, `underscore` (as a verb), `underscores`, `garner`, `bolstered`, `fostering` / `foster`, `enduring`, `robust`, `showcase` / `showcasing`, `align with` / `resonate with`, `interplay`, `landscape` (abstract, e.g. "the evolving landscape"), `meticulous` / `meticulously`, `vibrant`, `key` (as a filler adjective — "a key role"), `valuable insights`, `multifaceted`, `holistic`, `paramount`, `game-changer` / `game-changing`, `unleash`, `elevate` (figurative), `seamless`, `navigate` (figurative, "navigate this landscape"), `unlock` (figurative), `journey` (figurative, non-literal travel).

**Puffery / significance-inflation words** — never use these to manufacture importance: `stands/serves as`, `is a testament/reminder`, `a crucial/pivotal/vital/significant/key role/moment`, `underscores/highlights its importance`, `reflects broader`, `symbolizing its ongoing/enduring/lasting`, `contributing to the`, `setting the stage for`, `marking/shaping the`, `represents/marks a shift`, `key turning point`, `evolving landscape`, `focal point`, `indelible mark`, `deeply rooted`.

**Notability-flexing phrases** — never list source types to prove something is worth covering: `independent coverage`, `[X] media outlets`, `trade publications`, `profiled in`, `written by a leading expert`, `active social media presence` / `maintains a [strong/active] digital presence`.

**Superficial-analysis participle tacked onto sentence ends** — never end a sentence with a dangling "-ing" clause that claims significance: `..., highlighting its importance`, `..., ensuring accuracy`, `..., reflecting its legacy`, `..., contributing to X`, `..., cultivating/fostering Y`, `..., enhancing Z`.

**Promotional/travel-guide language**: `boasts a`, `vibrant`, `rich`, `profound`, `showcasing`, `exemplifies`, `commitment to`, `natural beauty`, `nestled`, `in the heart of`, `groundbreaking`, `renowned`, `featuring`, `diverse array`, `unique characteristics`.

**Vague-attribution / weasel phrases** — never attribute a claim to an unnamed authority: `industry reports`, `observers have cited`, `experts argue`, `some critics argue`, `several sources/publications` (unless you can actually name more than two), `such as` immediately before a list you're implying is non-exhaustive when it isn't.

**Didactic disclaimer filler**: `it's important/critical/crucial to note/remember/consider`, `worth noting`, `may vary`.

**Knowledge-gap speculation**: never write `as of my last update`, `not widely available/documented/disclosed`, `while specific details are limited`, `based on available information`, or invent a plausible-sounding reason for an information gap ("likely due to...", "probably because..."). If you don't know something, say so plainly and stop — don't speculate and dress the speculation as analysis.

**Collaborative-assistant leakage** — never let chat-register phrases survive into final content: `I hope this helps`, `Of course!`, `Certainly!`, `You're absolutely right!`, `Would you like...`, `is there anything else`, `let me know`, `here is a detailed breakdown`, `as an AI language model`, `I cannot... but I can...`.

**Canned summary framing**: never open a closing paragraph with `In summary`, `In conclusion`, `Overall,` — just stop when the point is made.

## 2. Banned sentence constructions

**Avoid copulas → marketing verbs.** LLMs replace plain "is/are/has" with inflated verbs. Default to the plain form:
- Write "X is a..." not "X serves as / stands as / functions as / operates as / represents a..."
- Write "X has..." not "X boasts / features / offers / maintains..."
- Write "X means..." not "X refers to..." (the "refers to" construction is a specific tell in opening/definition sentences)

**Negative parallelism — ban outright.** Never write "not just X, but Y" / "not only X but Y" / "it's not X, it's Y" / "no X, no Y, just Z" / "X rather than Y" used as a rhetorical flourish. These read as debate-club cadence, not explanation. If the contrast is real, state both facts as plain separate sentences.

**Rule of three — do not default to it.** Don't structure lists, adjective strings, or short-phrase sequences in groups of exactly three ("adjective, adjective, and adjective" / "clause, clause, and clause") as a reflex. Use however many items the content actually has — two, four, five, whatever's true. If you notice you've written three things and a comma-and, ask whether a fourth exists and got dropped for cadence.

**Elegant variation — do not do this.** If you named something once, use the same name again. Don't swap in a synonym purely to "avoid repetition" ("the ruling" → "the verdict" → "the pronouncement" → "the determination"). Repetition of the correct term is clearer and reads more human than synonym-cycling.

**No hedging qualifiers/intensifiers as filler**: cut `very`, `perhaps`, `tends to`, `arguably`, `in many ways` unless they're doing real semantic work.

**No wordy stock constructions**: replace `as a result of` → "because of" / "so"; `in order to` → "to"; `all of the` → "all the"; `the fact that` → rewrite around it; `a part of` → "part of".

**Prefer plain verbs over stiff/euphemistic synonyms**: `wrote` not "authored", `moved` not "relocated", `used` not "utilized", `tried` not "attempted", `died` not "passed away", `helped` not "facilitated".

**Avoid superlative/absolute claims you can't back with a citation in the same sentence**: `one of the best`, `is the only`, `was the first` — these need a specific supporting fact right next to them or they shouldn't be there at all.

## 3. Banned formatting habits

- **No em dashes.** Use a comma, a colon, parentheses, or just start a new sentence. If you notice you've written " — ", stop and rewrite. (This is one of the single most-cited LLM tells; some model vendors now actively suppress it, which tells you how strong a signal it is.)
- **No title case in headings.** "Why it matters for CLAT", not "Why It Matters For CLAT".
- **No inline-header vertical lists** — the pattern where a bullet starts with a bolded phrase and a colon, then a sentence (`- **Term**: description`), repeated down a whole list. If a list needs structure, either write it as prose or use a real table — don't fake structure with bold-colon bullets on every line.
- **No mechanical over-bolding.** Bold is for the rare word that truly needs visual emphasis, not for every instance of a key term (that "key takeaways" habit of bolding the same phrase every time it appears).
- **No decorative emoji** in headings, bullet points, or section markers. Emoji are fine only where the user/product explicitly wants them as UI elements (e.g. a rating star), never as prose decoration.
- **No unnecessary tables.** If two or three facts can be said in a sentence, say them in a sentence — don't build a two-column table for trivia that doesn't need tabular comparison.
- **No curly/smart quotes or curly apostrophes** in contexts where the surrounding house style uses straight quotes — check what the target file/platform already uses and match it exactly, don't introduce a mix.
- **No skipped heading levels** and no horizontal-rule (`---`) inserted before every heading — structure documents the way a human editor would, hierarchically and only where a break is actually meaningful.
- **No formulaic "Challenges and Future Outlook" closing section.** If you're writing a wrap-up, ground it in one specific, real, sourced fact — not a generic "despite these challenges, X continues to..." pivot to vague optimism.
- **No phrasal-template placeholders left in output** — `[insert X here]`, `[Your Name]`, `[link to Y]`, `2025-XX-XX`. If a value is unknown, either find it or flag it explicitly as missing — never ship a bracketed blank.

## 4. Statistical smoothing — the deeper problem, not just a symptom

Beyond individual banned words, the underlying failure mode is regression to the mean: LLMs default to the most statistically generic phrasing that could apply to the widest range of similar cases, which quietly deletes the specific, unusual, true details that make the subject what it actually is. A person becomes "a titan of industry" instead of "the inventor of the first train-coupling device." Before finishing any piece, ask: *does this sentence contain a fact only true of this specific subject, or could I paste it into an article about something else in the same category with zero edits?* If the latter, it's smoothed-over filler — replace it with the actual specific detail, or cut it.

## 5. Self-check before shipping any text

Run this checklist against the draft before it's considered done:

1. Search the draft for every word in the §1 banned-vocabulary list. Zero hits, or it's not done.
2. Search for em dashes. Zero, or it's not done.
3. Read every list — is each one three items because that's how many exist, or because three felt "right"?
4. Read every sentence with "is"/"are"/"has" replaced by something else — was the replacement earning its keep, or was it avoidance for its own sake?
5. Pick three factual sentences at random — could each one only be true of this specific subject, not a generic stand-in for the category?
6. Would a plain-spoken, knowledgeable person actually say this out loud to someone they're explaining it to? If a sentence sounds like a press release, a LinkedIn post, or a listicle, rewrite it.

If a downstream skill invokes `behuman`, it should run this checklist against its own output as a final pass, not as an afterthought — the checklist is the deliverable of this skill, not a suggestion alongside it.

## Source

Every rule above is a direct translation of a pattern documented at [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup), which compiles real, dated examples from Wikipedia edits across GPT-4, GPT-4o, GPT-5, Gemini, Claude, Grok, and DeepSeek output. Wikipedia-infrastructure-specific signs (broken wikitext, citation-template bugs, malformed categories, DOI errors) were left out since they don't generalize past MediaWiki markup — everything else on that list is captured above.
