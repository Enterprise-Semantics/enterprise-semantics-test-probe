# Value Stream Provenance tests (VS-CON-014)
#
# Per CR-ES-003 §26 + §29 + ADR-ES-003 §26.
# Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-23)

VS-CON-014: Every established Value Stream must reference its governing ADR and CR.

VALID:
  id: ES:CONCEPT:value-stream:order-to-cash
  status: ESTABLISHED
  provenance:
    - source: CR-ES-003
      note: Foundational Value Stream canonical definition.
    - source: ADR-ES-003
      note: Foundational Value Stream decision.

INVALID (missing governing ADR):
  id: ES:CONCEPT:value-stream:order-to-cash
  status: ESTABLISHED
  provenance:
    - source: CR-ES-003
      - (no ADR reference, VS-CON-014 violation)

INVALID (missing governing CR):
  id: ES:CONCEPT:value-stream:order-to-cash
  status: ESTABLISHED
  provenance:
    - source: ADR-ES-003
      - (no CR reference, VS-CON-014 violation)

Per ADR-ES-003 §26, the WSF grounding must be recorded explicitly
with the WSF concept id (external:wsf:*) and the relationship type
(specializes, references, etc.).

This test group is a stub. Implementation lands via CR-ES-003 conformance PR.
