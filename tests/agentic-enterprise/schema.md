# Schema tests for Agentic Enterprise

## AE-CON-001 ; Agentic Enterprise specialises Enterprise

Per CR-ES-010 §2 + ADR-ES-010 §1 + §3, the Agentic Enterprise
concept record MUST declare a direct specialisation of Enterprise.

Test:

```python
def test_ae_specializes_enterprise():
    record = load_concept('agentic-enterprise')
    assert record['id'] == 'ES:CONCEPT:agentic-enterprise'
    assert 'ES:CONCEPT:enterprise' in record['specializes']

def test_ae_no_subtype_agentic_operations():
    record = load_concept('agentic-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-operations'

def test_ae_no_subtype_agentic_value_stream():
    record = load_concept('agentic-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-value-stream'

def test_ae_no_subtype_agentic_workflow():
    record = load_concept('agentic-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-workflow'

def test_ae_no_subtype_agent():
    record = load_concept('agentic-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agent'
```
