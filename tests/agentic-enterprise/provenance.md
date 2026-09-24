# Provenance tests for Agentic Enterprise

## AE-CON-018 ; Provenance and semantic grounding

Per AE-CON-018 + ADR-ES-001, the Agentic Enterprise concept record
MUST declare complete provenance citing CR-ES-010 + ADR-ES-010.

Test:

```python
def test_ae_provenance_cites_cr_es_010():
    record = load_concept('agentic-enterprise')
    provenance = record.get('provenance', [])
    sources = [p.get('source', '') for p in provenance]
    assert any('CR-ES-010' in s for s in sources)

def test_ae_provenance_cites_adr_es_010():
    record = load_concept('agentic-enterprise')
    provenance = record.get('provenance', [])
    sources = [p.get('source', '') for p in provenance]
    assert any('ADR-ES-010' in s for s in sources)

def test_ae_provenance_supersedes_prior_hypothesis():
    record = load_concept('agentic-enterprise')
    supersedes = record.get('supersedes', [])
    assert len(supersedes) >= 1
    # the prior Profile-of-Enterprise hypothesis from FND-ES-AG-005
    # is documented as superseded
    for entry in supersedes:
        notes = entry.get('note', '').lower()
        assert 'profile-of-enterprise' in notes or 'specialisation-of-enterprise' in notes

def test_ae_cardinal_author_signature():
    record = load_concept('agentic-enterprise')
    provenance = record.get('provenance', [])
    sources_text = ' '.join(p.get('note', '') for p in provenance)
    assert 'Emmanuel A. Otchere' in sources_text or 'cardinal author' in sources_text.lower()
```
