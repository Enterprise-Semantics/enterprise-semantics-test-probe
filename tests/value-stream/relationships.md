# Value Stream Relationship tests (VS-CON-007, VS-CON-013)
#
# Per CR-ES-003 §9 + §10 + §29.
# Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-23)

VS-CON-007: Every established Value Stream must support a realizes relationship to Stakeholder Value.

VALID:
  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: realizes
    object: external:concept:stakeholder-value

INVALID (missing realizes relationship):
  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: contains
    object: ES:CONCEPT:value-stage

VS-CON-013: Every Value Stream predicate must exist in the relationship vocabulary.

VALID (predicate in vocabulary ;;; per CR-ES-003 §9 + vocabulary.yaml v0.2.0):
  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: realizes
    object: external:concept:stakeholder-value

  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: contains
    object: ES:CONCEPT:value-stage

  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: enabled-by
    object: ES:CONCEPT:capability

  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: realized-through
    object: external:concept:process

  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: produces
    object: external:concept:outcome

INVALID (predicate not in vocabulary):
  - subject: ES:CONCEPT:value-stream:order-to-cash
    predicate: delivers-value ;;; not in the 13 governed predicates
    object: external:concept:stakeholder-value

Reference: relationships/vocabulary.yaml v0.2.0 ;;; 13 governed predicates for Value Stream.

This test group is a stub. Implementation lands via CR-ES-003 conformance PR.
