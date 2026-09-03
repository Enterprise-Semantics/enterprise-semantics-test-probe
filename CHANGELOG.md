# Changelog

All notable changes to this repository are documented in this file. Dates use
the committer's local time.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) semantics.
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Profile conformance extension (cross-record checks, CR-ES-AG-012).
- Wire as CI gate on the rest of the org (currently enterprise-semantics + enterprise-semantics-mappings).

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
