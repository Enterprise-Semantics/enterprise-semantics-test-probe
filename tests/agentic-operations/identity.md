# Identity tests for Agentic Operations

## Identity uniqueness

Per CR-ES-001 §15 ;; `ES:CONCEPT:<kebab>` format must be unique.

Test:

```python
def test_aop_identity_unique():
    all_ids = [c['id'] for c in all_concepts()]
    assert all_ids.count('ES:CONCEPT:agentic-operations') == 1

def test_aop_id_format():
    record = load_concept('agentic-operations')
    assert record['id'] == 'ES:CONCEPT:agentic-operations'
    assert re.match(r'^ES:CONCEPT:[a-z][a-z0-9-]*$', record['id'])
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-007 §6 + ADR-ES-002 §11