# Value Stream Boundary tests (VS-CON-008, VS-CON-009, VS-CON-010, VS-CON-017)
#
# Per CR-ES-003 §29 + ADR-ES-003 §32 VS-INV-001..011.
# Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-23)

VS-CON-008: A Value Stream must not be modeled as a specialization of Process.

INVALID:
  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: is-a
    object: ES:CONCEPT:process ;;; Value Stream != Process

VS-CON-009: A Value Stream must not be modeled as a specialization of Capability.

INVALID:
  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: is-a
    object: ES:CONCEPT:capability ;;; Value Stream != Capability

VS-CON-010: A Value Stream must not be modeled as a Workflow.

INVALID:
  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: is-a
    object: ES:CONCEPT:workflow ;;; Value Stream != Workflow

VS-CON-017: No Agentic Value Stream concept may be promoted to canonical status by this CR.

INVALID (Agentic Value Stream promotion):
  - subject: ES:CONCEPT:agentic-value-stream
    status: CANONICAL ;;; Agentic Value Stream held for ADR-ES-005

Per ADR-ES-003 §32 invariants:
- VS-INV-001: Value Stream != Process
- VS-INV-002: Value Stream != Capability
- VS-INV-003: Value Stream != Workflow
- VS-INV-004: Value Stream != Service
- VS-INV-005: Value Stream != Organization
- VS-INV-010: Agentic behavior is not required for Value Stream identity
- VS-INV-011: Autonomy is not required for Value Stream identity

This test group is a stub. Implementation lands via CR-ES-003 conformance PR.
