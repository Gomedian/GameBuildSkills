#!/usr/bin/env python3
"""Read-only static audit for a Godot project."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

SKIP_DIRS = {".git", ".godot", ".import", "build", "dist", "exports"}
TEXT_EXTENSIONS = {".gd", ".cs", ".tscn", ".tres", ".godot"}
CONCERN_TERMS = {
    "scene_flow": ("scene", "transition", "loading"),
    "ui_navigation": ("ui", "screen", "popup", "modal", "menu"),
    "input": ("input", "control", "rebind"),
    "save": ("save", "persist", "storage"),
    "settings": ("setting", "option", "config"),
    "audio": ("audio", "sound", "music", "bgm"),
    "content_registry": ("content", "registry", "catalog", "database"),
}


def iter_project_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return ""


def parse_project(text: str) -> dict[str, Any]:
    section = ""
    values: dict[str, dict[str, str]] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(";"):
            continue
        match = re.fullmatch(r"\[([^]]+)]", line)
        if match:
            section = match.group(1)
            values.setdefault(section, {})
            continue
        if "=" in line and section:
            key, value = line.split("=", 1)
            values[section][key.strip()] = value.strip()
    return values


def unquote(value: str | None) -> str | None:
    if value is None:
        return None
    match = re.fullmatch(r'"(.*)"', value)
    return match.group(1) if match else value


def res_to_path(root: Path, value: str) -> Path | None:
    cleaned = value.lstrip("*")
    if not cleaned.startswith("res://"):
        return None
    return root / cleaned.removeprefix("res://")


def relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def audit(root: Path) -> dict[str, Any]:
    project_path = root / "project.godot"
    if not project_path.is_file():
        raise ValueError(f"project.godot not found under {root}")

    project_text = read_text(project_path)
    config = parse_project(project_text)
    app = config.get("application", {})
    features = re.findall(r'"([^"]+)"', config.get("application", {}).get("config/features", ""))
    main_scene = unquote(app.get("run/main_scene"))
    autoloads = {name: unquote(value) or "" for name, value in config.get("autoload", {}).items()}
    input_actions = sorted(config.get("input", {}).keys())

    files = list(iter_project_files(root))
    counts = Counter(path.suffix.lower() for path in files)
    scripts = [path for path in files if path.suffix.lower() in {".gd", ".cs"}]
    candidates: dict[str, list[str]] = {key: [] for key in CONCERN_TERMS}
    signals = {"direct_scene_changes": [], "user_writes": [], "global_group_queries": []}

    for path in scripts:
        rel = relative(root, path)
        lowered = rel.lower()
        for concern, terms in CONCERN_TERMS.items():
            if any(term in lowered for term in terms):
                candidates[concern].append(rel)
        text = read_text(path)
        if re.search(r"\b(change_scene_to_(?:file|packed)|reload_current_scene)\s*\(", text):
            signals["direct_scene_changes"].append(rel)
        if "user://" in text and re.search(r"\b(FileAccess|DirAccess)\b", text):
            signals["user_writes"].append(rel)
        if re.search(r"get_(?:first_)?node_in_group\s*\(", text):
            signals["global_group_queries"].append(rel)

    findings: list[dict[str, str]] = []
    if not main_scene:
        findings.append({"severity": "error", "code": "missing-main-scene", "message": "No application/run/main_scene is configured."})
    elif (resolved := res_to_path(root, main_scene)) is not None and not resolved.is_file():
        findings.append({"severity": "error", "code": "invalid-main-scene", "message": f"Configured main scene does not exist: {main_scene}"})

    for name, value in autoloads.items():
        resolved = res_to_path(root, value)
        if resolved is not None and not resolved.is_file():
            findings.append({"severity": "error", "code": "invalid-autoload", "message": f"Autoload {name} points to missing path: {value}"})

    if not autoloads:
        findings.append({"severity": "info", "code": "no-autoloads", "message": "No Autoloads are configured; this is valid if the project uses a root-scene composition."})
    if not input_actions:
        findings.append({"severity": "warning", "code": "no-input-actions", "message": "No project-defined Input Map actions were found."})

    addons = sorted({parts[1] for path in files if len((parts := path.relative_to(root).parts)) > 1 and parts[0] == "addons"})
    return {
        "project_root": str(root.resolve()),
        "project": {
            "name": unquote(app.get("config/name")),
            "config_version": re.search(r"^config_version=(\d+)", project_text, re.MULTILINE).group(1) if re.search(r"^config_version=(\d+)", project_text, re.MULTILINE) else None,
            "feature_tags": features,
            "renderer": unquote(config.get("rendering", {}).get("renderer/rendering_method")),
            "main_scene": main_scene,
        },
        "autoloads": autoloads,
        "input_actions": input_actions,
        "addons": addons,
        "file_counts": {"gdscript": counts[".gd"], "csharp": counts[".cs"], "scenes": counts[".tscn"], "resources": counts[".tres"]},
        "foundation_candidates": {key: sorted(value) for key, value in candidates.items()},
        "inspection_signals": {key: sorted(value) for key, value in signals.items()},
        "findings": findings,
    }


def markdown(report: dict[str, Any]) -> str:
    project = report["project"]
    lines = [
        f"# {project.get('name') or 'Godot project'} foundation audit",
        "",
        "## Project facts",
        f"- Root: `{report['project_root']}`",
        f"- Config version: `{project.get('config_version') or 'unresolved'}`",
        f"- Feature tags: {', '.join(f'`{x}`' for x in project['feature_tags']) or 'none found'}",
        f"- Renderer: `{project.get('renderer') or 'default/unresolved'}`",
        f"- Main scene: `{project.get('main_scene') or 'missing'}`",
        f"- Add-ons: {', '.join(f'`{x}`' for x in report['addons']) or 'none found'}",
        "",
        "## Configured authorities",
        "",
        "| Concern | Evidence |",
        "| --- | --- |",
        f"| Autoload | {', '.join(f'`{k}` → `{v}`' for k, v in report['autoloads'].items()) or 'none configured'} |",
        f"| Input Map | {', '.join(f'`{x}`' for x in report['input_actions']) or 'no project-defined actions'} |",
        f"| Main scene | `{project.get('main_scene') or 'missing'}` |",
        "",
        "## Foundation candidates",
    ]
    for concern, paths in report["foundation_candidates"].items():
        lines.append(f"- **{concern}:** {', '.join(f'`{p}`' for p in paths) or 'none by filename'}")
    lines.extend(["", "## Inspection signals"])
    for signal, paths in report["inspection_signals"].items():
        lines.append(f"- **{signal}:** {', '.join(f'`{p}`' for p in paths) or 'none'}")
    lines.extend(["", "## Findings"])
    if report["findings"]:
        for finding in report["findings"]:
            lines.append(f"- **{finding['severity']} / {finding['code']}:** {finding['message']}")
    else:
        lines.append("- No static project-setting failures found.")
    lines.extend(["", "## Required follow-up", "- Read each candidate before assigning authority.", "- Confirm the installed Godot executable version and run a headless startup check when available."])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = audit(args.project_root.resolve())
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    output = json.dumps(report, indent=2, ensure_ascii=False) + "\n" if args.format == "json" else markdown(report)
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

