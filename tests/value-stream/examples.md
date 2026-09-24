# Value Stream Examples tests
#
# Per CR-ES-003 §18 + §19 + §20 + §22.
# Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-23)

This test group verifies that worked examples for Value Stream
demonstrate the canonical definition, semantic boundaries, and
relationship vocabulary correctly.

Valid examples, per CR-ES-003 §18:

  - Order-to-Cash Value Stream (illustrative, OTCHERE Inc)
    Stages: Capture Demand, Confirm Order, Fulfil Order,
            Deliver Offering, Realize Payment
    Per value-stream-order-to-cash.yaml in enterprise-semantics-examples.

  - Value Stage example
    Stage: Fulfil Order
    Value Stream: Order-to-Cash
    Per value-stream-order-to-cash.yaml §stage.

  - Pay-to-Fulfillment Value Stream
    Stages: Establish Payment, Confirm Transaction, Authorize Fulfillment,
            Prepare Fulfillment, Fulfill Demand, Confirm Realization
    Per value-stream-pay-to-fulfillment.yaml.

Invalid examples, per CR-ES-003 §30 negative tests:

  Invalid example 1: Value Stream is-a Process
    Expected: FAIL, Value Stream != Process (VS-INV-001)

  Invalid example 2: Value Stream is-a Capability
    Expected: FAIL, Value Stream != Capability (VS-INV-002)

  Invalid example 3: Value Stage = Activity
    Expected: FAIL, Value Stage != Activity (per VST-ID-*)

  Invalid example 4: Value Stream contains Task as direct decomposition
    Expected: FAIL, Tasks belong to the Process execution layer

This test group is a stub. Implementation lands via CR-ES-003 conformance PR.
