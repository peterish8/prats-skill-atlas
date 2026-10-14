# Detailed Google JSON API rules

Derived from [Google JSON Style Guide revision 0.9](https://google.github.io/styleguide/jsoncstyleguide.xml), crawled on 2026-07-28. It describes JSON API conventions, not JSONC; comments shown in source examples are explanatory only and are invalid in real JSON.

## Data and names

- JSON supports only booleans, numbers, Unicode strings, arrays, objects, and `null`; select the truthful type. Consider omitting empty/null optional values.
- Use lowerCamelCase semantic names, arrays with plural names, and singular names for individual values. Avoid reserved JavaScript words.
- Document object-as-map properties; their arbitrary keys can be Unicode. Use structured objects for semantically coupled fields, otherwise do not add nesting for convenience.
- Strings represent extensible enums. Dates use RFC 3339, durations ISO 8601, and coordinates ISO 6709 when applicable.

## Reserved response fields

- `apiVersion` identifies the API version; `context` echoes a client correlation value; `id` is server-supplied response correlation; `method` names the operation; `params` carries RPC inputs.
- `data` and `error` are mutually exclusive. `data.kind` is a type discriminator, `etag` identifies a resource version, `updated` is RFC 3339, `deleted` signals deletion, and `lang` indicates language.
- Collections can use `items`, `currentItemCount`, `itemsPerPage`, `startIndex`, `totalItems`, `pageIndex`, `totalPages`, and a paging link template. Index/page fields are 1-based. `items` belongs last when a streaming parser benefits.
- Object links (`self`, `edit`, `next`, `previous`) can represent any reference; URI-string variants use the `Link` suffix (`selfLink`, `editLink`, `nextLink`, `previousLink`).
- Error envelopes use numeric `error.code`, primary `error.message`, and details in `error.errors[]`: `domain`, `reason`, `message`, `location`, `locationType`, `extendedHelp`, and `sendReport`.

## Compatibility

- Treat reserved names as semantically reserved even when optional. Do not redefine them. Resolve collisions with a new name or a major API version.
- Property order is generally free; put `kind` first and `data.items` last only where these legacy streaming conventions improve client performance.
