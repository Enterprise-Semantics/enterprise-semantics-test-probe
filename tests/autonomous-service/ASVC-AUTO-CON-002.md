# ASVC-AUTO-CON-002 , Autonomous Service retains Service semantics

**Filing:** VS-D2a of CR-ES-015 , Autonomous Service conformance tests
**Ratified by:** ADR-ES-015
**Implemented by:** CR-ES-015
**Status:** Candidate , awaiting CR-ES-015 implementation acceptance

## Test ID

`ASVC-AUTO-CON-002`

## Test Title

Autonomous Service retains Service semantics

## Test Intent

The Autonomous Service concept record preserves the Service -> Provider / Consumer / Service Interaction / Service Delivery / Capability / Outcome / Value / Service Context semantic anchors.

## Test Method

1. Load the Autonomous Service concept record from `enterprise-semantics/concepts/autonomous-service.concept.yaml`.
2. Verify the invariant encoded in the test intent.
3. For positive tests: assert that the expected semantic property is present.
4. For negative tests: assert that the forbidden semantic implication is absent.

## Pass Criteria

The test passes if the invariant is verified.

## Fail Criteria

The test fails if the invariant is violated. The release gate must fail per CR-ES-015 §18 if the invariant is violated.

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-24)