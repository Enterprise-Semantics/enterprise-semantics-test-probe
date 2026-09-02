# enterprise-semantics-test-probe

> Enterprise-Semantics conformance test harness: schema validation, unique-ID check, broken-reference detection, mapping integrity, lifecycle validity, generated-artifact consistency.

This repository implements the **conformance gate** for [`enterprise-semantics`](https://github.com/Enterprise-Semantics/enterprise-semantics) and [`enterprise-semantics-mappings`](https://github.com/Enterprise-Semantics/enterprise-semantics-mappings). Specifications that the harness enforces live in [`enterprise-semantics-spec`](https://github.com/Enterprise-Semantics/enterprise-semantics-spec).

## Status

**Skeleton (v0.0.1).** The harness becomes a CI gate in Phase 5.

## What the harness validates (target list)

- Unique concept identifiers across the seed.
- Valid names and required definitions.
- Valid relationship types and inverse relationships.
- No broken references.
- Valid lifecycle state values (Candidate, Investigating, Proposed, Established, Canonical, Mapped, Deprecated, Retired).
- Provenance completeness.
- Mapping integrity (source and target both resolve; predicates in the controlled vocabulary).
- Schema conformance (YAML/JSON records conform to the published schemas).
- Version consistency.
- Generated artifact consistency (regenerated Markdown, JSON, PlantUML match committed versions).

## Layout

```text
tools/
  validate.py            ; entry point for CI
tests/
  test_concept_ids.py
  test_lifecycle.py
  test_references.py
  test_mappings.py
fixtures/
  ; example seeded mini-source for local validation
```

## Relationship to other repositories

| Repository | Relationship |
|------------|--------------|
| [`enterprise-semantics-spec`](https://github.com/Enterprise-Semantics/enterprise-semantics-spec) | Spec source: defines the requirements this harness enforces. |
| [`enterprise-semantics`](https://github.com/Enterprise-Semantics/enterprise-semantics) | Under test. |
| [`enterprise-semantics-mappings`](https://github.com/Enterprise-Semantics/enterprise-semantics-mappings) | Under test. |
| [`enterprise-semantics-examples`](https://github.com/Enterprise-Semantics/enterprise-semantics-examples) | Golden path: examples must pass the harness. |

## License

Apache License 2.0. See [LICENSE](https://github.com/Enterprise-Semantics/enterprise-semantics-test-probe/blob/main/LICENSE).
