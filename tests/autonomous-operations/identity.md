# Identity tests for Autonomous Operations

## Identity uniqueness

Per CR-ES-001 §15 ;; `ES:CONCEPT:<kebab>` format must be unique.

Test:

```python
def test_auto_identity_unique():
    all_ids = [c['id'] for c in all_concepts()]
    assert all_ids.count('ES:CONCEPT:autonomous-operations') == 1

def test_auto_id_format():
    record = load_concept('autonomous-operations')
    assert record['id'] == 'ES:CONCEPT:autonomous-operations'
    assert re.match(r'^ES:CONCEPT:[a-z][a-z0-9-]*$', record['id'])
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-008 §6 + ADR-ES-002 §11