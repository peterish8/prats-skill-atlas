---
name: cli-delegate
description: Delegates a task, bug, or problem to an external CLI coding agent (Grok CLI or Codex CLI) instead of doing the work in this session. Writes a concise GSD-quick-style plan (problem, scope, do's/don'ts, numbered tasks, acceptance criteria) to a scratch file, hands it to the chosen CLI either headlessly in the background (`codex exec` / `grok -p` on Windows, output captured, nothing visible) or live — primarily via the agent-summoner MCP bridge, which opens the worker in a real terminal tab inside Devin itself; falling back to a standalone terminal window, then a shared tmux session in WSL if that's unavailable — then polls for completion and independently verifies the result before reporting back. Use when the user says "delegate this to grok/codex", "have grok/codex fix this", "run this with the grok cli", "use codex cli for this", "do this in the background with grok/codex", or invokes /cli-delegate.
---

# CLI Delegate — hand a task to Grok CLI or Codex CLI

Claude plans, an external CLI executes, Claude verifies. Claude does NOT edit repo files itself in this flow — the delegate CLI does.

There are **two separate installs of each CLI** in this environment, verified 2026-07-24 — don't mix them up:
- **Windows-native**: `grok` 0.2.82 (`~/.grok/bin/grok`, logged into grok.com) and `codex` 0.144.6 (npm, healthy per `codex doctor`). Used for **headless mode** (Step 2a), and by the agent-summoner bridge (Step 2b Tier 1) — proven reliable both ways.
- **WSL Ubuntu-native**: `grok` (`~/.grok/bin/grok` inside WSL, separate login, separate leader socket) and `codex` (`~/.npm-global/bin/codex` inside WSL, separate login). Used only by the tmux fallback (Step 2b Tier 3) via the [[shared-terminals]] skill.

## Step 0 — Resolve inputs

From the user's request, figure out:
- **CLI**: `grok` or `codex`. If genuinely ambiguous, ask.
- **Mode**: `headless` (background, silent, output captured) or `live` (visible terminal, Claude types the prompt in front of the user). If the user doesn't say, default `codex` → headless, `grok` → live — that's what was actually validated per-agent in the session that built this skill. Confirm the default back to the user in one line rather than silently assuming on a new task.
- **The task/problem** itself, in the user's own words.

## Step 1 — Write the plan (GSD-quick style)

