---
name: google-typescript-style
description: Apply the Google TypeScript Style Guide when writing, editing, reviewing, or refactoring TypeScript and TSX. Use for production TypeScript code, style reviews, type-design decisions, imports/exports, naming, documentation, and compiler-safety fixes that should follow Google conventions.
---

# Google TypeScript Style

Apply these instructions as the default style contract unless the repository has a documented, conflicting local rule. Preserve existing project tooling and public API compatibility.

## Workflow

1. Inspect the repository's formatter, linter, `tsconfig`, framework conventions, and nearby code.
2. Implement the requested behavior with the simplest readable TypeScript construct.
3. Apply the non-negotiable rules below. Do not introduce unrelated style churn.
4. Run the project's applicable formatter, lint, type-check, and tests. Report any rule that cannot be applied because of a local constraint.
5. For a detailed rule or review, read [references/rules.md](references/rules.md).

## Non-negotiable safety and module rules

- Use UTF-8 source files. Do not use a BOM. Keep ordinary whitespace in string literals; use explicit escapes for non-printing characters.
- Use ES modules only: `import`/`export`. Do not use TypeScript namespaces, triple-slash references, `import x = require(...)`, or CommonJS-style import forms.
- Keep imports at the top after any file-level JSDoc. Use relative paths for same-project code; do not use bare relative-directory paths such as `./` or `../`.
- Prefer named imports. Use namespace imports only for truly large, dynamic APIs or when required by the dependency. Do not rename imports merely to avoid a local collision; rename the local instead.
- Use `import type` and `export type` for type-only symbols. Use a bare `import 'module';` when a runtime side effect is required.
- Export only the intended module API. Prefer `export {name}` over inline `export` when it makes the public surface obvious. Never mutate an exported binding after initialization.
- Never use `eval`, `Function(string)`, `with`, `debugger`, `const enum`, non-standard platform/language features, or direct mutation of built-ins or their prototypes. Do not add globals except where a third-party API requires it.
- Never use `@ts-ignore`, `@ts-nocheck`, or `@ts-expect-error` in application code. In a unit test, avoid `@ts-expect-error`; if unavoidable, narrowly document why.

## Code shape

- Use `const` by default; use `let` only for reassignment. Never use `var`. Declare one variable per declaration.
- Use array/object literals, not `new Array()` or `new Object()`. Do not attach custom properties to arrays.
- Use spread deliberately: it is shallow, can be expensive, and can hide duplicate properties. Prefer explicit object construction when it makes ownership or overrides clearer.
- Prefer `for...of` for array iteration when a loop is clearer than a callback. Do not use `for...in` over arrays. For object keys, use `Object.keys`, `Object.entries`, or `Map`/`Set` as appropriate.
- Use destructuring when it improves clarity; do not destructure merely because it is available.
- Prefer function declarations for named functions. Use arrow functions for callbacks and short closures; do not use anonymous `function` expressions. Do not use `this` in arrow functions.
- Prefer arrow callbacks rather than `.bind(this)`. Do not pass methods requiring `this` as bare callbacks; wrap them or bind once intentionally.
- Give arrow functions expression bodies only when the expression is short and clear; otherwise use a block body. Use parentheses around a single parameter only when its type is written or grouping aids readability.
- Use rest parameters and spread rather than `arguments` or `Function.prototype.apply` when appropriate.
- Keep nested functions small and local. Prefer extracting only when it creates a reusable, coherent unit.
- Prefer classes only for objects with meaningful state/behavior. Do not manipulate prototypes directly except in framework code that genuinely requires it. Avoid container classes made only to group static functions; use modules.
- Make fields explicit, initialize them at declaration or in the constructor, and keep member visibility intentional. Use `readonly` for bindings that must not be reassigned.
- Do not define new decorators. Use framework-provided decorators only; place JSDoc before decorators and do not put a blank line between a decorator and its target.

## Expressions and control flow

- Use single quotes for ordinary strings; use template literals for interpolation or multiline strings. Do not use line continuations in strings.
- Use lowercase `0x`, `0o`, and `0b` numeric prefixes. Do not use legacy leading-zero numeric literals.
- Use `String()`, `Boolean()`, template literals, or `!!` for intentional coercion; never construct primitive wrapper objects. Compare enum values explicitly rather than coercing them to booleans.
- Always use `===` and `!==`. `x == null` and `x != null` are allowed only to intentionally match both `null` and `undefined`.
- Always brace control-flow bodies, including one-line branches and loops. Write `switch` cases deliberately, include `default` unless exhaustiveness makes it inappropriate, and avoid accidental fallthrough.
- Keep `try` blocks tight: put only statements that can throw the intended error inside. Throw `Error` objects, not strings. Handle exceptions only when recovery or context is meaningful.
- Avoid type assertions and non-null assertions. Prefer runtime validation, control-flow narrowing, a type guard, or a correct declaration. If an assertion is provably necessary, explain the invariant near it; use `as`, never angle-bracket assertions. For a required double assertion, cast through `unknown`.

