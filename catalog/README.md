# Prats Skill Atlas catalog

`skills.json` and `skills.md` are generated from the four runtime trees by `scripts/build-catalog.ps1`.

The catalog is the discovery layer used during onboarding. Agents should inspect its names, categories, runtime availability, and descriptions first, then read full `SKILL.md` files only for approved candidates.

## Categories

- `planning/project-planning` — plans, milestones, project execution, and launch workflows
- `product-growth/{user-research,funnel-and-activation,experimentation,monetization,retention-and-referral,measurement-and-ops,ethical-growth,orchestration}` — evidence-led research, activation, monetization, retention, experimentation, and growth operations
- `frontend/web-ui` — web UI, React, Next.js, CSS, browser, and interaction surfaces
- `backend/apis-and-platforms` — APIs, databases, server runtimes, cloud platforms, and typed backend work
- `architecture/system-design` — architecture, domain modeling, codebase boundaries, and system structure
- `mobile/native-and-cross-platform` — Expo, React Native, iOS, SwiftUI, Kotlin, and Android
- `design/visual-and-motion` — branding, product design, interaction, animation, and visual direction
- `security/appsec-and-privacy` — security, privacy, bug bounty, hardening, and security headers
- `security/reverse-engineering` — guarded reverse engineering and authorized security routing
- `testing/qa-and-verification` — accessibility, QA, testing, debugging, audits, and performance
- `devops/delivery-and-tooling` — Git, deployment, CI/CD, release, and environment setup
- `research-data/research-seo-and-content` — research, SEO, analytics, editorial, and data workflows
- `docs/writing-and-specs` — documentation, plans, specifications, PRDs, and writing workflows
- `integrations/platform-tools` — MCP, Figma, Google, Canva, Obsidian, and external tools
- `agent-workflows/{gsd,gstack,coordination,orchestration}` — agent coordination, multi-agent engineering loops, context, principles, GSD, and GStack workflows
- `specialists/domain-workflows` — legal, product, sales, education, and other domain-specific packages
- `tools-utilities/general-purpose` — general-purpose helpers and packages without a stronger category

Category assignment is name-based and deterministic. It is also encoded directly in each runtime tree; installers flatten the three-level category layout back to the runtime discovery layout.
