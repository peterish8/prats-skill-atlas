---
name: google-javascript-style
description: Apply the Google JavaScript Style Guide when writing, editing, reviewing, or refactoring JavaScript. Use for ES modules, Closure-compatible JavaScript, JSDoc, formatting, naming, classes, functions, and safe language-feature choices.
---

# Google JavaScript Style

Apply this as the default JavaScript contract unless a repository's documented local rule conflicts. The public Google JavaScript guide is older and recommends TypeScript for new typed code; use `$google-typescript-style` for TypeScript.

## Workflow

1. Inspect the project's formatter, linter, module system, target runtimes, and nearby code.
2. Write the simplest readable solution; do not mix unrelated style churn into a feature change.
3. Apply these rules and verify with the project's formatter, lint, tests, and supported runtime checks.
4. Read [references/rules.md](references/rules.md) for detailed Closure, JSDoc, and legacy-platform decisions.

## Required code and formatting rules

- Use UTF-8 and filenames containing lowercase letters, digits, `_`, or `-`, with `.js` extension. Use ordinary ASCII spaces; represent non-printing characters with escapes and use readable non-ASCII characters where helpful.
- Use ES modules for new code. Keep file sections ordered: copyright, `@fileoverview`, module/import declarations, then implementation. Follow project-required Closure declarations only in Closure code.
- Use `const` by default, `let` when reassigned, never `var` except an explicit legacy-platform exception. Declare one variable per declaration, near its first use, and initialize it promptly.
- Use `[]` and `{}`, never variadic `Array` or `Object` constructors. Use trailing commas in multiline arrays/objects. Do not add nonnumeric properties to arrays.
- Do not mix quoted and unquoted object keys. Use unquoted identifier keys; use quoted keys when required. A computed key follows the quoted-key style unless it is a symbol.
- Prefer property/method shorthand where it is clear. Use destructuring and spread deliberately; remember spread is shallow.
- Use classes for cohesive state and behavior. Do not write old prototype-style classes, directly mutate prototypes/built-ins, create static-container classes, or create nested namespaces.
- Use constructors to establish invariants, ordinary methods for behavior, static methods only without instance state, and getters/setters only for genuinely property-like operations.
- Use function declarations for named top-level functions. Use arrow functions for callbacks and lexical `this`; do not use an arrow when dynamic `this` is required. Keep closures small and intentional.
- Use single-quoted strings. Use template literals for interpolation or multiline text. Do not use string line continuations.
- Brace every control-flow body, use K&R braces, one statement per line, mandatory semicolons, 2-space indentation, and an 80-column limit where practical. Break at the highest syntactic level and indent continuations at least four spaces.
- Use `===`/`!==`. Permit loose equality only when intentional coercion is explicitly valuable (commonly `x == null` to match null and undefined).
- Do not use `with`, `eval`, string `Function`, ASI-dependent formatting, nonstandard features, primitive wrapper objects, or constructor calls without `()`.

## Names, comments, and policy

- Use descriptive ASCII camelCase names. Use UpperCamelCase for classes, interfaces, enums, typedefs, and templates; lowerCamelCase for methods, fields, variables, parameters, and modules; CONSTANT_CASE only for deeply immutable global/static constants and enum values.
- Treat acronyms as words: `loadHttpUrl`, not `loadHTTPURL`. Do not use leading/trailing underscores for private state except established project conventions; use a trailing underscore where Closure visibility rules require it.
- Use JSDoc for classes, fields, methods, functions, typedefs, and public APIs. Keep it valid, Markdown-capable, and informative; document parameter/return semantics, nullability, side effects, and constraints rather than repeating obvious code.
- Suppress compiler/linter warnings only at the narrowest scope with a reason. Mark APIs `@deprecated` with migration instructions. Preserve local style where the guide leaves a choice open.

## Review checklist

- [ ] Modules, imports, and file order match the project.
- [ ] Variables, object/array literals, classes, functions, control flow, and strings follow the rules above.
- [ ] No unsafe dynamic execution, prototype patching, forbidden feature, hidden coercion, or warning suppression was introduced.
- [ ] Naming and JSDoc make the API clear.
- [ ] Formatter, lint/compiler checks, and tests pass.
