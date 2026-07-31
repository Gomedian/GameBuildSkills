# Foundation Modules

Use this reference when the task concerns a reusable project foundation rather than a single gameplay feature.

## Audit before selecting modules

Build an evidence table from the project before proposing a foundation:

| Concern | Confirm | Typical conflict |
| --- | --- | --- |
| Startup | entry scene, bootstrap order, service dependencies | multiple boot paths |
| Scene flow | transition authority, loading UI, failure recovery | direct scene changes from many callers |
| UI navigation | screen stack, modal layer, focus, back action | panels owning game state |
| Input | action registry, device policy, context routing | gameplay input leaking through UI |
| Persistence | schema, commit boundary, migration, recovery | several independent writers |
| Settings | ownership, apply timing, defaults | settings mixed with progress |
| Audio | buses/channels, BGM policy, persistence | scene-local managers competing |
| Content identity | stable IDs, registry, localization keys | paths or display text used as IDs |
| Diagnostics | logs, validators, forced states, fixtures | setup failures discovered only in play |

Record confirmed owners and collisions. Do not recommend a replacement merely because the existing naming or style differs.

## Module disposition

Assign one disposition to every requested capability:

- **Reuse:** existing owner already satisfies the contract.
- **Configure:** engine or installed package supports it; only project settings or content setup is needed.
- **Integrate:** existing components are adequate but require an adapter or explicit wiring.
- **Generate:** no suitable owner exists; create a focused module.
- **Replace:** the current owner violates a critical invariant and cannot be adapted safely.
- **Defer:** policy or product requirements are not settled enough to build the module.

Explain evidence, dependency impact, migration risk, and validation for each choice.

## Foundation tiers

### Tier 0: required startup integrity

- bootstrap and initialization order;
- scene flow and transition lock;
- error reporting and setup validation;
- stable project configuration ownership.

### Tier 1: common player shell

- screen navigation and modal popup layer;
- pause and input contexts;
- settings and settings persistence;
- audio routing and BGM policy;
- localization integration when the product requires it.

### Tier 2: persistent game foundation

- versioned save coordinator and migrations;
- stable content ID registry;
- run/session result commit boundary;
- progress and unlock state.

### Tier 3: product-dependent domains

- currency and transactions;
- inventory and equipment;
- achievements and statistics;
- notifications and new-content markers;
- pooling and high-frequency object lifecycle.

Do not generate Tier 3 merely because many games contain it. Require concrete game rules first.

## Cross-module invariants

- One authoritative owner per mutable state.
- UI observes state and submits intent; it does not create capacity, currency, unlocks, or save truth.
- Stable content IDs are separate from localization and presentation keys.
- Purchases and rewards commit atomically or fail without partial mutation.
- Save writes pass through one coordinator and preserve a recoverable last known-good state.
- Scene changes, retry, and quit define whether pending run results commit or roll back.
- Global services expose narrow contracts and explicit startup dependencies.
- Missing required setup fails visibly and is covered by a validator.

## Planning order

1. List existing authorities and reusable contracts.
2. Identify requested player-facing capabilities.
3. Assign module dispositions.
4. Draw dependency order and startup order.
5. Define data ownership and public contracts before concrete classes or Nodes.
6. Separate code generation from scene, editor, and project-setting changes.
7. Define migration and compatibility for every replaced owner.
8. Define automated validation and a minimal real-play route.

Prefer the smallest coherent installation. A project foundation is successful when it removes ambiguous ownership and repeated setup, not when it contains the largest module count.
