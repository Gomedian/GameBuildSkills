# Godot Adaptation

Use this reference only for Godot projects. Confirm the exact major and minor version before choosing APIs or file formats.

## Inspect first

Confirm these project facts from `project.godot`, scenes, scripts, and add-ons:

- Godot version, renderer, target platforms, and main scene;
- GDScript, C#, GDExtension, or mixed-language policy;
- existing Autoloads and their initialization dependencies;
- Input Map actions and device assumptions;
- scene ownership, inherited scenes, unique node names, and groups;
- Resource and PackedScene loading strategy;
- pause modes, process modes, physics tick, and time-scale rules;
- save paths, schema versions, serialization format, and migration behavior;
- installed add-ons, editor plugins, tests, and command-line validation support.

Do not assume a plugin, test framework, or C# toolchain is installed. Do not hand-edit generated import metadata.

## Recommended responsibility split

- **Resource:** authored definitions, stable IDs, configuration, and presentation references.
- **RefCounted or plain script object:** rules and mutable state that do not need the SceneTree.
- **Node:** lifecycle, engine callbacks, scene integration, and orchestration.
- **Scene:** reusable presentation and composition boundary.
- **Autoload:** only truly process-wide services with an explicit startup contract.
- **Save DTO:** versioned persistent representation, separate from live Nodes and Resources.
- **EditorPlugin or `@tool` validator:** authoring support, setup checks, migrations, and content validation.

Avoid turning every domain system into an Autoload. Inventory, combat, achievements, and progression rules should remain project-owned state or services unless they genuinely span all scenes and sessions.

## Scene and service flow

- Give scene transitions one authority. Prevent concurrent transition requests and define failure recovery.
- Keep loading presentation downstream of transition state; a loading screen must not decide which scene is authoritative.
- Define whether persistent UI is an Autoload-owned CanvasLayer, part of a root scene, or recreated per gameplay scene.
- Connect and disconnect signals at clear ownership boundaries. Prefer one owner for each connection lifetime.
- Treat `queue_free()` as deferred. Invalidate old action identities and callbacks before replacement Nodes can become active.
- Use groups for discovery only when membership is an intentional contract; do not use global group searches as hidden dependency injection.

## Pause and input

- Separate game pause from modal UI input capture.
- Define `process_mode` for gameplay, transition, popup, pause-menu, and debug Nodes.
- Centralize Input Map action names and validate required actions.
- Route input by context so a popup, rebinding screen, or transition can block gameplay without duplicating pause state.
- Test controller focus recovery after scene changes and popup closure.

## Resources and persistence

- Treat imported or authored Resources as definitions, not mutable save state.
- Duplicate a Resource before mutating it when shared ownership is possible.
- Use stable content IDs rather than resource paths or localized text as persistent identity.
- Write saves under `user://` through one coordinated commit boundary.
- Include a schema version, validate before replacing the last known-good save, and make migrations explicit and ordered.
- Separate settings persistence from game progress when their lifecycle or recovery policy differs.

## Lifecycle safety

- Disconnect external signals, cancel timers and tweens, and invalidate async continuations when a Node exits its owning state.
- Reset pooled Nodes before reparenting or reuse, including visibility, collision, process mode, particles, animation, targets, and transient Resources.
- Verify behavior after first use, second use, interruption, scene transition, and pause.
- Avoid `await` chains that resume into freed or superseded Nodes without validity and action-identity checks.

## Validation and tests

- Run a headless project parse or startup check using the project's Godot executable when available.
- Prefer pure rule tests that do not require the SceneTree.
- Use minimal scene fixtures for signal wiring, pause, transition, physics, and lifecycle behavior.
- Add an editor or command-line validator for Autoload names, main scene, Input Map actions, stable IDs, required Node paths, and save migrations.
- Verify the actual startup scene and at least one transition, popup, pause cycle, save/reload cycle, and failure path.
