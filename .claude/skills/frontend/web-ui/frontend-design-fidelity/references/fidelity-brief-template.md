# Frontend fidelity brief

Use the parts relevant to the requested scope. A focused shared-field repair does not need a full product redesign document.

## Task and evidence

- Mode: existing app / prototype / planning only.
- Requested surfaces, existing features to preserve and explicit design requirements.
- Current source and rendered states inspected; old plans or hosted differences to resolve.
- Actual changes authorized; deployment and external actions only if separately requested.

## Recognizable design contract

| Role | Existing rule | Implementation owner | Evidence or unresolved choice |
| --- | --- | --- | --- |
| Canvas and surface hierarchy | | | |
| Body, label, data and display typography | | | |
| Accent, selected, error and focus meanings | | | |
| Control geometry and spacing relationships | | | |
| Media or identity treatment | | | |

## Composition and state ownership

For each affected surface, state the layout priorities, minimum useful content, scroll owner, overflow behavior, focused-field behavior and breakpoint transition. Identify the shared component or renderer that owns each rule. Record resource dependencies and usable fallbacks only where they apply.

| Condition | User-visible outcome | Responsible path | How to verify |
| --- | --- | --- | --- |
| Reference viewport with normal content | | | |
| Narrow and short available space | | | |
| Changed breakpoint boundaries | | | |
| Long content / large text / fallback font | | | |
| Focused field with software keyboard | | | |
| Slow resources / operation error / recovery | | | |
| Restored or unavailable draft storage | | | |
| Current generated output and stale-result race | | | |

Drop irrelevant rows and add product-specific cases. Do not turn a review into mandated tracking, a database migration or an external deployment.

## Observable acceptance criteria

Write outcomes instead of naming a technique. Examples:

- A two-line error remains associated with its input and does not obscure the recovery action.
- A short-height screen can reach every choice without a decorative stage creating a scroll trap.
- The shared field's keyboard focus is visible on each affected surface.
- Slow or missing display fonts do not leave ordinary page content behind an indefinite boot screen.
- Changing the selected item while a file renders cannot publish the old artifact as the current download.
- A prototype's successful simulated action remains clearly identified as simulated.

## Verification and handoff

Separate implementation review, automated checks, browser rendering, generated-file inspection, hosted parity and real-device checks. Report passed, failed, blocked or not run with the relevant environment. For planning only, deliver the contracts and untested acceptance criteria without claiming implementation. Include material limitations and unresolved product decisions; do not claim universal pixel identity across rendering engines.
