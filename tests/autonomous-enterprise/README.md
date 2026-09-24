# Conformance tests for Autonomous Enterprise

Per CR-ES-011 §22 + §23 + ADR-ES-011 §25 + §26.

This directory holds the conformance test stubs for the Autonomous
Enterprise concept. The tests cover:

- Positive invariants (AE-AUTO-CON-001 through AE-AUTO-CON-022),
  per ADR-ES-011 §25 + CR-ES-011 §22.
- Negative invariants (AE-AUTO-NEG-001 through AE-AUTO-NEG-018),
  per CR-ES-011 §23 + ADR-ES-011 §26.
- Boundary tests between Autonomous Enterprise and adjacent
  constructs (Enterprise, Agentic Enterprise, AI, Automation).

Each test file groups the stubs by category:

- boundaries.md ; Autonomous Enterprise vs adjacent constructs
- grounding.md ; WSF grounding
- identity.md ; canonical identity preservation
- lifecycle.md ; lifecycle state validity
- provenance.md ; provenance completeness
- relationships.md ; 14 canonical relationships
- schema.md ; schema conformance
- examples.md ; OTCHERE Inc example integration
- autonomy-integrity.md ; authority, governance, AI, autonomy
  boundaries

Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-24)
