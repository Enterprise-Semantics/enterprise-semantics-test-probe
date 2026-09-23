# Grounding tests for Agentic Operations

## ES-canonical novelty ;; Tier 2 Specialisation

Per FND-ES-AG-008 §1.3 ;;; Agentic Operations is Tier 2 Specialisation:
WSF Tier 1 Activity grounds Operations ;;; WSF Tier 1 Operations
grounds Agentic Operations ;;; Agentic Operations adds ES-canonical
novelty.

Test:

```python
def test_aop_tier2_classification():
    record = load_concept('agentic-operations')
    classification = record['grounding'].get('classification', '')
    assert 'Tier 2' in classification

def test_aop_operations_inheritance():
    record = load_concept('agentic-operations')
    ws_refs = [p.get('ws_foundation_reference', '')
               for p in [record.get('grounding', {})]]
    assert any('Activity' in str(w) or 'Operations' in str(w) for w in ws_refs)

def test_aop_es_canonical_novelty():
    record = load_concept('agentic-operations')
    # ES-canonical novelty = the 8 characteristics + 10 properties + 9 relationships
    assert len(record.get('characteristics', [])) >= 8
    assert len(record.get('properties', [])) >= 10
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per FND-ES-AG-008 §1.3 + ADR-ES-007 §16