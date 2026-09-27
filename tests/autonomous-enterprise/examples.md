# Examples integration tests for Autonomous Enterprise

## OTCHERE Inc example validation

The OTCHERE Inc Autonomous Enterprise example MUST demonstrate the
qualification criteria per CR-ES-011 §21 + AE-AUTO-CON-002 +
AE-AUTO-CON-007 + AE-AUTO-CON-008.

Test:

```python
def test_ae_otchere_example_validates():
    """The OTCHERE Inc example must demonstrate the Autonomous
    Enterprise qualification criteria per CR-ES-011 §21."""
    example = load_example('otchere-autonomous-enterprise')
    # verify example demonstrates a mixed operating model
    assert 'mixed_operating_model' in example
    # verify example declares enterprise-level outcomes
    assert 'enterprise_outcomes' in example
    # verify example declares escalation boundary
    assert 'escalation_boundary' in example
    # verify example declares intervention model
    assert 'intervention_model' in example
    # verify example declares bounded authority
    assert 'authority_context' in example
    assert 'unrestricted' in example.get('authority_context', '').lower()

def test_ae_otchere_example_orthogonal_to_agentic():
    """The OTCHERE Inc example must preserve the orthogonality
    invariant AE-AUTO-CON-013."""
    example = load_example('otchere-autonomous-enterprise')
    # the example may reference Agentic concepts (mixed mode) but
    # must not claim identity with Agentic Enterprise
    for r in example.get('relationships', []):
        assert r.get('object') != 'ES:CONCEPT:agentic-enterprise'

def test_ae_otchere_example_mixed_mode():
    """The OTCHERE Inc example must demonstrate a mixed operating
    model per AE-AUTO-CON-017."""
    example = load_example('otchere-autonomous-enterprise')
    mixed_model = example.get('mixed_operating_model', '')
    # verify the mixed operating model includes autonomous, agentic,
    # conventional, and human-led modes
    assert 'autonomous' in mixed_model.lower()
    assert 'agentic' in mixed_model.lower()
    assert 'conventional' in mixed_model.lower()
    assert 'human' in mixed_model.lower()
```
