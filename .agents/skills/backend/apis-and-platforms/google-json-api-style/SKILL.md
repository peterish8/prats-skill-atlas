---
name: google-json-api-style
description: Design, write, review, or document JSON API requests and responses using the Google JSON Style Guide. Use for REST or RPC JSON payload schemas, property names, values, pagination, links, errors, compatibility, and reserved response fields.
---

# Google JSON API Style

Apply this to JSON API contracts, not merely `.json` file formatting. This source is a legacy Google API guide; prioritize modern repository API standards, RFCs, OpenAPI contracts, and security requirements when they differ.

## Core contract

- Produce strict JSON: no comments, double-quoted property names and strings, and only `object`, `array`, `string`, `number`, `boolean`, or `null` values. Never embed JavaScript expressions/functions.
- Use meaningful ASCII lowerCamelCase property names. Start with a letter, `_`, or `$`; avoid JavaScript reserved words. Name array fields plural and other values singular, except naturally count-like names such as `itemCount`.
- Distinguish an object used as a structured record from one used as a map. Document maps explicitly; arbitrary map keys may use Unicode and need bracket-style client access.
- Do not arbitrarily nest/group data. Use a hierarchy only when the grouped fields form a semantic unit.
- Omit optional empty/null fields unless their presence has distinct semantics. Keep meaningful zero/false values.
- Encode evolving enum values as strings. Encode dates as RFC 3339 strings, durations as ISO 8601 strings, and lat/long as ISO 6709 strings where those concepts apply.
- Avoid name collisions. Add a new name or version the API at a major boundary—there is no JSON namespace mechanism.

## Google response layout (use only when compatible)

- A top-level envelope can contain `apiVersion`, client-echoed `context`, server-generated `id`, `method`, `params`, and exactly one of `data` or `error`.
- In `data`, use `kind` as a type discriminator, `etag` for versioning, and reserved pagination/link names only with their stated semantics. Put `kind` first in an object and `items` last in a `data` collection when stream parsing matters.
- Represent a collection with `items`, `currentItemCount`, `itemsPerPage`, `startIndex` (1-based), `totalItems`, `pageIndex` (1-based), `totalPages`, and appropriate `nextLink`/`previousLink` or object links. Do not emit fields a client cannot use.
- Represent errors as `error.code`, a human-readable `error.message`, and optional detailed `error.errors[]` entries with `domain`, `reason`, `message`, `location`, `locationType`, `extendedHelp`, and `sendReport`.

## Review checklist

- [ ] The payload is valid JSON and all names/values have intentional types and semantics.
- [ ] Optional values, enums, date/time values, maps, nesting, and compatibility are deliberate.
- [ ] Collection, link, version, and error fields follow the service contract.
- [ ] No reserved name has been repurposed and no backward-incompatible rename slipped in.

Read [references/rules.md](references/rules.md) for the full reserved-field meanings before designing an envelope or paginated response.
