# Provenance tests for Agentic Workflow

## AWF-CON-014 ;; Agentic Workflow preserves grounding and provenance

Per CR-ES-006 §28 + ADR-ES-006 §23 ;;; the Agentic Workflow concept
record MUST carry complete grounding and provenance.

Test:

```python
def test_awf_provenance_sources():
    record = load_concept('agentic-workflow')
    sources = [p['source'] for p in record['provenance']]
    # CR-ES-006 + ADR-ES-006 must be cited
    assert any('CR-ES-006' in s for s in sources)
    assert any('ADR-ES-006' in s for s in sources)

def test_awf_grounding_field():
    record = load_concept('agentic-workflow')
    assert 'grounding' in record
    assert record['grounding']['foundation'] == 'WSF'
    assert record['grounding']['semantic_authority'] == 'Enterprise-Semantics'

def test_awf_supersession_recorded():
    record = load_concept('agentic-workflow')
    notes = [p.get('note', '') for p in record['provenance']]
    supersession = any('superseded' in n.lower() or 'profile hypothesis' in n.lower()
                       for n in notes)
    assert supersession  # FND-ES-AG-003 Profile hypothesis superseded
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-006 §28 + ADR-ES-006 §23