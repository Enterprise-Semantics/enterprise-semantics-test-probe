# Autonomous Capability Conformance Tests

**Filing:** VS-D2a of CR-ES-013 , Autonomous Capability conformance tests
**Ratified by:** ADR-ES-013
**Implemented by:** CR-ES-013
**Authored by:** Emmanuel A. Otchere (cardinal author rule, 2026-09-24)

## Purpose

This directory contains conformance tests for the Autonomous Capability semantic specialization established by ADR-ES-013 + CR-ES-013.

The tests verify:

1. The Autonomous Capability concept is canonicalized as a specialization of the universal Capability concept.
2. The 2x2 matrix at the capability boundary (Agentic yes/no, Autonomous yes/no) is preserved as 4 orthogonal states.
3. Autonomous Capability is bounded by Authority, Policy, Constraints, and Governance.
4. Human participation remains valid.
5. AI and automation are NOT necessary conditions for Autonomous Capability.
6. Forbidden type inheritance (Autonomous Capability -> Agentic Capability, -> Agent, -> Autonomous Operations, -> Autonomous Value Stream, -> Autonomous Enterprise) is detected and rejected.
7. Provenance and grounding (ADR-ES-002, ADR-ES-004, ADR-ES-008, ADR-ES-009, ADR-ES-011, ADR-ES-012, ADR-ES-013, CR-ES-013) is complete.

## Test Index

### Positive tests (18)

The positive tests verify that Autonomous Capability exhibits the required semantic properties.

- ACAP-AUTO-CON-001 , Autonomous Capability specializes Capability
- ACAP-AUTO-CON-002 , Autonomous Capability retains enduring-ability semantics
- ACAP-AUTO-CON-003 , Autonomous Capability is outcome-oriented
- ACAP-AUTO-CON-004 , Autonomous Capability has defined autonomy scope
- ACAP-AUTO-CON-005 , Autonomous Capability has defined decision scope
- ACAP-AUTO-CON-006 , Autonomous Capability has defined action scope
- ACAP-AUTO-CON-007 , Autonomous Capability operates within authority
- ACAP-AUTO-CON-008 , Autonomous Capability is governed by policy
- ACAP-AUTO-CON-009 , Autonomous Capability is bounded by constraints
- ACAP-AUTO-CON-010 , Autonomous Capability may adapt within defined scope
- ACAP-AUTO-CON-011 , Autonomous Capability may retain human intervention
- ACAP-AUTO-CON-012 , Autonomous Capability supports escalation
- ACAP-AUTO-CON-013 , Autonomous Capability does not require AI
- ACAP-AUTO-CON-014 , Autonomous Capability does not require automation
- ACAP-AUTO-CON-015 , Autonomous Capability may coexist with Agentic behavior
- ACAP-AUTO-CON-016 , Autonomous Capability may support Autonomous Value Stream realization
- ACAP-AUTO-CON-017 , Autonomous Capability may be supported by Autonomous Operations
- ACAP-AUTO-CON-018 , Autonomous Capability retains provenance and grounding

### Negative tests (14)

The negative tests verify that forbidden semantic implications are absent.

- ACAP-AUTO-NEG-001 , Autonomous Capability is-a Agentic Capability (forbidden inheritance)
- ACAP-AUTO-NEG-002 , Agentic Capability is-a Autonomous Capability (forbidden reverse inheritance)
- ACAP-AUTO-NEG-003 , Autonomous Capability is-a Agent (forbidden what-vs-who collapse)
- ACAP-AUTO-NEG-004 , Autonomous Capability is-a Autonomous Operations (forbidden capability-vs-operations collapse)
- ACAP-AUTO-NEG-005 , Autonomous Capability is-a Autonomous Value Stream (forbidden capability-vs-value-stream collapse)
- ACAP-AUTO-NEG-006 , Autonomous Capability is-a Autonomous Enterprise (forbidden capability-vs-enterprise collapse)
- ACAP-AUTO-NEG-007 , Autonomous Capability requires AI (forbidden technology implication)
- ACAP-AUTO-NEG-008 , AI-enabled Capability automatically becomes Autonomous Capability (forbidden automation implication)
- ACAP-AUTO-NEG-009 , Automated Capability automatically becomes Autonomous Capability (forbidden automation implication)
- ACAP-AUTO-NEG-010 , Autonomous Capability requires elimination of humans (forbidden organizational implication)
- ACAP-AUTO-NEG-011 , Autonomous Capability implies unlimited authority (forbidden governance implication)
- ACAP-AUTO-NEG-012 , Autonomous Operations automatically make every supported Capability autonomous (forbidden operations implication)
- ACAP-AUTO-NEG-013 , Autonomous Value Stream automatically makes every enabling Capability autonomous (forbidden value-stream implication)
- ACAP-AUTO-NEG-014 , Autonomous Capability implies Agentic Capability (forbidden orthogonality violation)

## Semantic Integrity

The 2x2 matrix at the capability boundary:

| Agentic | Autonomous | Interpretation |
|---|---|---|
| No | No | Conventional capability realization |
| Yes | No | Agentic Capability |
| No | Yes | Autonomous Capability |
| Yes | Yes | Capability exhibiting both characteristics |

The fourth state is a compositional semantic characterization, NOT a new concept.

## Release Gate

The release gate must fail if any forbidden type inheritance or forbidden implication is detected. Per CR-ES-013 §17, the release gate must fail if Autonomous Capability -> Agentic Capability is inferred as mandatory inheritance, or if Autonomous Capability -> AI or Autonomous Capability -> Automation is encoded as a necessary condition.

## See Also

- ADR-ES-013 (Autonomous Capability Semantic Grounding)
- CR-ES-013 (Implement Autonomous Capability) §9 + §10
- ADR-ES-012 (Agentic Capability Semantic Grounding) , the orthogonal specialization
- enterprise-semantics/concepts/autonomous-capability.concept.yaml