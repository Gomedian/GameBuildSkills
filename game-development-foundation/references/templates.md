# Output Templates

Use the narrowest template matching the request. Replace every placeholder with evidence or mark it unresolved.

## Project foundation audit

```markdown
# <Project> foundation audit

## Project facts
- Engine/version:
- Language/toolchain:
- Targets:
- Entry point:
- Existing services/add-ons/packages:

## Current authorities
| Concern | Owner | Evidence | Confidence |
| --- | --- | --- | --- |

## Requested capabilities
## Conflicts and duplicate ownership
## Missing evidence
## Recommended next inspection
```

## Foundation installation plan

```markdown
# <Project> foundation plan

## Goal and non-goals
## Confirmed existing foundation
## Module decisions
| Module | Reuse/configure/integrate/generate/replace/defer | Reason | Dependencies |
| --- | --- | --- | --- |

## Startup and dependency order
## Public contracts and state ownership
## Files and engine/editor integration
## Migration and compatibility
## Validators and tests
## Real-play verification
## Remaining user decisions
```

## System contract

```markdown
# <System>

## Goal
<Player-facing result>

## Confirmed current structure
- <Source path or component>: <responsibility>

## Invariants
- <Rule that must always remain true>

## Data
- <Definition, ID, serialized fields>

## Runtime
- States:
- Transitions:
- Authority:
- Timing or turn policy:

## Outcomes
- Success:
- Expected failure:
- System failure:
- Cancel/timeout:
- Retry/reset:

## Presentation
- Animation:
- VFX/audio:
- UI/camera:

## Persistence
- Save scope:
- Migration:

## Integration
- Code:
- Scene/prefab/entity:
- Data/editor:

## Validation
- Deterministic tests:
- Integration tests:
- Play route:

## Non-goals
- <Explicit exclusions>
```

## Implementation instruction

```markdown
# <Task> implementation instruction

## Objective
## Evidence from the current project
## Files and systems in scope
## Required behavior
## Data and API changes
## Runtime flow
## Failure, cancellation, and reset
## Genre-specific constraints
## Engine/editor setup
## Tests
## Acceptance criteria
## Do not change
```

Instructions must identify the authoritative owner and exact setup work. Do not prescribe fabricated paths or names.

## Review report

```markdown
# <Branch or change> review

## Verdict
<Accept / accept with fixes / needs revision>

## Confirmed execution path
## Findings
### <Severity> — <Finding>
- Evidence:
- Consequence:
- Reproduction:
- Smallest safe correction:

## Test assessment
## Scene/content integration
## Accepted limitations
## Next action
```

Prioritize runtime correctness, data loss, progression blocks, soft locks, duplicate rewards, invalid saves, collision failures, and lifecycle leaks over style.

## Test plan

```markdown
# <Feature> test plan

## Invariants
## Pure rule tests
## Integration tests
## Deterministic fixtures
## Failure and cancellation
## Reuse/retry/save-load
## Representative play route
## Instrumentation and expected logs
## Pass criteria
```
