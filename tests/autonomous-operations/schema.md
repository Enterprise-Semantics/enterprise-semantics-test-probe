# Schema tests for Autonomous Operations

## AOP-AUTO-CON-001 ;; Autonomous Operations specialises Operations

Per CR-ES-008 §24 + ADR-ES-008 §22, the Autonomous Operations
concept record MUST declare a direct specialisation of Operations.

Test:

```python
def test_auto_specializes_operations():
    record = load_concept('autonomous-operations')
    assert record['id'] == 'ES:CONCEPT:autonomous-operations'
    assert 'ES:CONCEPT:operations' in record['specializes']

def test_auto_specialization_predicate():
    record = load_concept('autonomous-operations')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    assert any(r['object'] == 'ES:CONCEPT:operations' for r in specializes_rels)

def test_auto_no_subtype_agentic_operations():
    record = load_concept('autonomous-operations')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-operations'

def test_auto_no_subtype_agentic_workflow():
    record = load_concept('autonomous-operations')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-workflow'

def test_auto_no_subtype_agentic_value_stream():
    record = load_concept('autonomous-operations')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-value-stream'
```

## AOP-AUTO-CON-017 ;; Autonomous Operations preserves grounding and provenance

Per CR-ES-008 §24 + ADR-ES-008 §22, the Autonomous Operations
concept record MUST carry grounding and provenance.

Test:

```python
def test_auto_governance_field():
    record = load_concept('autonomous-operations')
    assert record['governance'] == 'enterprise-semantics'

def test_auto_provenance_field():
    record = load_concept('autonomous-operations')
    sources = [p['source'] for p in record['provenance']]
    assert 'CR-ES-008' in sources
    assert 'ADR-ES-008' in sources

def test_auto_grounding_field():
    record = load_concept('autonomous-operations')
    assert 'grounding' in record
    assert record['grounding']['foundation'] == 'WSF'
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-008 §24 + ADR-ES-008 §22