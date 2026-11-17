"""PRE-SETUP-001-R5: regression checks for root discovery and archive execution."""

import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("verify_gitignore.py")
SPEC = importlib.util.spec_from_file_location("verify_gitignore", SCRIPT)
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class RootDiscoveryTests(unittest.TestCase):
    def test_active_and_archived_locations_with_both_config_names(self):
        # PRE-SETUP-001-R5: depth and YAML extension do not change root resolution.
        with tempfile.TemporaryDirectory(prefix="gitignore-root-test-") as directory:
            root = Path(directory).resolve()
            (root / "openspec").mkdir()
            for config_name in ("config.yaml", "config.yml"):
                config = root / "openspec" / config_name
                config.write_text("schema: spec-driven\n", encoding="utf-8")
                for relative in ("openspec/changes/add-gitignore/verify_gitignore.py",
                                 "openspec/changes/archive/2026-11-17-add-gitignore/verify_gitignore.py"):
                    with self.subTest(config=config_name, path=relative):
                        self.assertEqual(CHECKER.find_project_root(root / relative), root)
                config.unlink()

    def test_missing_root_fails_explicitly(self):
        # PRE-SETUP-001-R5: no silent fallback to the working directory.
        with tempfile.TemporaryDirectory(prefix="gitignore-root-test-") as directory:
            with self.assertRaisesRegex(RuntimeError, "Cannot locate project root"):
                CHECKER.find_project_root(Path(directory) / "verify_gitignore.py")

    def test_archived_checker_executes_full_matrix_from_another_directory(self):
        # PRE-SETUP-001-R5: exercise the actual script, not just the helper.
        with tempfile.TemporaryDirectory(prefix="gitignore-archive-test-") as directory:
            root = Path(directory).resolve()
            archived = root / "openspec/changes/archive/2026-11-17-add-gitignore"
            archived.mkdir(parents=True)
            (root / "openspec/config.yaml").write_text("schema: spec-driven\n", encoding="utf-8")
            project = CHECKER.find_project_root(SCRIPT)
            for relative in (".gitignore", "frontend/.gitignore", "backend/.gitignore"):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(project / relative, target)
            copied = archived / SCRIPT.name
            shutil.copyfile(SCRIPT, copied)
            result = subprocess.run([sys.executable, "-B", str(copied)],
                                    cwd=archived, text=True, encoding="utf-8",
                                    capture_output=True, check=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("46/46 cases passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
