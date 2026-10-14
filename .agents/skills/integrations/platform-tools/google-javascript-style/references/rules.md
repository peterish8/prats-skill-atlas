# Detailed Google JavaScript rules

This operational reference condenses the [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html), crawled on 2026-07-28. Follow the source and project tooling if a detail changes.

## Modules and dependencies

- New files are ES modules or `goog.module` files. Do not mix module systems casually.
- In ES modules, place imports before code; prefer named exports; prevent circular dependencies; avoid default exports except where a dependency/project convention requires them.
- In Closure code, use one `goog.module` statement, `goog.require` for values, `goog.requireType` for types, and follow declared module hierarchy. Avoid `goog.module.declareLegacyNamespace` except compatibility boundaries.
- Do not write `goog.setTestOnly` in production code. Keep dependency declarations ordered and grouped before implementation.

## Formatting details

- Put opening braces at the end of the preceding line; put closing braces on their own line. Empty blocks may be `{}` when clear.
- Indent every block two spaces. Treat multiline arrays, objects, classes, functions, and switch bodies as blocks; do not use horizontal alignment to create columns.
- Separate logical sections with a single blank line. Do not add trailing whitespace. Add spaces around binary operators, after commas, and after control keywords; do not put spaces just inside delimiters or before argument-list parentheses.
- Use grouping parentheses whenever they make precedence or intent easier to see. Use block comments for multi-line explanations and parameter-name comments only to clarify an otherwise ambiguous argument.

## Language details

- Prefer `for...of` for iterable values; do not use `for...in` without an own-property guard. Keep `try` blocks focused and throw/catch `Error` objects where possible.
- Use complete `switch` cases with intentional `default` and explicit fallthrough handling.
- Do not use `new Boolean`, `new Number`, `new String`, `with`, dynamic evaluation, unsupported language extensions, or mutations of native constructors/prototypes.
- Use generators only when lazy iteration materially helps; do not create needlessly complex generator control flow.
- Use `this` only where its receiver is clear. Wrap/bind methods passed as callbacks when needed rather than losing their receiver.

## JSDoc and diagnostics

- Write JSDoc as a well-formed `/** ... */` block; use single-line form only when it fits. Use Markdown, wrap prose sensibly, and distinguish documentation from implementation comments.
- Document files, classes, enum/typedef declarations, public methods/functions, and properties with behavior-focused descriptions. State nullable types, casts, templates, visibility, and Closure annotations precisely when the codebase uses Closure checking.
- Do not hide a warning broadly. Correct the code first; otherwise, suppress exactly the warning at the smallest justified scope and document it.
- Do not broadly reformat existing nonconforming code. Keep new/changed code in style; generated code is mostly exempt but externally referenced names still need consistent naming.
