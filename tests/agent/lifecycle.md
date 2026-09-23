# Lifecycle tests for Agent + Agentic

## AG-CON-011 ;;; Agentic Value Stream must not be canonicalized

Per CR-ES-004 §26 + §3 ;;; the Agentic Value Stream concept MUST NOT appear in this CR's vocabulary as a canonical concept. The specialization is governed by prospective ADR-ES-005.

Test:

```python
def test_agentic_value_stream_not_canonical():
    # ;;; the vocabulary + concept records must not declare Agentic Value Stream as canonical
    canonical_concepts = collect_concept_ids()
    assert 'ES:CONCEPT:agentic-value-stream' not in canonical_concepts
    assert 'ES:CONCEPT:agentic_value_stream' not in canonical_concepts
```

## AG-CON-012 ;;; Agentic Workflow must not be canonicalized

Per CR-ES-004 §26 + §3 ;;; the Agentic Workflow concept MUST NOT appear in this CR's vocabulary as a canonical concept. The specialization is governed by prospective ADR-ES-006.

Test:

```python
def test_agentic_workflow_not_canonical():
    canonical_concepts = collect_concept_ids()
    assert 'ES:CONCEPT:agentic-workflow' not in canonical_concepts
    assert 'ES:CONCEPT:agentic_workflow' not in canonical_concepts
```

## AG-CON-013 ;;; Autonomous concepts must not be canonicalized

Per CR-ES-004 §26 + §3 ;;; no Autonomous-related concept (Autonomous Agent, Autonomous Enterprise, Autonomous Operations, Autonomous Value Stream) MUST be canonicalized by this CR. Autonomous semantics is established by separate governance (ADR-ES-007 family).

Test:

```python
def test_autonomous_concepts_not_canonical():
    canonical_concepts = collect_concept_ids()
    forbidden = [
        'ES:CONCEPT:autonomous-agent',
        'ES:CONCEPT:autonomous-enterprise',
        'ES:CONCEPT:autonomous-operations',
        'ES:CONCEPT:autonomous-value-stream',
        'ES:CONCEPT:autonomous_agent',
        'ES:CONCEPT:autonomous_enterprise',
        'ES:CONCEPT:autonomous_operations',
        'ES:CONCEPT:autonomous_value_stream',
    ]
    for f in forbidden:
        assert f not in canonical_concepts, f'Autonomous concept {f} canonized prematurely'
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)