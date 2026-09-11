---
name: tactile-ui-system
description: Applies a physical, tactile control system to a UI — buttons that visibly press down and lose their bottom shadow on click, inset "pressed-in" inputs, layered panel depth, and fast 100-190ms motion. This is a theme-agnostic interaction language (the physics), not a color palette — it adapts to whatever colors/tokens the target project already uses. This skill should be used when the user asks for buttons/controls to "feel pressable," "feel physical," "feel like Vyra," "feel tactile," or complains that an interface feels flat, glassy, or like a generic gradient AI SaaS product.
---

# Tactile UI System

A portable interaction language extracted from Vyra's control feel: buttons read as
physically raised, inputs read as physically inset, and pressing something moves it.
It is defined by depth and motion, not by any specific palette — apply it to whatever
colors a project already has.

## Core principle: separate physics from palette

Every control in this system has two independent layers:

1. **Physics (non-negotiable defaults)** — border, inset highlight, dark bottom edge,
   exterior shadow, press displacement, timing. These transfer to any project unchanged.
2. **Palette (always adapt to the target project)** — surface colors, text colors, accent
   color. Never impose a specific color scheme (e.g. warm cream/lime) on a project that
   already has its own design tokens or brand colors, unless the user explicitly asks for
   that exact look. Read the project's existing CSS variables/Tailwind theme first, then
   plug those into the formulas below.

If the target project has no existing token system yet, propose one and confirm the
palette direction with the user before generating a full component set — don't assume
"warm black + cream + lime" is wanted just because it's this skill's origin example.

## Non-negotiable physical rules

- 1px border on every control.
- A subtle **inset top highlight** (`inset 0 1px 0 <lighter-than-surface>`) — the "light
  hitting the top edge" cue.
- A solid, non-blurred **bottom edge** 1-2px down in a darker shade — this is what reads
  as "raised," not a soft shadow alone.
- One soft **exterior shadow** for ambient elevation — keep it small, never a large glow.
- On `:active`, raised controls (buttons) translate down 2px **and lose the bottom edge
  shadow** — that disappearance is what sells the press. Inset controls (inputs, the AI
  composer) do the opposite: they're already recessed via `inset` shadow, so focus adds a
  colored ring instead of movement.
- Timing is fast: 100-120ms for button press, 130-190ms for hover/dropdown, 200-260ms for
  panels/modals, up to 360ms only for a deliberate flip/flourish (e.g. a card flip). Full
  table in `references/motion-timing.md`.
- Never use `scale()` on hover for ordinary controls — vertical displacement reads as
  physical, scaling reads as a web-app hover effect.
- Never use large glows, blur/glassmorphism, oversized pill radii, or continuous/pulsing
  animation on interactive elements. Restraint is what keeps this feeling like a precision
  tool instead of a marketing SaaS page.

## Workflow

1. **Read the project's existing tokens.** Grep for CSS custom properties, a Tailwind
   theme config, or a design-tokens file. Identify: base background, 2-3 surface levels,
   primary text, muted text, one accent/brand color, and any existing radius scale. If
   none exist, ask the user for (or propose) a minimal palette before proceeding.

2. **Map physics onto those tokens.** Open `references/button-system.css` — it's written
   against generic variable names (`--surface-1`, `--surface-3`, `--accent`, `--border-default`,
   `--text-primary`, etc.). Substitute the project's actual token names/values in place of
   those, keeping every shadow/border/transform value as-is. Do not simplify away the
   inset-highlight + bottom-edge + press-displacement combination — that combination *is*
   the effect.

3. **Build the button set.** At minimum: primary (the highest-contrast "raised" control,
   typically light-on-dark or the strongest brand color), secondary (neutral raised), an
   accent/action variant (for AI or brand-highlighted actions — a tinted fill with a
   colored border, not a glow), ghost (no border/shadow until hover), and destructive. If
   the project uses Tailwind + `cva`, adapt `references/tailwind-cva-pattern.tsx` instead
   of writing raw CSS classes.

4. **Extend the same physics to non-button controls**: icon buttons (compact, 30-34px,
   same border/highlight system at smaller scale), inputs and search/command fields
   (inset shadow instead of raised, colored focus ring), panels/cards (hairline border +
   soft ambient shadow, not the button's hard bottom edge), and list/sidebar rows (flat
   until hover, a small tinted background plus a thin accent-colored indicator bar for the
   active state). All of these are in `references/button-system.css`.

5. **Apply the motion table** from `references/motion-timing.md` across every interactive
   element so the whole surface feels consistently fast, not just the buttons.

6. **Sanity check before finishing**: does anything glow, blur, scale on hover, or use a
   pill radius bigger than the rest of the UI? If yes, that element is off-system — fix it
   or justify why it's an intentional exception.

## Reference files

- `references/button-system.css` — full component CSS: primary/secondary/accent/ghost
  buttons, icon buttons, inputs, panels, list rows, a card-flip pattern, and a dot-grid
  canvas background. Variable names are illustrative placeholders — retarget them to the
  project's real tokens per step 2 above.
- `references/tailwind-cva-pattern.tsx` — the same button system as a Tailwind `cva()`
  variant map, for projects using `class-variance-authority`.
- `references/motion-timing.md` — the full interaction-duration table and easing curves.
- `references/full-example-notekit.md` — a complete worked application of this system to
  a specific product (a warm-black/cream/lime AI notes editor, including page layout,
  type scale, and domain-specific blocks like quizzes/flashcards/flowcharts). Read this
  when the user wants that *exact* look, or as a worked example of how to extend the
  system with domain-specific "instrument" components beyond plain buttons — not as a
  default palette to apply elsewhere.
