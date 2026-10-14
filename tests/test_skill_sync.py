"""Behavioral tests for copy-only local and public Atlas synchronization."""
import argparse
import hashlib
import importlib.util
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / ".agents/skills/agent-workflows/coordination/sync-agent-skills/scripts"
spec = importlib.util.spec_from_file_location("atlas_sync_test_subject", PACKAGE / "sync_atlas.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


def package(root, name, text="original"):
    destination = root / name
    destination.mkdir(parents=True)
    (destination / "SKILL.md").write_text(f"---\nname: {name}\ndescription: example\n---\n{text}\n", encoding="utf-8")
    (destination / "references").mkdir()
    (destination / "references/contract.md").write_text("real supporting contract", encoding="utf-8")
    return destination


class SynchronizationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_copy_retains_supporting_files_and_excludes_runtime_cache(self):
        source = package(self.root / "source", "example")
        (source / "node_modules").mkdir()
        (source / "node_modules/runtime.txt").write_text("do not copy")
        dest = self.root / "target/example"
        sync.core.copy_package(source, dest)
        self.assertEqual((dest / "references/contract.md").read_text(), "real supporting contract")
        self.assertFalse((dest / "node_modules").exists())

    def test_windows_move_denial_falls_back_without_overwriting(self):
        source = package(self.root / "source", "example")
        dest = self.root / "target/example"
        with patch.object(sync.core.os, "replace", side_effect=PermissionError("managed directory")), patch.object(sync.core, "WINDOWS_HOST", True):
            sync.core.copy_package(source, dest)
        self.assertTrue((dest / "references/contract.md").is_file())
        self.assertEqual((dest / "SKILL.md").read_bytes(), (source / "SKILL.md").read_bytes())

    def test_existing_destination_is_not_changed_on_move_failure(self):
        source = package(self.root / "source", "example", "incoming")
        dest = package(self.root / "target", "example", "keep me")
        before = (dest / "SKILL.md").read_bytes()
        with self.assertRaises(RuntimeError):
            sync.core.copy_package(source, dest)
        self.assertEqual((dest / "SKILL.md").read_bytes(), before)

    def test_publication_keeps_assets_and_licenses_but_excludes_builds(self):
        source = package(self.root / "source", "example")
        (source / "assets").mkdir()
        (source / "assets/art.png").write_bytes(b"binary artwork")
        (source / "LICENSE").write_text("MIT license retained")
        (source / "dist").mkdir()
        (source / "dist/generated.js").write_text("generated")
        manifest, _ = sync.publication_manifest(source)
        dest = self.root / "public/example"
        sync.publish_missing(source, dest, manifest)
        self.assertTrue((dest / "assets/art.png").is_file())
        self.assertTrue((dest / "LICENSE").is_file())
        self.assertFalse((dest / "dist").exists())

    def test_lowercase_windows_entrypoint_is_portable_in_public_catalog(self):
        source = package(self.root / "source", "example")
        original = (source / "SKILL.md").read_bytes()
        (source / "SKILL.md").unlink()
        (source / "skill.md").write_bytes(original)
        manifest, _ = sync.publication_manifest(source)
        self.assertIn("SKILL.md", manifest)
        dest = self.root / "public/example"
        sync.publish_missing(source, dest, manifest)
        self.assertEqual((dest / "SKILL.md").read_bytes(), original)

    def test_changed_source_after_preflight_does_not_create_destination(self):
        source = package(self.root / "source", "example")
        manifest, _ = sync.publication_manifest(source)
        (source / "references/contract.md").write_text("changed after preflight")
        dest = self.root / "public/example"
        with self.assertRaises(RuntimeError):
            sync.publish_missing(source, dest, manifest)
        self.assertFalse(dest.exists())

    def test_secret_input_blocks_publication_without_printing_secret(self):
        source = package(self.root / "source", "example")
        token = "sk-" + "A" * 35
        (source / "references/contract.md").write_text(token)
        with self.assertRaises(RuntimeError) as caught:
            sync.publication_manifest(source)
        self.assertNotIn(token, str(caught.exception))

    def test_risk_management_url_is_not_mistaken_for_an_api_key(self):
        source = package(self.root / "source", "example")
        (source / "references/contract.md").write_text("https://example.com/risk-management-and-your-trade-plan.html")
        sync.publication_manifest(source)

    def test_documented_aws_example_does_not_hide_other_key_matches(self):
        self.assertFalse(sync.has_secret("AWS documented example: AKIAIOSFODNN7EXAMPLE"))
        self.assertTrue(sync.has_secret("AKIAIOSFODNN7EXAMPLE and AKIA" + "Z" * 16))

    def test_pem_documentation_marker_is_allowed_but_key_body_is_blocked(self):
        self.assertFalse(sync.has_secret('JSON example: "-----BEGIN PRIVATE KEY-----\\n..."'))
        body = "-----BEGIN PRIVATE KEY-----\n" + "A" * 80 + "\n-----END PRIVATE KEY-----"
        self.assertTrue(sync.has_secret(body))

    def test_environment_credentials_are_blocked(self):
        source = package(self.root / "source", "example")
        (source / ".env").write_text("SECRET=private")
        with self.assertRaises(RuntimeError):
            sync.publication_manifest(source)

    def test_reviewed_fixture_exception_is_bound_to_full_file_contents(self):
        source = package(self.root / "source", "fixture-package")
        content = "fake test token: sk-" + "A" * 35
        path = source / "references/contract.md"
        path.write_text(content)
        digest = hashlib.sha256(content.encode()).hexdigest()
        with patch.dict(sync.REVIEWED_SECRET_FIXTURES, {("fixture-package", "references/contract.md"): digest}):
            sync.publication_manifest(source)
            path.write_text(content + "\nunreviewed addition")
            with self.assertRaises(RuntimeError):
                sync.publication_manifest(source)

    def test_union_sync_and_dry_run_preserve_existing_variants(self):
        repo = self.root / "atlas"
        (repo / "scripts").mkdir(parents=True)
        (repo / "AGENTS.md").write_text("fixture contract")
        (repo / "scripts/category-rules.ps1").write_text("fixture")
        for runtime in sync.RUNTIME_NAMES.values():
            (repo / runtime / "skills").mkdir(parents=True)
        package(repo / ".claude/skills/testing/qa-and-verification", "atlas-only")
        c, d, a = self.root / "claude", self.root / "codex", self.root / "agents"
        package(c, "claude-only")
        package(d, "codex-only")
        c_shared = package(c, "shared", "Claude variant")
        d_shared = package(d, "shared", "Codex variant")
        a.mkdir()
        before_c, before_d = (c_shared / "SKILL.md").read_bytes(), (d_shared / "SKILL.md").read_bytes()
        args = argparse.Namespace(atlas_root=repo, claude_root=c, codex_root=d, agents_root=a, dry_run=True)
        def placement(_repo, sources):
            return {name: ["testing", "qa-and-verification"] for name in sources}
        with patch.object(sync, "placement_map", side_effect=placement):
            preview = sync.synchronize(args)
            self.assertFalse((c / "atlas-only").exists())
            self.assertFalse((repo / ".codex/skills/testing").exists())
            self.assertEqual(preview["after"]["claude"], 4)
            args.dry_run = False
            result = sync.synchronize(args)
            self.assertTrue(result["after"]["matching_names"])
            self.assertEqual(result["after"]["claude"], 4)
            self.assertEqual((c_shared / "SKILL.md").read_bytes(), before_c)
            self.assertEqual((d_shared / "SKILL.md").read_bytes(), before_d)
            again = sync.synchronize(args)
            self.assertTrue(all(not names for names in again["local_additions"].values()))
            self.assertTrue(all(not names for names in again["atlas_additions"].values()))


if __name__ == "__main__":
    unittest.main()
