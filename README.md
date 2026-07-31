# GameBuildSkills

Reusable agent skills for planning, implementing, reviewing, and testing game projects.

## Skills

### [Game Development Foundation](game-development-foundation/SKILL.md)

An engine-aware project foundation and gameplay-system workflow with conditional engine and genre profiles:

- Godot 4 project auditing and foundation planning
- Unity project auditing and adaptation
- 2D/3D platformer
- metroidvania
- roguelike turn-based dungeon crawler

The skill inspects the current project before proposing architecture. For foundation work, it classifies each capability as reuse, configure, integrate, generate, replace, or defer. It produces project audits, selective foundation plans, implementation-ready system contracts, change instructions, validation plans, and review reports without assuming one repository structure.

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
```

Engine, foundation, and genre documents are conditional references. Load only the profiles relevant to the current project.

## Usage

Ask the agent to audit or establish a project foundation, or to design, implement, diagnose, review, or test a game feature. State the engine and genre when known. If either materially changes the solution, the skill must inspect the project or ask before committing to an architecture.

## License

MIT
