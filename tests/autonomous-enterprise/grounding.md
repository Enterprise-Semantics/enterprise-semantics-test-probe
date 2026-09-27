# Grounding tests for Autonomous Enterprise

## AE-AUTO-CON-003 ; WSF grounding via Enterprise

Per CR-ES-011 §30 + ADR-ES-011 §30 + FND-ES-AG-008 §1.3, the
Autonomous Enterprise is a Tier 2 Specialisation + ES-canonical
novelty.

Test:

```python
def test_ae_tier2_specialisation():
    record = load_concept('autonomous-enterprise')
    wsf_grounding = record.get('wsf_grounding', [])
    assert any(
        g.get('wsf_concept_id', '').endswith('Entity')
        for g in wsf_grounding
    ), 'Autonomous Enterprise must declare WSF Entity grounding via Enterprise'

def test_ae_inherits_via_enterprise():
    record = load_concept('autonomous-enterprise')
    enterprise_record = load_concept('enterprise')
    assert enterprise_record['id'] == 'ES:CONCEPT:enterprise'
    assert 'ES:CONCEPT:enterprise' in record['specializes']

def test_ae_no_new_wsf_foundational_concept():
    record = load_concept('autonomous-enterprise')
    wsf_grounding = record.get('wsf_grounding', [])
    for g in wsf_grounding:
        # only WSF Entity grounding is acceptable at Tier 1
        assert g.get('wsf_concept_id', '').endswith('Entity')

def test_ae_orthogonal_to_agentic_enterprise():
    record = load_concept('autonomous-enterprise')
    orthogonal_rels = [r for r in record['relationships']
                       if r.get('predicate') == 'orthogonal-to']
    assert any(r['object'] == 'ES:CONCEPT:agentic-enterprise' for r in orthogonal_rels)
```