## Names and APIs

- Use ASCII identifiers. Use `UpperCamelCase` for classes, interfaces, types, enums, decorators, type parameters, and TSX component functions; `lowerCamelCase` for variables, parameters, functions, methods, properties, and import aliases; `CONSTANT_CASE` for global constant values and enum values.
- Treat acronyms as words: `loadHttpUrl`, not `loadHTTPURL`; preserve platform spellings such as `XMLHttpRequest`.
- Choose descriptive, pronounceable names. Do not encode types into names, use Hungarian notation, prefix optional parameters with `opt_`, mark interfaces with `I`, or mark private members with leading/trailing underscores.
- Avoid `$` except an established third-party convention (for example, Observable streams). Avoid abbreviations unless they are universally understood in the domain.
- Use `T` for a single unconstrained type parameter; use descriptive `UpperCamelCase` names for meaningful type parameters.
- Name tests for the behavior and condition they exercise. Use underscores only for structured test names or constants.

## Type design

- Rely on inference for obvious literals and constructors. Add annotations for empty generic collections, public/structural contracts, complex expressions, or when they materially improve readability. Add return types when they document complex behavior or local policy requires them.
- Model absence deliberately. Prefer optional properties/parameters over `| undefined` when omission is the semantics. Use `null` only where it conveys a distinct intentional state; do not add it casually.
- Use interfaces for structural object shapes, and annotate structural implementations at their declaration: `const user: User = {...}`. Prefer interfaces over object-literal type aliases; reserve `type` for unions, intersections, primitives, tuples, mapped/conditional expressions, and aliases that cannot be interfaces.
- Use the simplest type that expresses the contract. Prefer explicit properties and small interfaces to clever mapped or conditional types. Repetition is often cheaper than opaque type algebra.
- Use `T[]`/`readonly T[]` for simple element types; use `Array<T>`/`ReadonlyArray<T>` when the element type is complex (for example a union or object literal).
- Prefer `Map` and `Set` over object-as-dictionary when their semantics fit. Give index-signature keys meaningful names. Use `Record<K, V>` only for a statically known key set.
- Avoid `any`. Prefer a precise interface, generic, union, or `unknown`. When handling `unknown`, narrow it before use. If `any` is unavoidable, suppress the lint rule at the narrowest site and document why.
- Do not use `String`, `Number`, `Boolean`, or `Object` as types; use lowercase primitives and use `object` or `{}` only with their precise semantics in mind.
- Avoid tuple types except fixed, small, naturally positional values. Prefer named object properties for values with independent meaning.
- Do not create return-type-only generic APIs. When consuming an existing one, specify its generic argument explicitly.

## Comments and documentation

- Use `/** ... */` for API documentation readers need; use `//` for implementation intent. Do not restate types in JSDoc.
- Document every top-level exported symbol. Document a class's purpose, a method/function's behavior and important side effects, and parameter properties with `@param` descriptions.
- Write complete sentences and useful Markdown in JSDoc. Explain constraints, units, ownership, mutation, error conditions, or rationale—never narrate obvious code.
- Do not use TypeScript-redundant JSDoc tags such as `@type`, typed `@param`/`@return`, `@private`, `@implements`, `@enum`, or `@override` when TypeScript syntax already states it.
- Mark deprecated APIs with `@deprecated` and concrete migration instructions.

## Review checklist

- [ ] Behavior is correct; code is idiomatic for the repository.
- [ ] Imports/exports are ES-module based and type-only symbols use `import type`/`export type`.
- [ ] No unsafe suppressions, `any`, assertion, namespace, dynamic evaluation, wrapper, prototype/global mutation, or forbidden feature was introduced.
- [ ] Names, visibility, mutability, nullability, and public API are intentional.
- [ ] Types are simple, structural contracts use interfaces, and `unknown` is narrowed.
- [ ] Control flow is explicit and exceptions are narrowly scoped.
- [ ] Documentation adds reader value and public exports are documented.
- [ ] Formatting, linting, type-checking, and relevant tests pass.
