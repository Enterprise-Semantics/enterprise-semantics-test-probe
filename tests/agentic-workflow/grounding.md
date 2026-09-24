# Grounding tests for Agentic Workflow

## ES-canonical novelty ;; Tier 2 Specialisation

Per FND-ES-AG-008 §1.3, Agentic Workflow is Tier 2 Specialisation:
WSF Tier 1 Activity grounds Workflow ;; WSF Tier 1 Workflow grounds
Agentic Workflow, Agentic Workflow adds ES-canonical novelty.

Test:

```python
def test_awf_tier2_classification():
    record = load_concept('agentic-workflow')
    classification = record['grounding'].get('classification', '')
    assert 'Tier 2' in classification

def test_awf_workflow_inheritance():
    record = load_concept('agentic-workflow')
    # Must reference WSF Activity via Workflow
    ws_refs = [p.get('ws_foundation_reference', '')
               for p in [record.get('grounding', {})]]
    assert any('Activity' in str(w) for w in ws_refs)

def test_awf_es_canonical_novelty():
    record = load_concept('agentic-workflow')
    # ES-canonical novelty = the 8 characteristics + 8 properties + 8 relationships
    assert len(record.get('characteristics', [])) >= 8
    assert len(record.get('properties', [])) >= 8
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per FND-ES-AG-008 §1.3 + ADR-ES-006 §16