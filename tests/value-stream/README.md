# Value Stream Tests, 17 conformance rules
#
# Per CR-ES-003 §29 + §30 + §31.
# Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-23)

This test group covers the 17 conformance rules (VS-CON-001..017)
declared in CR-ES-003 §29. Each rule is documented in detail in the
corresponding subdirectory:

  - schema.md        , VS-CON-001 (Definition), VS-CON-002 (Identity)
  - identity.md      , VS-ID-001..005 (Identity Rules)
  - lifecycle.md     , VS-CON-016 (Lifecycle)
  - relationships.md , VS-CON-007 (realizes), VS-CON-013 (Predicate vocab)
  - boundaries.md    , VS-CON-008 (Process), VS-CON-009 (Capability),
                       - VS-CON-010 (Workflow), VS-CON-017 (Agentic isolation)
  - provenance.md    , VS-CON-014 (Governing ADR + CR)
  - grounding.md     , VS-CON-015 (WSF grounding)
  - examples.md      , §18 OTCHERE Inc worked examples + §30 negative tests

Additional rules covered across the subdirectories:

  - VS-CON-003, Stakeholder, every published Value Stream must
    identify a stakeholder context, see schema.md and boundaries.md
  - VS-CON-004, Initiation, every published Value Stream must
    identify an initiating condition, see schema.md
  - VS-CON-005, Realization Boundary, every published Value Stream
    must define its realization boundary, see schema.md
  - VS-CON-006, Stages, every established Value Stream must
    contain at least one Value Stage, see relationships.md
  - VS-CON-011, Stage Integrity, every published Value Stage must
    reference a Value Stream, see examples.md
  - VS-CON-012, Stage Ordering, if stage ordering is asserted,
    preceding/following references must resolve, see relationships.md

Per CR-ES-003 §30, the test probe includes explicit failure cases
(Invalid examples 1-4) that exercise the negative conformance tests
documented above.

This is the value-stream/ test group index. The full test directory
per CR-ES-003 §31:

  enterprise-semantics-test-probe/
  `-- tests/
      `-- value-stream/
          |-- schema/
          |-- identity/
          |-- lifecycle/
          |-- relationships/
          |-- boundaries/
          |-- provenance/
          |-- grounding/
          `-- examples/

Each directory contains a markdown stub that documents the rule(s)
covered, the valid and invalid examples, and the provenance reference.
Implementation lands via a future CR-ES-003 conformance PR that
promotes these stubs to executable Python tests.
