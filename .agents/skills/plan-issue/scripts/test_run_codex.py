import os
import subprocess
import sys
import tempfile
import tomllib
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch

import run_codex


class WindowsRunnerTest(unittest.TestCase):
    def test_permission_config_preserves_settings_without_legacy_sandbox_overrides(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            source = home / "config.toml"
            original = (
                'model = "configured-model"\nsandbox_mode = "danger-full-access"\n'
                'default_permissions = ":danger-full-access"\napproval_policy = "never"\n'
                '[sandbox_workspace_write]\nwritable_roots = ["C:/unrelated"]\n'
                '[windows]\nsandbox = "unelevated"\n'
            )
            source.write_text(original, encoding="utf-8")
            with patch.dict(os.environ, {"CODEX_HOME": directory}), ExitStack() as cleanup:
                name = run_codex.permission_profile_config(cleanup)
                profile = home / f"{name}.config.toml"
                config = tomllib.loads(profile.read_text(encoding="utf-8"))
                self.assertEqual(config["model"], "configured-model")
                self.assertEqual(config["approval_policy"], "never")
                self.assertNotIn("sandbox_mode", config)
                self.assertNotIn("sandbox_workspace_write", config)
                self.assertNotIn("default_permissions", config)
                self.assertEqual(source.read_text(encoding="utf-8"), original)
            self.assertFalse(profile.exists())

    @unittest.skipUnless(os.name == "nt", "Windows-specific validation environment")
    def test_validation_cleans_temporary_permissions_when_codex_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            (home / "config.toml").write_text('sandbox_mode = "danger-full-access"\n', encoding="utf-8")
            prompt = home / "prompt.txt"
            prompt.write_text("Validate without modifying code.", encoding="utf-8")
            argv = [
                "run_codex.py", "--mode", "validate", "--prompt", str(prompt),
                "--schema", str(home / "schema.json"), "--result", str(home / "result.json"),
                "--repo", str(home),
            ]
            observed = {}

            def fail(command, **options):
                observed["temporary"] = Path(options["env"]["TEMP"])
                observed["profile"] = home / f'{command[command.index("--profile") + 1]}.config.toml'
                self.assertTrue(observed["temporary"].is_dir())
                self.assertTrue(observed["profile"].is_file())
                self.assertIn("--ignore-user-config", command)
                self.assertNotIn("--sandbox", command)
                raise subprocess.SubprocessError("runner unavailable")

            with patch.dict(os.environ, {"CODEX_HOME": directory}), patch.object(sys, "argv", argv):
                with patch.object(run_codex, "cli_compatibility", return_value=None), patch.object(run_codex.subprocess, "run", fail):
                    with self.assertRaises(subprocess.SubprocessError):
                        run_codex.main()
            self.assertFalse(observed["temporary"].exists())
            self.assertFalse(observed["profile"].exists())


if __name__ == "__main__":
    unittest.main()
