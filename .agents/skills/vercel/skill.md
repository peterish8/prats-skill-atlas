---
name: vercel
description: Vercel deployment, CLI, environment variables, Next.js integration, storage, CI/CD, and observability best practices. This skill should be used whenever deploying to Vercel, running vercel CLI commands, managing env vars, setting up Neon/Blob/Upstash storage, configuring CI/CD pipelines, or working with Vercel AI Gateway and AI SDK v6.
---

# Vercel Best Practices

## Critical Rules (Never Break)

- **Never echo or log secret values** — only names/metadata in output
- **Never run `vercel --prod` without explicit user confirmation**
- **Never run db migrations before `vercel link` is complete**
- **Never run `vercel` commands outside a directory with `.vercel/project.json`**
- **MCP-first, CLI-fallback** — prefer Vercel MCP tools when available, fall back to CLI

---

## Project Linking (Do This First)

```bash
vercel link                  # single project → creates .vercel/project.json
vercel link --repo           # monorepo → creates .vercel/repo.json
```

**Always verify linking before any other command:**
```bash
cat .vercel/project.json     # confirms project + org IDs
```

Monorepo mistake: `vercel link` (without `--repo`) links one package only. Use `--repo` for monorepos.

---

## Bootstrap Workflow (New Project Setup)

Strict execution order — do NOT skip steps:

1. Detect package manager (`package.json` → `packageManager` field)
2. `vercel link` (or `vercel link --repo` for monorepos)
3. `vercel env pull .env.local` — sync all env vars locally
4. Provision databases (Neon preferred for Postgres, Upstash for KV/Redis)
5. Verify required keys exist in `.env.local`
6. Run migrations only after env verification
7. Start dev server last

```bash
# Step 3
vercel env pull .env.local

# Step 5 — verify before proceeding
grep -E "DATABASE_URL|AUTH_SECRET|NEXT_PUBLIC_" .env.local
```

---

## Deployments

### Preview (safe, no confirmation needed)
```bash
vercel deploy
```

### Production (requires explicit user confirmation)
```bash
vercel deploy --prod
# OR promote a known-good preview:
vercel promote <deployment-url>
```

### Rollback
```bash
vercel rollback              # reverts to previous production
vercel rollback <url>        # reverts to specific deployment
```

### Pre-built (custom CI — fastest)
```bash
vercel build                 # builds locally
vercel deploy --prebuilt     # uploads build artifacts
```

### Inspection after deploy
```bash
vercel inspect <url>         # state, build duration, framework, functions
vercel logs <url>            # build + runtime logs
vercel ls                    # last 5 deployments
```

**Deployment states**: READY ✓ | ERROR ✗ | QUEUED ⏳ | BUILDING 🔨  
On ERROR: always run `vercel logs <url>` before reporting to user.

---

## Environment Variables

### Listing (safe — names only, never values)
```bash
vercel env ls                          # all envs
vercel env ls production               # production only
vercel env ls preview                  # preview only
```

### Adding
```bash
vercel env add MY_VAR                  # interactive — Vercel prompts for value
vercel env add MY_VAR production       # production only
```

**CRITICAL**: Never pass the value as a CLI argument — it ends up in shell history.

### Pulling
```bash
vercel env pull .env.local             # overwrites local file
```

### Removing (destructive — confirm before running)
```bash
vercel env rm MY_VAR production        # production only
```

### After any mutation
```bash
vercel env ls                          # verify the change
```

### OIDC Federation (service-to-service, no static tokens)
```bash
# In vercel.json
{
  "oidc": { "enabled": true }
}
# Runtime: process.env.VERCEL_OIDC_TOKEN is auto-injected
```
Prefer OIDC over static `VERCEL_TOKEN` for service-to-service auth.

---

## CI/CD (GitHub Actions / GitLab / Bitbucket)

### Required env vars in CI
```
VERCEL_TOKEN      # from vercel.com/account/tokens
VERCEL_ORG_ID     # from .vercel/project.json
VERCEL_PROJECT_ID # from .vercel/project.json
```

### Recommended GitHub Actions pattern
```yaml
- name: Pull Vercel Environment
  run: vercel env pull .env.local --token=${{ secrets.VERCEL_TOKEN }}

- name: Build
  run: vercel build --token=${{ secrets.VERCEL_TOKEN }}

- name: Deploy
  run: vercel deploy --prebuilt --token=${{ secrets.VERCEL_TOKEN }}
```

Always use `--prebuilt` in CI — build once, deploy artifact (faster + consistent).

**Do NOT** use `vercel --prod` in CI without a separate promotion step:
```bash
vercel promote <deployment-url> --token=$VERCEL_TOKEN
```

---

## Storage Selection

| Need | Use | Package |
|------|-----|---------|
| Postgres | Neon | `@neondatabase/serverless` |
| Key-Value / Redis | Upstash | `@upstash/redis` |
| Files / Blobs | Vercel Blob | `@vercel/blob` |
| Edge config / flags | Edge Config | `@vercel/edge-config` |

