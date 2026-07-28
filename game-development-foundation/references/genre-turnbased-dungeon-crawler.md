# Roguelike Turn-Based Dungeon Crawler Profile

Apply to grid or node-based dungeon exploration where simulation advances through discrete actions.

## Turn authority

Use an explicit resolution pipeline:

1. Receive a command.
2. Validate actor, target, cost, and legality.
3. Commit the command or reject it according to the failure policy.
4. Resolve movement, combat, interaction, and triggered consequences.
5. Resolve enemy or initiative actions.
6. Process status durations, hazards, deaths, rewards, and objectives in a defined order.
7. Publish presentation events.
8. Persist allowed state and accept the next command.

Animation may delay presentation but must not change the resolved simulation result.

## Command contract

Represent actions such as move, attack, skill, item, equip, interact, wait, open, ascend, descend, or flee as commands.

Each command defines:

- actor and stable action ID;
- target entity, tile, direction, or object;
- preconditions and legality;
- action/energy/resource cost;
- RNG calls and ordering;
- success and failure outcomes;
- whether failure consumes a turn;
- emitted combat log and presentation events.

Prevent duplicate dispatch and re-entry while resolution is active.

## Determinism

Own RNG through an explicit seeded service. Record seed and, when required for save continuity, RNG state or deterministic event position.

The same initial state and command sequence must produce the same logical results. Keep cosmetic randomness separate from simulation randomness.

## Dungeon generation

Define:

- seed and generation version;
- room/corridor or node graph;
- start, exit, required path, and optional branches;
- doors, keys, hazards, enemies, rewards, and resource budgets;
- reachability and occupancy constraints;
- retry or fallback behavior when generation fails.

Validate that required objectives and exits are reachable, keys do not depend circularly on their own gates, actors do not overlap invalid tiles, and difficulty budgets remain bounded.

## Enemy decisions

Separate observation, intent selection, and command execution. Enemy AI should use the same legal command boundary as the player where practical.

Define behavior for:

- target visibility and memory;
- range, path, and occupied tiles;
- attack commitment and cooldown;
- hazards and friendly blocking;
- retreat, guard, search, and idle;
- path failure and unreachable targets.

## Inventory and ownership

Treat pickup, stack, equip, swap, consume, drop, sell, and reward as atomic transfers. Validate the entire destination state before committing. Item identity may disappear only through an explicit consumption or destruction outcome.

## Persistence

Separate:

| Persistent profile | Current run |
| --- | --- |
| unlocks, codex, achievements, settings, meta currency | seed, generation version, floor, actor states, inventory, map knowledge, RNG continuity |

Define save points, quit-resume policy, death cleanup, victory transfer, and schema migration. Partial writes must not produce mixed profile/run state.

## Validation

Cover:

- identical seed and command replay;
- invalid command and turn-cost policy;
- status-effect ordering and expiry;
- simultaneous death/victory;
- duplicate command prevention;
- reachable exit and objectives;
- door/key dependency validity;
- inventory conservation;
- floor transition;
- save/quit/resume;
- death and meta-progression transfer;
- old generation and save versions.
