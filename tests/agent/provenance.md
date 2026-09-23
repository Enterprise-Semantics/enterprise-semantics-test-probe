# Provenance tests for Agentic

## Provenance must be non-empty

Per the existing schema validation (VS-CON-014 pattern for Value Stream) ;;; every Concept record MUST declare a non-empty `provenance` field listing the governing CR + ADR + FND references.

Test:

```python
def test_agent_provenance_non_empty(agent_record):
    provenance = agent_record.get('provenance', [])
    assert len(provenance) > 0, 'Agent concept must have non-empty provenance'

def test_agentic_provenance_non_empty(agentic_record):
    provenance = agentic_record.get('provenance', [])
    assert len(provenance) > 0, 'Agentic concept must have non-empty provenance'

def test_intent_provenance_non_empty(intent_record):
    provenance = intent_record.get('provenance', [])
    assert len(provenance) > 0

def test_authority_provenance_non_empty(authority_record):
    provenance = authority_record.get('provenance', [])
    assert len(provenance) > 0

def test_action_provenance_non_empty(action_record):
    provenance = action_record.get('provenance', [])
    assert len(provenance) > 0
```

## Provenance must cite governing artefacts

Per CR-ES-004 + ADR-ES-004 ;;; provenance MUST cite at least one of: CR-ES-004 + ADR-ES-004 + FND-ES-AG-008.

Test:

```python
def test_agent_provenance_cites_governing(agent_record):
    sources = ' '.join(p.get('source', '') for p in agent_record.get('provenance', []))
    assert any(ref in sources for ref in ['CR-ES-004', 'ADR-ES-004', 'FND-ES-AG-008'])
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)