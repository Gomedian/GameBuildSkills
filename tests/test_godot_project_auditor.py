import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "godot-project-auditor" / "scripts" / "audit_godot_project.py"
SPEC = importlib.util.spec_from_file_location("audit_godot_project", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class GodotProjectAuditorTests(unittest.TestCase):
    def test_reads_project_wiring_and_static_signals(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "scenes").mkdir()
            (root / "scripts").mkdir()
            (root / "project.godot").write_text(
                '''config_version=5

[application]
config/name="Audit Fixture"
run/main_scene="res://scenes/main.tscn"
config/features=PackedStringArray("4.3", "GL Compatibility")

[autoload]
SceneFlow="*res://scripts/scene_flow.gd"

[input]
pause={"deadzone": 0.5, "events": []}
''', encoding="utf-8")
            (root / "scenes" / "main.tscn").write_text("[gd_scene format=3]\n", encoding="utf-8")
            (root / "scripts" / "scene_flow.gd").write_text(
                'extends Node\nfunc save():\n FileAccess.open("user://save.dat", FileAccess.WRITE)\n', encoding="utf-8")

            report = MODULE.audit(root)

            self.assertEqual(report["project"]["name"], "Audit Fixture")
            self.assertEqual(report["autoloads"]["SceneFlow"], "*res://scripts/scene_flow.gd")
            self.assertEqual(report["input_actions"], ["pause"])
            self.assertIn("scripts/scene_flow.gd", report["inspection_signals"]["user_writes"])
            self.assertEqual(report["findings"], [])

    def test_reports_missing_main_scene_and_autoload(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "project.godot").write_text(
                '''config_version=5
[application]
run/main_scene="res://missing.tscn"
[autoload]
Save="*res://missing.gd"
''', encoding="utf-8")

            codes = {item["code"] for item in MODULE.audit(root)["findings"]}

            self.assertIn("invalid-main-scene", codes)
            self.assertIn("invalid-autoload", codes)
            self.assertIn("no-input-actions", codes)


if __name__ == "__main__":
    unittest.main()
