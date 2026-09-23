# Tests: Agentic Operations (AOP-CON-* rules)

## Scope

Conformance rules per CR-ES-007 §23 + ADR-ES-007 §27 ;; 15 rules + 12 negative tests (per CR-ES-007 §24).

## Rules overview

| Rule | Description |
|---|---|
| AOP-CON-001 | Agentic Operations specialises Operations |
| AOP-CON-002 | Material agentic participation in operational behavior |
| AOP-CON-003 | Agentic Operations operates within defined authority |
| AOP-CON-004 | Operational behavior is governed by applicable policies |
| AOP-CON-005 | Agentic Operations is outcome-oriented |
| AOP-CON-006 | Agentic Operations may engage Agents |
| AOP-CON-007 | Agentic Operations may use Agentic Workflows |
| AOP-CON-008 | Agentic Operations may coordinate Processes |
| AOP-CON-009 | Human participation is permitted |
| AOP-CON-010 | Automation may coexist with Agentic Operations |
| AOP-CON-011 | Agentic Operations does not require AI |
| AOP-CON-012 | Agentic Operations does not imply autonomy |
| AOP-CON-013 | Agentic Operations is not Agentic Workflow |
| AOP-CON-014 | Agentic Operations is not Agentic Value Stream |
| AOP-CON-015 | Agentic Operations preserves grounding and provenance |

## Negative tests (per CR-ES-007 §24)

The following must fail validation:

- Agentic Operations is-a Agentic Workflow
- Agentic Operations is-a Agentic Value Stream
- Agentic Operations is-a Process
- Agentic Operations requires AI
- Agentic Operations implies Autonomous Operations
- Agentic Operations requires removal of human participation
- Operations containing an Agent automatically become Agentic Operations
- Agentic Operations = Agentic Workflow
- Agentic Operations = AIOps
- Agentic Operations = Automated Operations
- Agentic Operations establishes Autonomous Operations

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-007 §23 + §24 + ADR-ES-007 §27