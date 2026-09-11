# Full worked example: an AI notes editor ("NoteKit")

This is one complete, specific application of the tactile UI system — a warm-black,
cream, and chartreuse study/notes app whose control feel is borrowed from Vyra's video
editor. Read this when the user explicitly wants *this* look, or as a model for how to
extend the base button/input/panel system (see `button-system.css`) into a full product
with domain-specific "instrument" blocks. Do not apply this palette to an unrelated
project by default — it's an example, not this skill's house style.

## Visual metaphor

The product should feel like a modern digital study desk, the notes equivalent of a
professional editing desk:

| Vyra              | Notes app                     |
| ------------------ | ------------------------------ |
| Video timeline       | Note block canvas              |
| Footage panel          | Notebook/library panel          |
| AI editing chat          | AI study assistant               |
| Video tracks               | Structured note blocks            |
| Export                       | Publish/share                      |
| Playhead                       | Current reading position            |
| Media properties                 | Block properties                     |
| Effects                            | Themes and interactive tools          |

Overall it should read as dark, warm and focused; dense enough for serious work but
friendly enough for students; modular (notes built from blocks); and AI-native (AI
activity visible but not visually overpowering). Explicitly avoid: a generic
purple-gradient AI SaaS look, a Notion clone, glassmorphism, or childish education
software.

## Color tokens

```css
:root {
  /* Main backgrounds */
  --background: #0d0e0c;
  --background-deep: #080907;
  --canvas: #11120f;

  /* Surfaces */
  --surface-1: #151613;
  --surface-2: #1b1c18;
  --surface-3: #23241f;
  --surface-hover: #292a24;
  --surface-active: #303129;
  --surface-elevated: #272822;

  /* Text */
  --text-primary: #f3f1e8;
  --text-secondary: #c8c6bc;
  --text-muted: #8b8c83;
  --text-faint: #62635c;
  --text-disabled: #484941;

  /* Main tactile color (the "raised button" surface) */
  --cream: #eeeadd;
  --cream-hover: #faf7ed;
  --cream-pressed: #ddd9cc;
  --ink-on-cream: #161713;

  /* AI and progress */
  --accent: #d6f36a;
  --accent-hover: #e4ff79;
  --accent-soft: rgba(214, 243, 106, 0.12);
  --accent-border: rgba(214, 243, 106, 0.35);

  /* Study block colors — one semantic hue per block type */
  --note-blue: #89a7e3;
  --quiz-purple: #b592d1;
  --flashcard-orange: #d8a86f;
  --diagram-cyan: #77bab6;
  --code-green: #85bd91;
  --warning-yellow: #e4c76d;
  --danger-red: #df7770;
  --success-green: #7dd596;

  /* Borders */
  --border-subtle: rgba(244, 242, 232, 0.07);
  --border-default: rgba(244, 242, 232, 0.12);
  --border-strong: rgba(244, 242, 232, 0.2);

  /* Radius */
  --radius-xs: 4px;
  --radius-sm: 6px;
  --radius-md: 9px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-pill: 999px;
}
```

Color rules — don't color every block randomly, keep the mapping meaningful:

- Cream = important human action.
- Lime = AI, connection, progress, active status.
- Blue = normal notes. Purple = quiz. Orange = flashcards. Cyan = flowcharts/diagrams.
- Green = code or a completed state. Red = destructive actions/errors.

## Page structure

```text
+-----------------------------------------------------------------+
| Logo  Notebook / Chapter                    Share  Publish      |
+--------------+---------------------------------+----------------+
|              |                                 |                |
|  Library     |        Note Canvas              | AI Assistant   |
|              |                                 |                |
|  Notebooks   |  Title                          | Chat           |
|  Recent      |  Text blocks                    | Suggestions    |
|  Favourites  |  Quiz                           | Tool activity  |
|  Trash       |  Flashcards                     | Sources        |
|              |  Flowcharts                     |                |
|              |                                 |                |
+--------------+---------------------------------+----------------+
|  Saved - 2 collaborators - AI connected - Version history        |
+-----------------------------------------------------------------+
```

```css
--sidebar-width: 248px;
--assistant-width: 340px;
--topbar-height: 52px;
--statusbar-height: 30px;
--canvas-max-width: 820px;
```

The center note canvas stays calm and readable; the side panels can be denser.

## Typography

One expressive display face only for landing-page headings — the editor itself stays
plain and readable.

```css
:root {
  --font-ui: "Geist", "Inter", sans-serif;
  --font-reading: "Inter", sans-serif;
  --font-editorial: "Source Serif 4", serif;
  --font-mono: "Geist Mono", monospace;
}
```

