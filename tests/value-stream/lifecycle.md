# Value Stream Lifecycle tests (VS-CON-016)
#
# Per CR-ES-003 §25 + §29 + ADR-ES-003 §29.
# Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-23)

VS-CON-016: All lifecycle values must conform to the Enterprise-Semantics lifecycle specification.

VALID lifecycle states (per ADR-ES-003 §29):
- PROPOSED
- CANDIDATE
- ESTABLISHED
- CANONICAL

Exceptional states:
- REJECTED
- SUPERSEDED
- DEPRECATED

VALID:
  id: ES:CONCEPT:value-stream:order-to-cash
  status: CANDIDATE

INVALID (lifecycle value not in registry):
  id: ES:CONCEPT:value-stream:order-to-cash
  status: DRAFT ;;; not a registered lifecycle state

This test group is a stub. Implementation lands via CR-ES-003 conformance PR.
