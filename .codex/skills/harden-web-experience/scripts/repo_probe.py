#!/usr/bin/env python3
"""Create a read-only signal map of an unfamiliar web repository.

This script intentionally reports navigation signals rather than findings. It never
prints source lines or environment-variable values.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


IGNORED_DIRECTORIES = {
    ".cache",
    ".git",
    ".gradle",
    ".next",
    ".nuxt",
    ".output",
    ".parcel-cache",
    ".svelte-kit",
    ".turbo",
    ".venv",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "target",
    "vendor",
    "venv",
}

SOURCE_SUFFIXES = {
    ".astro",
    ".cjs",
    ".css",
    ".go",
    ".html",
    ".java",
    ".js",
    ".jsx",
    ".kt",
    ".mjs",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".scss",
    ".svelte",
    ".swift",
    ".ts",
    ".tsx",
    ".vue",
}

ASSET_SUFFIXES = {
    ".avif",
    ".gif",
    ".jpeg",
    ".jpg",
    ".m4a",
    ".mp3",
    ".mp4",
    ".ogg",
    ".otf",
    ".png",
    ".svg",
    ".ttf",
    ".wav",
    ".webm",
    ".webp",
    ".woff",
    ".woff2",
}

MANIFEST_NAMES = {
    "Cargo.toml",
    "Gemfile",
    "go.mod",
    "package.json",
    "pom.xml",
    "pyproject.toml",
    "requirements.txt",
}

LOCKFILE_NAMES = {
    "bun.lock",
    "bun.lockb",
    "Cargo.lock",
    "composer.lock",
    "Gemfile.lock",
    "package-lock.json",
    "pnpm-lock.yaml",
    "poetry.lock",
    "uv.lock",
    "yarn.lock",
}

CONFIG_NAMES = {
    ".dockerignore",
    ".gitignore",
    "Dockerfile",
    "astro.config.mjs",
    "compose.yaml",
    "docker-compose.yml",
    "eslint.config.js",
    "lighthouserc.js",
    "next.config.js",
    "next.config.mjs",
    "next.config.ts",
    "nuxt.config.ts",
    "playwright.config.js",
    "playwright.config.ts",
    "svelte.config.js",
    "tsconfig.json",
    "vercel.json",
    "vite.config.js",
    "vite.config.ts",
    "vitest.config.js",
    "vitest.config.ts",
}

KNOWN_WEB_PACKAGES = {
    "@angular/core",
    "@opentelemetry/api",
    "@playwright/test",
    "@sentry/browser",
    "@sentry/nextjs",
    "@tanstack/react-query",
    "@trpc/client",
    "astro",
    "axios",
    "express",
    "fastify",
    "hono",
    "next",
    "nuxt",
    "playwright",
    "react",
    "remix",
    "svelte",
    "vite",
    "vue",
}

MAX_TEXT_BYTES = 1_500_000

SIGNALS = {
    "request_call": re.compile(
        r"\b(fetch|axios\.(get|post|put|patch|delete)|useQuery|useMutation|graphql|trpc)\s*\(",
        re.IGNORECASE,
    ),
    "form_or_action": re.compile(
        r"(<form\b|<button\b|\bonSubmit\b|\bonClick\b|\bserver action\b)",
        re.IGNORECASE,
    ),
    "loading_state": re.compile(
        r"\b(isLoading|isPending|loading|pending|aria-busy|Suspense)\b",
        re.IGNORECASE,
    ),
    "error_feedback": re.compile(
        r"\b(error|errorMessage|role=[\"']alert|toast\.(error|warning))\b",
        re.IGNORECASE,
    ),
    "empty_state": re.compile(
        r"\b(emptyState|noResults|noData|items\.length\s*===?\s*0)\b",
        re.IGNORECASE,
    ),
    "auth_or_permission": re.compile(
        r"\b(authenticate|authorization|authorize|permission|session|tenantId|ownerId)\b",
        re.IGNORECASE,
    ),
    "validation": re.compile(
        r"\b(zod|yup|joi|validator|validate|safeParse|parseAsync)\b",
        re.IGNORECASE,
    ),
    "transaction_or_idempotency": re.compile(
        r"\b(transaction|idempotenc|upsert|deduplicat)\w*\b",
        re.IGNORECASE,
    ),
    "retry_timeout_or_cancel": re.compile(
        r"\b(retry|timeout|AbortController|signal\.abort|backoff)\b",
        re.IGNORECASE,
    ),
    "telemetry": re.compile(
        r"\b(opentelemetry|sentry|captureException|traceId|spanId|logger\.)\b",
        re.IGNORECASE,
    ),
    "raw_html_sink": re.compile(
        r"\b(dangerouslySetInnerHTML|innerHTML\s*=|outerHTML\s*=)\b",
        re.IGNORECASE,
    ),
    "dynamic_code_execution": re.compile(
        r"\b(eval\s*\(|new\s+Function\s*\(|exec\s*\(|spawn\s*\()",
        re.IGNORECASE,
    ),
    "browser_credential_storage": re.compile(
        r"(localStorage|sessionStorage).{0,80}\b(token|secret|password|credential)\b",
        re.IGNORECASE,
    ),
    "wildcard_cors_hint": re.compile(
        r"(access-control-allow-origin.{0,40}[\"']\*[\"']|origin\s*:\s*[\"']\*[\"'])",
        re.IGNORECASE,
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Map web-repository surfaces and navigation signals without editing it."
    )
    parser.add_argument("root", type=Path, help="Repository root to inspect.")
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format (default: markdown).",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=80,
        help="Maximum paths or hits shown per section (default: 80).",
    )
    return parser.parse_args()


def walk_files(root: Path) -> Iterable[Path]:
    for directory, directory_names, file_names in os.walk(root):
        directory_names[:] = sorted(
            name
            for name in directory_names
            if name not in IGNORED_DIRECTORIES
            and not Path(directory, name).is_symlink()
        )
        for file_name in sorted(file_names):
            path = Path(directory, file_name)
            if not path.is_symlink():
                yield path


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_environment_file(path: Path) -> bool:
    return path.name == ".env" or path.name.startswith(".env.")


def is_route_candidate(path: Path, root: Path) -> bool:
    relative_path = path.relative_to(root)
    parts = {part.lower() for part in relative_path.parts[:-1]}
    name = path.name.lower()
    route_names = {
        "+page.js",
        "+page.svelte",
        "+page.ts",
        "+server.js",
        "+server.ts",
        "page.js",
        "page.jsx",
        "page.ts",
        "page.tsx",
        "route.js",
        "route.ts",
    }
    if name in route_names:
        return True
    return bool(parts.intersection({"api", "controllers", "handlers", "pages", "routes"}))


def is_test_candidate(path: Path) -> bool:
    name = path.name.lower()
    parts = {part.lower() for part in path.parts}
    return (
        "test" in parts
        or "tests" in parts
        or "__tests__" in parts
        or bool(re.search(r"\.(spec|test)\.[^.]+$", name))
    )


def package_summary(path: Path) -> dict[str, Any] | None:
    if path.name != "package.json" or path.stat().st_size > MAX_TEXT_BYTES:
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None
    scripts = data.get("scripts", {})
    dependencies: set[str] = set()
    for field in ("dependencies", "devDependencies", "peerDependencies"):
        value = data.get(field, {})
        if isinstance(value, dict):
            dependencies.update(value)
    return {
        "scripts": sorted(scripts) if isinstance(scripts, dict) else [],
        "web_packages": sorted(dependencies.intersection(KNOWN_WEB_PACKAGES)),
    }


def scan(root: Path, max_items: int) -> dict[str, Any]:
    manifests: list[dict[str, Any]] = []
    environment_files: list[str] = []
    config_files: list[str] = []
    route_candidates: list[str] = []
    test_candidates: list[str] = []
    assets: list[dict[str, Any]] = []
    signal_counts: dict[str, int] = defaultdict(int)
    signal_hits: dict[str, list[dict[str, Any]]] = defaultdict(list)
    files_seen = 0
    source_files_scanned = 0
    source_files_skipped = 0

    for path in walk_files(root):
        files_seen += 1
        relative_path = relative(path, root)
        try:
            size = path.stat().st_size
        except OSError:
            continue

        if path.name in MANIFEST_NAMES:
            manifest: dict[str, Any] = {"path": relative_path}
            summary = package_summary(path)
            if summary is not None:
                manifest.update(summary)
            manifests.append(manifest)

        if is_environment_file(path):
            environment_files.append(relative_path)
            continue

        relative_parts = set(path.relative_to(root).parts)
        if (
            path.name in CONFIG_NAMES
            or path.name in LOCKFILE_NAMES
            or ".github" in relative_parts
        ):
            config_files.append(relative_path)

        if is_route_candidate(path, root):
            route_candidates.append(relative_path)

        if is_test_candidate(path):
            test_candidates.append(relative_path)

        if path.suffix.lower() in ASSET_SUFFIXES:
            assets.append({"path": relative_path, "bytes": size})

        if path.suffix.lower() not in SOURCE_SUFFIXES:
            continue
        if size > MAX_TEXT_BYTES:
            source_files_skipped += 1
            continue

        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            source_files_skipped += 1
            continue

        source_files_scanned += 1
        for line_number, line in enumerate(lines, start=1):
            for label, pattern in SIGNALS.items():
                if not pattern.search(line):
                    continue
                signal_counts[label] += 1
                if len(signal_hits[label]) < max_items:
                    signal_hits[label].append(
                        {"path": relative_path, "line": line_number}
                    )

    assets.sort(key=lambda item: item["bytes"], reverse=True)
    manifests.sort(key=lambda item: item["path"])
    environment_files.sort()
    config_files.sort()
    route_candidates.sort()
    test_candidates.sort()

    return {
        "root": str(root),
        "summary": {
            "files_seen": files_seen,
            "source_files_scanned": source_files_scanned,
            "source_files_skipped": source_files_skipped,
            "manifests_found": len(manifests),
            "environment_files_found": len(environment_files),
            "config_files_found": len(config_files),
            "route_candidates_found": len(route_candidates),
            "test_candidates_found": len(test_candidates),
            "static_assets_found": len(assets),
        },
        "manifests": manifests[:max_items],
        "environment_files": environment_files[:max_items],
        "config_files": config_files[:max_items],
        "route_candidates": route_candidates[:max_items],
        "test_candidates": test_candidates[:max_items],
        "largest_assets": assets[: min(max_items, 30)],
        "signal_counts": dict(sorted(signal_counts.items())),
        "signal_hits": {
            label: signal_hits[label] for label in sorted(signal_hits)
        },
        "warning": "Signals are navigation hints, not confirmed defects or coverage.",
    }


def print_paths(title: str, paths: list[str], total: int) -> None:
    print(f"\n## {title} ({total})\n")
    if not paths:
        print("None found in the displayed scope.")
        return
    for path in paths:
        print(f"- `{path}`")


def print_markdown(result: dict[str, Any]) -> None:
    summary = result["summary"]
    print("# Web repository probe")
    print(f"\nRoot: `{result['root']}`")
    print(
        "\nScanned "
        f"{summary['source_files_scanned']} source files from "
        f"{summary['files_seen']} files; skipped "
        f"{summary['source_files_skipped']} oversized/unreadable source files."
    )
    print(f"\n> {result['warning']}")

    print(f"\n## Manifests ({summary['manifests_found']})\n")
    if not result["manifests"]:
        print("None found.")
    for manifest in result["manifests"]:
        print(f"- `{manifest['path']}`")
        scripts = manifest.get("scripts", [])
        packages = manifest.get("web_packages", [])
        if scripts:
            print(f"  - scripts: {', '.join(scripts)}")
        if packages:
            print(f"  - web packages: {', '.join(packages)}")

    print_paths(
        "Environment filenames (values not read)",
        result["environment_files"],
        summary["environment_files_found"],
    )
    print_paths(
        "Configuration", result["config_files"], summary["config_files_found"]
    )
    print_paths(
        "Route/API candidates",
        result["route_candidates"],
        summary["route_candidates_found"],
    )
    print_paths(
        "Test candidates",
        result["test_candidates"],
        summary["test_candidates_found"],
    )

    print(f"\n## Largest static assets ({summary['static_assets_found']})\n")
    if not result["largest_assets"]:
        print("None found.")
    for asset in result["largest_assets"]:
        kibibytes = asset["bytes"] / 1024
        print(f"- `{asset['path']}` - {kibibytes:.1f} KiB")

    print("\n## Source signals\n")
    if not result["signal_counts"]:
        print("None found.")
        return
    for label, count in result["signal_counts"].items():
        print(f"### {label} ({count})\n")
        for hit in result["signal_hits"].get(label, []):
            print(f"- `{hit['path']}:{hit['line']}`")
        print()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: repository root is not a directory: {root}", file=sys.stderr)
        return 2
    if args.max_items < 1:
        print("error: --max-items must be positive", file=sys.stderr)
        return 2

    result = scan(root, args.max_items)
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print_markdown(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
