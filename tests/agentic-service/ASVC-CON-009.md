# ASVC-CON-009 ; Agentic Service operates within defined authority

**Filing:** VS-D2a of CR-ES-014 ; Agentic Service conformance tests
**Ratified by:** ADR-ES-014
**Implemented by:** CR-ES-014
**Status:** Candidate ; awaiting CR-ES-014 implementation acceptance

## Test ID

`ASVC-CON-009`

## Test Title

Agentic Service operates within defined authority

## Test Intent

The Agentic Service concept record contains an operates-within relationship pointing to Authority; the authority_context property is defined.

## Test Method

1. Load the Agentic Service concept record from `enterprise-semantics/concepts/agentic-service.concept.yaml`.
2. Verify the invariant encoded in the test intent.
3. For positive tests: assert that the expected semantic property is present.
4. For negative tests: assert that the forbidden semantic implication is absent.

## Pass Criteria

The test passes if the invariant is verified.

## Fail Criteria

The test fails if the invariant is violated. The release gate must fail per CR-ES-014 §17 if the invariant is violated.

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-24)