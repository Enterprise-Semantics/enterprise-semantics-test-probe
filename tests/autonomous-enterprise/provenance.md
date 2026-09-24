# Provenance tests for Autonomous Enterprise

## AE-AUTO-CON-022 ; Provenance and semantic grounding

Per AE-AUTO-CON-022 + ADR-ES-001, the Autonomous Enterprise concept
record MUST declare complete provenance citing CR-ES-011 + ADR-ES-011.

Test:

```python
def test_ae_provenance_cites_cr_es_011():
    record = load_concept('autonomous-enterprise')
    provenance = record.get('provenance', [])
    sources = [p.get('source', '') for p in provenance]
    assert any('CR-ES-011' in s for s in sources)

def test_ae_provenance_cites_adr_es_011():
    record = load_concept('autonomous-enterprise')
    provenance = record.get('provenance', [])
    sources = [p.get('source', '') for p in provenance]
    assert any('ADR-ES-011' in s for s in sources)

def test_ae_provenance_cites_v1_release():
    record = load_concept('autonomous-enterprise')
    provenance = record.get('provenance', [])
    notes = ' '.join(p.get('note', '') for p in provenance)
    assert 'v1.0.0' in notes or 'first major release' in notes.lower()

def test_ae_cardinal_author_signature():
    record = load_concept('autonomous-enterprise')
    provenance = record.get('provenance', [])
    sources_text = ' '.join(p.get('note', '') for p in provenance)
    assert 'Emmanuel A. Otchere' in sources_text or 'cardinal author' in sources_text.lower()
```
