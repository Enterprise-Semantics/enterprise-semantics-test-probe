# Grounding tests for Agentic Enterprise

## AE-CON-003 ; WSF grounding via Enterprise

Per CR-ES-010 §7 + ADR-ES-010 §1 + FND-ES-AG-008 §1.3, the Agentic
Enterprise is a Tier 2 Specialisation + ES-canonical novelty.

Test:

```python
def test_ae_tier2_specialisation():
    record = load_concept('agentic-enterprise')
    # WSF grounding inherited via Enterprise (Tier 1 Specialisation)
    wsf_grounding = record.get('wsf_grounding', [])
    assert any(
        g.get('wsf_concept_id', '').endswith('Entity')
        for g in wsf_grounding
    ), 'Agentic Enterprise must declare WSF Entity grounding via Enterprise'

def test_ae_inherits_via_enterprise():
    record = load_concept('agentic-enterprise')
    enterprise_record = load_concept('enterprise')
    # verify Agentic Enterprise inherits Enterprise grounding
    assert enterprise_record['id'] == 'ES:CONCEPT:enterprise'
    assert 'ES:CONCEPT:enterprise' in record['specializes']

def test_ae_no_new_wsf_foundational_concept():
    record = load_concept('agentic-enterprise')
    # Agentic Enterprise must not introduce a new WSF foundational
    # concept; it must inherit from WSF Entity via Enterprise
    wsf_grounding = record.get('wsf_grounding', [])
    for g in wsf_grounding:
        # only WSF Entity grounding is acceptable at Tier 1
        assert g.get('wsf_concept_id', '').endswith('Entity')
```
