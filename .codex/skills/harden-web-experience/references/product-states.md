# Product state and message contracts

## Contents

1. Async action contract
2. Screen-state contract
3. Human-readable errors
4. Destructive and optimistic actions
5. Accessibility details

## 1. Async action contract

Every request-backed control must answer: Did my action start? Can I safely click again? Did it finish? What changed? What should I do if it failed?

| State | Product behavior |
| --- | --- |
| Idle | Clear action label and enabled state based on actual prerequisites. |
| Pending | Immediate local spinner/progress text, stable geometry, repeated activation prevented or safely idempotent, cancellation when meaningful. |
| Success | Confirm the real outcome, reconcile displayed data, restore focus/controls, and avoid redundant success noise for obvious transitions. |
| Validation failure | Preserve input, identify each problem, explain the correction, associate errors with fields, focus first invalid field when useful. |
| Auth failure | Explain that the session/access changed, preserve safe work, offer sign-in or a permitted destination. |
| Conflict | Explain that data changed, prevent silent overwrite, offer refresh/review/merge appropriate to the domain. |
| Offline/timeout | State that completion was not confirmed, preserve work, expose retry/reconnect, and avoid unsafe automatic mutation retry. |
| Unexpected failure | Plain-language outcome, safe next step, retained context, and an internal correlation path if the product supports it. |

For long work, prefer determinate progress when measurable. For short unknown work, use a spinner or concise progress label. Do not show a skeleton for an action that already has content; keep the content and mark it refreshing.

## 2. Screen-state contract

| State | Required content |
| --- | --- |
| Initial loading | Size-stable structure matching final content; meaningful progress name when needed; no blank page. |
| Refreshing | Existing usable data remains; subtle refresh indicator; stale content is not presented as freshly confirmed when that matters. |
| First-use empty | What belongs here, why it helps, and one primary next action. |
| Empty search/filter | Query/filter remains visible; say nothing matched; offer clear/reset or useful guidance. |
| Permission | Explain access is unavailable without revealing protected data; give a safe route back or request-access action if real. |
| Not found/deleted | State the item is unavailable and offer the nearest useful destination. |
| Partial data | Keep working sections, identify the unavailable section, and offer targeted retry. |
| Offline/cached | Clearly distinguish cached content, pending changes, and unsent/failed changes. |

Reserve media and dynamic-content space to prevent layout shift. Avoid indefinite loaders: use a timeout transition or helpful delayed message when the operation exceeds normal duration.

## 3. Human-readable errors

Write messages as:

`what happened + what was preserved/affected + what the user can do next`

Examples:

- `We couldn't save your changes. Your edits are still here; check your connection and try again.`
- `This invite has expired. Ask the workspace owner for a new link.`
- `That name is already in use. Choose a different name.`
- `Your session ended before the upload finished. Sign in and retry the upload.`
- `We couldn't confirm the payment. Check your orders before trying again.`

Avoid `Unknown error`, `Request failed`, raw status codes, blame, false certainty, jokes during serious failure, and instructions the product cannot actually perform. Tailor copy to the action and user role.

## 4. Destructive and optimistic actions

- Name the affected object and consequence. Use confirmation for irreversible/high-impact actions, not every minor action.
- Prefer undo or recovery for reversible actions. Do not call a permanent delete `remove` if it cannot be restored.
- Disable confirmation while pending and prevent duplicate mutations.
- For optimistic UI, define rollback and server reconciliation before enabling it. Do not use optimistic confirmation for payments, permissions, or other high-risk outcomes unless the domain protocol supports it.
- On ambiguous failure, do not encourage a duplicate write. Check server state or provide a safe verification path first.

## 5. Accessibility details

- Prefer native `button`, `a`, `input`, `progress`, and `dialog` semantics where supported.
- Use `aria-busy` on the affected region when it helps. Keep status text available to assistive technology even when the visual uses only a spinner.
- Use polite status updates for routine progress and alerts for urgent errors. Avoid announcing the same message repeatedly.
- Keep focus on the initiating control for inline operations. Move focus only when context changes or the user must correct an error; return focus after dialogs.
- Ensure disabled behavior does not strand users or hide why an action is unavailable. If explanation or focus is required, consider an enabled control with guarded activation or `aria-disabled` plus correct event handling.
- Respect reduced motion and do not use animation as the only progress cue.
