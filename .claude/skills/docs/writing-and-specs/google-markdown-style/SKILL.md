---
name: google-markdown-style
description: Write, edit, and review Markdown documentation using the Google Markdown Style Guide. Use for README files, technical docs, headings, TOCs, lists, code samples, links, images, tables, and portable maintainable Markdown.
---

# Google Markdown Style

Write documentation that is accurate, newcomer-friendly, readable as source, and portable across renderers. Improve docs iteratively; do not make a small change wait for an imaginary perfect rewrite.

## Document structure

- Start with one `#` title, ideally close to the filename, then a 1–3 sentence introduction for an unfamiliar reader. Use `[TOC]` after the introduction when the document is longer than above-the-fold content and the renderer supports it. Start content sections at `##`; finish with `## See also` when useful.
- Use ATX headings (`#`), blank lines before and after headings, spaces after `#`, and unique, complete heading names so anchors are clear. Follow the Google documentation capitalization guidance and preserve product/tool spellings.
- Wrap prose at 80 characters except headings, tables, code blocks, URLs, and long link-related punctuation. Do not use trailing whitespace; use a trailing backslash only for a necessary hard break.

## Content syntax

- Use lists when information is sequential or scannable; use tables only for genuinely tabular comparison/data. Use lazy `1.` numbering for long/changing ordered lists; use normal numbering for short stable lists. Indent nested/wrapped list content by four spaces.
- Use backticks for inline code, commands, literal tokens, generic file types, and escaped Markdown-looking text. Use fenced code blocks, always declare the language where possible, and escape shell line continuations with `\` for copy/paste commands. Indent fenced blocks correctly inside lists.
- Use explicit, informative Markdown links. Prefer explicit repository paths; avoid relative paths except within the same directory. Use reference links for long/repeated URLs and define each after first use.
- Use images sparingly only when they communicate faster than prose. Provide meaningful alt text. Prefer standard Markdown to HTML; do not use HTML hacks unless a big table or a genuine renderer limitation requires it.

## Review checklist

- [ ] Title, introduction, hierarchy, and TOC make sense to a first-time reader.
- [ ] Headings are unique; whitespace, wrapping, lists, and code blocks are consistent.
- [ ] Links are useful and durable; images have alt text; tables are genuinely appropriate.
- [ ] Markdown is standard and portable, with no trailing whitespace or unnecessary HTML.

Read [references/rules.md](references/rules.md) for detailed layout and source-formatting conventions.
