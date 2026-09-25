# Autonomous Service Conformance Tests

**Filing:** VS-D2a of CR-ES-015 , Autonomous Service conformance tests
**Ratified by:** ADR-ES-015
**Implemented by:** CR-ES-015
**Authored by:** Emmanuel A. Otchere (cardinal author rule, 2026-09-24)

## Purpose

This directory contains conformance tests for the Autonomous Service semantic specialization established by ADR-ES-015 + CR-ES-015.

The tests verify:

1. The Autonomous Service concept is canonicalized as a specialization of the universal Service concept.
2. The Service 2x2 matrix at the service boundary (Agentic yes/no, Autonomous yes/no) is preserved as 4 orthogonal states.
3. Autonomous Service operates within bounded Authority, Policy, Constraints, Governance, Service Contract.
4. Autonomy Materiality is enforced (mere use of AI/automation/Agent/autonomous system/ML/predefined rules does NOT establish autonomy).
5. Human participation remains valid.
6. AI and Automation are NOT necessary/sufficient conditions for Autonomous Service.
7. Forbidden type inheritance (Autonomous Service -> Agentic Service, -> Agent, -> Autonomous Capability, -> Autonomous Operations, -> Autonomous Value Stream, -> Autonomous Enterprise) is detected and rejected.
8. The Agentic/Autonomous orthogonality at the service boundary is preserved.
9. Provenance and grounding (ADR-ES-003, ADR-ES-004, ADR-ES-007, ADR-ES-008, ADR-ES-009, ADR-ES-011, ADR-ES-014, ADR-ES-015, CR-ES-015) is complete.

## Test Index

### Positive tests (20)

The positive tests verify that Autonomous Service exhibits the required semantic properties.

- ASVC-AUTO-CON-001 , Autonomous Service specializes Service
- ASVC-AUTO-CON-002 , Autonomous Service retains Service semantics
- ASVC-AUTO-CON-003 , Autonomous Service has material autonomous realization
- ASVC-AUTO-CON-004 , Autonomous Service has defined service objective
- ASVC-AUTO-CON-005 , Autonomous Service has defined autonomy scope
- ASVC-AUTO-CON-006 , Autonomous Service has defined decision scope
- ASVC-AUTO-CON-007 , Autonomous Service has defined action scope
- ASVC-AUTO-CON-008 , Autonomous Service operates within authority
- ASVC-AUTO-CON-009 , Autonomous Service is bounded by policy
- ASVC-AUTO-CON-010 , Autonomous Service is bounded by constraints
- ASVC-AUTO-CON-011 , Autonomous Service is bounded by governance
- ASVC-AUTO-CON-012 , Autonomous Service may adapt within defined scope
- ASVC-AUTO-CON-013 , Autonomous Service supports escalation
- ASVC-AUTO-CON-014 , Human intervention remains permitted
- ASVC-AUTO-CON-015 , AI is not required
- ASVC-AUTO-CON-016 , Automation is not sufficient
- ASVC-AUTO-CON-017 , Autonomous Service may use Agentic Workflow
- ASVC-AUTO-CON-018 , Autonomous Service may be supported by Autonomous Operations
- ASVC-AUTO-CON-019 , Autonomous Service may participate in Autonomous Value Stream realization
- ASVC-AUTO-CON-020 , Autonomous Service retains provenance and grounding

### Negative tests (16)

The negative tests verify that forbidden semantic implications are absent.

- ASVC-AUTO-NEG-001 , Autonomous Service is-a Agentic Service (forbidden orthogonality violation)
- ASVC-AUTO-NEG-002 , Autonomous Service is-a Agent (forbidden what-vs-who collapse)
- ASVC-AUTO-NEG-003 , Autonomous Service is-a Autonomous Capability (forbidden service-vs-capability collapse)
- ASVC-AUTO-NEG-004 , Autonomous Service is-a Autonomous Operations (forbidden service-vs-operations collapse)
- ASVC-AUTO-NEG-005 , Autonomous Service is-a Autonomous Value Stream (forbidden service-vs-value-stream collapse)
- ASVC-AUTO-NEG-006 , Autonomous Service is-a Autonomous Enterprise (forbidden service-vs-enterprise collapse)
- ASVC-AUTO-NEG-007 , Autonomous Service requires AI (forbidden technology implication)
- ASVC-AUTO-NEG-008 , AI-enabled Service automatically becomes Autonomous Service (forbidden AI implication)
- ASVC-AUTO-NEG-009 , Automated Service automatically becomes Autonomous Service (forbidden automation implication)
- ASVC-AUTO-NEG-010 , A Service containing an Agent automatically becomes Autonomous Service (forbidden Agent implication)
- ASVC-AUTO-NEG-011 , Autonomous Service requires elimination of humans (forbidden organizational implication)
- ASVC-AUTO-NEG-012 , Autonomous Service has unlimited authority (forbidden governance implication)
- ASVC-AUTO-NEG-013 , Autonomous Operations automatically make every Service autonomous (forbidden operations implication)
- ASVC-AUTO-NEG-014 , Autonomous Value Stream automatically makes every participating Service autonomous (forbidden value-stream implication)
- ASVC-AUTO-NEG-015 , Autonomous Capability automatically makes every delivered Service autonomous (forbidden capability implication)
- ASVC-AUTO-NEG-016 , Autonomous Service automatically becomes Agentic Service (forbidden orthogonality violation)

## Service 2x2 Matrix (now structurally complete)

Per ADR-ES-015 §7 + ADR-ES-014 §11:

| Agentic | Autonomous | Interpretation |
|---|---|---|
| No | No | Conventional Service |
| Yes | No | Agentic Service (ADR-ES-014, v1.3.0) |
| No | Yes | Autonomous Service (ADR-ES-015, v1.4.0) |
| Yes | Yes | Combined characterization (NOT a new subtype) |

The fourth state is a combined characterization, NOT another foundational subtype.

## Release Gate

The release gate must fail if any forbidden type inheritance or forbidden implication is detected. Per CR-ES-015 §18, the release gate must fail if Autonomous Service -> Agentic Service is encoded as mandatory inheritance, or if AI -> Autonomous Service or Automation -> Autonomous Service is encoded as a necessary semantic condition.

## See Also

- ADR-ES-015 (Autonomous Service Semantic Grounding)
- CR-ES-015 (Implement Autonomous Service) §10 + §11
- ADR-ES-014 (Agentic Service Semantic Grounding)
- enterprise-semantics/concepts/autonomous-service.concept.yaml