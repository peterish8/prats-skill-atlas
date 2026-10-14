# Website review protocol

## Establish the brief

Record audience, use context, main journey, real capabilities and approved claims, route scope, prototype limits, visual references, existing tokens/components, stack, authorization, and the planned inspection methods. Label provisional assumptions. A reference is visual input unless the user makes its content a requirement.

For textured or 3D references, preserve art direction while checking legibility, edge contrast, hierarchy, recognizable controls, and rendering cost. An expressive surface is not automatically a defect.

## Interpret the checklist

The four bases in audit-map.json distinguish:
- **heuristic:** a visual judgment evaluated against the brief and experience.
- **practice:** usability or engineering guidance, sometimes derived rather than directly prescribed by a source.
- **standard:** an accessibility criterion with scope and exceptions.
- **product_constraint:** truth or data integrity dependent on the product contract and evidence.

Every check was reviewed for useful wording. That does not establish 150 universal requirements or 150 website passes. Keep IDs stable for traceability. Group IDs that describe one root defect into a single finding.

## Outcomes and evidence

| Status | Requirement |
| --- | --- |
| PASS | Applicable behavior/design inspected in the stated scope, with supporting evidence. |
| FAIL | Observed problem, location/state, user impact, and reproducible evidence where applicable. |
| NOT_APPLICABLE | Prerequisite absent; record why. An inaccessible state is not N/A. |
| UNVERIFIED | Missing evidence, unexercised state, or material uncertainty. |

| Method | What it supports | Limit |
| --- | --- | --- |
| SCREENSHOT | Visible composition, text, clipping, hierarchy | Only the captured state |
| SOURCE | Implementation paths, semantics, configuration | No runtime or persistence proof |
| DOM | Names, landmarks, roles, relationships, computed styles | No proof of actual screen reader output |
| TASK | Recorded actions and resulting states | Only tested routes, roles, devices, and failure paths |
| MEASUREMENT | Contrast, dimensions, timings, layout shifts | Named conditions only |
| DOCUMENT | Requirements, approved claims, source records | No proof of working UI |

Name the actual assistive technology/device before claiming screen reader validation. Never perform destructive, paid, or private production actions merely to fill the ledger without authorization. Mark untested cases UNVERIFIED.

For a full audit, start with all 150 rows, determine applicability, and record each outcome plus route/component, state, viewport, method, and evidence. For a small change, identify the checks examined and report the limited scope.

## Priorities

| Priority | Observed impact |
| --- | --- |
| P0 | Serious data loss, unauthorized disclosure, or materially deceptive product information |
| P1 | Main task blocked, core information unusable, or an essential control inoperable |
| P2 | Task possible with confusion, delays, interpretation errors, or workarounds |
| P3 | Visual polish or consistency with limited task impact |

Justify priority and confidence using evidence. An unconfirmed suspicion stays UNVERIFIED. Do not convert this scale into an AI score or an arbitrary overall trust score.

## Reusable report

Use this structure for a substantial audit; concise prose is sufficient for a narrow fix.

```markdown
# Website design review

## Scope and evidence
Product/audience/main journey:
Routes/roles/viewports/states inspected:
Prototype or connected service:
Methods/measurements:
Unavailable states and limitations:

## Findings
| Finding | Check IDs | Priority | Location/state | Observation and impact | Evidence | Fix | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Decisions to preserve
Describe deliberate choices that suit the brief and why.

## Coverage
PASS: ...; FAIL: ...; NOT_APPLICABLE: ...; UNVERIFIED: ...
For a full audit the counts sum to 150; link the complete ledger.

## Changes and remaining work
Record actual authorized changes and before/after evidence.
Describe unresolved findings and their required evidence or next action.
```

A finding needs observation, impact, location/state, and a justified fix. “Looks AI” alone is not a finding. Preserve deliberate gradients, shadows, 3D, whitespace, and familiar patterns when they serve the product.
