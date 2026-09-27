# Provenance tests for Agentic Operations

## AOP-CON-015 ;; Agentic Operations preserves grounding and provenance

Per CR-ES-007 §23 + ADR-ES-007 §27, the Agentic Operations
concept record MUST carry complete grounding and provenance.

Test:

```python
def test_aop_provenance_sources():
    record = load_concept('agentic-operations')
    sources = [p['source'] for p in record['provenance']]
    assert any('CR-ES-007' in s for s in sources)
    assert any('ADR-ES-007' in s for s in sources)

def test_aop_grounding_field():
    record = load_concept('agentic-operations')
    assert 'grounding' in record
    assert record['grounding']['foundation'] == 'WSF'

def test_aop_supersession_recorded():
    record = load_concept('agentic-operations')
    notes = [p.get('note', '') for p in record['provenance']]
    supersession = any('superseded' in n.lower() or 'profile hypothesis' in n.lower()
                       for n in notes)
    assert supersession  # FND-ES-AG-004 Profile hypothesis superseded
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-007 §23 + ADR-ES-007 §27