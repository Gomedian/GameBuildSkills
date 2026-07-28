# Platformer Profile

Apply to 2D or 3D platformers. Resolve axis, physics, and camera conventions from the project.

## Movement authority

Model explicit movement sources:

- player locomotion;
- jump and air control;
- dash or special traversal;
- moving-platform contribution;
- knockback and forced movement;
- scripted movement, teleport, and respawn.

Define priority, composition, cancellation, and collision policy when sources overlap.

## Player states

Use the smallest set required by the game, commonly:

- grounded, rising, falling, landing;
- crouched, dashing, wall contact, ledge action;
- attacking, hurt, disabled, defeated.

For each state specify entry conditions, exit conditions, minimum duration, allowed input, velocity ownership, collision changes, and interrupt rules.

## Movement specification

Record:

- acceleration, deceleration, maximum speed;
- ground and air control;
- initial jump velocity and gravity policy;
- variable jump height;
- coyote time and input buffering;
- slope, step, ceiling, ledge, and one-way platform behavior;
- moving-platform inheritance;
- dash and knockback collision response;
- respawn placement and state reset.

Treat forgiving input features as explicit timers with testable boundaries.

## Collision invariants

- No movement source may finish inside blocking geometry.
- Ceiling contact must end upward travel consistently.
- Grounding must be stable at edges and slopes without accepting invalid walls.
- One-way platforms need clear approach, drop-through, and re-entry rules.
- Moving platforms must define attachment, inherited velocity, detach, teleport, and unload behavior.
- Checkpoints must validate a safe respawn volume.

## Camera and readability

Define follow target, look-ahead, dead zones, vertical fall policy, room bounds, boss locks, transition blending, shake priority, and reduced-motion behavior. Camera modifiers must not change gameplay authority.

## Platform combat

Specify startup, active, recovery, facing lock, aerial/ground legality, movement influence, hit stop, knockback, invulnerability, and interruption. Test attacks at platform edges, ceilings, slopes, moving platforms, and during landing.

## Deterministic fixtures

Cover:

- coyote and buffered jump boundaries;
- short and full jump;
- ceiling contact;
- slope and corner behavior;
- one-way platform approach/drop-through;
- moving-platform attach and detach;
- dash or knockback into walls;
- checkpoint retry;
- low and high frame-rate behavior;
- pause during traversal or combat.
