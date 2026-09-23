# Provenance tests for Agentic Value Stream

## AVS-CON-012 ;; Agentic Value Stream instances carry appropriate grounding and provenance

Per CR-ES-005 §21 + ADR-ES-005 §17 ;; the Agentic Value Stream instance
MUST carry appropriate grounding and provenance.

Test:

```python
def test_avs_provenance_non_empty(avs_record):
    provenance = avs_record.get('provenance', [])
    assert len(provenance) > 0

def test_avs_provenance_cites_governing(avs_record):
    sources = ' '.join(p.get('source', '') for p in avs_record.get('provenance', []))
    assert any(ref in sources for ref in ['CR-ES-005', 'ADR-ES-005', 'FND-ES-AG-008'])

def test_avs_wsf_grounding(avs_record):
    wsf = avs_record.get('wsf_grounding', [])
    assert len(wsf) > 0, 'Agentic Value Stream must have wsf_grounding'

def test_avs_mappings_present(avs_record):
    mappings = avs_record.get('mappings', [])
    assert len(mappings) > 0, 'Agentic Value Stream must have mappings'
    authorities = {m['authority'] for m in mappings}
    assert 'wsf' in authorities
    assert 'opendea' in authorities
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)