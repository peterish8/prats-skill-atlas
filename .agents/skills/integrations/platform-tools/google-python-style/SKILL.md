---
name: google-python-style
description: Apply the Google Python Style Guide when writing, editing, reviewing, or refactoring Python. Use for imports, exceptions, resource management, type annotations, docstrings, naming, formatting, testing, and safe Python language features.
---

# Google Python Style

Apply this style unless a repository's formatter, linter, supported Python version, or documented local convention conflicts. Match surrounding code on choices the guide leaves open.

## Workflow

1. Inspect Python version, formatter/linter/type checker, test conventions, package layout, and nearby code.
2. Write clear, typed, resource-safe code; avoid clever features that make maintenance harder.
3. Validate with the project's formatter, lint, type checker, and tests.
4. Read [references/rules.md](references/rules.md) for the detailed language, documentation, type, and naming rules.

## Required code rules

- Run linting and fix warnings; suppress only narrowly with a reason. Import modules, not individual names, except from `typing`, `collections.abc`, or an explicit local exception. Do not use wildcard imports.
- Use packages with `__init__.py` where the project requires them. Keep imports at top, grouped standard library, third-party, then local, with one blank line between groups.
- Raise specific built-in/custom exceptions, not bare `Exception` or strings. Do not catch broadly unless you re-raise or can recover meaningfully. Use `finally`/context managers for cleanup.
- Avoid mutable global state; constants are allowed and encouraged. Explain any necessary mutable global state.
- Use nested functions/classes only for narrow closure/local scope. Prefer comprehensions/generator expressions for simple transformations; do not build complicated nested expressions. Use generators when laziness is useful.
- Avoid `lambda` except a short expression callback; use `def` for named/multiline logic. Use conditional expressions only when concise and readable. Never use mutable default arguments; use `None` then construct the value.
- Use properties for cheap attribute-like access; do not hide expensive computation, side effects, or behavior subclasses may need to override behind a property.
- Prefer implicit false (`if items:`), but test `None` with `is None`/`is not None`. Do not rely on lexical-scope surprises or mutate captured state without a strong reason.
- Use decorators judiciously, standard thread-safe primitives for shared state, and avoid power features/metaclasses/dynamic behavior unless their benefit is compelling and documented.
- Use `from __future__ import` when it safely enables required modern semantics for the supported runtime.
- Add type annotations to public/changed APIs and enable static checking where practical. Prefer built-in generics such as `list[str]`, use `str` for text and `bytes` for binary data, and do not hide type errors broadly.

## Formatting, docs, and names

- Use 4-space indentation, no tabs, 80-character lines with documented exceptions, and implicit continuation inside parentheses/brackets/braces—not backslash continuations. Never use semicolons to join/terminate statements.
- Use two blank lines between top-level definitions, one blank line between methods, standard punctuation spacing, and trailing commas in multiline literals where they aid diffs.
- Use `"""` docstrings: a punctuated summary line, then a blank line and details if needed. Document modules, public/nontrivial functions, classes, arguments, returns, raises, and side effects—not obvious implementation. Write accurate comments with grammar.
- Use `with` for files, sockets, and other stateful resources. Put executable behavior in `main()` and gate it with `if __name__ == '__main__':`.
- Use `lower_with_under` for modules/functions/variables, `CapWords` for classes/exceptions, and `CAPS_WITH_UNDER` for constants. Use a single leading `_` for internal/protected names; avoid double-dunder names and type-encoded/single-letter names outside narrow conventional scopes.

## Review checklist

- [ ] Imports, exceptions, global state, defaults, properties, and resource lifetimes are safe.
- [ ] Control flow and Python features are clear rather than clever.
- [ ] Formatting, docstrings, TODOs, names, main guard, and tests match local conventions.
- [ ] Public/changed APIs are correctly typed and static checks pass.
