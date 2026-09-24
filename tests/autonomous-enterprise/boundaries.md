# Boundary tests for Autonomous Enterprise

## AE-AUTO-NEG-001 ; Autonomous Enterprise is NOT AI Enterprise

Per ADR-ES-011 §16 + AE-AUTO-NEG-001. AI is not a defining
characteristic.

Test:

```python
def test_ae_not_ai_enterprise():
    record = load_concept('autonomous-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:ai-enterprise'

def test_ae_ai_not_mandatory():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        if 'ai' in str(r.get('object', '')).lower():
            assert r.get('qualification', '') != 'mandatory'
```

## AE-AUTO-NEG-002 ; Autonomous Enterprise is NOT Automated Enterprise

Per ADR-ES-011 §17 + AE-AUTO-NEG-002. Automation alone does not
establish Autonomous Enterprise.

Test:

```python
def test_ae_not_automated_enterprise():
    record = load_concept('autonomous-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:automated-enterprise'

def test_ae_automation_not_sufficient():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'automation establishes autonomous enterprise' not in rationale
```

## AE-AUTO-NEG-003 ; Autonomous Enterprise is NOT Agentic Enterprise

Per ADR-ES-011 §11 + AE-AUTO-CON-013 + AE-AUTO-NEG-003. The two
are orthogonal.

Test:

```python
def test_ae_not_agentic_enterprise():
    record = load_concept('autonomous-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-enterprise'

def test_ae_no_identity_with_agentic_enterprise():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        if r.get('object') == 'ES:CONCEPT:agentic-enterprise':
            assert r['predicate'] not in ('is-a', 'specializes', 'isa')
```
