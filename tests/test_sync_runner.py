"""One-command sync behavior, using isolated catalogs rather than the user's skills."""
import argparse
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / ".agents/skills/agent-workflows/coordination/sync-agent-skills/scripts/run_sync.py"
spec = importlib.util.spec_from_file_location("one_command_sync_test", ENTRY)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def skill(root, name, body="keep this"):
    folder = root / name
    folder.mkdir(parents=True)
    (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: fixture\n---\n{body}", encoding="utf-8")
    return folder


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.repo = self.root / "home/Documents/Codex/prats-skill-atlas"
        (self.repo / "scripts").mkdir(parents=True)
        (self.repo / "AGENTS.md").write_text("fixture")
        for name in ["category-rules.ps1", "organize-runtime-trees.ps1", "build-catalog.ps1", "validate.ps1"]:
            (self.repo / "scripts" / name).write_text("fixture")
        for runtime in runner.engine.RUNTIME_NAMES.values():
            (self.repo / runtime / "skills").mkdir(parents=True)
        self.c, self.d, self.a = [self.root / name for name in ["claude", "codex", "agents"]]
        self.args = argparse.Namespace(atlas_root=self.repo, claude_root=self.c, codex_root=self.d, agents_root=self.a, report=self.root / "private/report.json", dry_run=False, refresh_catalog=False, verbose=False)

    def tearDown(self):
        self.temp.cleanup()

    def test_default_discovers_known_checkout_without_scanning_home(self):
        found = runner.find_atlas(home=self.root / "home", cwd=self.root / "elsewhere", environ={})
        self.assertEqual(found, self.repo.resolve())

    def test_invalid_explicit_or_environment_root_does_not_fall_back(self):
        for explicit, environment in [(self.root / "wrong", {}), (None, {"PRATS_SKILL_ATLAS": str(self.root / "wrong")})]:
            with self.assertRaises(RuntimeError):
                runner.find_atlas(explicit, home=self.root / "home", cwd=self.repo, environ=environment)

    def test_preflight_sync_and_second_run_are_copy_only_and_idempotent(self):
        c = skill(self.c, "shared", "Claude version")
        d = skill(self.d, "shared", "Codex version")
        skill(self.c, "claude-only")
        skill(self.d, "codex-only")
        skill(self.repo / ".claude/skills/testing/qa-and-verification", "atlas-only")
        self.a.mkdir()
        original = [(c / "SKILL.md").read_bytes(), (d / "SKILL.md").read_bytes()]
        def placement(_repo, sources):
            return {name: ["testing", "qa-and-verification"] for name in sources}
        with patch.object(runner.engine, "placement_map", side_effect=placement), patch.object(runner, "refresh_catalog") as refresh:
            self.args.dry_run = True
            preview = runner.run_atlas(self.args)
            self.assertEqual(preview["status"], "preview")
            self.assertFalse((self.c / "atlas-only").exists())
            refresh.assert_not_called()
            self.args.dry_run = False
            first = runner.run_atlas(self.args)
            self.assertEqual(first["status"], "synced")
            self.assertTrue(first["after"]["matching_names"])
            self.assertEqual(first["after"]["claude"], 4)
            refresh.assert_called_once_with(self.repo.resolve())
        self.assertEqual((c / "SKILL.md").read_bytes(), original[0])
        self.assertEqual((d / "SKILL.md").read_bytes(), original[1])
        with patch.object(runner.engine, "placement_map") as placement_call, patch.object(runner, "catalog_needs_refresh", return_value=False), patch.object(runner, "refresh_catalog") as refresh:
            again = runner.run_atlas(self.args)
            self.assertEqual(again["status"], "already_synced")
            placement_call.assert_not_called()
            refresh.assert_not_called()

    def test_secret_blocks_preflight_before_any_local_copy(self):
        source = skill(self.c, "unsafe")
        (source / "private.txt").write_text("sk-" + "A" * 35)
        self.d.mkdir()
        self.a.mkdir()
        with patch.object(runner.engine, "placement_map", return_value={"unsafe": ["testing", "qa-and-verification"]}):
            with self.assertRaises(RuntimeError):
                runner.run_atlas(self.args)
        self.assertFalse((self.d / "unsafe").exists())
        self.assertFalse((self.repo / ".claude/skills/testing").exists())

    def test_stale_catalog_is_repaired_even_when_no_skill_names_are_missing(self):
        for root in [self.c, self.d, self.a]:
            root.mkdir()
        with patch.object(runner, "refresh_catalog") as refresh:
            report = runner.run_atlas(self.args)
        self.assertEqual(report["status"], "already_synced")
        self.assertTrue(report["catalog_refreshed"])
        refresh.assert_called_once()

    def test_catalog_freshness_checks_names_and_entrypoint_changes(self):
        entry = skill(self.repo / ".claude/skills/testing/qa-and-verification", "example") / "SKILL.md"
        (self.repo / "catalog").mkdir()
        index = self.repo / "catalog/skills.json"
        index.write_text(json.dumps({"skills": [{"name": "example"}], "skillCount": 1}))
        os.utime(entry, ns=(1_000_000_000, 1_000_000_000))
        self.assertFalse(runner.catalog_needs_refresh(self.repo))
        index.write_text(json.dumps({"skills": [], "skillCount": 0}))
        self.assertTrue(runner.catalog_needs_refresh(self.repo))

    def test_private_report_cannot_be_written_into_public_checkout(self):
        self.args.report = self.repo / "private-report.json"
        with self.assertRaises(RuntimeError):
            runner.run_atlas(self.args)
        self.assertFalse(self.args.report.exists())

    def test_count_refresh_preserves_unrelated_readme_text_and_line_endings(self):
        original = b'# Atlas\r\nWebsite work stays untouched.\r\n| [`.claude/skills`](.claude/skills) | 8 | packages |\r\n| **Unique skill names** | **8** | total |\r\n'
        (self.repo / "README.md").write_bytes(original)
        (self.repo / "catalog").mkdir()
        (self.repo / "catalog/skills.json").write_text(json.dumps({"skillCount": 1, "skills": [{"name": "example", "presentIn": ["Claude"]}]}))
        runner.refresh_readme_counts(self.repo)
        result = (self.repo / "README.md").read_bytes()
        self.assertEqual(result, original.replace(b'| 8 |', b'| 1 |').replace(b'**8**', b'**1**'))


if __name__ == "__main__":
    unittest.main()
