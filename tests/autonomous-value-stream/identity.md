# Identity tests for Autonomous Value Stream

## Identity uniqueness

Per CR-ES-001 §15 ;; `ES:CONCEPT:<kebab>` format must be unique.

Test:

```python
def test_avs_identity_unique():
    all_ids = [c['id'] for c in all_concepts()]
    assert all_ids.count('ES:CONCEPT:autonomous-value-stream') == 1

def test_avs_id_format():
    record = load_concept('autonomous-value-stream')
    assert record['id'] == 'ES:CONCEPT:autonomous-value-stream'
    assert re.match(r'^ES:CONCEPT:[a-z][a-z0-9-]*$', record['id'])
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-009 §6 + ADR-ES-002 §11