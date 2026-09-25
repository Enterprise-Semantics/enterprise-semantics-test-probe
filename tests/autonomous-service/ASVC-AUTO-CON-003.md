# ASVC-AUTO-CON-003 , Autonomous Service has material autonomous realization

**Filing:** VS-D2a of CR-ES-015 , Autonomous Service conformance tests
**Ratified by:** ADR-ES-015
**Implemented by:** CR-ES-015
**Status:** Candidate , awaiting CR-ES-015 implementation acceptance

## Test ID

`ASVC-AUTO-CON-003`

## Test Title

Autonomous Service has material autonomous realization

## Test Intent

The Autonomous Service concept record includes the materiality-required relationship ; material autonomous progression in service realization is required (mere use of AI/automation/Agent/autonomous system/ML/predefined rules does NOT establish autonomy).

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