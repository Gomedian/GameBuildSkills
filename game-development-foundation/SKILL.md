---
name: game-development-foundation
description: Audit, plan, design, implement, diagnose, review, or test reusable game foundations and gameplay systems for Unity or Godot projects, including platformers, metroidvanias, and roguelike turn-based dungeon crawlers. Use for project bootstrap, scene flow, UI navigation, popups, pause, input contexts, settings, saves, audio, content registries, movement, combat, inventory, progression, procedural dungeons, debugging, implementation instructions, and branch reviews. Inspect the real project before prescribing architecture, then load only the matching foundation, genre, and engine references.
---

# Game Development Foundation

Build from the project's actual contracts, then apply the narrowest matching genre rules.

## Start with evidence

Before proposing code or scene changes, inspect the relevant project sources:

- engine, version, rendering mode, target platforms, and input system;
- scenes or world composition, data definitions, runtime state, presentation, persistence, and tests;
- authoritative owners of movement, time, combat contact, inventory, spawning, and save state;
- prefab/entity lifecycle, pooling, reset behavior, and debug surfaces;
- existing conventions, local instructions, documentation, and uncommitted work.

Do not invent class names, paths, APIs, serialized fields, or scene assignments. Clearly separate confirmed facts, inferences, and recommendations.

## Select references

Read only what the task needs:

- Always use [core-architecture.md](references/core-architecture.md) for architectural or implementation work.
- Read [foundation-modules.md](references/foundation-modules.md) when auditing, planning, creating, or reviewing reusable project foundations.
- Read [engine-unity.md](references/engine-unity.md) for Unity projects.
- Read [engine-godot.md](references/engine-godot.md) for Godot projects.
- Read [genre-platformer.md](references/genre-platformer.md) for platformer movement, collision, cameras, checkpoints, or platform combat.
- For metroidvania work, read both [genre-platformer.md](references/genre-platformer.md) and [genre-metroidvania.md](references/genre-metroidvania.md).
- Read [genre-turnbased-dungeon-crawler.md](references/genre-turnbased-dungeon-crawler.md) for turn authority, command resolution, seeded generation, grid AI, or run persistence.
- Use [templates.md](references/templates.md) when producing a design contract, implementation instruction, review report, or test plan.

If the game crosses profiles, state which rules apply to each subsystem. Do not silently blend incompatible time, movement, or persistence models.

## Workflow

1. Classify the request as project audit, foundation planning, implementation, diagnosis, or review.
2. Restate the player-facing goal and the invariant that must remain true.
3. Trace the current runtime path from input or trigger to final state and presentation.
4. Identify the smallest authoritative owner that can enforce the rule.
5. Define data, runtime states, transitions, failure paths, reset behavior, and persistence.
6. For foundation work, classify every requested module as reuse, configure, integrate, generate, replace, or defer.
7. Define engine/scene/editor integration separately from runtime code.
8. Specify deterministic tests and a short real-play verification route.
9. Implement only when requested. Preserve unrelated work.
10. Review the resulting diff against the contract, not merely compilation success.

## System boundaries

Prefer explicit separation:

- **Definition:** stable authored facts and identifiers.
- **Runtime:** current state, timers, commands, outcomes, and authoritative rules.
- **Presentation:** animation, VFX, audio, camera, and UI driven by runtime outcomes.
- **Persistence:** save schema, migration, checkpoints, run state, and unlock state.
- **Debug:** state forcing, fixed seeds, event logs, and reproducible fixtures.
- **Tests:** pure rules first, integration boundaries second, representative play last.

Animation and rendered pose may communicate a result but must not be the sole authority for damage, ownership, progression, or turn completion.

## Change discipline

- Prefer extending an existing contract over creating a parallel source of truth.
- Make transfers and ownership changes atomic.
- Make cleanup and pool return idempotent.
- Treat missing required bounds, references, or destinations as explicit failures.
- Define cancellation for death, unload, retry, pause, state interruption, and scene transition.
- Avoid hardcoded genre rules in generic infrastructure; keep them in definitions or profile-specific policy.
- When requirements conflict, surface the conflict before implementation.

## Completion standard

A task is complete only when:

- the player-facing behavior matches the requested rule;
- data, runtime, presentation, and persistence agree;
- scene/prefab/editor setup is documented where required;
- failure, cancel, retry, and reuse paths are covered;
- deterministic tests or fixtures cover important boundaries;
- real play verifies timing, readability, controls, and performance;
- remaining risks and intentionally excluded work are stated.
