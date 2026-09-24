# Agentic Capability Conformance Tests

Per ADR-ES-012 §23 + CR-ES-012 §23 + CR-ES-012 §24.

This directory contains the conformance test suite for the Agentic
Capability semantic boundary established by ADR-ES-012.

## Coverage

- `identity.md`: ACAP-CON-001..004 (4 tests, specialization + definition + materiality + outcome-orientation)
- `boundaries.md`: ACAP-CON-005..013 (9 tests, agent/workflow/operations/value-stream/enterprise boundaries)
- `integration.md`: ACAP-CON-014..018 (5 tests, integration + provenance)
- `negative.md`: ACAP-NEG-001..014 (14 tests, rejected interpretations)

Total: 18 positive + 14 negative = 32 conformance tests.

## Status

Test stubs pending conformance probe activation. The skill text
remains the authoritative specification source (ADR-ES-012 §23 +
CR-ES-012 §23 + CR-ES-012 §24). Test bodies assert False with the
specification reference so that an unimplemented test surfaces
clearly in the conformance probe output.

## Cardinal rules

Authored by Emmanuel A. Otchere (cardinal author rule, 2026-09-24).
Zero forbidden glyphs, zero inline , .
