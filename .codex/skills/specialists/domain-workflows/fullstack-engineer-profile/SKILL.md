---
name: fullstack-engineer-profile
description: Build evidence-based full-stack engineer profiles and resumes by assessing frontend and backend work in the user's selected portfolio projects.
---

# Full Stack Engineer Profile

Use this skill when Prathick asks for a full-stack resume, a description of frontend and backend strengths, or an evidence review of his selected product work.

## Scope

Use the current project list on [Prathick's portfolio](https://prathick.vercel.app) as the source of eligible projects. Also include Allegra at [allegravibe.vercel.app](https://allegravibe.vercel.app) and the LuvLyrics Android app in <allegra-root>, because the user explicitly added them. Read [portfolio-scope.md](references/portfolio-scope.md) for the starting list and local paths, then refresh the live portfolio and repository state before making claims.

For the initial resume request, the user excluded Gavelogy. Keep it out of those deliverables. Apply a later change in scope if the user asks for it.

Search only the user-designated project roots and <allegra-root>. Prefer read-only inspection; preserve existing worktree changes. Confirm that a local folder maps to the named product using its README, deployment metadata, or remote before using it. If source is not present, keep claims at the level stated on the portfolio and label the gap.

## Evidence workflow

1. Separate each claim into frontend, backend/data, integration, and delivery evidence.
2. For frontend, look for implemented user flows, state handling, responsive behavior, accessibility, interaction design, and visual-system decisions. For backend, look for data models, persistence, APIs, authentication, provider integrations, synchronization, offline behavior, validation, and failure handling.
3. Keep a short evidence trail with repository-relative paths or public URLs. Mark each item as code-verified, documentation-stated, portfolio-stated, or unknown.
4. Describe strengths with concrete examples. Use labels such as demonstrated, partial, or not evidenced when a summary is useful. Do not assign unsupported numerical scores or call a whole product excellent based on its stack.
5. Distinguish product capabilities from Prathick's contribution. The portfolio describes his work; when a repository has multiple contributors or ownership is unclear, phrase the claim narrowly and do not imply sole authorship.
6. Use metrics only when their source and measurement context are clear. Do not estimate adoption, revenue, latency, scale, or performance.

## Resume and profile writing

Emphasize the interface-to-data path: the user problem, the frontend behavior, the backend seam, and what the implementation enables. Prefer a few well-supported project examples over a catalog of technology names. Keep project names and stacks aligned with the refreshed sources.

For an ATS resume, use standard headings, a single-column layout, selectable text, and concise action-led bullets. Avoid tables, icons, rating bars, and keyword stuffing. Keep the target role's requested emphasis; a full-stack resume should show both sides without burying the frontend work.

The portfolio identifies Prathick as a B.Tech CSE student and exposes pratsprofess@gmail.com, GitHub peterish8, and prathick.vercel.app. Prathick provided Polaris School of Technology and expected graduation year 2029 for the current resume. Do not assume other personal details such as a phone number or LinkedIn URL; omit them unless provided.

Do not edit application repositories or publish external changes when preparing a profile or resume. If a requested deliverable has missing personal facts, create the best accurate draft and call out only the remaining facts needed to finalize it.
