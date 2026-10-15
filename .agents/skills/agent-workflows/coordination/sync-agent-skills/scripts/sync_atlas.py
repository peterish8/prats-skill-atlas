#!/usr/bin/env python3
"""Copy missing packages between local Claude/Codex catalogs and an Atlas checkout."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("skill_sync_core", Path(__file__).with_name("sync_skills.py"))
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)

RUNTIME_NAMES = {"Claude": ".claude", "Codex": ".codex", "Agents": ".agents"}
EXCLUDED_DIRS = core.RUNTIME_DIRS | {
    ".git", ".next", ".svelte-kit", "dist", "dist-packages", "build", "target", "coverage",
}
TEXT_SUFFIXES = {".md", ".py", ".ps1", ".sh", ".json", ".yaml", ".yml", ".toml", ".txt", ".js", ".mjs", ".ts", ".tsx", ".svelte", ".css", ".html", ".xml"}
SECRET_PATTERN = re.compile(
    r"(?<![A-Za-z0-9_-])(?:gh[pousr]_[A-Za-z0-9]{30,}|sk-(?:proj-)?[A-Za-z0-9_-]{30,}|AKIA[A-Z0-9]{16})"
)
PRIVATE_KEY_PATTERN = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |ENCRYPTED )?PRIVATE KEY-----\s*[A-Za-z0-9+/=\s]{64,}-----END (?:RSA |EC |OPENSSH |ENCRYPTED )?PRIVATE KEY-----")
PUBLIC_EXAMPLE_KEYS = {"AKIAIOSFODNN7EXAMPLE"}
# Content-reviewed synthetic credential test vectors. These exemptions are
# pinned to complete normalized file contents, never to a whole test directory.
REVIEWED_SECRET_FIXTURES = {
    ("gstack", "test/brain-sync.test.ts"): "863875f209b12d6142f0ddd1a6a99843f8b21c6620d4fc6215dbe3a99916e3ff",
    ("gstack", "test/gstack-memory-ingest.test.ts"): "d27554db3522df0f7a5c5ac260c8706c47c3f0466b7ca87ce8601e16026f6980",
    ("gstack", "test/gstack-redact-cli.test.ts"): "b69b587a405f9fd9e74107aec8a1fef881a790c1de2d6e5ca1747194ad97c881",
    ("gstack", "test/redact-engine.test.ts"): "84dd4dc4b721e3bfe5347409c4c2b00eae3a01f572a0fce3f96817477462b787",
    ("gstack", "test/redact-prepush-hook.test.ts"): "efc095af9284f9d2d21df3bed29888b7e4eabdd1b7d45a4d2f9d49b1e4cfc108",
    ("gstack", "test/ship-template-redaction.test.ts"): "4be982b227b5c0955822eac5d01adf0c0efa681c30f9571c47cb8e21b7beca8e",
    ("gstack", "test/skill-e2e-cso.test.ts"): "ce4331205b501339407cf65ebfb0975720f183ccefb66c1f520dba00340e71ac",
}


def has_secret(text: str) -> bool:
    return bool(PRIVATE_KEY_PATTERN.search(text)) or any(match.group() not in PUBLIC_EXAMPLE_KEYS for match in SECRET_PATTERN.finditer(text))


def atlas_inventory(repo: Path, runtime: str) -> dict[str, Path]:
    root = repo / RUNTIME_NAMES[runtime] / "skills"
    result = {}
    if not root.is_dir():
        raise RuntimeError(f"Missing Atlas runtime tree: {runtime}")
    for skill in sorted(root.glob("*/*/*/SKILL.md")):
        key = skill.parent.name.casefold()
        if key in result:
            raise RuntimeError(f"Duplicate Atlas package name in {runtime}: {key}")
        result[key] = skill.parent
    return result


def files_for_package(package: Path):
    """Never follow nested links or include caches, credentials, or build outputs."""
    for directory, dirs, files in os.walk(package, followlinks=False):
        dirs[:] = sorted(name for name in dirs if name.casefold() not in EXCLUDED_DIRS)
        for name in list(dirs):
            candidate = Path(directory) / name
            if candidate.is_symlink() or candidate.is_junction():
                raise RuntimeError(f"Nested directory link needs manual packaging: {candidate}")
        for name in sorted(files):
            source = Path(directory) / name
            if source.is_symlink():
                raise RuntimeError(f"Nested file link needs manual packaging: {source}")
            lower = name.casefold()
            if lower == ".env" or (lower.startswith(".env.") and lower not in {".env.example", ".env.sample", ".env.template"}):
                raise RuntimeError(f"Credential file cannot be published: {source}")
            if source.suffix.casefold() in {".pem", ".p12", ".pfx", ".key", ".pyc"}:
                raise RuntimeError(f"Private-key or runtime file cannot be published: {source}")
            yield source.relative_to(package), source


def portable_text(name: str, relative: Path, text: str) -> str:
    """Change public documentation only; installed local originals are retained."""
    home = str(Path.home())
    for spelling in {home, home.replace("\\", "/"), home.replace("\\", "\\\\")}:
        text = text.replace(spelling, "~")
    text = text.replace("/home/user/project", "<project-root>")
    if name == "fullstack-engineer-profile":
        text = re.sub(r"[A-Za-z]:\\dev\\allegra", "<allegra-root>", text)
        for folder, token in [("movieX", "<cineblock-root>"), ("Cubify", "<cubify-root>"), ("ClassDrop", "<classdrop-root>")]:
            text = text.replace("~\\Desktop\\1 prats projects\\" + folder, token)
        if relative.as_posix() == "references/portfolio-scope.md":
            text += "\nConfigure the named project-root placeholders from user-designated checkouts before inspecting source. No machine-specific checkout location is distributed.\n"
    if name == "website-design-unslop" and relative.as_posix() == "references/sources.md":
        text = re.sub(r"`~[/\\]\.codex[/\\]attachments[/\\][^`]+`", "the user's private source attachment (not distributed)", text)
    if name == "tactile-reference-ui":
        preparation = "This public package carries source, references, artwork, fonts, and licenses. Generated output is excluded. In `assets/design-kit`, run `npm ci`, `npm run build`, and `npm run pack:libs` to generate the local adapter tarballs before following installation commands. Follow the project's existing dependency-install authorization.\n\n"
        if relative.as_posix() == "SKILL.md":
            text = text.replace("The bundled `assets/design-kit/dist-packages/` contains installable tokens and framework tarballs.", "After building and packing the source kit, `assets/design-kit/dist-packages/` contains installable tokens and framework tarballs.")
            text = text.replace("## Use the actual library\n", "## Use the actual library\n\n" + preparation)
        elif relative.as_posix() == "references/framework-guide.md":
            text = text.replace("## Install from the portable bundle\n", "## Install from the portable bundle\n\n" + preparation)
    return text


def publication_manifest(package: Path):
    result = {}
    transforms = []
    for relative, source in files_for_package(package):
        # Windows accepts skill.md, but the public Linux catalog requires the
        # conventional uppercase entrypoint. Keep the source file untouched.
        if relative.as_posix().casefold() == "skill.md":
            relative = Path("SKILL.md")
        data = source.read_bytes()
        if source.suffix.casefold() in TEXT_SUFFIXES:
            text = data.decode("utf-8", errors="strict")
            fixture_digest = hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()
            reviewed_fixture = REVIEWED_SECRET_FIXTURES.get((package.name.casefold(), relative.as_posix())) == fixture_digest
            if has_secret(text) and not reviewed_fixture:
                raise RuntimeError(f"Secret-shaped content requires review: {source}")
            portable = portable_text(package.name.casefold(), relative, text)
            if portable != text:
                transforms.append(relative.as_posix())
                data = portable.encode("utf-8")
        result[relative.as_posix()] = (source, hashlib.sha256(data).hexdigest())
    if "SKILL.md" not in result:
        raise RuntimeError(f"Missing package entrypoint: {package}")
    return result, transforms


def publish_missing(package: Path, destination: Path, manifest):
    if destination.exists():
        raise RuntimeError(f"Refusing to overwrite existing Atlas package: {destination}")
    # Recheck every source before creating the destination, so concurrent edits
    # cannot invalidate the reviewed publication plan.
    current, _ = publication_manifest(package)
    if {k: v[1] for k, v in current.items()} != {k: v[1] for k, v in manifest.items()}:
        raise RuntimeError(f"Source changed after preflight: {package}")
    destination.mkdir(parents=True, exist_ok=False)
    for relative in sorted(manifest, key=lambda x: (x == "SKILL.md", x)):
        source = manifest[relative][0]
        data = source.read_bytes()
        if source.suffix.casefold() in TEXT_SUFFIXES:
            data = portable_text(package.name.casefold(), Path(relative), data.decode("utf-8")).encode("utf-8")
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(data)
        if hashlib.sha256(target.read_bytes()).hexdigest() != manifest[relative][1]:
            raise RuntimeError(f"Copy verification failed: {target}")


def placement_map(repo: Path, sources: dict[str, Path]):
    import subprocess
    command = ". ./scripts/category-rules.ps1; $names = Get-Content -Raw -LiteralPath $env:SKILL_SYNC_NAMES | ConvertFrom-Json; $result = @{}; foreach ($name in $names) { $p = Get-SkillPlacement -Name $name; $result[$name] = @($p.Category,$p.Subcategory) }; $result | ConvertTo-Json -Depth 3 -Compress"
    import tempfile
    with tempfile.TemporaryDirectory(prefix="atlas-placement-") as scratch:
        names = Path(scratch) / "names.json"
        names.write_text(json.dumps(sorted(sources)), encoding="utf-8")
        env = {**os.environ, "SKILL_SYNC_NAMES": str(names)}
        run = subprocess.run(["pwsh", "-NoProfile", "-Command", command], cwd=repo, env=env, text=True, capture_output=True, check=True)
    result = json.loads(run.stdout.strip())
    for name, parts in result.items():
        if len(parts) != 2 or any(not re.fullmatch(r"[A-Za-z0-9_-]+", part) for part in parts):
            raise RuntimeError(f"Unsafe category placement for {name}")
    return result


def synchronize(args):
    repo = args.atlas_root.expanduser().resolve()
    if not (repo / "AGENTS.md").is_file() or not (repo / "scripts/category-rules.ps1").is_file():
        raise RuntimeError("Atlas root must contain its instructions and category rules")
    croot, droot, aroot = (x.expanduser() for x in (args.claude_root, args.codex_root, args.agents_root))
    claude, codex, agents = core.inventory(croot), core.inventory(droot), core.inventory(aroot)
    effective = {**agents, **codex}
    atlas = {runtime: atlas_inventory(repo, runtime) for runtime in RUNTIME_NAMES}
    known = {**atlas["Agents"], **atlas["Codex"], **atlas["Claude"]}
    union = set(claude) | set(effective) | set(known)
    report = {"before": {"claude": len(claude), "codex_direct": len(codex), "codex_effective": len(effective), "atlas_unique": len(known)}, "local_additions": {"Claude": [], "Codex": []}, "atlas_additions": {key: [] for key in RUNTIME_NAMES}, "portable_files": [], "dry_run": args.dry_run}
    # No existing local package is replaced. Atlas runtime variants take priority
    # only for names that are unavailable locally.
    planned = []
    for runtime, target, local, preferred in [("Claude", croot, claude, {**known, **atlas["Claude"], **effective}), ("Codex", droot, effective, {**known, **atlas["Codex"], **claude})]:
        for name in sorted(union - local.keys()):
            source = preferred[name]
            destination = target / source.name
            if destination.exists():
                raise RuntimeError(f"Existing path is not a loadable skill: {destination}")
            planned.append((runtime, source, destination))
            report["local_additions"][runtime].append(name)
            if args.dry_run:
                if runtime == "Claude": claude[name] = source
                else: effective[name] = source
    if not args.dry_run:
        for runtime, source, destination in planned:
            print(f"Add local {runtime}: {source.name}", flush=True)
            core.copy_package(source, destination)
        claude, codex = core.inventory(croot), core.inventory(droot)
        effective = {**agents, **codex}
    if set(claude) != union or set(effective) != union:
        raise RuntimeError("Local effective catalogs do not match the planned union")
    publications = []
    for runtime, sources in [("Claude", claude), ("Codex", effective), ("Agents", agents)]:
        missing = sources.keys() - atlas[runtime].keys()
        if not missing:
            continue
        placement = placement_map(repo, {name: sources[name] for name in missing})
        for name in sorted(missing):
            if getattr(args, "verbose", False):
                print(f"Preflight Atlas {runtime}: {name}", flush=True)
            source = sources[name]
            parts = placement[name]
            destination = repo / RUNTIME_NAMES[runtime] / "skills" / parts[0] / parts[1] / source.name
            if destination.exists():
                raise RuntimeError(f"Unexpected Atlas path collision: {destination}")
            manifest, changes = publication_manifest(source)
            publications.append((runtime, source, destination, manifest))
            report["atlas_additions"][runtime].append(name)
            report["portable_files"].extend(f"{runtime}/{name}/{path}" for path in changes)
    if not args.dry_run:
        for runtime, source, destination, manifest in publications:
            print(f"Add Atlas {runtime}: {source.name}", flush=True)
            publish_missing(source, destination, manifest)
        final_atlas = {key: atlas_inventory(repo, key) for key in RUNTIME_NAMES}
        if set(final_atlas["Claude"]) != union or set(final_atlas["Codex"]) != union:
            raise RuntimeError("Atlas Claude/Codex name sets differ from the local union")
    report["after"] = {"claude": len(claude), "codex_effective": len(effective), "matching_names": set(claude) == set(effective), "same_name_instruction_variants_preserved": len(core.skill_text_differences(claude, effective))}
    return report


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    defaults = core.roots_from_environment()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atlas-root", type=Path, required=True)
    parser.add_argument("--claude-root", type=Path, default=defaults[0])
    parser.add_argument("--codex-root", type=Path, default=defaults[1])
    parser.add_argument("--agents-root", type=Path, default=defaults[2])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--verbose", action="store_true", help="show package-level preflight progress")
    args = parser.parse_args()
    try:
        report = synchronize(args)
    except (OSError, RuntimeError, UnicodeError) as error:
        print(f"Sync stopped: {error}", file=sys.stderr)
        return 1
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"before": report["before"], "local_added": {k: len(v) for k, v in report["local_additions"].items()}, "atlas_added": {k: len(v) for k, v in report["atlas_additions"].items()}, "portable_files": len(report["portable_files"]), "after": report["after"], "dry_run": args.dry_run}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
