# Google TypeScript rule reference

Use this reference for detailed decisions while applying `$google-typescript-style`. It is a condensed, operational restatement of the [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html), checked on 2026-07-28. The source guide is authoritative if this reference and it ever diverge.

## Source files and modules

### File basics

- Encode source in UTF-8 without a BOM.
- Preserve normal whitespace in string literals. Use escape sequences for non-printing characters; use actual non-ASCII characters when they are more readable than a Unicode escape.
- Put copyright and file-level `@fileoverview` JSDoc before imports when required by the repository.

### Imports and exports

- Put imports after the file header and before implementation code.
- Use project-relative paths only for same-project imports. Avoid `./` and `../` as a complete import path.
- Prefer named imports. Namespace imports are appropriate only for large/dynamic APIs or dependency conventions; default imports follow the dependency's public API.
- Avoid arbitrary import renaming. Rename the local declaration when that resolves a collision. Use a module alias only where it improves clarity.
- Make exports intentional. Export symbols that form the module API; avoid broad re-export barrels when they obscure dependencies.
- Never mutate an exported value after declaration. Prefer exported functions, classes, and immutable values.
- Use `import type`/`export type` for type-only imports/re-exports; this supports file-by-file transpilation. Use bare side-effect imports intentionally.
- Use ES modules. Do not use namespaces, legacy internal `module`, triple-slash references, or `import = require`.

## Language features

### Variables, arrays, and objects

- Use `const`; use `let` only if a binding changes; never use `var`.
- Declare one variable per declaration.
- Use `[]` and `{}` literals rather than `new Array` and `new Object`.
- Do not add non-index properties to arrays.
- Use spread only with awareness that it is shallow and can allocate/copy. Object spread later properties override earlier properties.
- Prefer `Map`/`Set` when modeling keyed collections or membership. When iterating an object, prefer `Object.keys`, `Object.values`, or `Object.entries` over inherited-property iteration.
- Use computed property names only when the property is genuinely dynamic.
- Destructure when it improves a value's readability or avoids repeated access; do not destructure large/nested data only for style.

### Classes

- Prefer class declarations, not class expressions. Keep classes cohesive and stateful; use modules for namespace-like grouping.
- Prefer ordinary methods to function-valued properties unless property semantics are necessary (for example, an instance callback retaining lexical `this`).
- Use static methods only for operations that do not need instance state.
- Constructors establish object invariants. In subclasses, call `super()` before using `this`.
- Declare fields and their visibility intentionally. Make immutable fields `readonly`; use parameter properties sparingly and document them with `@param`.
- Do not manually manipulate prototypes, create mixins through prototype mutation, or patch built-ins. Framework infrastructure is the narrow exception.

### Functions and `this`

- Use a function declaration for a named function, including named local helpers.
- Do not use `function` expressions. Use an arrow for callback/closure expressions.
- Use expression-bodied arrows for concise, obvious expressions; use a block for branching, statements, or nontrivial logic.
- Avoid nested functions that become long or capture broad mutable state.
- An arrow captures lexical `this`; a regular function's `this` depends on the call site. Do not use arrow functions when a dynamic `this` is required.
- Pass arrows as callbacks when they call an instance method needing `this`; avoid rebinding with `.bind(this)` repeatedly.
- Do not pass a method as a bare callback if it relies on `this`.
- Use parameter defaults for simple defaults. Use rest parameters and spread instead of `arguments` and `apply` where suitable.
- Treat event handlers as callbacks: preserve the required receiver deliberately and name them for the event/action.

### Literals, flow, and errors

- Use single-quoted strings by default. Use template literals for interpolation or multiline content.
- Write numeric bases as lowercase `0x`, `0o`, `0b`; do not write a leading zero decimal literal.
- Use `String`, `Boolean`, template strings, or `!!` for conversion. Never use `new String`, `new Number`, or `new Boolean`.
- Explicitly compare enum values; a zero-valued enum member makes boolean coercion wrong.
- Brace every conditional/loop body. Add grouping parentheses only when they clarify precedence or a reader could misparse the expression.
- Use `try` only around operations whose thrown errors you intend to handle. Do not catch-and-ignore errors; preserve cause/context when rethrowing.
- Write complete `switch` logic, include `default` where relevant, and make fallthrough explicit.
- Use `===`/`!==`. Only use loose `== null`/`!= null` for the explicit combined null-or-undefined check.
- Avoid `as` and `!`. Prove types through validation/narrowing. Use `as` (not angle syntax) for a justified assertion. If a double assertion is required, write `value as unknown as Target` and explain why.

### Prohibited or restricted features

- Do not define decorators; only use supported framework decorators directly adjacent to their targets.
- Do not use primitive wrapper objects, Automatic Semicolon Insertion-dependent formatting, `const enum`, `debugger`, `with`, `eval`, or `Function` from a string.
- Do not use unstandardized ECMAScript/Web APIs unless a project explicitly targets the runtime that supports them.
- Do not modify built-ins or globals, including through declarations, unless an external integration requires it.

