# Value Stream Schema tests (VS-CON-001, VS-CON-002)
#
# Per CR-ES-003 §29 + §7 + §8.
# Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-23)

VS-CON-001: Every Value Stream must have a definition.

VALID:
  id: ES:CONCEPT:value-stream:order-to-cash
  definition: An end-to-end sequence of value-creating stages.

INVALID (no definition):
  id: ES:CONCEPT:value-stream:order-to-cash
  name: Order-to-Cash

VS-CON-002: Every Value Stream must have a unique identifier.

VALID:
  id: ES:CONCEPT:value-stream:order-to-cash
  definition: An end-to-end sequence.

INVALID (no id):
  definition: An end-to-end sequence.

INVALID (duplicate id with another Value Stream):
  id: ES:CONCEPT:value-stream:order-to-cash
  definition: An end-to-end sequence.
  ;;; (assuming another record already has id: ES:CONCEPT:value-stream:order-to-cash)

This test group is a stub. Implementation lands via CR-ES-003 conformance PR.
