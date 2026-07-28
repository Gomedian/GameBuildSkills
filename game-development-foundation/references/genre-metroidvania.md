# Metroidvania Profile

Load the Platformer Profile first when traversal is platform-based. This profile adds interconnected-world, ability-gate, backtracking, map, and persistent-state rules.

## World graph

Represent world connectivity with stable identifiers rather than inferring it from decoration.

For each room or region define:

- stable room ID;
- entry and exit IDs with direction and destination;
- required abilities, keys, events, or world states;
- checkpoint and fast-travel anchors;
- encounter, reward, and reset policy;
- map discovery and display state;
- loading, unloading, and transition behavior.

Validate reciprocal links where intended and deliberate one-way links where required.

## Ability gates

For each gate define:

- required capability or predicate;
- player-visible hint before acquisition;
- entry side and reverse access;
- whether it persists open;
- intended and unintended alternate solutions;
- sequence-break policy;
- failure and return path.

The required ability must be obtainable through a reachable path that does not already require that ability.

## Progression and persistence

Separate:

- permanent abilities and upgrades;
- keys, event flags, doors, levers, bosses, and unique rewards;
- discovered rooms and map annotations;
- respawning enemies and non-respawning world changes;
- checkpoints and fast-travel state;
- run-local resources from save-global progress.

Use stable IDs and versioned save data. Never persist direct scene-object references.

## Backtracking quality

When a new ability is acquired, identify:

- newly reachable critical path;
- optional rewards and shortcuts;
- return route;
- navigation cues and map updates;
- old traversal that becomes faster or gains new meaning.

Avoid long mandatory return travel without new decisions, shortcuts, or changed encounters.

## Sequence breaking

Classify bypasses:

- intended alternate route;
- advanced technique accepted by design;
- harmless shortcut;
- progression-breaking exploit.

Do not automatically block every bypass. Protect only invariants required to keep the world completable and save data valid.

## Validation

Build automated or tool-assisted checks for:

- reachability at each expected ability set;
- unobtainable keys or circular gates;
- room-link and spawn-anchor validity;
- save/load after door, boss, reward, and checkpoint changes;
- death and retry across room transitions;
- fast travel with partial progression;
- ability removal or temporary disable;
- duplicate unique rewards;
- soft locks and missing return paths.
