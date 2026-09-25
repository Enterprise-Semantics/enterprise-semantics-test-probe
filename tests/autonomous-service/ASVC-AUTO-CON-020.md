# ASVC-AUTO-CON-020 , Autonomous Service retains provenance and grounding

**Filing:** VS-D2a of CR-ES-015 , Autonomous Service conformance tests
**Ratified by:** ADR-ES-015
**Implemented by:** CR-ES-015
**Status:** Candidate , awaiting CR-ES-015 implementation acceptance

## Test ID

`ASVC-AUTO-CON-020`

## Test Title

Autonomous Service retains provenance and grounding

## Test Intent

The Autonomous Service concept record contains provenance entries referencing ADR-ES-003, ADR-ES-004, ADR-ES-007, ADR-ES-008, ADR-ES-009, ADR-ES-011, ADR-ES-014, ADR-ES-015, CR-ES-015, FND-ES-AG-008.

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