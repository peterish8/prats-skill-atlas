# devops/delivery-and-tooling

Skills in this category: 14

| Skill | Available in | Description |
| --- | --- | --- |
| `git-guardrails-claude-code` | Agents, Claude | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code. |
| `vercel-cli-with-tokens` | Agents, Claude | Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login — e.g. "deploy to vercel", "set up vercel", "add environment variables to vercel". |
| `sandbox-sdk` | Agents, Claude, Codex | Build sandboxed applications for secure code execution. Load when building AI code execution, code interpreters, CI/CD systems, interactive dev environments, or executing untrusted code. Covers Sandbox SDK lifecycle, commands, files, code interpreter, and preview URLs. Biases towards retrieval from Cloudflare docs over pre-trained knowledge. |
| `setup-matt-pocock-skills` | Agents, Claude | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills. |
| `deployment-engineer` | Agents, Codex | Use this agent when designing, building, or optimizing CI/CD pipelines and deployment automation strategies. |
| `migrate-to-shoehorn` | Agents, Claude | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data. |
| `git-workflow-manager` | Agents, Codex | Use this agent when you need to design, establish, or optimize Git workflows, branching strategies, and merge management for a project or team. |
| `vercel-optimize` | Agents, Claude | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps. Collect Vercel metrics, usage, project config, and code scan results first; investigate only metric-backed candidates; produce ranked recommendations grounded in verified files and version-aware Vercel/framework docs. Trigger for Vercel bill reduction, slow or expensive routes, caching opportunities, Function Invocations, Build Minutes, Fast Data Transfer, Core Web Vitals, Bot Management, Fluid compute, or cost breakdown requests. |
| `vercel` | Agents, Claude | Vercel deployment, CLI, environment variables, Next.js integration, storage, CI/CD, and observability best practices. This skill should be used whenever deploying to Vercel, running vercel CLI commands, managing env vars, setting up Neon/Blob/Upstash storage, configuring CI/CD pipelines, or working with Vercel AI Gateway and AI SDK v6. |
| `setup-ts-deep-modules` | Agents, Claude | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point files. User-invoked. |
| `deploy-to-vercel` | Agents, Claude | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment". |
| `setup-pstack` | Codex | Configure which models pstack uses per role. Detects your available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-pstack, "configure pstack models", or changing pstack's model choices. |
| `vercel-composition-patterns` | Agents, Claude |  |
| `setup-pre-commit` | Agents, Claude | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing. |
