# Tests: Agentic Value Stream (AVS-CON-* rules)

## Scope

Conformance rules per CR-ES-005 §21 + ADR-ES-005 §17 ;; 12 rules + 10 negative tests (per CR-ES-005 §22).

## Rules overview

| Rule | Description |
|------|-------------|
| AVS-CON-001 | Agentic Value Stream specialises Value Stream. |
| AVS-CON-002 | Agentic Value Stream retains stakeholder-value realisation semantics. |
| AVS-CON-003 | Agentic Value Stream retains initiating-condition semantics. |
| AVS-CON-004 | Agentic Value Stream retains realisation-boundary semantics. |
| AVS-CON-005 | An Agentic Value Stream identifies at least one material agentic characteristic. |
| AVS-CON-006 | Agentic participation is associated with delegated intent and bounded authority. |
| AVS-CON-007 | Agentic participation may apply to one or more stages ;; complete-stream agency not required. |
| AVS-CON-008 | Agentic Value Stream does not imply Autonomous Value Stream. |
| AVS-CON-009 | Agentic Value Stream does not require AI. |
| AVS-CON-010 | Agentic Value Stream does not redefine Process, Activity, Task, Workflow. |
| AVS-CON-011 | Agentic Value Stream preserves stakeholder value realisation as primary semantic purpose. |
| AVS-CON-012 | Agentic Value Stream instances carry appropriate grounding and provenance. |

## Negative tests

Per CR-ES-005 §22 ;; the following must fail semantic validation:

- AI is-a Agentic Value Stream
- Agentic Value Stream is-a AI System
- Agentic Value Stream is-a Autonomous Value Stream
- Agentic Value Stream requires AI
- Agentic Value Stream requires full autonomy
- Agentic Value Stream replaces Value Stream
- Agentic Value Stream is-a Process
- Agentic Value Stream is-a Workflow
- Agentic Value Stream establishes Agentic Workflow
- Agentic Value Stream establishes Agentic Operations

## Cross-references

- [Schema](./schema.md) ;; AVS-CON-001, AVS-CON-002 + negative tests
- [Identity](./identity.md)
- [Lifecycle](./lifecycle.md)
- [Relationships](./relationships.md) ;; AVS-CON-005 + AVS-CON-006
- [Boundaries](./boundaries.md) ;; AVS-CON-008..010
- [Provenance](./provenance.md) ;; AVS-CON-012
- [Grounding](./grounding.md)
- [Examples](./examples.md)

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)