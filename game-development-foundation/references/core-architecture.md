# Core Architecture

Use this reference for architecture, implementation, diagnosis, and review across supported genres.

## Project discovery

Resolve these questions from source before choosing a solution:

| Concern | Evidence to locate |
| --- | --- |
| Authority | Component/system that owns the final rule |
| Data | Definitions, IDs, serialized assets, configuration |
| State | Runtime state machine, timers, commands, cooldowns |
| Presentation | Animation, VFX, audio, UI, camera adapters |
| Lifecycle | Spawn, enable, disable, pool return, unload, retry |
| Persistence | Save schema, checkpoints, run state, migration |
| Integration | Scene, prefab, entity, editor, build setup |
| Validation | Unit, integration, fixture, debug, play route |

## Feature contract

For every feature define:

1. Player-facing goal.
2. Preconditions and legal inputs.
3. Authoritative owner.
4. Data and stable identifiers.
5. Runtime states and transition guards.
6. Success, failure, cancel, timeout, and retry outcomes.
7. Presentation events downstream of outcomes.
8. Lifecycle and reset guarantees.
9. Save/load behavior and migration impact.
10. Debug controls and deterministic tests.
11. Editor or content-author setup.
12. Non-goals and compatibility constraints.

## State and outcome rules

- Give each action a stable identity for its full logical lifetime.
- Apply a contact, reward, transfer, or command once per valid identity pair.
- Separate expected gameplay failure from system failure.
- Do not report cancellation as successful completion.
- Define who consumes recovery and who releases locks.
- Keep transitions explicit enough to test without waiting through a full playthrough.
- Use fixed seeds or injectable clocks where nondeterminism would prevent reproduction.

## Content and runtime separation

Authored data should contain stable facts. Runtime state should contain mutable progress. UI and animation should read resolved state rather than duplicate rules.

Examples:

- Item definitions do not own current quantities.
- Attack animations do not own health subtraction.
- Room decoration does not define navigation connectivity.
- A HUD slot does not create inventory capacity.
- A particle effect does not decide whether an attack hit.

## Lifecycle safety

Every reusable or asynchronous object needs a reset contract:

- cancel timers, tasks, coroutines, callbacks, and subscriptions;
- clear previous targets, action IDs, cached paths, trails, particles, and transient materials;
- restore required children, colliders, renderers, and animator state;
- make repeated cleanup safe;
- prevent delayed results from a previous use affecting the next use.

## Testing layers

1. **Pure rules:** state transitions, costs, timing boundaries, generation validity.
2. **Integration:** collision, navigation, save/load, prefab/entity setup, event wiring.
3. **Deterministic fixtures:** fixed phase, position, inventory, room, seed, or turn.
4. **Representative play:** intended camera distance, controls, frame rate, readability.
5. **Regression:** cancellation, repeated use, reload, retry, and old save data.

Test outcomes and invariants, not only final transforms or screenshots.

## Review standard

A review should report:

- confirmed execution path;
- contract violations and their concrete consequence;
- severity and reproducibility;
- smallest safe correction;
- tests missing or invalid;
- required content/editor changes;
- intentionally accepted limitations.
