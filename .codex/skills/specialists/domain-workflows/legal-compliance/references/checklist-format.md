# Checklist format

The reader is the founder, not a lawyer. They should be able to scan it in two minutes and know
what to do first.

## Structure

1. **Header**: product, date, one sentence on how it was built, and "not legal advice".
2. **Progress**: "Done X of N", updating as boxes are ticked.
3. **If you only do three things**: the three highest-value items in one line each.
4. **Phases in deadline order**, each with a heading, a deadline label and its own count:
   1. Decide first (no code): who runs it and at what address, the complaints contact, the
      minimum age, and the hard question the code cannot answer (licensing).
   2. Repository and licensing, if the code is or will be public.
   3. Product: do now (rules already in force, or cheap fixes).
   4. Product: before the next legal deadline (name the date).
   5. Only when a feature is added (payments, email). Drop this phase if the user says the
      feature will never exist.
   6. Mobile app, if there is one.
5. **The rules behind this list**: a small table of law, what it touches here, when, and what
   happens if ignored.
6. **Sources**: links to what was actually opened, plus a line naming anything taken from
   general knowledge.

## Each item

- A checkbox with a stable id.
- A tag: **Add** (new), **Change** (exists today), **Decide** (not code).
- A title that is an action: "Serve the fonts from your own domain".
- Why, in one or two plain sentences, naming the rule and the consequence.
- Where: the file path and line when it is a code change.

## Writing rules

- Plain words. Expand any abbreviation on first use. No statute numbers in titles.
- State facts found in the repo as facts; state legal conclusions as what the rule says.
- No item that is advice to evade a rule. Describe the risk and the honest options.
- When the user changes the premise (free, open source, no payments), revise the list: remove
  phases that no longer apply and add the ones the new premise creates.

## As a published page

Static HTML with checkboxes; save ticks in `localStorage` inside try/catch and say on the page
that ticks stay in this browser. The agent cannot read them, so ask the user to paste the list
back or name the items. Follow the artifact tool's own design rules, and use the product's own
colours and fonts when it has a design system.
