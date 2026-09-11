---
name: shared-terminals
description: Gives Claude a real, watchable, interruptible terminal — a persistent tmux session (inside WSL Ubuntu) that the user can attach to at any time with `wsl -d Ubuntu -e tmux attach -t claude`, watch commands execute live, and take over or answer prompts themselves. Claude drives named windows inside it via the `claude-term` wrapper (list/new/run/send/read/kill) instead of a hidden background shell. For grok/codex specifically this is Tier 3 (last-resort) behind the agent-summoner MCP bridge and a standalone terminal window — see [[cli-delegate]]. Use this directly for anything else that needs to be genuinely visible/interactive: a long-running server, an auth flow needing browser/device-code interaction, or anything the user asked to "watch happen" rather than get a summary of afterward.
---

# Shared Terminals — a tmux session Claude and the user both hold

One persistent tmux session (`claude`, inside WSL Ubuntu — installed 2026-07-24) that Claude drives via `~/.claude/bin/claude-term` and the user can attach to and interact with directly at any point. Originally built as the primary live-mode mechanism for [[cli-delegate]]; superseded there by the agent-summoner MCP bridge (a proper VS Code extension that opens a real Pseudoterminal tab inside the user's editor, no attach command needed) once that got installed and verified 2026-07-24 — this is now cli-delegate's Tier 3 fallback, used only when the bridge isn't connected and a standalone terminal window isn't preferred. Still the right direct choice for anything outside grok/codex delegation that needs a genuinely live, attachable view — see "Why this exists" below for what was tried and rejected first.

## How the user watches / takes over

From ANY terminal on their machine (PowerShell, cmd, a terminal inside their editor — anywhere), they run:
```
wsl -d Ubuntu -e tmux attach -t claude
```
`Ctrl-b w` switches between windows. `Ctrl-b d` detaches without killing anything. They can type directly into whatever window they're viewing, including answering a prompt Claude is waiting on.

**This is the one command that's safe for a human to run themselves whenever they want to watch — nothing Claude does needs to orchestrate it.** Tell the user this command whenever you start real work in the session, don't assume they remember it.

## The wrapper: `claude-term`

Lives inside WSL Ubuntu at `~/.claude/bin/claude-term` (installed on PATH via `~/.bashrc`). Invoke it from Claude's own (Windows-side) Bash/PowerShell tool by wrapping every call:
```bash
wsl -d Ubuntu -e bash -lc "export PATH=\"\$HOME/.claude/bin:\$PATH\"; claude-term <subcommand> ..."
```

Commands:
- `claude-term list` — shells + which one the user is currently viewing
- `claude-term new <name> [dir]` — create a named shell (blocks until it's actually ready for input)
- `claude-term run <name> [-t sec] [-f] -- CMD` — run a **single-line** shell command, wait for completion via marker protocol, print output, exit with the command's real exit code. Refuses if the target window isn't at a shell prompt (busy running something interactive) — use `send`/`read` for those instead.
- `claude-term send <name> KEYS…` — raw `tmux send-keys` passthrough — for interactive programs (TUIs, prompts, REPLs). Multiple args/lines are typed in sequence like a paste.
- `claude-term read <name> [-n N | -a]` — capture the shell's current screen (last N lines, or `-a` for full scrollback)
- `claude-term kill <name>` — close a shell

## Workflow rules

- **One window per concern.** `grok`, `codex`, `build`, `server` — reuse the same named window for the same ongoing concern rather than spawning a new one per command.
- **`run` for one-shot commands, `send`+`read` for anything interactive.** A CLI's own TUI (grok, codex) is never driven with `run` — launch it with `send`, then `send` further prompts, and `read` to check state/wait for prompts like approval dialogs.
- **Read before you send.** Check `claude-term read <name>` before sending into a window that might be mid-something (an approval prompt, a REPL, the user's own typing) — don't blindly assume its state.
- **Always tell the user the attach command** at the start of any real (non-test) session in a window, so they know they can watch or step in.
- **Never print credential values** that land on screen into the conversation — env var *names* are fine, values aren't. `claude-term read` output can end up in the transcript.
- **The user's own attention is not yours to grab.** If they're actively viewing/typing in a window (visible via `list`'s "[user is viewing this one]" marker), don't send competing keystrokes into it without checking first.

## Why this exists — what was tried and rejected first

This environment is Windows 11, the user's editor is a VSCode-fork app ("Devin") with the Claude Code extension running inside it. Before landing on this design, three approaches were tried against Devin's own window and failed or were too risky to keep using:

1. **OS-level `AppActivate`+`SendKeys` targeting Devin's window** — works for a standalone terminal Claude opens itself (still valid, see fallback below), but Devin has multiple internal panels (editor, its own Claude Code chat, several real terminal tabs) and window-level activation can't tell which one has keyboard focus. Confirmed failure mode: a launch command was typed straight into Devin's own AI chat panel instead of a terminal, sending an unintended message to another Claude session.
2. **Windows UI Automation (`SetFocus()` / `SelectionItemPattern.Select()`) targeting a specific terminal tab element** — the `SetFocus()` call itself threw `"Target element cannot receive focus"` on the real terminal tab element; keys were then (wrongly) sent anyway, landing wherever the user's actual cursor happened to be.
3. **Running the Windows `grok.exe`/`codex` binaries through WSL's Windows-interop layer inside a Linux tmux session** — the interactive TUI rendered correctly at first, but consistently crashed back to a shell prompt within ~10-15s with a `"leader mode"` warning — a real conflict between grok's persistent leader-process architecture and being launched through the interop translation layer. Reproduced twice.

**What actually works, tested 2026-07-24:** installing `grok` and `codex` **natively inside WSL Ubuntu** (separate binaries, separate config/leader-socket from the Windows installs — `curl -fsSL https://x.ai/cli/install.sh | bash` for grok, `npm install -g @openai/codex` for codex, both logged in separately) and driving them through a real Linux tmux session. No focus-guessing anywhere — `send-keys`/`capture-pane` target a specific tmux pane by name, unambiguously, every time. Verified end-to-end: launched grok live, typed a real prompt, watched it request file-write approval, approved it, confirmed the file landed on disk.

**Fallback for one-off cases where WSL isn't wanted:** a standalone Windows Terminal window Claude opens itself (`Start-Process` + `AppActivate` by window title, since Claude fully controls that window from creation, no ambiguity) still works and is documented in [[cli-delegate]] — but the shared tmux session is the default now that it exists, since it's watchable/interruptible in a way a fire-and-forget standalone window isn't.

## Hard rules

- Never attempt to focus/select a panel inside the user's own editor (Devin or otherwise) via window automation — this was tested, failed, and risked real collateral damage (see above). If a task needs to run visibly inside their actual editor, only the user's own hands on their own terminal satisfy that.
- If a `claude-term` call errors, STOP — don't retry blindly, don't fall back to raw `tmux`/`SendKeys` outside the wrapper's guardrails "just to get it done."
- `run` is single-line only, no override for embedded newlines — that's what breaks the marker protocol. Multi-step sequences go through `send` (paste semantics) or a temp script.
