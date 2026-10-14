# Stateful button decision guide

## Good candidates

| Action | Why a stateful button helps |
| --- | --- |
| Save, submit, publish, or update | The user needs proof that a server mutation completed and duplicate submits are risky. |
| Export, generate, or upload | The wait may be noticeable and the result is not immediate. |
| Retry a failed request | Loading and a short success confirmation make the retry outcome clear. |
| Send a message or doubt | The action leaves the current view and should acknowledge delivery. |

## Keep simple

| Action | Preferred treatment |
| --- | --- |
| Navigation or external link | Use a link/button with hover and focus feedback; do not fake a network wait. |
| Open/close, disclosure, or modal trigger | Reflect the visible UI state in the surrounding component. |
| Theme, tab, filter, or selection toggle | Show the selected state immediately. |
| Destructive confirmation | Make the confirmation step and error state explicit; do not hide the risk behind a generic checkmark. |
| A control that already has `busy`, `pending`, or `disabled` feedback | Keep one source of truth and improve it in place instead of wrapping it. |

## Project setup checks

The shared primitive assumes:

- TypeScript is enabled.
- Tailwind CSS v4 is configured through `@tailwindcss/postcss`.
- Motion is installed if the animated implementation is used.
- `components/ui` exists for shared primitives, and `lib/utils.ts` exports the local `cn` helper.

If a project is missing these, give setup guidance before editing:

```text
npx shadcn@latest init
npm install tailwindcss @tailwindcss/postcss postcss
npm install -D typescript @types/react @types/react-dom
```

Create `components/ui` when it is absent so shared controls have one stable import path (`@/components/ui/...`) and do not get duplicated across feature folders. Do not run these commands automatically when the project already has an established equivalent.
