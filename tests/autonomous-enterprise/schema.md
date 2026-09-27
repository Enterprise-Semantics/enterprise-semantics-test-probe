# Schema tests for Autonomous Enterprise

## AE-AUTO-CON-001 ; Autonomous Enterprise specialises Enterprise

Per CR-ES-011 §2 + ADR-ES-011 §1 + §3.1, the Autonomous Enterprise
concept record MUST declare a direct specialisation of Enterprise.

Test:

```python
def test_ae_specializes_enterprise():
    record = load_concept('autonomous-enterprise')
    assert record['id'] == 'ES:CONCEPT:autonomous-enterprise'
    assert 'ES:CONCEPT:enterprise' in record['specializes']

def test_ae_no_subtype_agentic_enterprise():
    record = load_concept('autonomous-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-enterprise'

def test_ae_no_subtype_autonomous_operations():
    record = load_concept('autonomous-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:autonomous-operations'

def test_ae_no_subtype_autonomous_value_stream():
    record = load_concept('autonomous-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:autonomous-value-stream'
```
