#!/usr/bin/env python3
"""Run the packaged Claude/Codex copy-only sync against this Atlas checkout."""
import runpy
import sys
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
entry = repo / ".agents/skills/agent-workflows/coordination/sync-agent-skills/scripts/run_sync.py"
if not entry.is_file():
    raise SystemExit("The shared sync-agent-skills package is required in this checkout")
if "--local-only" not in sys.argv and not any(arg == "--atlas-root" or arg.startswith("--atlas-root=") for arg in sys.argv[1:]):
    sys.argv.extend(["--atlas-root", str(repo)])
runpy.run_path(str(entry), run_name="__main__")
