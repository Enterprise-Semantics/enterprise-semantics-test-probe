# Value Stream Identity tests (VS-ID-001..005)
#
# Per CR-ES-003 §11 + §15 + ADR-ES-003 §15 + §32 VS-INV-009.
# Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-23)

VS-ID-001: Value Stream identifiers must be globally unique within Enterprise-Semantics.

VS-ID-002: A Value Stream identifier must not encode:
- organizational ownership
- implementation technology
- process identifier
- system identifier
- workflow identifier

VALID:
  id: ES:CONCEPT:value-stream:order-to-cash

INVALID (encodes organizational ownership):
  id: ES:CONCEPT:value-stream:OTCHERE-Inc-order-to-cash

INVALID (encodes implementation technology):
  id: ES:CONCEPT:value-stream:sap-order-to-cash

VS-ID-003: Changing the implementation of a Value Stream must not require changing its semantic identity.

VS-ID-004: A Value Stream name may change without changing its identifier when semantic identity remains unchanged.

VALID:
  id: ES:CONCEPT:value-stream:order-to-cash
  name: Order-to-Cash (revised 2026)

VS-ID-005: A fundamentally different value journey requires a distinct Value Stream identity.

VALID (different journey, different identity):
  id: ES:CONCEPT:value-stream:hire-to-retire
  definition: An end-to-end sequence covering hiring through retirement.

INVALID (same journey, different identity, violation of VS-ID-005):
  id: ES:CONCEPT:value-stream:order-to-fulfilment
  definition: Same as order-to-cash.

This test group is a stub. Implementation lands via CR-ES-003 conformance PR.
