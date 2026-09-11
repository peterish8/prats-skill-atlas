# Windows Vercel auth discovery

Use this when working on a Windows machine where Vercel may already be logged in locally.

## Proven flow
1. Check identity first:
   ```bash
   vercel whoami
   vercel teams list
   ```
2. If `whoami` already succeeds, do **not** ask the user to log in again.
3. Use the returned team slug with `--scope` on all project commands.
4. If you need a token for Hermes non-interactive commands, inspect the local CLI auth record and mirror the `token` value into Hermes' `.env` as `VERCEL_TOKEN`.
5. Re-check with `vercel whoami` before deploying.

## Practical notes
- Team display names and team slugs are not always the same.
- `vercel project ls --scope <team-slug>` is a good sanity check before linking or deploying.
- Default to preview deploys unless the user explicitly asks for production.