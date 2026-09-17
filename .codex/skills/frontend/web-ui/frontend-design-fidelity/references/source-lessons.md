# Lessons from the Polaris frontend

These lessons were extracted from the inspected Polaris Cubing Club Survey checkout on 2026-09-17, baseline `390fc6ff1c168e5b14229207c557974ad3f094a1`. Paths below identify evidence in that source; this skill does not require that repository. They supplement the earlier motion and UX extraction with implementation fidelity.

| Source evidence | Additional lesson | Transfer to another product |
| --- | --- | --- |
| `src/app/globals.css` defines semantic surfaces, text roles, border strengths, accent meanings and shared controls | Consistent small decisions make a recognizable interface | Map existing roles and fix the common primitive when several consumers drift |
| `src/app/layout.tsx` assigns sans, mono and display fonts; badge identity uses display type while ordinary labels remain sans | Distinctive typography needs a limited job | Keep expression on identity surfaces and readability on operational copy |
| `globals.css` chooses different height/scroll behavior for story, question, review and badge modes, with short-height and desktop rules | Responsiveness is a composition and content decision | Choose scroll ownership per surface; preserve all choices and actions before preserving ornament |
| `layout.tsx` sets the document background before stylesheet delivery; `use-page-ready.ts` races font readiness against a 1500ms cap and then schedules painted frames | The first usable frame is part of the design | Avoid a mismatched initial flash; wait only for necessary resources and keep a bounded fallback |
| `ui/text-field.tsx` links label, hint and error; `lib/keyboard.ts` yields global shortcuts to controls; journey code moves focus after advance | Interaction semantics carry the design through keyboard use | Repair labels, focus ownership and announcement behavior in shared controls |
| `lib/journey-store.ts` uses versioned tab storage with guarded read/write; journey code restores history and trims retained answers after submission | A designed experience must account for interruption and local-data lifetime | Specify what resumes, how malformed drafts are handled and what is cleared |
| `experience/badge.tsx` measures ticker/container width, limits name size and precomputes a share file; `badge-image.ts` separately measures text for canvas output | Final polish depends on real dimensions and the actual output | Check long content, resize boundaries, fonts and current-snapshot artifact readiness |

## Source observations versus guarantees

The initial extraction included a public 390×844 walkthrough through review/edit, a fresh 1440×900 opening and two isolated source-generated 1080×1350 PNGs. It did not test final production submission, native sharing, every desktop state or real-device keyboard/reduced-motion behavior. The hosted review differed from the current checkout. These observations must not be carried into another app as proof that its implementation works.

The source also contains tradeoffs to improve rather than copy mechanically:

- Old planning files describe blue/violet controls and older geometry; the current stylesheet implements gold/cream, pill actions and a different flow. An explicit locked user requirement still takes precedence, but resolve stale-plan differences from current evidence instead of mixing systems.
- The on-screen badge estimates name width from character count, while canvas uses measured text. This demonstrates two renderers, not a universal text-fitting formula. Proportional glyphs, scripts and translations need representative checks.
- The decorative opening caps font waiting; the independent canvas renderer directly awaits font readiness. Do not infer that every resource path is bounded or has a usable fallback.
- Mobile inputs are moved high in the stage and viewport metadata requests keyboard overlay behavior. That is a strategy, not a cross-browser device guarantee.
- Source storage has a version/navigation check and guards exceptions. A new target should validate its whole restored payload and permitted ranges; copied existence checks are not a security or correctness proof.
- Share preparation is tied to name/pattern effects, but readiness, activation and target-app support remain platform concerns. Do not promise delivery because a browser API returned.

The reusable result is a method for preserving fidelity across conditions. It is not a claim of measured engagement, complete accessibility conformance or production readiness.
