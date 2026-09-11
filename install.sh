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
  *) echo "Usage: $0 [all|claude|codex|agents]" >&2; exit 2 ;;
esac

echo 'Installation complete. Existing unrelated skill packages were not deleted.'
