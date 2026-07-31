# GameBuildSkills

Reusable agent skills and deterministic tools for auditing, planning, implementing, reviewing, and testing game projects.

## Skills

### [Game Development Foundation](game-development-foundation/SKILL.md)

An engine-aware project foundation and gameplay-system workflow with conditional engine and genre profiles:

- Godot 4 project auditing and foundation planning
- Unity project auditing and adaptation
- 2D/3D platformer
- metroidvania
- roguelike turn-based dungeon crawler

The skill inspects the current project before proposing architecture. For foundation work, it classifies each capability as reuse, configure, integrate, generate, replace, or defer. It produces project audits, selective foundation plans, implementation-ready system contracts, change instructions, validation plans, and review reports without assuming one repository structure.

### [Godot Project Auditor](godot-project-auditor/SKILL.md)

A read-only Godot 4 project auditor that:

- parses `project.godot` without requiring the Godot editor;
- inventories the main scene, Autoloads, Input Map, add-ons, scripts, scenes, and resources;
- locates candidate owners for scene flow, UI, input, save, settings, audio, and content registries;
- reports invalid local main-scene and Autoload paths;
- identifies source locations that need manual inspection for direct scene changes, `user://` writes, and global group queries;
- emits Markdown for review or JSON for later builder and validator tools.

Run it directly with:

```bash
python3 godot-project-auditor/scripts/audit_godot_project.py /path/to/godot-project
```

## Structure

```text
game-development-foundation/
  SKILL.md
  agents/openai.yaml
  references/
    core-architecture.md
    foundation-modules.md
    engine-godot.md
    engine-unity.md
    genre-platformer.md
    genre-metroidvania.md
    genre-turnbased-dungeon-crawler.md
    templates.md

godot-project-auditor/
  SKILL.md
  agents/openai.yaml
  scripts/
    audit_godot_project.py

tests/
  test_godot_project_auditor.py
```

Engine, foundation, and genre documents are conditional references. Load only the profiles relevant to the current project.

## Usage

Ask the agent to audit or establish a project foundation, or to design, implement, diagnose, review, or test a game feature. State the engine and genre when known. If either materially changes the solution, the skill must inspect the project or ask before committing to an architecture.

## License

MIT
