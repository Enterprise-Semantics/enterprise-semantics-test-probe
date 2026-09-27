# Conformance tests for Agentic Enterprise

Per CR-ES-010 §15 + §16 + ADR-ES-010 §19.

This directory holds the conformance test stubs for the Agentic
Enterprise concept. The tests cover:

- **Positive invariants** (AE-CON-001 through AE-CON-018), per
  ADR-ES-010 §19 + CR-ES-010 §15.
- **Negative invariants** (AE-NEG-001 through AE-NEG-018), per
  CR-ES-010 §16 + ADR-ES-010 §20.
- **Boundary tests** between Agentic Enterprise and adjacent
  constructs (Enterprise, Autonomous Enterprise, AI, Automation).

Each test file groups the stubs by category:

- `boundaries.md` ; Agentic Enterprise vs adjacent constructs
- `grounding.md` ; WSF grounding
- `identity.md` ; canonical identity preservation
- `lifecycle.md` ; lifecycle state validity
- `provenance.md` ; provenance completeness
- `relationships.md` ; 10 canonical relationships
- `schema.md` ; schema conformance
- `examples.md` ; OTCHERE Inc example integration
- `autonomy-integrity.md` ; authority, governance, AI, autonomy
  boundaries

Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-24)
