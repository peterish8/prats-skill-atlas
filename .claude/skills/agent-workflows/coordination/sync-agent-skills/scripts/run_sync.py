#!/usr/bin/env python3
"""One-command, copy-only Claude/Codex/Atlas synchronization. No network or Git writes."""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

spec = importlib.util.spec_from_file_location("atlas_sync_runner_engine", Path(__file__).with_name("sync_atlas.py"))
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)


def valid_atlas(root: Path) -> bool:
    required = ["AGENTS.md", "scripts/category-rules.ps1", "scripts/organize-runtime-trees.ps1", "scripts/build-catalog.ps1", "scripts/validate.ps1"]
    return all((root / name).is_file() for name in required) and all((root / runtime / "skills").is_dir() for runtime in engine.RUNTIME_NAMES.values())


def find_atlas(explicit: Path | None = None, *, home: Path | None = None, cwd: Path | None = None, environ=None) -> Path:
    environ = os.environ if environ is None else environ
    home = Path.home() if home is None else home
    cwd = Path.cwd() if cwd is None else cwd
    requested = explicit or environ.get("PRATS_SKILL_ATLAS")
    if requested:
        root = Path(requested).expanduser().resolve()
        if not valid_atlas(root):
            raise RuntimeError(f"Configured Atlas checkout is invalid: {root}")
        return root
    for root in [cwd, *cwd.parents, home / "Documents/Codex/prats-skill-atlas", home / "prats-skill-atlas"]:
        if valid_atlas(root):
            return root.resolve()
    raise RuntimeError("Atlas checkout not found. Pass --atlas-root PATH or set PRATS_SKILL_ATLAS. Use --local-only only when Atlas is intentionally excluded.")


def has_additions(report) -> bool:
    return any(report[group][runtime] for group in ("local_additions", "atlas_additions") for runtime in report[group])


def refresh_catalog(repo: Path):
    for script in ("organize-runtime-trees.ps1", "build-catalog.ps1", "validate.ps1"):
        result = subprocess.run(["pwsh", "-NoProfile", "-File", str(repo / "scripts" / script)], cwd=repo, capture_output=True, text=True, timeout=300)
        if result.returncode:
            raise RuntimeError(f"Catalog step failed: {script}. Skill copies may already exist; repair the check and rerun.\n{result.stdout}\n{result.stderr}")
    refresh_readme_counts(repo)


def refresh_readme_counts(repo: Path):
    readme = repo / "README.md"
    if not readme.is_file():
        return
    catalog = json.loads((repo / "catalog/skills.json").read_text(encoding="utf-8-sig"))
    original = readme.read_bytes().decode("utf-8")
    text = re.sub(r"\d+_unique_skills", f"{catalog['skillCount']}_unique_skills", original)
    text = re.sub(r'\d+ unique skills(?=\")', f"{catalog['skillCount']} unique skills", text)
    for runtime in ("Claude", "Codex", "Agents", "Grok", "Antigravity"):
        root = re.escape(f".{runtime.lower()}/skills")
        count = sum(runtime in item["presentIn"] for item in catalog["skills"])
        pattern = rf"(?m)^(\| \[`{root}`\]\({root}\) \| )\d+( \|)"
        text = re.sub(pattern, lambda match: f"{match[1]}{count}{match[2]}", text)
    text = re.sub(r"(?m)^(\| \*\*Unique skill names\*\* \| \*\*)\d+(\*\* \|)", lambda match: f"{match[1]}{catalog['skillCount']}{match[2]}", text)
    if text != original:
        readme.write_bytes(text.encode("utf-8"))


