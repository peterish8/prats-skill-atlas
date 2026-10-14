---
name: google-html-css-style
description: Apply the Google HTML/CSS Style Guide when writing, editing, reviewing, or refactoring raw HTML, CSS, Sass, or GSS. Use for semantic markup, accessibility, selectors, declarations, formatting, and stylesheet maintainability.
---

# Google HTML and CSS Style

Apply these conventions to authored HTML/CSS unless component/framework tooling or a documented repository rule requires a different form. Preserve accessibility and semantic correctness over superficial formatting.

## Workflow

1. Inspect existing framework, formatter, design-system tokens, browser support, and accessibility requirements.
2. Use semantic HTML and the smallest stable CSS surface. Avoid visual-only markup and selector escalation.
3. Apply the rules below; validate with project tooling and, when relevant, HTML/CSS/accessibility checks.
4. Read [references/rules.md](references/rules.md) for detailed selector, formatting, and legacy-guide rules.

## Required rules

- Use `<!doctype html>` and valid, no-quirks HTML. Use valid CSS unless proprietary syntax or a documented validator limitation requires otherwise.
- Use HTTPS for embedded resources whenever available. Use UTF-8. Indent with 2 spaces, never tabs; use lowercase HTML element/attribute names and CSS selectors/properties/values except literal strings.
- Use elements for their purpose: headings for headings, buttons for actions, links for navigation, labels with form controls, and landmarks where useful. Do not use clickable generic `div`s in place of interactive semantic controls.
- Provide meaningful `alt` text for informative images. Use `alt=""` only for decorative/redundant images. Provide captions/transcripts or equivalent alternatives for audio/video/canvas content.
- Keep structure (HTML), presentation (CSS), and behavior (JS) separated. Do not use presentational elements or inline event handlers/styles except a project-bound exception.
- Use double quotes for HTML attribute values. Omit optional tags only when the resulting DOM and readability are unambiguous. Omit `type` attributes where HTML/CSS defaults make them unnecessary.
- Use meaningful, purpose-based class names in lowercase hyphenated form. Prefer reusable generic helper names only when no domain name exists. Avoid presentational, cryptic, or arbitrary abbreviations.
- Prefer class selectors; avoid type selectors when a class communicates intent, and avoid IDs for styling. Do not use browser detection or CSS hacks unless there is no durable alternative.
- Use shorthand CSS only when it does not obscure needed overrides. Omit units after `0`; omit the leading zero for fractional values; use short lowercase hex where possible. Do not use `!important`.
- Keep declaration order logical and consistent. Put one declaration per line, end declarations with semicolons, place a space after `:`, separate declaration blocks and rules with blank lines, and use single quotes in CSS strings.
- Write concise comments that explain intent and use `TODO(name):` for actionable work.

## Review checklist

- [ ] Markup is valid, semantic, keyboard-accessible, and has appropriate alternatives for media.
- [ ] Resources use HTTPS and HTML/CSS stay separated from behavior.
- [ ] Classes/selectors are purpose-based, stable, and not overly specific.
- [ ] No `!important`, UA hacks, visual-only markup, or unnecessary ID/type selectors were added.
- [ ] Formatting, lowercase syntax, quotes, indentation, and CSS declarations are consistent.
