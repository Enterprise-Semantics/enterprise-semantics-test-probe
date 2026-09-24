# Relationship tests for Autonomous Enterprise

## 14 canonical relationships (per CR-ES-011 §5)

Per CR-ES-011 §5 + ADR-ES-011 §11-§15, the Autonomous Enterprise
concept record MUST declare 14 canonical relationships.

Test:

```python
def test_ae_enterprise_realizes_through():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'autonomous-enterprise-realizes-through']
    assert any(r['object'] == 'ES:CONCEPT:autonomous-value-stream' for r in rels)

def test_ae_enterprise_operates_through():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'autonomous-enterprise-operates-through']
    assert any(r['object'] == 'ES:CONCEPT:autonomous-operations' for r in rels)

def test_ae_specializes_enterprise():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'specializes']
    assert any(r['object'] == 'ES:CONCEPT:enterprise' for r in rels)

def test_ae_operates_within_authority():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'operates-within']
    assert any(r['object'] == 'ES:CONCEPT:authority' for r in rels)

def test_ae_governed_by_policy():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'governed-by']
    assert any('policy' in r.get('object', '').lower() for r in rels)

def test_ae_uses_agentic_operations_mixed_mode():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'uses']
    assert any(r['object'] == 'ES:CONCEPT:agentic-operations' for r in rels)

def test_ae_uses_agentic_workflow():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'uses']
    assert any(r['object'] == 'ES:CONCEPT:agentic-workflow' for r in rels)

def test_ae_realizes_through_agentic_value_stream():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'autonomous-enterprise-realizes-through']
    assert any(r['object'] == 'ES:CONCEPT:agentic-value-stream' for r in rels)

def test_ae_produces_outcome():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'produces']
    assert any('outcome' in r.get('object', '').lower() for r in rels)

def test_ae_adapts_to_context():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'adapts-to']
    assert any('context' in r.get('object', '').lower() for r in rels)
```

## AE-AUTO-NEG-017 ; Autonomous Enterprise is NOT Autonomous Operations

Per AE-AUTO-NEG-017. The Autonomous Enterprise concept record MUST
NOT declare an identity relationship with Autonomous Operations.

Test:

```python
def test_ae_not_identity_with_autonomous_operations():
    record = load_concept('autonomous-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:autonomous-operations'

def test_ae_no_autonomous_operations_identity_relationship():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        if r.get('object') == 'ES:CONCEPT:autonomous-operations':
            assert r['predicate'] != 'is-a'
            assert r['predicate'] != 'specializes'
            assert r.get('qualification', '') != 'identity'
```

## AE-AUTO-NEG-018 ; Autonomous Enterprise is NOT Autonomous Value Stream

Per AE-AUTO-NEG-018.

Test:

```python
def test_ae_not_identity_with_autonomous_value_stream():
    record = load_concept('autonomous-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:autonomous-value-stream'

def test_ae_no_autonomous_value_stream_identity_relationship():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        if r.get('object') == 'ES:CONCEPT:autonomous-value-stream':
            assert r['predicate'] != 'is-a'
            assert r['predicate'] != 'specializes'
```
