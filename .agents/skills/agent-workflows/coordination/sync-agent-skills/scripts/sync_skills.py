#!/usr/bin/env python3
"""Audit and add missing skills between Claude and Codex global catalogs."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Callable

RUNTIME_DIRS = {
    ".cache",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "ms-playwright",
    "node_modules",
    "venv",
}
WINDOWS_HOST = os.name == "nt"


def roots_from_environment() -> tuple[Path, Path, Path]:
    home = Path.home()
    claude_config = Path(os.environ.get("CLAUDE_CONFIG_DIR", home / ".claude")).expanduser()
    codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex")).expanduser()
    return (
        claude_config / "skills",
        codex_home / "skills",
        home / ".agents" / "skills",
    )


def inventory(root: Path) -> dict[str, Path]:
    """Map case-insensitive skill names to package paths."""
    packages: dict[str, Path] = {}
    if not root.is_dir():
        return packages

    for entry in root.iterdir():
        try:
            if not entry.is_dir() or not (entry / "SKILL.md").is_file():
                continue
        except OSError as exc:
            raise RuntimeError(f"Cannot inspect {entry}: {exc}") from exc

        key = entry.name.casefold()
        previous = packages.get(key)
        if previous is not None:
            raise RuntimeError(
                f"Case-insensitive duplicate skill names in {root}: "
                f"{previous.name!r} and {entry.name!r}"
            )
        packages[key] = entry
    return packages


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def skill_text_differences(
    claude: dict[str, Path], codex: dict[str, Path]
) -> list[str]:
    differences = []
    for key in sorted(claude.keys() & codex.keys()):
        if file_hash(claude[key] / "SKILL.md") != file_hash(codex[key] / "SKILL.md"):
            differences.append(claude[key].name)
    return differences


def build_plan(
    source: dict[str, Path], target: dict[str, Path], target_root: Path
) -> list[tuple[str, Path, Path]]:
    plan = []
    for key in sorted(source.keys() - target.keys()):
        package = source[key]
        destination = target_root / package.name
        if destination.exists():
            raise RuntimeError(
                f"Destination collision at {destination}; no files were changed. "
                "Inspect the existing path before retrying."
            )
        if not (package / "SKILL.md").is_file():
            raise RuntimeError(f"Source is no longer a valid skill package: {package}")
        plan.append((package.name, package, destination))
    return plan


def copy_package(source: Path, destination: Path) -> set[Path]:
    """Stage a complete package, then publish it without replacing an existing path."""
    skipped: set[Path] = set()

    def ignore_runtime(directory: str, names: list[str]) -> list[str]:
        directory_path = Path(directory)
        ignored = []
        for name in names:
            candidate = directory_path / name
            if name.casefold() in RUNTIME_DIRS and candidate.is_dir():
                skipped.add(candidate)
                ignored.append(name)
        return ignored

    destination.parent.mkdir(parents=True, exist_ok=True)
    source_path = source.resolve() if source.is_symlink() else source

    with tempfile.TemporaryDirectory(
        prefix=".sync-agent-skills-", dir=destination.parent
    ) as temporary:
        staged = Path(temporary) / destination.name
        shutil.copytree(
            source_path,
            staged,
            symlinks=True,
            ignore=ignore_runtime,
        )
        if not (staged / "SKILL.md").is_file():
            raise RuntimeError(f"Copied package has no SKILL.md: {source}")
        if destination.exists():
            raise RuntimeError(f"Destination appeared during sync; left untouched: {destination}")
        try:
            os.replace(staged, destination)
        except PermissionError:
            # Some Windows-managed skill roots permit creation but deny directory
            # moves. Preserve the no-overwrite contract in the fallback too.
            if not WINDOWS_HOST or destination.exists():
                raise
            shutil.copytree(staged, destination, symlinks=True)

    return skipped


def parse_args() -> argparse.Namespace:
    claude_default, codex_default, agents_default = roots_from_environment()
    parser = argparse.ArgumentParser(
        description="Compare and add missing Claude Code and Codex skill packages."
    )
    parser.add_argument("--claude-root", type=Path, default=claude_default)
    parser.add_argument("--codex-root", type=Path, default=codex_default)
    parser.add_argument("--agents-root", type=Path, default=agents_default)
    parser.add_argument("--dry-run", action="store_true", help="audit without copying")
    parser.add_argument("--list", action="store_true", help="list skill names in the copy plan")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    claude_root = args.claude_root.expanduser()
    codex_root = args.codex_root.expanduser()
    agents_root = args.agents_root.expanduser()

    try:
        claude = inventory(claude_root)
        codex = inventory(codex_root)
        agents = inventory(agents_root)
        # Codex's direct package wins when both Codex roots contain the same name.
        codex_effective = {**agents, **codex}

        to_claude = build_plan(codex_effective, claude, claude_root)
        to_codex = build_plan(claude, codex_effective, codex_root)
    except (OSError, RuntimeError) as exc:
        print(f"Sync stopped before copying: {exc}", file=sys.stderr)
        return 2

    differences_before = skill_text_differences(claude, codex_effective)
    print(f"Claude skills: {len(claude)}")
    print(f"Codex direct skills: {len(codex)}")
    print(f"Shared Agents skills: {len(agents)}")
    print(f"Codex effective skills: {len(codex_effective)}")
    print(f"Missing from Claude: {len(to_claude)}")
    print(f"Missing from Codex effective catalog: {len(to_codex)}")
    if args.list:
        for name, _, destination in to_claude:
            print(f"ADD Claude: {name} -> {destination}")
        for name, _, destination in to_codex:
            print(f"ADD Codex: {name} -> {destination}")
    if args.dry_run:
        print(f"Same-name SKILL.md differences preserved: {len(differences_before)}")
        return 0

    skipped: set[Path] = set()
    copied_claude = []
    copied_codex = []
    try:
        for name, source, destination in to_claude:
            skipped.update(copy_package(source, destination))
            copied_claude.append(name)
        for name, source, destination in to_codex:
            skipped.update(copy_package(source, destination))
            copied_codex.append(name)

        claude_after = inventory(claude_root)
        codex_after = inventory(codex_root)
        agents_after = inventory(agents_root)
        codex_effective_after = {**agents_after, **codex_after}
        missing_after = sorted(claude_after.keys() ^ codex_effective_after.keys())
        if missing_after:
            raise RuntimeError(
                "Post-sync skill-name sets still differ: " + ", ".join(missing_after)
            )
        differences_after = skill_text_differences(claude_after, codex_effective_after)
    except (OSError, RuntimeError) as exc:
        print(f"Sync incomplete: {exc}", file=sys.stderr)
        return 1

    print(f"Added to Claude: {len(copied_claude)}")
    print(f"Added to Codex direct folder: {len(copied_codex)}")
    print(f"Skill-name sets match after sync: {len(claude_after)}")
    print(f"Same-name SKILL.md differences preserved: {len(differences_after)}")
    print(f"Runtime directories skipped: {len(skipped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