| Purpose          | Size    | Weight |
| ----------------- | ------- | -----: |
| Landing hero        | 64-76px | 600    |
| Page heading           | 28-36px | 600    |
| Note title                | 36-44px | 620    |
| Section heading              | 22-26px | 600    |
| Note body                       | 16-17px | 400    |
| UI label                           | 12-13px | 550    |
| Metadata                              | 11-12px | 500    |
| Tiny status                              | 10-11px | 550    |

Notes use 1.65-1.75 line height for comfortable reading; UI controls use tighter line
heights.

## Domain-specific blocks

Each interactive learning block should feel like an embedded instrument inside the
document, using the same border/highlight/depth system as buttons but its own semantic
accent color.

**Quiz block** — tinted with `--quiz-purple`, border `rgba(181,146,209,0.24)`,
background `rgba(181,146,209,0.055)`. Answer options depress slightly when selected,
same physics as a button press.

**Flashcard block** — see `.flip-card` in `button-system.css`; a 280-360ms 3D flip,
text stays static/readable after flipping, no exaggerated spring bounce.

**Flowchart/diagram block** — see `.dot-grid-canvas` in `button-system.css`; nodes use
the same tactile border + top-highlight system as buttons.

## AI assistant panel

The AI assistant should feel built into the editor, not pasted in as a separate
chatbot. Header pattern:

```text
* Note Assistant
  Reading: Hessian Matrix

                 Clear  ...
```

Composer uses `.composer-input` from `button-system.css` (inset, not raised), inset
into the panel:

```text
+------------------------------------------+
| Ask about this note...                    |
|                                            |
| + Context                 [Send arrow]    |
+------------------------------------------+
```

When the AI calls a tool, show visible, itemized activity rather than a spinner:

```text
* Creating quiz

  [x] Read note structure
  [x] Found 4 core concepts
  [ ] Generating questions
```

On completion, link directly to the affected content:

```text
[x] Quiz created
    5 questions added below "Concurrency"
                              View block ->
```

## Library / sidebar

Notebook items are compact rows (`.list-row` in `button-system.css`), not oversized
cards — 34px min height, active item gets a 3px lime indicator bar.

## Inputs, search, command palette

Inputs feel pressed inward (`.input` in `button-system.css`); a `/` command menu groups
commands by category (Basic, Study, Visual, AI) with ~42-46px rows — not giant.

## Per-note themes

Users can set a mood per note, but the app chrome stays consistent. A theme changes
only: canvas background, reading/heading fonts, block accents, cover, paper texture,
and note width. It never redesigns navigation, buttons, or dialogs.

```ts
type NoteTheme = {
  id: string;
  name: string;
  canvas: string;
  text: string;
  mutedText: string;
  accent: string;
  headingFont: string;
  bodyFont: string;
  contentWidth: "compact" | "comfortable" | "wide";
  texture: "none" | "paper" | "grain" | "grid";
  cornerStyle: "soft" | "square";
};
```

Example theme directions: Focus (warm black/cream), Paper (warm ivory), Midnight (dark
blue-black), Forest (muted green-black), Sakura (warm grey + dusty pink), Legal (ink
navy + parchment), Terminal (black/green/monospace), Classroom (off-white, blue/red
accents).

## Landing page

More spacious than the editor itself. Warm black background, large cream typography,
one live product demo built from real note blocks (not a 3D render or stock photo), and
small lime status indicators. No floating glass objects, no purple AI orb, no
gradient-text hero.

The strongest demo is showing the actual differentiator: an AI assistant (ChatGPT,
Claude, Codex, etc.) issuing an instruction like "turn my concurrency notes into a quiz
and flowchart," and the editor's blocks appearing live in response — because the same
notes are addressable by MCP, not just the in-app assistant.

## One-paragraph brief for a coding agent

> Build the notes platform as a warm, tactile, professional creative workspace inspired
> by the interaction quality of Vyra's video editor, while keeping an original
> notes-first visual identity. It must not resemble a generic purple-gradient AI SaaS,
> Notion clone, glassmorphism dashboard, or childish education app. Use warm near-black
> backgrounds, layered charcoal surfaces, cream primary controls, and a restrained
> chartreuse accent for AI activity, progress, connectivity, and focus. Tactility comes
> from 1px borders, inset top highlights, dark 2px bottom edges, small exterior shadows,
> 1-2px downward press movement, and fast 100-160ms timing. Primary buttons must
> translate down 2px and lose their bottom shadow on press; inputs feel inset rather
> than raised. Avoid blur, neon glow, large gradients, oversized radii, floating orbs,
> continuous animation, and hover scaling. Keep the note canvas calm and borderless by
> default, revealing block controls only on hover/selection. Interactive blocks (quiz,
> flashcard, flowchart, code) feel like embedded instruments with their own restrained
> semantic accent but the same geometry and depth system as everything else. The AI
> assistant feels integrated into the editor, with visible tool activity that links to
> the block it produced.