## Naming

- Restrict identifiers to ASCII letters, digits, underscores (constants and structured tests), and rare `$` required by external convention.
- Use descriptive lowerCamelCase words. Treat acronym runs as normal words: `parseHtml`, `userId`, `loadHttpUrl`.
- Do not encode types, visibility, optionality, or interfaces in names: no Hungarian prefixes, `opt_`, `_private`, `IThing`, or `ThingInterface`.
- Use `UpperCamelCase` for classes, interfaces, type aliases, enums, decorators, type parameters, and TSX component functions.
- Use `lowerCamelCase` for functions, methods, variables, properties, parameters, and aliases.
- Use `CONSTANT_CASE` for global constants and enum members. Local constants generally remain `lowerCamelCase`.
- Use one-letter `T` only for a generic with no domain meaning; otherwise choose a concise `UpperCamelCase` name, such as `Element` or `Response`.
- `$` is normally forbidden; established Observable naming is an allowed exception.
- Test names should state condition and expected behavior; structured test names may contain underscores.

## Type system

### Inference and absence

- Omit trivial annotations such as `const enabled: boolean = true`. Add type arguments for empty generic collections and annotations for complex values that readers cannot infer at a glance.
- Function return annotations are optional unless they clarify non-obvious behavior or local policy requires them.
- Use `null` and `undefined` intentionally. Prefer `prop?: T` to `prop: T|undefined` when callers may omit the property/argument.
- Do not add nullable unions just because a value is hard to model; validate input and establish an invariant instead.

### Structural and collection types

- TypeScript is structural: type object-shaped contracts with interfaces, and write the interface on structural implementations so excess/missing property errors occur at the correct boundary.
- Prefer `interface` to `type X = { ... }`. Use `type` for unions, intersections, primitive aliases, tuples, and type-level expressions that interfaces cannot represent.
- Spell arrays of simple types as `T[]` / `readonly T[]`; spell arrays of complex union/object types as `Array<T>` / `ReadonlyArray<T>`.
- Use meaningful index key names, e.g. `{[userName: string]: User}`. Prefer `Map`/`Set` for dynamic keys; use `Record` for fixed known keys.
- Prefer simple, explicit types over mapped/conditional types. Use `Partial`, `Readonly`, `Pick`, conditional types, and key remapping only when they reduce genuine duplication without hiding relationships.
- Avoid `{}` unless its exact “anything except null/undefined” semantics are intended; prefer `object` for nonprimitive values.
- Avoid tuples for data with named meanings. Use a small fixed tuple only when its position is conventional and obvious.

### `any`, `unknown`, and generics

- Do not introduce `any` casually. Use the narrowest truthful type, an interface, a generic, a union, or `unknown`.
- Treat `unknown` as untrusted: narrow with `typeof`, `instanceof`, discriminants, or a type guard before access.
- If an interop boundary requires `any`, contain it at the boundary and add a narrowly scoped lint suppression with a reason.
- Use lowercase primitive types. Never annotate with wrapper object types (`String`, `Number`, `Boolean`) or `Object`.
- Avoid APIs whose only generic type parameter appears in the return type; callers cannot infer it. For legacy APIs of that form, pass the type argument explicitly.

## Toolchain and documentation

- Require all `.ts`/`.tsx` code to type-check in the project's standard compiler setup.
- Do not use `@ts-ignore`, `@ts-nocheck`, or application-code `@ts-expect-error`. Fix the type model. A narrow test-only exception should be documented and avoided where a local cast expresses intent better.
- Obey project/global conformance and security rules in addition to this skill.
- Use JSDoc for API documentation, ordinary comments for implementation rationale. Keep multi-line comments readable and Markdown-friendly.
- Document all top-level exports, classes, methods/functions where behavior is not obvious, and parameter properties. Put documentation before decorators.
- Do not repeat TypeScript types in JSDoc or write redundant TS tags (`@param {Type}`, `@return {Type}`, `@private`, `@override`, `@implements`, `@enum`).
- Explain behavior, effects, constraints, ownership, units, error cases, or rationale. Do not narrate syntax or restate an identifier's name.
- Use `@deprecated` with a clear replacement or migration path.

## Change policy

- Preserve surrounding code unless the requested change touches it. Do not reformat an unrelated file merely to modernize it.
- When substantially editing a file, bring the edited areas into this style without burying product changes in broad style-only edits.
- Generated code is generally exempt, but any generated identifier used by hand-written code must still follow naming requirements (underscores are permitted to avoid collisions).

## Source and scope

This skill is derived from the public Google TypeScript Style Guide. Google explicitly notes that its internal environment has constraints that may not apply to every external project. Honor repository-specific rules where they conflict, and favor the repository's runtime/toolchain requirements.
