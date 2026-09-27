# Lifecycle tests for Agentic Enterprise

## AE-CON-017 ; Defined governance boundaries

Per AE-CON-017 + ADR-ES-010 §17, the Agentic Enterprise concept
record MUST declare defined governance boundaries.

Test:

```python
def test_ae_governance_field_present():
    record = load_concept('agentic-enterprise')
    assert 'governance' in record
    assert record['governance'] == 'enterprise-semantics'
```

## AE-NEG-016 ; Agentic Enterprise implies Autonomous Enterprise (FALSE)

Per AE-NEG-016. The Agentic Enterprise does NOT imply the
Autonomous Enterprise; they are orthogonal.

Test:

```python
def test_ae_no_autonomous_implication():
    record = load_concept('agentic-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    # verify no relationship claims Agentic Enterprise specialises
    # Autonomous Enterprise
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:autonomous-enterprise'

def test_ae_no_autonomous_identity_relationship():
    record = load_concept('agentic-enterprise')
    for r in record['relationships']:
        # no identity predicate with Autonomous Enterprise
        if r.get('object') == 'ES:CONCEPT:autonomous-enterprise':
            assert r.get('predicate') != 'is-a'
            assert r.get('predicate') != 'specializes'
```
