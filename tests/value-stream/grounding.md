# Value Stream Grounding tests (VS-CON-015)
#
# Per CR-ES-003 §26 + §29 + FND-ES-AG-008 §1.3.
# Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-23)

VS-CON-015: Every established Value Stream must declare its WSF grounding status.

VALID (Tier 1 Kernel Reference + ES-canonical novelty):
  id: ES:CONCEPT:value-stream
  wsf_grounding:
    - wsf_concept_id: external:wsf:Value
      relationship: specializes
      note: Tier 1 Kernel Reference + ES-canonical novelty per FND-ES-AG-008 §1.3.

INVALID (missing wsf_grounding):
  id: ES:CONCEPT:value-stream
  status: ESTABLISHED
  - (no wsf_grounding block, VS-CON-015 violation)

INVALID (mixed grounding, per FND-ES-AG-008 §1.4 working hypothesis):
  wsf_grounding:
    - wsf_concept_id: external:wsf:Value
      relationship: specializes
    - wsf_concept_id: external:wsf:Capability
      relationship: references
  - (mixed claims without resolution, per ADR-ES-001 §4.1 violation)

Per FND-ES-AG-008 §1.3, Value Stream is classified as Tier 1 Kernel
Reference + ES-canonical novelty. The Stream construct is ES-canonical
novelty, WSF grounds the kernel Value.

This test group is a stub. Implementation lands via CR-ES-003 conformance PR.
