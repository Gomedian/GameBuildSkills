# Unity Adaptation

Use this reference only for Unity projects.

## Inspect first

Confirm the Unity version and actual project choices before recommending APIs:

- Input System or legacy input;
- 2D or 3D physics and fixed timestep;
- Animator and animation-event responsibilities;
- ScriptableObject, MonoBehaviour, ECS, or custom data patterns;
- scene loading and additive composition;
- Addressables, Resources, direct references, or custom asset loading;
- prefab variants, pooling, and domain/scene reload behavior;
- EditMode and PlayMode test conventions.

Do not assume a package is installed.

## Recommended responsibility split

- ScriptableObject or serializable definition: authored facts only.
- Runtime component/service: mutable state and authoritative rules.
- View/adapter component: Animator, SpriteRenderer/MeshRenderer, VFX, audio, UI.
- Save DTO: versioned persistent representation, separate from live components.
- Editor tooling: setup, validation, migration, and debug fixtures.

Avoid mutating shared ScriptableObject assets during play unless the asset is explicitly runtime-owned.

## Physics and timing

- Choose Update, FixedUpdate, coroutines, animation events, or a custom clock based on authority, not convenience.
- Keep physics writes consistent with the selected Rigidbody model.
- Treat teleport, dash, knockback, root motion, and moving platforms as explicit movement sources.
- Validate destination occupancy and collision along forced movement.
- Define pause and time-scale behavior for timers and effects.
- Do not use transform appearance as proof that physics contact succeeded.

## Animation

Animator state expresses runtime state; it should not become a second gameplay state machine.

Animation events may notify an already-defined phase, but runtime code must validate that the action identity and state are still current. Cancellation must invalidate delayed animation callbacks.

## Prefabs and pooling

On acquisition, restore all required child objects and transient components. On release, stop effects and unregister callbacks. Test the same instance on first, second, and interrupted use.

Use validation tooling for required serialized references. Missing required references should fail clearly rather than creating silently degraded behavior.

## Scenes and serialized assets

Separate code changes from required scene, prefab, Animator, layer, tag, physics matrix, and data-asset setup. A code-complete feature is not integration-complete until these assignments are verified.

Preserve unrelated serialized changes. Avoid broad scene rewrites when a focused prefab or data change is sufficient.

## Tests

- Put deterministic rule tests in EditMode when they do not require scene timing.
- Use PlayMode for physics, Animator, scene, lifecycle, and pooled-instance behavior.
- Add fixtures that force phase, position, state, inventory, seed, or checkpoint.
- Account for Unity lifecycle methods that tests may not invoke automatically.
