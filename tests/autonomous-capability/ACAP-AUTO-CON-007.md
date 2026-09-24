# ACAP-AUTO-CON-007 , Autonomous Capability operates within authority

**Filing:** VS-D2a of CR-ES-013 , Autonomous Capability conformance tests
**Ratified by:** ADR-ES-013
**Implemented by:** CR-ES-013
**Status:** Candidate , awaiting CR-ES-013 implementation acceptance

## Test ID

`ACAP-AUTO-CON-007`

## Test Title

Autonomous Capability operates within authority

## Test Intent

The Autonomous Capability concept record contains an operates-within relationship pointing to Authority, with defined authority_context property.

## Test Method

1. Load the Autonomous Capability concept record from `enterprise-semantics/concepts/autonomous-capability.concept.yaml`.
2. Verify the invariant encoded in the test intent.
3. For positive tests: assert that the expected semantic property is present.
4. For negative tests: assert that the forbidden semantic implication is absent.

## Pass Criteria

The test passes if the invariant is verified.

## Fail Criteria

The test fails if the invariant is violated. The release gate must fail per CR-ES-013 §17 if the invariant is violated.

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-24)