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

## [0.6.0] ; 2026-09-23 ; VS-D2a ;;; 15 AOP-CON-001..015 Agentic Operations conformance rules + 12 negative tests per CR-ES-007 §23 + §24 + ADR-ES-007 §27

### Added

- tests/agentic-operations/README.md
- tests/agentic-operations/schema.md
- tests/agentic-operations/identity.md
- tests/agentic-operations/lifecycle.md
- tests/agentic-operations/relationships.md
- tests/agentic-operations/boundaries.md
- tests/agentic-operations/provenance.md
- tests/agentic-operations/grounding.md
- tests/agentic-operations/examples.md
- tests/agentic-operations/operational-loop.md

### Cardinal rules

- Author: Emmanuel A. Otchere on all 10 files
- D-004 clean ;;; 0 forbidden glyphs
- No vendor-specific material from embargoed sources
- Per CR-ES-007 §23 + §24 + ADR-ES-007 §27

## [0.5.0] ; 2026-09-23 ; VS-D2a ;;; 14 AWF-CON-001..014 Agentic Workflow conformance rules + 10 negative tests per CR-ES-006 §28 + §29 + ADR-ES-006 §23

### Added

- tests/agentic-workflow/README.md
- tests/agentic-workflow/schema.md
- tests/agentic-workflow/identity.md
- tests/agentic-workflow/lifecycle.md
- tests/agentic-workflow/relationships.md
- tests/agentic-workflow/boundaries.md
- tests/agentic-workflow/provenance.md
- tests/agentic-workflow/grounding.md
- tests/agentic-workflow/examples.md

### Cardinal rules

- Author: Emmanuel A. Otchere on all 9 files
- D-004 clean ;;; 0 forbidden glyphs
- No vendor-specific material from embargoed sources
- Per CR-ES-006 §28 + §29 + ADR-ES-006 §23

## [0.4.0] ; 2026-09-23 ; VS-D2a ;; 12 AVS-CON-001..012 conformance rules + 10 negative tests for Agentic Value Stream per CR-ES-005 §21 + §22 + ADR-ES-005 §17

### Added

- tests/agentic-value-stream/README.md ;;; test group index covering all 12 AVS-CON-001..012 conformance rules + 10 negative tests per CR-ES-005 §21 + §22
- tests/agentic-value-stream/schema.md ;;; AVS-CON-001 + AVS-CON-002 + `AI is-a Agentic Value Stream` negative test
- tests/agentic-value-stream/identity.md ;;; identity uniqueness + format + specialisation validation + profile binding validation
- tests/agentic-value-stream/lifecycle.md ;;; AVS-CON-003 + AVS-CON-004 (initiating-condition + realisation-boundary retention)
- tests/agentic-value-stream/relationships.md ;;; AVS-CON-005 + AVS-CON-006 + AVS-CON-007 + reference resolution
- tests/agentic-value-stream/boundaries.md ;;; AVS-CON-008 + AVS-CON-009 + AVS-CON-010 + 4 negative tests
- tests/agentic-value-stream/provenance.md ;;; AVS-CON-012 ;;; grounding + mappings presence
- tests/agentic-value-stream/grounding.md ;;; ES-canonical novelty ;; Tier 2 Specialisation per FND-ES-AG-008 §1.3
- tests/agentic-value-stream/examples.md ;;; OTCHERE Inc demonstration tests + 5 negative example tests

### Cardinal rules

- Author: Emmanuel A. Otchere on all 9 files
- D-004 clean ;; 0 forbidden glyphs
- No vendor-specific material from embargoed sources

## [0.3.0] ; 2026-09-23 ; VS-D2a Agentic test stubs

### Added

- `tests/agent/README.md` ;;; test group index covering all 13 AG-CON-001..013 conformance rules from CR-ES-004 §26 + 5 negative tests per §27.
- `tests/agent/schema.md` ;;; AG-CON-001 (Agent definition), AG-CON-002 (Agentic definition) ;;; + negative test for `AI is-a Agent` per CR-ES-004 §27.
- `tests/agent/identity.md` ;;; identity uniqueness + format tests ;;; subject_type alignment with concept identities per CR-ES-004 §10.
- `tests/agent/lifecycle.md` ;;; AG-CON-011 (Agentic Value Stream not canonical), AG-CON-012 (Agentic Workflow not canonical), AG-CON-013 (Autonomous concepts not canonical) per CR-ES-004 §3 + §26.
- `tests/agent/relationships.md` ;;; AG-CON-007 (Agent acts-within Authority), AG-CON-008 (Agentic has Intent), AG-CON-009 (Agentic supports Action Selection), AG-CON-010 (Agentic is outcome-oriented) ;;; + reference resolution tests.
- `tests/agent/boundaries.md` ;;; AG-CON-003 (Agentic characteristics), AG-CON-004 (Agentic != AI), AG-CON-005 (Agentic != Automation), AG-CON-006 (Agentic != Autonomous) ;;; + negative tests for `Agentic is-a Autonomous` and `Automation is-a Agentic`.
- `tests/agent/provenance.md` ;;; non-empty provenance + governing artefact citations (CR-ES-004 + ADR-ES-004 + FND-ES-AG-008).
- `tests/agent/grounding.md` ;;; ES-canonical novelty ;;; no WSF Tier 1 or Tier 2 equivalent ;;; grounding entries document the absence.
- `tests/agent/examples.md` ;;; OTCHERE Inc Customer Service Agent demonstration tests ;;; 6/6 characteristics + 8+/11 predicates + human escalation + OTCHERE Inc naming ;;; + negative example tests.

### Cardinal rules

- Author: Emmanuel A. Otchere on all 9 files
- D-004 clean ;;; 0 forbidden glyphs on all 9 files
- No vendor-specific material from embargoed sources

### Held non-actions

- Tests remain markdown stubs (Python test promotion is held for a future CR)
- No executable Python harness added
- No CI wiring changes (test-probe already wired as a CI gate by upstream CRs)

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
