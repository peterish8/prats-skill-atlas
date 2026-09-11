---
name: product-to-launch
description: Run a product from canonical scope through architecture, implementation, verification, deployment, marketing, and sales.
metadata:
  short-description: Product build-to-launch workflow
---

# Product to launch

Use this skill when the user wants an end-to-end product change or launch workflow, from shaping the request through building, testing, releasing, and creating the first growth and sales assets. It is also useful when the user explicitly asks to run the product-manager -> architect -> build -> design -> verify -> deploy -> marketing -> sales sequence.

## Source of truth

Before making decisions, inspect the exact repository and read its local contract files: `AGENTS.md`, `CONTEXT.md`, planning/requirements/roadmap files, architecture decisions, and the existing implementation. Treat those files and the current product UI as authoritative. Do not import rules from another project, invent credentials, or replace an established product feel with a generic redesign.

Start by checking the current Git state, runtime/tooling, available tests, deployment target, and whether the request is implementation, diagnosis, or read-only review. Preserve unrelated changes. For Windows JavaScript projects, prefer `npm.cmd`/`npx.cmd` when the PowerShell shims are broken.

## The workflow

Run these lanes as gated handoffs. Parallelize only disjoint work and never let multiple writers edit the same files without an explicit integration pass.

### 1. Product manager: define the slice

- Reconcile the request with the repository's canonical scope.
- State the user journey, acceptance criteria, non-goals, dependencies, and release gates.
- Identify the smallest complete vertical slice instead of creating placeholder routes or disconnected UI.
- If the idea itself is unvalidated, use `project-idea-validator` before implementation.

### 2. Architect reviewer: protect the system

- Map callers, modules, data flow, persistence, auth boundaries, and failure states.
- Reuse existing seams and equivalent implementations before introducing a subsystem.
- Record decisions and rejected alternatives when they affect storage, contracts, routing, or deployment.
- Check that the proposed slice does not violate local invariants such as ownership boundaries, source-of-truth content, or no-cron constraints.

### 3. Build: choose the correct specialist

Use the narrowest implementation lane that covers the change:

- `nextjs-developer` for Next.js App Router, server/client boundaries, SEO, loading/error states, and deployment-aware web work.
- `fullstack-developer` for a complete vertical slice across UI, auth, APIs, and persistence.
- `expo-react-native-expert` for Expo/React Native mobile work; use the installed Kotlin specialist for native Kotlin/Compose projects.

Implement real behavior and persistence where required. Do not stop at mockups, placeholder content, route shells, or a passing typecheck. Keep authorization, validation, async feedback, human-readable errors, retry paths, and empty states in the same slice.

### 4. UI designer: preserve and extend the product language

Inspect existing tokens, typography, spacing, interaction patterns, and reference screens first. Refine the shared renderer or component path. Keep the established layout and behavior unless the product contract explicitly changes them. Include responsive behavior, keyboard/focus states, disabled/loading states, and accessible names.

### 5. UI/UX tester: exercise the real journey

Test the documented user flow end to end, including first load, loading, success, empty, error, retry, disabled, mobile, keyboard, and navigation states. Check spacing, hierarchy, touch targets, visual consistency, and whether state survives the expected navigation. Capture concrete defects with file/route and reproduction steps.

### 6. QA expert: verify the change

Create a focused test matrix from the acceptance criteria. Run the smallest relevant checks first, then the repository's full lint/type/test/build suite when practical. Add or update tests for the changed contract and failure paths. Distinguish a static pass from browser, live-service, device, or production evidence.

### 7. Security auditor: harden before release

Audit authentication and authorization, secrets, input validation, injection/IDOR paths, uploads, rate limits, error leakage, dependency/configuration exposure, and deployment settings. Keep an audit read-only unless the user requested fixes; when fixing, make narrow changes and rerun the affected checks. Never print credentials in logs or reports.

### 8. Deployment engineer: make release evidence explicit

Verify the production build, migrations/configuration, environment variables, preview or deployment path, rollback plan, and post-deploy smoke checks. Report local build success, deployed success, live-service success, signed-artifact success, and physical-device success as separate facts. If a required CLI or credential is missing, state the exact blocker and the next command; do not infer deployment success.

### 9. Marketing: turn the verified product into a message

Only after the product journey is demonstrable, produce positioning, target audience, problem/outcome messaging, landing-page copy, screenshots or demo narrative, launch content, SEO targets, and a short announcement plan. Use `landing-page-copywriter`, `content-marketer`, and `seo-specialist` as appropriate. Keep claims tied to verified behavior; do not market placeholder or unverified capabilities.

### 10. Sales: create a repeatable path to adoption

Define the ICP, buyer/user distinction, qualifying questions, discovery script, product demo sequence, objections, proof points, pilot/onboarding path, pricing assumptions, and follow-up sequence. Use `sales-engineer` for technical demos and institutional or B2B products. Use `customer-success-manager` after launch for onboarding, activation, retention, and churn signals.

## Coordination rules

- Maintain a visible task plan and mark a lane complete only after its evidence exists.
- Keep delegated work scoped to named files or artifacts; inspect the result and integrate it locally.
- Do not claim parity from route presence, a successful build, or a generated artifact alone.
- For mobile, separate export/build from emulator or physical-device installation and runtime verification.
- For web deployments, separate local checks from live Vercel/production checks. The Vercel CLI may be needed for `vercel env pull`, `vercel deploy`, or `vercel logs`.
- If the request is explicitly read-only, stop before edits, writes, commits, deployment, or launch publication.

## Final handoff

Report:

1. What was shipped and which files/contracts changed.
2. Checks that passed, with exact commands where useful.
3. What was manually tested and what was not tested.
4. Open blockers separated into credentials, live deployment, device, signing, capacity, or product decisions.
5. The launch message, target audience, sales next step, and the smallest follow-up task.
