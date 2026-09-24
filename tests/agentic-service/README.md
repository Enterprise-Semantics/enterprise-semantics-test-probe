# Agentic Service Conformance Tests

**Filing:** VS-D2a of CR-ES-014 ; Agentic Service conformance tests
**Ratified by:** ADR-ES-014
**Implemented by:** CR-ES-014
**Authored by:** Emmanuel A. Otchere (cardinal author rule, 2026-09-24)

## Purpose

This directory contains conformance tests for the Agentic Service semantic specialization established by ADR-ES-014 + CR-ES-014.

The tests verify:

1. The Agentic Service concept is canonicalized as a specialization of the universal Service concept.
2. Material agentic behavior is required, NOT mere use of AI/automation/Agent.
3. The Agentic Materiality rule is enforced.
4. Agentic Service operates within bounded Authority, Policy, Service Contract, Governance.
5. Human participation remains valid (in-the-loop, on-the-loop, over-the-loop).
6. AI and Automation are NOT necessary/sufficient conditions for Agentic Service.
7. Forbidden type inheritance (Agentic Service -> Agent, -> Capability, -> Agentic Capability, -> Agentic Workflow, -> Agentic Operations, -> Agentic Value Stream, -> Autonomous Service) is detected and rejected.
8. The Agentic/Autonomous orthogonality at the service boundary is preserved.
9. Provenance and grounding (ADR-ES-002, ADR-ES-003, ADR-ES-004, ADR-ES-005, ADR-ES-006, ADR-ES-007, ADR-ES-012, ADR-ES-014, CR-ES-014) is complete.

## Test Index

### Positive tests (19)

The positive tests verify that Agentic Service exhibits the required semantic properties.

- ASVC-CON-001 ; Agentic Service specializes Service
- ASVC-CON-002 ; Agentic Service retains Service semantics
- ASVC-CON-003 ; Agentic Service has material agentic realization
- ASVC-CON-004 ; Agentic Service may interpret delegated intent
- ASVC-CON-005 ; Agentic Service may interpret contextual conditions
- ASVC-CON-006 ; Agentic Service may dynamically select actions
- ASVC-CON-007 ; Agentic Service may coordinate actions
- ASVC-CON-008 ; Agentic Service may adapt service behavior
- ASVC-CON-009 ; Agentic Service operates within defined authority
- ASVC-CON-010 ; Agentic Service may be governed by policy
- ASVC-CON-011 ; Agentic Service may engage an Agent
- ASVC-CON-012 ; Agentic Service may use Agentic Workflow
- ASVC-CON-013 ; Human participation is permitted
- ASVC-CON-014 ; AI is not required
- ASVC-CON-015 ; Automation is not sufficient
- ASVC-CON-016 ; Agentic Service remains distinct from Agentic Capability
- ASVC-CON-017 ; Agentic Service remains distinct from Agentic Operations
- ASVC-CON-018 ; Agentic Service remains distinct from Agentic Value Stream
- ASVC-CON-019 ; Agentic Service retains provenance and grounding

### Negative tests (15)

The negative tests verify that forbidden semantic implications are absent.

- ASVC-NEG-001 ; Agentic Service is-a Agent (forbidden what-vs-who collapse)
- ASVC-NEG-002 ; Agentic Service is-a Agentic Capability (forbidden service-vs-capability collapse)
- ASVC-NEG-003 ; Agentic Service is-a Agentic Workflow (forbidden service-vs-workflow collapse)
- ASVC-NEG-004 ; Agentic Service is-a Agentic Operations (forbidden service-vs-operations collapse)
- ASVC-NEG-005 ; Agentic Service is-a Agentic Value Stream (forbidden service-vs-value-stream collapse)
- ASVC-NEG-006 ; Agentic Service is-a Autonomous Service (forbidden orthogonality violation)
- ASVC-NEG-007 ; Agentic Service requires AI (forbidden technology implication)
- ASVC-NEG-008 ; AI-enabled Service automatically becomes Agentic Service (forbidden AI implication)
- ASVC-NEG-009 ; Automated Service automatically becomes Agentic Service (forbidden automation implication)
- ASVC-NEG-010 ; A Service containing an Agent automatically becomes Agentic Service (forbidden Agent implication)
- ASVC-NEG-011 ; Agentic Service requires removal of humans (forbidden organizational implication)
- ASVC-NEG-012 ; Agentic Service implies autonomous behavior (forbidden autonomous implication)
- ASVC-NEG-013 ; Agentic Service implies Autonomous Operations (forbidden operations implication)
- ASVC-NEG-014 ; Agentic Service implies Autonomous Value Stream (forbidden value-stream implication)
- ASVC-NEG-015 ; Agentic Service implies Autonomous Enterprise (forbidden enterprise implication)

## Agentic/Autonomous Orthogonality at Service Boundary

Per ADR-ES-014 §11:

| Agentic | Autonomous | Interpretation |
|---|---|---|
| No | No | Conventional Service |
| Yes | No | Agentic Service (ADR-ES-014) |
| No | Yes | Future Autonomous Service (ADR-ES-015, deferred) |
| Yes | Yes | Future combined characterization |

The fourth state is a compositional semantic characterization, NOT a new concept.

## Release Gate

The release gate must fail if any forbidden type inheritance or forbidden implication is detected. Per CR-ES-014 §17, the release gate must fail if AI -> Agentic Service or Automation -> Agentic Service or Agent -> Agentic Service is encoded as a necessary semantic implication.

## See Also

- ADR-ES-014 (Agentic Service Semantic Grounding)
- CR-ES-014 (Implement Agentic Service) §10 + §11
- ADR-ES-012 (Agentic Capability Semantic Grounding)
- enterprise-semantics/concepts/agentic-service.concept.yaml