# Identity tests for Agentic Enterprise

## AE-CON-002 ; Material agentic participation

Per ADR-ES-010 §3 + §6 + AE-CON-002, the Agentic Enterprise
concept record MUST declare material agentic participation in
enterprise-level behaviour.

Test:

```python
def test_ae_identity_canonical():
    record = load_concept('agentic-enterprise')
    assert record['id'] == 'ES:CONCEPT:agentic-enterprise'
    assert record['canonical_name'] == 'Agentic Enterprise'

def test_ae_definition_includes_material_participation():
    record = load_concept('agentic-enterprise')
    definition = record['definition'].lower()
    assert 'agentic behavior' in definition
    assert 'material' in definition
    assert 'enterprise' in definition

def test_ae_no_identity_collapse_with_autonomous_enterprise():
    record = load_concept('agentic-enterprise')
    assert 'autonomous enterprise' not in record['canonical_name'].lower()
```
