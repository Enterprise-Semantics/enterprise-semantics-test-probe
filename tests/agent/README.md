# Tests: Agentic (AG-CON-* rules)

## Scope

Conformance rules per CR-ES-004 §26, 13 rules + 5 negative tests (per §27).

## Rules overview

| Rule | Description |
|------|-------------|
| AG-CON-001 | Agent must have a definition. |
| AG-CON-002 | Agentic must have a definition. |
| AG-CON-003 | Agentic must identify its semantic characteristics. |
| AG-CON-004 | Agentic must not be defined as AI. |
| AG-CON-005 | Agentic must not be defined as Automation. |
| AG-CON-006 | Agentic must not be defined as Autonomous. |
| AG-CON-007 | Agent must have an authority relationship when modeled as acting agentically. |
| AG-CON-008 | Agentic execution must have an intent or objective. |
| AG-CON-009 | Agentic execution must support action selection. |
| AG-CON-010 | Agentic execution must be outcome-oriented. |
| AG-CON-011 | Agentic Value Stream must not be canonicalized by this CR. |
| AG-CON-012 | Agentic Workflow must not be canonicalized by this CR. |
| AG-CON-013 | Autonomous concepts must not be canonicalized by this CR. |

## Negative tests

Per CR-ES-004 §27, the following must fail semantic validation:

- `AI is-a Agent`, when intended as a universal identity
- `Agentic is-a Autonomous`
- `Automation is-a Agentic`
- `Agentic Value Stream is established by CR-ES-004`
- `Agentic Workflow is established by CR-ES-004`

## Cross-references

- [Schema](./schema.md), AG-CON-001 + AG-CON-002 (definitions)
- [Lifecycle](./lifecycle.md), AG-CON-011..013
- [Relationships](./relationships.md), AG-CON-007..010
- [Boundaries](./boundaries.md), AG-CON-003..006
- [Provenance](./provenance.md)
- [Grounding](./grounding.md)
- [Examples](./examples.md)

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)