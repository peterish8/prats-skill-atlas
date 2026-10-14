# Detailed Google Markdown rules

Derived from the [Google Markdown Style Guide](https://google.github.io/styleguide/docguide/style.html), crawled on 2026-07-28.

- Maintain a small, fresh set of documentation; remove obsolete cruft. Prefer a good incremental update to delaying useful docs for perfection.
- Layout: one H1 title, a brief beginner-oriented intro, optional author, `[TOC]` after intro before H2s, and a final See also section for miscellaneous links.
- Use 80-column prose. Do not wrap URLs, headings, tables, or code blocks solely to meet the limit. Avoid trailing spaces; paragraphs are preferable to forced line breaks.
- Use ATX headings, exact spacing, one H1, and unique descriptive heading text. Keep product/tool capitalization canonical.
- For nested lists, use four-space indentation. Long editable ordered lists may use `1.` repeatedly; short immutable lists should show their actual numbering.
- Favor inline code for literals and fences with language labels for multi-line samples. Fences are searchable, unambiguous, and support highlighting. Ensure nested blocks are indented under their list item.
- Write explicit paths and meaningful link text. Prefer reference links for lengthy/repeated URLs and place each definition immediately after first use.
- Use a screenshot/image only when visual information is essential; always add useful alternate text. Use tables only for data readers need to compare across rows/columns.
- Use ordinary Markdown rather than HTML because plain-source readers and many renderers do not support HTML consistently.
