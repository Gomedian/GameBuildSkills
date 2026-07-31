---
name: godot-project-auditor
description: Inspect an existing Godot 4 project and produce an evidence-based foundation audit from project.godot, scenes, scripts, resources, add-ons, Autoloads, Input Map, and startup configuration. Use before planning or generating Bootstrap, scene flow, UI, pause, input contexts, settings, save, audio, content registry, or other reusable Godot foundation modules, and when diagnosing duplicate ownership or missing project wiring.
---

# Godot Project Auditor

Audit the real project before proposing or installing a foundation.

## Run the audit

1. Resolve the project root containing `project.godot`.
2. Run:

   ```bash
   python3 scripts/audit_godot_project.py <project-root> --format markdown
   ```

3. Use `--format json` when another script will consume the result.
4. Treat script output as discovered evidence, not a complete architectural verdict.
5. Inspect the reported candidate files before assigning ownership or recommending replacement.

The script is read-only. Do not let it scan `.godot`, `.git`, imported assets, or generated build output.

## Interpret results

- Separate confirmed configuration from filename-based candidates.
- Record one authoritative owner per mutable concern only after reading its implementation.
- Classify requested modules as `reuse`, `configure`, `integrate`, `generate`, `replace`, or `defer`.
- Flag missing main scene, invalid local Autoload paths, and missing Autoload dependencies as setup failures.
- Flag direct scene changes, `user://` writes, and global group searches as inspection targets; do not call them defects without tracing context.
- Do not infer the installed Godot executable version from project feature tags alone.

## Continue the workflow

For architectural interpretation, load the sibling `game-development-foundation` skill and its Godot and foundation-module references. Produce the project-foundation audit template from that skill, citing paths from this audit and any subsequent source inspection.

Do not modify the target project unless the user also asks for implementation.

