# Detailed Google Python rules

Derived from the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), crawled on 2026-07-28.

## Language and safety

- Use linting. Import modules rather than symbols, avoid relative/wildcard imports, and use `typing`/`collections.abc` symbol imports for concise annotations.
- Catch precise exceptions. Keep try blocks short; use `finally` or a context manager for cleanup. Explain mutable global state; module constants are fine.
- Nested definitions are fine for tight closures. Use comprehensions/generator expressions only when simple; use `for` loops for complex logic. Use generators for large/lazy streams.
- Do not assign lambdas to names. Use a ternary only for a short clear choice. Never use mutable defaults. Use `None` as a sentinel and construct the mutable value inside.
- Use properties only for cheap logical attributes. Prefer implicit truthiness, except compare explicitly to `None` with `is`. Use decorators and threading primitives carefully; avoid obscure metaprogramming/power features.

## Formatting and documentation

- Use 4 spaces, no semicolons, max 80 columns except imports/URLs/paths/long constants/disable comments. Use implicit line joining, not `\` continuations.
- Use no spaces inside delimiters, one after commas/colons, and no space before call/index parentheses. Use two blank lines between top-level definitions and one between methods.
- A directly executable script may start `#!/usr/bin/env python3`; imported modules normally should not. Every non-test module should have an informative triple-double-quoted module docstring.
- Give public, nontrivial, or non-obvious functions a docstring explaining calls/semantics/side effects; use `Args:`, `Returns:`, `Raises:` sections where they add value. Use `TODO(name):` with a specific owner/context.
- Prefer `%`-style or logging's deferred formatting in logging calls as required by the project; write error messages clearly without redundant punctuation/values.
- Manage files/sockets with `with` or `contextlib.closing`. Keep top-level imports/definitions safe on module import; use `main()` plus the main guard for executables.

## Names and types

- Modules/packages are `lower_with_under`; classes/exceptions `CapWords`; functions/methods/locals/parameters `lower_with_under`; constants `CAPS_WITH_UNDER`. A single `_` marks internal/protected names; avoid dunder name mangling.
- Avoid dashes, offensive words, type-suffixed names, and vague single letters except tight counters, `e` exception variables, `f` file handles, and conventional mathematical notation with a cited source.
- Put annotations in source where practical, especially public APIs. Use built-in generic syntax, `str` for text, `bytes` for binary, `None` not `NoneType` in annotations, and `X | None`/`Optional[X]` as local version policy permits.
- Use type aliases for complex repeated types, `TypeVar`/`ParamSpec` with meaningful scope, `TYPE_CHECKING`/forward references to break import cycles, and narrow type ignores with a reason.
