# Identity tests for Autonomous Enterprise

## AE-AUTO-CON-002 ; Material enterprise-level autonomous behavior

Per ADR-ES-011 §3.1 + AE-AUTO-CON-002, the Autonomous Enterprise
concept record MUST declare material enterprise-level autonomous
behavior in value realisation, operational coordination,
decision-making, execution, or adaptation.

Test:

```python
def test_ae_identity_canonical():
    record = load_concept('autonomous-enterprise')
    assert record['id'] == 'ES:CONCEPT:autonomous-enterprise'
    assert record['canonical_name'] == 'Autonomous Enterprise'

def test_ae_definition_includes_material_autonomy():
    record = load_concept('autonomous-enterprise')
    definition = record['definition'].lower()
    assert 'independently' in definition or 'independent' in definition
    assert 'enterprise' in definition
    assert 'governance' in definition or 'authority' in definition

def test_ae_no_identity_collapse_with_agentic_enterprise():
    record = load_concept('autonomous-enterprise')
    assert 'agentic enterprise' not in record['canonical_name'].lower()
```
