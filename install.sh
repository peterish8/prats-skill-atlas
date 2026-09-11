#!/usr/bin/env bash
set -euo pipefail

repo_root="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
mode="${1:-all}"

copy_tree() {
  local name="$1"
  local source="$2"
  local target="$3"
  mkdir -p "$target"
  local count=0
  while IFS= read -r -d '' skill_file; do
    skill_dir="${skill_file%/SKILL.md}"
    cp -R "$skill_dir" "$target/"
    count=$((count + 1))
  done < <(find "$source" -mindepth 4 -maxdepth 4 -type f -name SKILL.md -print0)
  printf '%s: installed %s skill packages into %s\n' "$name" "$count" "$target"
}

case "$mode" in
  all)
    copy_tree Claude "$repo_root/.claude/skills" "${HOME}/.claude/skills"
    copy_tree Codex "$repo_root/.codex/skills" "${HOME}/.codex/skills"
    copy_tree Agents "$repo_root/.agents/skills" "${HOME}/.agents/skills"
    ;;
  claude) copy_tree Claude "$repo_root/.claude/skills" "${HOME}/.claude/skills" ;;
  codex) copy_tree Codex "$repo_root/.codex/skills" "${HOME}/.codex/skills" ;;
  agents) copy_tree Agents "$repo_root/.agents/skills" "${HOME}/.agents/skills" ;;
  selection)
    manifest="${2:?Usage: $0 selection path/to/selection.json}"
    python3 - "$manifest" "$repo_root" <<'PY'
import json
import shutil
import sys
from pathlib import Path

manifest_path = Path(sys.argv[1]).expanduser().resolve()
repo_root = Path(sys.argv[2]).resolve()
data = json.loads(manifest_path.read_text(encoding="utf-8"))
if data.get("schemaVersion") != 1:
    raise SystemExit("Unsupported selection manifest schemaVersion. Expected 1.")

selection = {}
for item in data.get("skills", []):
    name = item if isinstance(item, str) else item.get("name")
    if name:
        item_targets = set() if isinstance(item, str) else set(item.get("targets", []))
        selection.setdefault(name, set()).update(item_targets)
if not selection:
    raise SystemExit("Selection manifest contains no skills.")

roots = {
    "Claude": (repo_root / ".claude" / "skills", Path.home() / ".claude" / "skills"),
    "Codex": (repo_root / ".codex" / "skills", Path.home() / ".codex" / "skills"),
    "Agents": (repo_root / ".agents" / "skills", Path.home() / ".agents" / "skills"),
}
targets = data.get("targets", [])
if not targets:
    raise SystemExit("Selection manifest contains no targets.")

for target_name in targets:
    if target_name not in roots:
        raise SystemExit(f"Unknown target runtime: {target_name}")
    source, destination_root = roots[target_name]
    available = {path.parent.name: path.parent for path in source.glob("*/*/*/SKILL.md")}
    installed = 0
    missing = []
    for name, item_targets in selection.items():
        if item_targets and target_name not in item_targets:
            continue
        if name not in available:
            missing.append(name)
            continue
        destination_root.mkdir(parents=True, exist_ok=True)
        shutil.copytree(available[name], destination_root / name, dirs_exist_ok=True)
        installed += 1
    print(f"{target_name}: installed {installed} selected skill packages into {destination_root}")
    if missing:
        print(f"{target_name}: unavailable in this runtime tree: {', '.join(missing)}")
PY
    ;;
  *) echo "Usage: $0 [all|claude|codex|agents|selection path/to/selection.json]" >&2; exit 2 ;;
esac

echo 'Installation complete. Existing unrelated skill packages were not deleted.'
