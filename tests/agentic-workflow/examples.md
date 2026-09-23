# Examples tests for Agentic Workflow

## OTCHERE Inc Order Fulfillment (Workflow + Agentic Workflow)

Per CR-ES-006 §27 ;;; the foundational examples demonstrate:

- 6 conventional Workflow steps
- 10 Agentic Workflow steps with agentic interpretation ;;; bounded
  authority ;;; dynamic action selection ;;; coordination ;;; and
  runtime adaptation

Test:

```python
def test_awf_conventional_workflow_steps():
    record = load_example('order-fulfillment-workflow')
    assert len(record['conventional_workflow']['steps']) == 6

def test_awf_agentic_workflow_steps():
    record = load_example('order-fulfillment-agentic-workflow')
    assert len(record['agentic_workflow']['steps']) >= 9

def test_awf_example_8_characteristics():
    record = load_example('order-fulfillment-agentic-workflow')
    boundaries = record['boundaries_demonstrated']
    # Must reference all 8 characteristics
    required_chars = [
        'workflow_intent', 'contextual_interpretation', 'dynamic_routing',
        'agentic_coordination', 'adaptive_execution',
        'bounded_decision_authority', 'exception_interpretation',
        'human_intervention'
    ]
    assert all(any(req in str(b) for b in boundaries) for req in required_chars)
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-006 §27 + ADR-ES-006 §21