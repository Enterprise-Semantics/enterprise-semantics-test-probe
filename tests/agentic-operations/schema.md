# Schema tests for Agentic Operations

## AOP-CON-001 ;; Agentic Operations specialises Operations

Per CR-ES-007 §21 + §23 + ADR-ES-007 §2 + §21 + §27, the
Agentic Operations concept record MUST declare a direct
specialisation of Operations.

Test:

```python
def test_aop_specializes_operations():
    record = load_concept('agentic-operations')
    assert record['id'] == 'ES:CONCEPT:agentic-operations'
    assert 'ES:CONCEPT:operations' in record['specializes']

def test_aop_specialization_predicate():
    record = load_concept('agentic-operations')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    assert any(r['object'] == 'ES:CONCEPT:operations' for r in specializes_rels)
```

## AOP-CON-015 ;; Agentic Operations preserves grounding and provenance

Per CR-ES-007 §23 + ADR-ES-007 §27, the Agentic Operations
concept record MUST carry grounding and provenance.

Test:

```python
def test_aop_governance_field():
    record = load_concept('agentic-operations')
    assert record['governance'] == 'enterprise-semantics'

def test_aop_provenance_field():
    record = load_concept('agentic-operations')
    sources = [p['source'] for p in record['provenance']]
    assert 'CR-ES-007' in sources
    assert 'ADR-ES-007' in sources

def test_aop_grounding_field():
    record = load_concept('agentic-operations')
    assert 'grounding' in record
    assert record['grounding']['foundation'] == 'WSF'
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-007 §23 + ADR-ES-007 §27