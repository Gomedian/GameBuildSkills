# GameBuildSkills

Reusable agent skills for planning, implementing, reviewing, and testing game projects.

## Skills

### [Game Development Foundation](game-development-foundation/SKILL.md)

An engine-aware foundation workflow with conditional genre profiles:

- 2D/3D platformer
- metroidvania
- roguelike turn-based dungeon crawler
- optional Unity adaptation

The skill inspects the current project before proposing architecture. It produces implementation-ready system contracts, change instructions, validation plans, and review reports without assuming one repository structure.

## Structure

```text
game-development-foundation/
  SKILL.md
  agents/openai.yaml
  references/
    core-architecture.md
    engine-unity.md
    genre-platformer.md
    genre-metroidvania.md
    genre-turnbased-dungeon-crawler.md
    templates.md
```

Each genre is a conditional reference. Load only the profile relevant to the current project.

## Usage

Ask the agent to design, implement, diagnose, review, or test a game feature. State the genre when it is known. If the genre or engine materially changes the solution, the skill must inspect the project or ask before committing to an architecture.

## License

MIT