### Deprecated (migrate away from these)
- `@vercel/postgres` → migrate to `@neondatabase/serverless`
- `@vercel/kv` → migrate to `@upstash/redis`

### Neon setup
```bash
vercel storage create          # follow prompts → picks Neon
vercel env pull .env.local     # pulls DATABASE_URL automatically
```

### Blob upload
```ts
import { put } from "@vercel/blob";
const { url } = await put("file.png", file, { access: "public" });
```

---

## Next.js + Vercel Integration

### Rendering decisions
- **Static (SSG)**: `generateStaticParams` + no dynamic data
- **Dynamic SSR**: `export const dynamic = "force-dynamic"` or `cookies()`/`headers()`
- **ISR**: `export const revalidate = 60` (seconds)
- **Streaming**: `loading.tsx` + `Suspense` boundaries

### Data cache (Next.js 15+)
```ts
// Cache with tag
fetch(url, { next: { tags: ["products"] } });

// Revalidate by tag (Server Action or Route Handler)
import { revalidateTag } from "next/cache";
revalidateTag("products");
```

### Common Next.js + Vercel mistakes
- Using `getServerSideProps` / `getStaticProps` in App Router — these don't exist
- `next/router` in App Router — use `next/navigation`
- Missing `"use client"` on components using `useState`/`useEffect`
- `useRef()` without argument in React 19 — must be `useRef<T>(null)`

### Middleware / Proxy (Next.js 16+)
```ts
// proxy.ts (replaces middleware.ts pattern)
export default function proxy(req) { ... }
```

---

## Vercel Functions

### Edge vs Serverless
| | Edge | Serverless |
|---|---|---|
| Cold start | ~0ms | ~100ms |
| Max duration | 25s | 300s (pro) |
| Node APIs | ❌ | ✅ |
| Use for | Auth, redirects, A/B | DB queries, heavy logic |

```ts
// Edge function
export const runtime = "edge";

// Serverless (default — no annotation needed)
```

### Max duration (vercel.json)
```json
{
  "functions": {
    "app/api/heavy/**": { "maxDuration": 300 }
  }
}
```

---

## AI SDK v6 (Critical — Everything Pre-v6 Is Wrong)

**Always check `node_modules/ai/docs/` for current API — never rely on memory.**

### Breaking changes from v5
| v5 | v6 |
|----|-----|
| `parameters` | `inputSchema` |
| `CoreMessage` | `ModelMessage` |
| `maxSteps: N` | `stopWhen: stepCountIs(N)` |
| `useChat({ api })` | transport-based config |

### Basic patterns
```ts
import { generateText, streamText } from "ai";
import { anthropic } from "@ai-sdk/anthropic";

// Text generation
const { text } = await generateText({
  model: anthropic("Codex-sonnet-4-6"),
  prompt: "...",
});

// Streaming
const result = streamText({
  model: anthropic("Codex-sonnet-4-6"),
  messages,
});
return result.toDataStreamResponse();
```

### AI Gateway (use for production — multi-provider routing)
```ts
import { createVercelGateway } from "@ai-sdk/vercel-gateway";
const gateway = createVercelGateway();

const { text } = await generateText({
  model: gateway("anthropic/Codex-sonnet-4-6"),
  prompt: "...",
});
```

Benefits: provider fallbacks, response caching, rate limiting per user, full observability.

---

## Observability

### Analytics + Speed Insights (add to every project)
```bash
npm install @vercel/analytics @vercel/speed-insights
```

```tsx
// app/layout.tsx
import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <Analytics />
        <SpeedInsights />
      </body>
    </html>
  );
}
```

### Log Drains (production)
- Format: JSON or NDJSON preferred
- Always set `DRAIN_SECRET` env var
- Verify HMAC-SHA1 signature on drain endpoint (timing-safe comparison)

---

## Project Health Check (`/status` workflow)

Run these to audit a project:
```bash
vercel ls                           # recent deployments + states
vercel inspect $(vercel ls --json | jq -r '.[0].url')  # latest details
vercel env ls                       # env var names (no values)
cat vercel.json 2>/dev/null         # config
```

Check for:
- [ ] Analytics + SpeedInsights installed
- [ ] Log drain configured with secret
- [ ] No deprecated packages (`@vercel/postgres`, `@vercel/kv`)
- [ ] OIDC enabled if service-to-service calls exist
- [ ] Custom domains with valid SSL

---

## vercel.json Reference

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "installCommand": "npm ci",
  "framework": "nextjs",
  "regions": ["iad1"],
  "oidc": { "enabled": true },
  "functions": {
    "app/api/heavy/**": { "maxDuration": 300 }
  },
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" }
      ]
    }
  ],
  "rewrites": [
    { "source": "/old-path", "destination": "/new-path" }
  ]
}
```

---

## Security Checklist

- [ ] No secrets in `vercel.json` or committed `.env` files
- [ ] Production env vars scoped to production only
- [ ] `VERCEL_TOKEN` rotated regularly, scoped to project not team
- [ ] Drain endpoint verifies HMAC signature
- [ ] Edge middleware validates auth before forwarding to origin
- [ ] OIDC used for service-to-service (no static tokens)
