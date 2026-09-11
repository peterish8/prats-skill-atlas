# Upstream provenance and integration

## Source

- Project: `zhaoxuya520/reverse-skill`
- Repository: https://github.com/zhaoxuya520/reverse-skill
- Audited snapshot: `7e2097fd90d25c2f976f6eba26d6c00aa88051df`
- Audit date: 2026-09-12
- Default shared checkout: `~/.agents/vendor/reverse-skill`

Verify a checkout with `git -C <path> rev-parse HEAD` and compare it with the expected snapshot before relying on the audit. A newer or dirty checkout is not automatically unsafe, but it is outside this snapshot and its executable surface must be reviewed before use.

## Packaging choice

The Atlas distributes this guarded adapter, not a second copy of the full upstream repository. The audited upstream snapshot contained 596 files, 89 `SKILL.md` files, and 69 files with common executable-script extensions. Its executable surface includes tool downloads and installs, recursive cleanup, local-service startup, dynamic instrumentation, device installation, scanners, exploit workflows, and security-evasion material.

Keeping one pinned shared checkout avoids triplicating that executable and payload surface in Claude, Codex, and Agents. The adapter can still route into every upstream specialist while the command-risk policy controls execution.

## Safe use

- Read upstream routing configuration and specialist Markdown as methodology.
- Do not execute bootstrap, setup, router, case, service, exploit, or sample scripts automatically.
- Do not disable antivirus if a payload corpus triggers detection.
- Treat upstream MCP examples as documentation, not authorization to register or start servers.
- Updating the checkout, changing its pin, or enabling executable integrations is R2 and requires explicit permission.

## Licensing

The upstream repository states that its main project is MIT licensed and its `CTF-Sandbox-Orchestrator` subtree is GPLv3. External tools retain their own licenses. This adapter is a modified integration for Prats Skill Atlas and is not represented as an unchanged upstream release. Preserve attribution when redistributing it; see [upstream-license.txt](upstream-license.txt).