def catalog_needs_refresh(repo: Path) -> bool:
    index = repo / "catalog/skills.json"
    try:
        catalog = json.loads(index.read_text(encoding="utf-8-sig"))
        names = {item["name"].casefold() for item in catalog["skills"]}
        indexed_at = index.stat().st_mtime_ns
        actual = set()
        for runtime in (".claude", ".codex", ".agents", ".grok", ".antigravity"):
            for entry in (repo / runtime / "skills").glob("*/*/*/SKILL.md"):
                actual.add(entry.parent.name.casefold())
                if entry.stat().st_mtime_ns > indexed_at:
                    return True
        return names != actual or catalog["skillCount"] != len(actual)
    except (OSError, ValueError, KeyError, TypeError):
        return True


def run_atlas(args):
    repo = find_atlas(args.atlas_root)
    args.atlas_root = repo
    if args.report.resolve().is_relative_to(repo):
        raise RuntimeError("Write the sync report outside the public Atlas checkout.")
    # All publication checks run before this runner permits local or Atlas copies.
    preview_args = argparse.Namespace(**vars(args))
    preview_args.dry_run = True
    preview = engine.synchronize(preview_args)
    changed = has_additions(preview)
    public_changed = any(preview["atlas_additions"].values())
    if args.dry_run:
        report = preview
    elif changed:
        report = engine.synchronize(args)
    else:
        report = preview
        report["dry_run"] = False
    refresh_needed = not args.dry_run and (public_changed or args.refresh_catalog or catalog_needs_refresh(repo))
    if refresh_needed:
        refresh_catalog(repo)
    report.update({"mode": "atlas", "atlas_root": str(repo), "catalog_refreshed": refresh_needed, "status": "preview" if args.dry_run else "synced" if changed else "already_synced"})
    return report


def run_local(args):
    command = [sys.executable, str(Path(__file__).with_name("sync_skills.py")), "--claude-root", str(args.claude_root), "--codex-root", str(args.codex_root), "--agents-root", str(args.agents_root)]
    if args.dry_run:
        command.append("--dry-run")
    if args.list:
        command.append("--list")
    result = subprocess.run(command, check=False)
    if result.returncode:
        raise RuntimeError("Local sync failed; inspect the helper output before rerunning.")
    return {"mode": "local_only", "status": "preview" if args.dry_run else "synced", "dry_run": args.dry_run, "atlas_checked": False}


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    defaults = engine.core.roots_from_environment()
    private_root = Path(os.environ.get("LOCALAPPDATA", Path.home() / ".cache")) / "PratsSkillAtlas"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atlas-root", type=Path)
    parser.add_argument("--local-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--list", action="store_true", help="List missing names; combine with --dry-run for a preview")
    parser.add_argument("--refresh-catalog", action="store_true", help="Rebuild Atlas metadata even when no packages are missing")
    parser.add_argument("--report", type=Path, default=private_root / "last-sync.json")
    parser.add_argument("--claude-root", type=Path, default=defaults[0])
    parser.add_argument("--codex-root", type=Path, default=defaults[1])
    parser.add_argument("--agents-root", type=Path, default=defaults[2])
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    args.report = args.report.expanduser().resolve()
    if args.local_only and (args.atlas_root or args.refresh_catalog):
        parser.error("--local-only cannot be combined with Atlas options")
    started = time.perf_counter()
    try:
        report = run_local(args) if args.local_only else run_atlas(args)
        report["elapsed_seconds"] = round(time.perf_counter() - started, 3)
        args.report = args.report.expanduser()
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    except (OSError, RuntimeError, UnicodeError, subprocess.SubprocessError) as error:
        print(f"Sync incomplete: {error}", file=sys.stderr)
        return 1
    if report["mode"] == "atlas":
        print(json.dumps({key: report[key] for key in ("status", "before", "after", "catalog_refreshed", "elapsed_seconds")}, indent=2))
        for group in ("local_additions", "atlas_additions"):
            print(f"{group}: " + ", ".join(f"{runtime} +{len(names)}" for runtime, names in report[group].items()))
            if args.list:
                for runtime, names in report[group].items():
                    for name in names:
                        print(f"  {group}/{runtime}: {name}")
    print(f"Private report: {args.report}")
    print("No Git commit, push, deployment, or existing-package replacement was performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
