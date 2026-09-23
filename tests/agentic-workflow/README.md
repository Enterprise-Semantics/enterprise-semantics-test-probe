# Tests: Agentic Workflow (AWF-CON-* rules)

## Scope

Conformance rules per CR-ES-006 §28 + ADR-ES-006 §23 ;; 14 rules + 10 negative tests (per CR-ES-006 §29).

## Rules overview

| Rule | Description |
|---|---|
| AWF-CON-001 | Agentic Workflow specialises Workflow |
| AWF-CON-002 | Agentic Workflow retains Workflow semantics |
| AWF-CON-003 | Agentic Workflow materially incorporates agentic behavior into coordination or execution |
| AWF-CON-004 | Agentic Workflow operates within defined authority |
| AWF-CON-005 | Agentic Workflow has an identifiable intent or execution objective |
| AWF-CON-006 | Agentic Workflow may coordinate Activities and Tasks |
| AWF-CON-007 | Agentic Workflow may engage Agents |
| AWF-CON-008 | Human intervention is permitted |
| AWF-CON-009 | Agentic Workflow does not require AI |
| AWF-CON-010 | Agentic Workflow does not imply autonomy |
| AWF-CON-011 | Agentic Workflow is not a Process |
| AWF-CON-012 | Agentic Workflow is not a Value Stream |
| AWF-CON-013 | Agentic Workflow is not an Agent |
| AWF-CON-014 | Agentic Workflow preserves grounding and provenance |

## Negative tests (per CR-ES-006 §29)

The following must fail validation:

- Agentic Workflow is-a Process
- Agentic Workflow is-a Value Stream
- Agentic Workflow is-a Agent
- Agentic Workflow requires AI
- AI Workflow is-a Agentic Workflow
- Agentic Workflow implies Autonomous Workflow
- Agentic Workflow requires removal of human intervention
- Agentic Workflow establishes Agentic Operations
- Agentic Workflow establishes Autonomous Operations
- Agentic Workflow = Workflow merely containing an Agent

The last test is important because it protects the
material-participation criterion (per ADR-ES-006 §10 + §24.5).

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-006 §28 + §29 + ADR-ES-006 §23