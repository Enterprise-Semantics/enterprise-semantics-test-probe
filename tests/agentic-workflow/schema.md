# Schema tests for Agentic Workflow

## AWF-CON-001 ;; Agentic Workflow specialises Workflow

Per CR-ES-006 §21 + §28 + ADR-ES-006 §2 + §18 + §23 ;;; the
Agentic Workflow concept record MUST declare a direct
specialisation of Workflow.

Test:

```python
def test_awf_specializes_workflow():
    record = load_concept('agentic-workflow')
    assert record['id'] == 'ES:CONCEPT:agentic-workflow'
    assert 'ES:CONCEPT:workflow' in record['specializes']

def test_awf_specialization_predicate():
    record = load_concept('agentic-workflow')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    assert any(r['object'] == 'ES:CONCEPT:workflow' for r in specializes_rels)
```

## AWF-CON-002 ;; Agentic Workflow retains Workflow semantics

Per CR-ES-006 §5 + ADR-ES-006 §5 ;;; Agentic Workflow MUST inherit
the Workflow semantics rather than redefine Workflow.

Test:

```python
def test_awf_inherits_workflow_semantics():
    workflow_record = load_concept('workflow')
    awf_record = load_concept('agentic-workflow')
    # Workflow identity preserved
    assert workflow_record['canonical_name'] == 'Workflow'
    # Agentic Workflow does not redefine Workflow
    assert awf_record['specializes'][0] == 'ES:CONCEPT:workflow'
    # No concurrent Workflow definition in AWF
    assert 'workflow_definition' not in awf_record
```

## AWF-CON-014 ;; Agentic Workflow preserves grounding and provenance

Per CR-ES-006 §21 + ADR-ES-006 §23 ;;; the Agentic Workflow concept
record MUST carry:

- `governance:` top-level field
- `provenance:` list with CR-ES-006 + ADR-ES-006 sources
- `grounding:` with WSF + Enterprise-Semantics authority

Test:

```python
def test_awf_governance_field():
    record = load_concept('agentic-workflow')
    assert record['governance'] == 'enterprise-semantics'

def test_awf_provenance_field():
    record = load_concept('agentic-workflow')
    sources = [p['source'] for p in record['provenance']]
    assert 'CR-ES-006' in sources
    assert 'ADR-ES-006' in sources
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-006 §28 + ADR-ES-006 §23