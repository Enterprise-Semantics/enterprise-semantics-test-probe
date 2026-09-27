# Boundary tests for Agentic Enterprise

## AE-NEG-001 ; Agentic Enterprise is NOT AI Enterprise

Per ADR-ES-010 §11 + AE-NEG-001. AI is not a defining characteristic
of Agentic Enterprise.

Test:

```python
def test_ae_not_ai_enterprise():
    record = load_concept('agentic-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:ai-enterprise'
    # verify no AI concept appears as a mandatory relationship target
    ai_targets = [r for r in record['relationships']
                  if 'ai' in str(r.get('object', '')).lower()]
    for r in ai_targets:
        # AI may appear as an external reference but not as a
        # specialisation; verify status is not 'mandatory'
        assert r.get('status', 'proposed') in ('proposed', 'external', 'informational')
```

## AE-NEG-002 ; Agentic Enterprise does NOT require AI

Per AE-CON-010 + AE-NEG-002. AI is not required.

Test:

```python
def test_ae_does_not_require_ai():
    record = load_concept('agentic-enterprise')
    # verify no relationship declares AI as a mandatory dependency
    for r in record['relationships']:
        if 'ai' in str(r.get('object', '')).lower():
            # AI may exist as an external reference, but not as a
            # required dependency
            assert r.get('qualification', '') != 'mandatory'
            assert r.get('rationale', '').lower().find('requires ai') == -1
```
