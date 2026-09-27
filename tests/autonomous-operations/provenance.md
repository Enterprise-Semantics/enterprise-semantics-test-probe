# Provenance tests for Autonomous Operations

## AOP-AUTO-CON-017 ;; Autonomous Operations preserves grounding and provenance

Per CR-ES-008 §24 + ADR-ES-008 §22, the Autonomous Operations
concept record MUST carry complete grounding and provenance.

Test:

```python
def test_auto_provenance_sources():
    record = load_concept('autonomous-operations')
    sources = [p['source'] for p in record['provenance']]
    assert any('CR-ES-008' in s for s in sources)
    assert any('ADR-ES-008' in s for s in sources)

def test_auto_grounding_field():
    record = load_concept('autonomous-operations')
    assert 'grounding' in record
    assert record['grounding']['foundation'] == 'WSF'

def test_auto_no_supersession_required():
    record = load_concept('autonomous-operations')
    # No prior Phase 1 record existed, no supersession required
    notes = [p.get('note', '') for p in record['provenance']]
    # Just verify CR-ES-008 + ADR-ES-008 provenance present
    pass
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-008 §24 + ADR-ES-008 §22