Write a plan file to the scratchpad directory (NOT into the project repo — this keeps the delegation plan out of the codebase and avoids interacting with this repo's own GSD workflow enforcement, since the delegate CLI does the actual repo edits, not Claude):

`<scratchpad>/delegate-plans/PLAN-<slug>-<yyyymmdd-HHMM>.md`

```markdown
# Plan: <task, one line>

## Problem
<what's wrong / what's wanted, 2-4 sentences>

## Scope
In: <bullet list>
Out: <bullet list — be explicit, this bounds a CLI you won't be watching closely>

## Do
- <concrete, numbered constraints — e.g. "use pnpm, not npm", "match existing component patterns", "Server Components by default">

## Don't
- <explicit guardrails — e.g. "don't touch lib/supabase/serviceRole.ts", "don't add new dependencies", "don't commit/push">

## Tasks
1. <numbered, concrete, in order>
2. ...

## Acceptance criteria
- <how Claude will verify this after the fact — typecheck passes, specific behavior works, a test passes, etc.>
```

Keep it tight — this is the "quick" tier, not a full spec. Pull real project conventions (stack, constraints) from CLAUDE.md / the codebase so the plan doesn't contradict them.

Also decide the **status marker path**: `<scratchpad>/delegate-plans/STATUS-<slug>-<yyyymmdd-HHMM>.json`. The delegate CLI will write this when done.

## Step 2a — Headless mode

Run in the background (`run_in_background: true` on Bash, or note it'll exceed the sync timeout and let it move to background automatically — either is fine, just don't block the conversation on it).

**Codex:**
```bash
codex exec "Read the plan at <PLAN_PATH> and execute it completely and exactly, following the Do/Don't list. Don't ask questions — make reasonable calls yourself and record them. When fully done, or if you get stuck, write JSON to <STATUS_PATH> as {\"status\":\"done\"|\"blocked\",\"summary\":\"...\",\"filesChanged\":[...],\"notes\":\"...\"} and stop." \
  -s workspace-write -c approval_policy="never" -C "<repo path>"
```
`-s workspace-write` scopes filesystem writes to the workspace (not full-disk access); `approval_policy="never"` is required or the run hangs forever waiting for an approval nobody will grant headlessly. Do NOT use `--dangerously-bypass-approvals-and-sandbox` unless the user explicitly asks for full, unscoped access.

**Grok:**
```bash
grok -p "Read the plan at <PLAN_PATH> and execute it completely and exactly, following the Do/Don't list. Don't ask questions — make reasonable calls yourself and record them. When fully done, or if you get stuck, write JSON to <STATUS_PATH> as {\"status\":\"done\"|\"blocked\",\"summary\":\"...\",\"filesChanged\":[...],\"notes\":\"...\"} and stop." \
  --permission-mode acceptEdits --cwd "<repo path>"
```

Codex cold starts can be slow in this environment (~1-4 min observed, due to MCP/skill/hook loading) — don't assume a fast timeout means failure; check the background task's output file before concluding it errored.

## Step 2b — Live mode (opposite of headless) — three tiers, in order

Try Tier 1 first. Only drop to Tier 2 if Tier 1 is genuinely unavailable; only drop to Tier 3 if Tier 2 is also unavailable. Don't skip straight to a fallback out of convenience — the whole point of the tier order is that each one down is a worse experience for the user.

### Tier 1 (primary) — agent-summoner MCP bridge, live tab inside Devin

The proper, API-level solution — verified end-to-end 2026-07-24, including manual approval + stuck-session recovery (see below). `<USER_HOME>\Desktop\apps\agent-summoner` is the user's own project: an MCP server (`summon_agent`, `send_to_agent`, `send_raw_input`, `get_agent_output`, `list_agents`, `check_reports`, `wait_for_report`, plus worker-facing `report_done`/`report_progress`/`ask_conductor`) paired with a VS Code extension that, when its bridge is connected, opens each summoned agent in a real terminal tab **inside Devin** — the user just watches their own editor, no separate window, no automation risk.

**Before using Tier 1, confirm the bridge is actually connected** — the MCP tools exist either way but silently fall back to headless without it, which isn't live mode:
```bash
cat ~/.agent-summoner/bridge.json   # or the Windows path: <USER_HOME>\.agent-summoner\bridge.json
```
If it exists (has `port`/`token`/a recent `updatedAt`), the bridge is live — proceed. If it doesn't exist, drop to Tier 2. If the tools don't even show up in ToolSearch at all, see "If the tools vanish after an update" below before assuming Tier 1 is unavailable — that's usually a fixable config issue, not a real outage.

**Basic usage:**
```
summon_agent(agent: "grok" | "codex", prompt: "<task prompt, referencing PLAN_PATH>", cwd: "<repo path>")
```
This blocks until the worker calls `report_done` and returns its summary, tagged `[live · editor tab]` (or `[headless]` if the bridge silently wasn't connected — always check this tag, don't assume). For a follow-up in the same session, use `send_to_agent(id, prompt)` with the id from the summon result (e.g. `"grok-1"`). If the worker calls `ask_conductor` instead of finishing, that's a real question surfacing to you — relay it to the user or answer it yourself if it's something the plan already fully specifies. For parallel/background work, pass `wait: false` and collect results with `wait_for_report`/`check_reports`.

**Approval mode.** Default (`approvalMode: "auto"`, or omitted) never stops for approval — matches plain headless behavior. Pass `approvalMode: "manual"` when the task is sensitive enough that a real approval gate should stay live in the tab (the worker's own CLI will show its normal numbered/y-n prompt instead of auto-approving). Manual mode has **no automatic detection** of a native approval prompt sitting there (it doesn't go through the MCP report channel) — use `wait: false` and either have the user watch the tab, or poll `get_agent_output`; if `status` stays `waiting-for-report` with no new report after the "started" one, it's very likely sitting on a prompt. Answer it with:
```
send_raw_input(id: "grok-1", text: "3")   # or "y", or whatever the visible prompt's options actually show
```
`send_raw_input` types directly into the live terminal and works even mid-turn (unlike `send_to_agent`, which refuses while a turn is pending). Verified live: grok's real "Allow Edit? 1) always-approve 2) this session 3) yes 4) no" dialog answered correctly with `text: "3"`.

**Stuck-session detection.** Every worker's first required action is calling `report_progress` with note `"started"`, before anything else — this gives an unambiguous liveness signal within seconds, independent of how long the real task takes. If a worker never reports anything at all within ~2 minutes (grok CLI occasionally hangs at its own startup/leader-negotiation), the bridge automatically closes that stuck tab and `summon_agent`/`send_to_agent`'s result says so explicitly (mentions "never made contact" / "likely stuck at startup"). On that result: don't retry the same call blindly — just call `summon_agent` again fresh (a new session id opens a new tab). This is automatic; you don't need to poll for it unless using `wait: false`, in which case check `list_agents`/`check_reports` for a `stuck-no-contact` status.

Tell the user once per task that a new tab may open in Devin for the worker (labeled by agent id, e.g. `grok-1`) — they can watch it directly, no attach command needed.

**If the tools vanish after an extension update:** this happened once and had a real root cause, now fixed — worth knowing in case it ever recurs on a *different* machine that hasn't gotten the fix. `~/.claude.json` is a read-modify-write file Claude Code *also* owns (dozens of its own settings live in the same file). The extension used to write a version-specific server path into it on every update, which raced against Claude Code's own periodic save-its-whole-config-back-to-disk behavior — Claude Code's stale in-memory copy would win and silently revert the entry to the previous version's (now-deleted) path, making the MCP server fail to start with zero visible error. Fixed in `claudeConfig.ts`: `~/.claude.json` now points at a **stable, version-independent launcher** (`~/.agent-summoner/server-launcher.cjs`) that reads the actual current server path from `~/.agent-summoner/current-server.json` (a file only this extension ever touches, zero race exposure) — so `~/.claude.json` itself is written once, ever, and never touched again on future updates. If tools are missing on a machine that predates this fix, or something has clearly gone wrong: check `cat ~/.claude.json | grep -A3 agent-summoner` — if `args` contains a versioned path like `...-vscode-0.1.9\out\server.cjs` instead of `server-launcher.cjs`, that's the bug; the fix is already in the extension source, just reinstall the current build (`node scripts/bundle.mjs` then `vsce package` then `devin-desktop --install-extension`).

**Install/setup note** (only relevant if the bridge ever needs reinstalling from scratch on a machine that's never had it — e.g. a fresh machine): the extension's built `.vsix` may declare an `engines.vscode` floor newer than Devin's actual VS Code engine version, which makes `--install-extension` refuse it outright. Current source already sets a conservative floor (`^1.85.0` in `vscode-extension/package.json`) — check that's still true before assuming this will bite you again. If it does: **use PowerShell's `Expand-Archive`/`Compress-Archive` to repackage, never bash `unzip`/`zip`** — a prior bash-zip attempt silently dropped native `node-pty` binaries required for the terminal to work, producing a corrupt-but-installable extension. When rewriting manifest text with PowerShell, use `[System.IO.File]::WriteAllText($path, $content, (New-Object System.Text.UTF8Encoding $false))` rather than `Set-Content -Encoding utf8` — the latter adds a UTF-8 BOM in Windows PowerShell 5.1 that breaks Devin's JSON manifest parser. Verify integrity with `unzip -t` before installing (zero CRC errors, all files present — this check is not optional). Better: build properly instead of patching a binary — `node scripts/bundle.mjs` (esbuild, both `esbuild` and `@vscode/vsce` are already in the project's `node_modules`) then `vsce package --allow-missing-repository --skip-license` from `vscode-extension/`. Note: modifying/repackaging an extension binary by hand reliably trips Claude Code's own safety classifier ("Blocked by classifier") — if that happens, don't work around it; hand the exact commands to the user to run themselves in their own terminal, which is unrestricted. Building properly via `vsce package` does not trip it.

### Tier 2 (fallback) — standalone terminal window, Claude-controlled

Only if Tier 1's bridge isn't connected. A fresh terminal window Claude opens and fully controls itself (no ambiguity about focus, since nothing else has ever had it):
```powershell
Add-Type -AssemblyName System.Windows.Forms
Start-Process powershell -ArgumentList '-NoExit','-Command',"cd '<repo path>'; <grok|codex>"
Start-Sleep -Seconds 5
$wshell = New-Object -ComObject wscript.shell
$activated = $wshell.AppActivate('<grok|codex>')   # grok/codex set their own console title once initialized
Start-Sleep -Milliseconds 700
[System.Windows.Forms.SendKeys]::SendWait($escapedPrompt)
Start-Sleep -Milliseconds 400
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
```
Uses the **Windows-native** grok/codex installs. `SendKeys` special chars (`+ ^ % ~ ( ) { } [ ]`) need brace-escaping; build the argument as a single-quoted PowerShell string (double-quoted mishandles backtick); activate by window **title**, never `$proc.Id` (Windows 11 hosts the console inside Windows Terminal, so the PID isn't the window owner). If any `AppActivate`/focus call fails or returns false, ABORT — do not send keys anyway.

**Never** point this at the user's own editor/IDE window (Devin or otherwise) — only a window Claude opened itself. That was tried repeatedly against Devin specifically and caused real misfires (a keystroke once landed in another Claude Code chat session inside it). Tier 1 is what properly solves "visible inside the editor"; Tier 2 does not attempt that, on purpose.

### Tier 3 (fallback of fallback) — shared tmux session in WSL

Only if Tier 2 is also unavailable/undesired (e.g. the user wants to attach and type themselves from any terminal, not just watch a Claude-opened window). **Invoke the `shared-terminals` skill** (Skill tool, `skill: "shared-terminals"`) — it owns the full tmux/`claude-term` mechanism, workflow rules, and gotchas; don't reimplement it here. Quick summary of the call shape:
```bash
wsl -d Ubuntu -e bash -lc "export PATH=\"\$HOME/.claude/bin:\$PATH\"; claude-term <subcommand> ..."
```
`claude-term new/send/read` against the `claude` tmux session, using the **WSL-native** grok/codex installs (`~/.grok/bin/grok`, `~/.npm-global/bin/codex` inside WSL — separate logins/leader-sockets from the Windows installs; running the *Windows* binaries through WSL's interop layer was tried and rejected, see [[shared-terminals]] for why). Tell the user the attach command (`wsl -d Ubuntu -e tmux attach -t claude`) every time, not just once.

In every live tier, don't force auto-approve flags by default — let real approval prompts surface; the user (or Claude, for prompts the plan already fully anticipated) can answer them.

## Step 3 — Verify (never skip this — this is the whole point of "verify by u")

1. Poll for the status marker file (`<scratchpad>/delegate-plans/STATUS-...json`) every ~20-30s up to a generous timeout (headless codex can take several minutes cold). While waiting, `git status --porcelain` in the repo gives a live signal that something's actually happening even before the marker lands.
2. Once the marker appears, read it. Cross-check `filesChanged` against `git diff --stat` — don't just trust the CLI's self-report.
3. Run whatever this project's own verification commands are (e.g. `pnpm typecheck`, `pnpm lint`, `pnpm test` — check `package.json`/CLAUDE.md for the actual ones, don't assume) against the delegate's changes.
4. Report to the user: PASS/FAIL/BLOCKED, what changed (files + one-line summary), what you verified and how, and anything the delegate flagged as a blocker or judgment call. If verification fails, say so plainly — don't paper over a broken result because the CLI claimed "done."

## Hard rules

- Claude never edits the repo directly in this flow — that defeats the purpose of delegating. Claude writes the plan (outside the repo) and verifies the result; the external CLI does the work.
- Headless mode always needs an explicit non-interactive approval/sandbox config (see Step 2a) — never let it hang waiting for approval that will never come.
- Live mode never auto-approves — a human is present or watching, let them approve.
- Try Tier 1 (agent-summoner bridge) before any fallback — check `~/.agent-summoner/bridge.json` first. Don't drop to Tier 2/3 just because it's more familiar; only because Tier 1 genuinely isn't connected.
- Tier 2 (standalone terminal) never targets the user's own editor/IDE window — only a window Claude opened itself. This was tried against Devin directly, repeatedly, and caused real misfires (a keystroke landed in another Claude Code chat session inside it). If any focus/activate call in Tier 2 fails or returns false, ABORT — do not send keys anyway "just in case."
- In Tier 3, always tell the user the tmux attach command at the start of every live-mode task — don't skip it because it was said before.
- Always verify independently in Step 3, regardless of which tier ran the task. A CLI (or a worker's `report_done`) reporting "done" is a claim, not a fact.

