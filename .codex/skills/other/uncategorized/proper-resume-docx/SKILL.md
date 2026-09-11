---
name: proper-resume-docx
description: Use when creating, rewriting, or formatting Prathick Dhanes R resumes as .docx files, especially master resumes, SDE resumes, mobile resumes, project-bank resumes, ATS resumes, or any request to follow the clean Claude-style Node docx resume format.
metadata:
  short-description: Build Prathick resume DOCX files in the strict Node docx format
---

# Proper Resume DOCX

Use this skill whenever the user asks to create or modify a resume/CV for Prathick Dhanes R, especially if they mention master resume, SDE resume, mobile resume, full-stack resume, ATS, `.docx`, Claude-style formatting, or the strict resume format.

## Non-Negotiables

- Create a fresh `.docx` unless the user explicitly asks to update an existing one.
- Use the `docx` npm package in Node.js for new resumes. Do not use `python-docx` for final generation unless the user explicitly asks for a fallback.
- Use Arial for every visible run. Every `TextRun` must specify `font: "Arial"` unless using a helper that does it.
- Use Letter paper: `12240 x 15840` DXA.
- Use 1 inch margins (`1440` DXA) for full/master resumes. Use 0.75 inch (`1080` DXA) only when the user explicitly asks for a one-page resume.
- No header/footer content.
- Default full/master line spacing should be `line: 276, lineRule: "auto"`.
- Section order for Prathick master resumes:
  1. Name
  2. Link row
  3. Professional Summary
  4. Freelancing Experience
  5. Projects
  6. Open Source Contributions, when relevant
  7. Skills
  8. Education
  9. Extra-Curricular
- Do not mention Rocket.Chat, Oppia, or any other org unless the user explicitly asks. For open source, use only MoFA by default.
- Near-completion notes, TODOs, or project cleanup lists belong in chat, not in the resume.

## Style Contract

- Primary text: `1A1A1A`
- Link blue: `1155CC`, underlined
- Grey metadata: `444444`
- Name: 18 pt (`size: 36`), bold
- Section headers: 12 pt (`size: 24`), bold, uppercase, bottom border only
- Job/project title rows: 12 pt (`size: 24`), bold left text, right date 10 pt grey
- Sub rows: 10 pt (`size: 20`), italic, grey
- Body, bullets, skills, links: 10 pt (`size: 20`)
- Use right tab stop at `9360` for two-column title/date rows.
- Section header border: `BorderStyle.SINGLE`, `size: 8`, black `000000`, `space: 2`.
- Bullets use `numbering` reference `"bullets"` with `LevelFormat.BULLET`, text `"-"`, indent `{ left: 360, hanging: 180 }`.
- If the renderer hides bullet numbering, either keep numbering and add visible dash text, or use visible dash paragraphs consistently. Prefer a clean visual result over blind adherence.

## Workflow

1. Read the user’s requested target: master, SDE, mobile, full-stack, one-page, project bank, or custom.
2. Gather facts from the local project folders or existing resumes if needed. Do not invent links, dates, metrics, companies, or education details.
3. Read `references/generator-pattern.md` before writing the Node generator.
4. Write a `generate_*.js` file in the workspace using the helper pattern from the reference.
5. Run it with the available Node runtime and `NODE_PATH` pointing to the runtime’s `node_modules`.
6. Validate content:
   - Search generated source/text for forbidden org names when the user has excluded them.
   - Confirm MoFA PRs if included:
     - `https://github.com/mofa-org/mofa/pull/1666`
     - `https://github.com/mofa-org/mofa/pull/1674`
   - Confirm no TODO/near-completion wording appears inside the resume.
7. Render the DOCX to page PNGs using the Documents skill renderer when available, inspect pages, and iterate until layout is clean.
8. Final response should link the final `.docx` and briefly mention verification. Keep any near-completion project list separate in chat only.

## Prathick Defaults

Use these defaults only when the user has not provided better current values:

- Name: `Prathick Dhanes R`
- GitHub: `https://github.com/peterish8`
- MoFA PRs: `pull/1666`, `pull/1674`
- Good project categories:
  - Client/freelance: Gavelogy, ASPPL, Rotary Club of Gudalur Garden City
  - Full-stack: CineBlock, ClassDrop, SkillSync, Indian Cubing League, Meet&Study
  - Mobile: FamilyForge, CallRemind, Memoir
  - Developer/AI tooling: PixelPatch, SonicForge, Luma Note AI
- If the user says “only MoFA,” exclude all other open-source organizations.

## Quality Bar

A proper resume from this skill should feel like a clean recruiter-facing document, not a project dump. Prefer stronger projects, concise impact bullets, concrete technologies, and live links where verified. Keep master resumes complete but organized; keep targeted resumes selective and tighter.
