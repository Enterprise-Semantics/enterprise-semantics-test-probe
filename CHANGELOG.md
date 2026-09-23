# Changelog

All notable changes to this repository are documented in this file. Dates use
the committer's local time.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) semantics.
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Wire as CI gate on the rest of the org (currently enterprise-semantics + enterprise-semantics-mappings).
- Promote the value-stream/ stubs to executable Python tests in a future CR-ES-003 conformance PR.
- Profile conformance extension (cross-record checks, CR-ES-AG-012).

## [0.2.0] ; 2026-09-23 ; VS-D2a Value Stream test stubs

### Added

- `tests/value-stream/README.md` ;;; test group index covering all 17 VS-CON-001..017 conformance rules from CR-ES-003 §29.
- `tests/value-stream/schema.md` ;;; VS-CON-001 (Definition), VS-CON-002 (Identity) test stubs.
- `tests/value-stream/identity.md` ;;; VS-ID-001..005 identity rules test stubs per CR-ES-003 §11.
- `tests/value-stream/lifecycle.md` ;;; VS-CON-016 lifecycle test stub per CR-ES-003 §25 + ADR-ES-003 §29.
- `tests/value-stream/relationships.md` ;;; VS-CON-007 (realizes), VS-CON-013 (predicate vocabulary) test stubs.
- `tests/value-stream/boundaries.md` ;;; VS-CON-008 (Process), VS-CON-009 (Capability), VS-CON-010 (Workflow), VS-CON-017 (Agentic isolation) test stubs.
- `tests/value-stream/provenance.md` ;;; VS-CON-014 (governing ADR + CR) test stub per CR-ES-003 §26.
- `tests/value-stream/grounding.md` ;;; VS-CON-015 (WSF grounding) test stub per FND-ES-AG-008 §1.3.
- `tests/value-stream/examples.md` ;;; OTCHERE Inc worked examples + §30 negative test cases per CR-ES-003 §18 + §30.

### Scope

This release implements VS-D2a of CR-ES-003 ;;; the 8 test directories from CR-ES-003 §31 (schema + identity + lifecycle + relationships + boundaries + provenance + grounding + examples). The tests are markdown stubs (mirroring the capability/ test directory pattern from CR-ES-002). Each stub documents the conformance rule(s), valid examples, invalid examples, and provenance reference. Promotion to executable Python tests is held for a future conformance PR.

### Coverage of the 17 VS-CON rules

| Rule | Description | Test directory |
|---|---|---|
| VS-CON-001 | Definition | schema.md |
| VS-CON-002 | Identity (unique id) | schema.md |
| VS-CON-003 | Stakeholder | schema.md + examples.md |
| VS-CON-004 | Initiation | schema.md |
| VS-CON-005 | Realization Boundary | schema.md |
| VS-CON-006 | Stages (>=1) | relationships.md |
| VS-CON-007 | realizes relationship | relationships.md |
| VS-CON-008 | Not specialization of Process | boundaries.md |
| VS-CON-009 | Not specialization of Capability | boundaries.md |
| VS-CON-010 | Not modeled as Workflow | boundaries.md |
| VS-CON-011 | Stage references Value Stream | examples.md |
| VS-CON-012 | Stage ordering resolves | relationships.md |
| VS-CON-013 | Predicate in vocabulary | relationships.md |
| VS-CON-014 | Provenance (governing ADR + CR) | provenance.md |
| VS-CON-015 | WSF grounding declared | grounding.md |
| VS-CON-016 | Lifecycle conformant | lifecycle.md |
| VS-CON-017 | Agentic isolation | boundaries.md |

### Cardinal rules applied

- Author: Emmanuel A. Otchere (cardinal author rule, 2026-09-23) ;;; present in all 9 new files.
- No en-dash (U+2013) or em-dash (U+2014) in any new file (D-004 dash rule). Section dividers use `;;;` boundary lines per existing convention.
- No vendor-specific material from embargoed sources in any new file (cardinal embargo, 2026-09-22).
- ES is sourced from SDO-neutral standardisation only (ISO/IEC, ITU-T, ETSI, NIST).

### Held non-actions

- No PlantUML visuals (held for VS-D2b in enterprise-semantics-visuals).
- No ADR-ES-003 promotion to Accepted (gated on CR-ES-003 implementation completion).
- No release tag (per v3.1.4 user directive).

## [0.1.0] ; 2026-09-03 ; Phase 5 conformance gate promoted

### Changed

- `tools/validate.py` promoted from skeleton (always return 1) to real harness that invokes `enterprise-semantics/conformance/check.py` and `check_concepts.py`. No source-of-truth duplication ;; the harness sources the authority repo.
- `tests/test_smoke.py` rewritten to cover `--help` and `NO_DRIFT` against the authority repo.
- `tests/conftest.py` adds `tools/` to `sys.path` for pytest.
- Discovery order: `--source PATH` > sibling-of-test-probe in workspace > CWD-sibling > CWD itself.

### Added

- Phase 5 wiring: `enterprise-semantics/.github/workflows/conformance.yml` and `enterprise-semantics-mappings/.github/workflows/conformance.yml` run this harness on every push and PR to main.

## [0.0.1] ; 2026-09-02 ; Skeleton

### Added

- README.md (purpose, ownership, status, relationship to other repos).
- CODEOWNERS (sole owner: @emmanuel-a-otchere).
- CHANGELOG.md (this file).
- .gitignore (credential, AI-model, and workspace-noise patterns).
- LICENSE (Apache-2.0).
- Skeleton harness at `tools/validate.py`.
- Skeleton test at `tests/test_smoke.py` + `tests/conftest.py`.
