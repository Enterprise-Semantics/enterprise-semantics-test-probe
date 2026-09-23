# Lifecycle tests for Agentic Workflow

## AWF-CON-005 ;; Agentic Workflow has an identifiable intent or execution objective

Per CR-ES-006 §5 + §12 + ADR-ES-006 §4.1 + §19 ;;; the Agentic
Workflow concept record MUST have a `workflow_intent` property of
type `reference` with `required: true`.

Test:

```python
def test_awf_workflow_intent_required():
    record = load_concept('agentic-workflow')
    intent_props = [p for p in record['properties']
                    if p['name'] == 'workflow_intent']
    assert len(intent_props) == 1
    assert intent_props[0]['type'] == 'reference'
    assert intent_props[0]['required'] is True
```

## AWF-CON-004 ;; Agentic Workflow operates within defined authority

Per CR-ES-006 §5 + §13 + ADR-ES-006 §4.6 + §11 ;;; the Agentic
Workflow concept record MUST have an `authority_context` property of
type `reference` with `required: true`.

Test:

```python
def test_awf_authority_context_required():
    record = load_concept('agentic-workflow')
    auth_props = [p for p in record['properties']
                  if p['name'] == 'authority_context']
    assert len(auth_props) == 1
    assert auth_props[0]['type'] == 'reference'
    assert auth_props[0]['required'] is True
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-006 §5 + ADR-ES-006 §19