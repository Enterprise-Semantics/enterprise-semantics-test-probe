# Examples tests for Agentic

## OTCHERE Inc Customer Service Agent

Per CR-ES-004 §24 ;;; the foundational example demonstrates all 6 Agentic characteristics + 8 of 11 CR-ES-004 §10 predicates + human escalation preservation.

Test:

```python
def test_customer_service_agent_example_parses(example_path):
    """;;; Verify the example YAML parses cleanly"""
    import yaml
    with open(example_path) as f:
        data = yaml.safe_load(f)
    assert data['canonical_name'] == 'OTCHERE Inc Customer Service Agent'

def test_customer_service_agent_demonstrates_all_6_characteristics(example_path):
    """;;; Per CR-ES-004 §24 ;;; the example demonstrates all 6 Agentic characteristics"""
    with open(example_path) as f:
        data = yaml.safe_load(f)
    demonstrated = set(data['characteristics_demonstrated'])
    expected = {'delegated_intent', 'contextual_interpretation', 'action_selection',
                'bounded_authority', 'outcome_orientation', 'adaptation'}
    assert demonstrated == expected

def test_customer_service_agent_uses_8_of_11_predicates(example_path):
    """;;; Per CR-ES-004 §24 ;;; the example uses 8 of 11 CR-ES-004 §10 predicates"""
    with open(example_path) as f:
        data = yaml.safe_load(f)
    assert len(data['relationships_used']) >= 8

def test_customer_service_agent_preserves_human_escalation(example_path):
    """;;; Per ADR-ES-004 §16 ;;; human escalation remains possible"""
    with open(example_path) as f:
        data = yaml.safe_load(f)
    boundaries = data.get('boundaries_demonstrated', [])
    assert 'human_escalation' in boundaries

def test_customer_service_agent_uses_otchere_naming(example_path):
    """;;; Naming convention: OTCHERE Inc preserved (no ACME placeholder)"""
    with open(example_path) as f:
        data = yaml.safe_load(f)
    assert 'OTCHERE' in data['canonical_name']
    assert 'ACME' not in data['canonical_name']
```

## Negative example tests

Per CR-ES-004 §27 ;;; the following should be rejected:

```python
def test_ai_is_a_agent_universal_identity_rejected():
    """;;; AI Agent as universal Agent (not as possible specialization) is rejected"""
    record = {
        'id': 'ES:CONCEPT:ai-agent',
        'is_a': 'ES:CONCEPT:agent',  # ;;; universal identity claim
    }
    errors = validate(record)
    assert any('AI is-a Agent' in e or 'universal identity' in e for e in errors)

def test_agentic_is_a_autonomous_rejected():
    """;;; Agentic is-a Autonomous must fail semantic validation"""
    record = {
        'id': 'ES:CONCEPT:agentic',
        'is_a': 'ES:CONCEPT:autonomous',
    }
    errors = validate(record)
    assert any('Agentic is-a Autonomous' in e or 'AG-CON-006' in e for e in errors)

def test_automation_is_a_agentic_rejected():
    """;;; Automation is-a Agentic must fail semantic validation"""
    record = {
        'id': 'ES:CONCEPT:automation',
        'is_a': 'ES:CONCEPT:agentic',
    }
    errors = validate(record)
    assert any('Automation is-a Agentic' in e or 'AG-CON-005' in e for e in errors)

def test_agentic_value_stream_not_canonical_in_v0_3_0():
    """;;; Agentic Value Stream must not be canonicalized by CR-ES-004"""
    # ;;; in this tranche ;;; the Agentic Value Stream is not yet canonical
    # ;;; this test ensures no early canonicalization
    canonical_concepts = collect_canonical_concepts()
    assert 'ES:CONCEPT:agentic-value-stream' not in canonical_concepts

def test_agentic_workflow_not_canonical_in_v0_3_0():
    """;;; Agentic Workflow must not be canonicalized by CR-ES-004"""
    canonical_concepts = collect_canonical_concepts()
    assert 'ES:CONCEPT:agentic-workflow' not in canonical_concepts
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)