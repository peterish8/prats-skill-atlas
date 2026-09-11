# Detailed Google HTML/CSS rules

Derived from the [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html), crawled on 2026-07-28.

## General and HTML

- Use HTTPS, UTF-8, 2-space indentation, lowercase code, no trailing whitespace, concise comments, and `TODO(name):` action items.
- Start documents with the HTML5 doctype. Use validators to catch invalid HTML/CSS where practical.
- Use semantic tags, not generic elements for links/buttons/headings. Supply multimedia fallbacks: useful `alt`, and audio/video captions or transcripts where available.
- Keep structure, presentation, and behavior separate. Avoid entity references unless they improve readability or escaping requires them. Avoid unnecessary `type` and `id` attributes.
- Format block, list, and table markup cleanly; wrap long lines for readability; use double quotes for HTML attribute values.

## CSS

- Use valid CSS. Name classes for meaning, not appearance; write lowercase hyphen-delimited names; use prefixes only to prevent meaningful collisions.
- Prefer class selectors. Avoid qualifying classes with element selectors and avoid ID selectors unless a genuine identifier is required.
- Favor the shortest clear property form. Use `0` without units, `.5` not `0.5`, lowercase short hex such as `#fff` where equivalent, and avoid `!important`.
- Avoid user-agent sniffing and browser-specific hacks. Fix the architecture, use standards, or isolate a documented compatibility exception.
- Order declarations consistently, indent blocks by two spaces, terminate declarations, use one declaration per line, place blank lines between rule blocks, and use single quotes for CSS strings.
- Use section comments only where they materially aid navigation; do not create decorative comment banners.
