# Lifecycle tests for Agentic Operations

## AOP-CON-005 ;; Agentic Operations is outcome-oriented

Per CR-ES-007 §7 + §23 + ADR-ES-007 §18 + §19 + §27, the
Agentic Operations concept record MUST have an `operational_intent`
property of type `reference` with `required: true`.

Test:

```python
def test_aop_operational_intent_required():
    record = load_concept('agentic-operations')
    intent_props = [p for p in record['properties']
                    if p['name'] == 'operational_intent']
    assert len(intent_props) == 1
    assert intent_props[0]['type'] == 'reference'
    assert intent_props[0]['required'] is True
```

## AOP-CON-003 ;; Agentic Operations operates within defined authority

Per CR-ES-007 §7 + §23 + ADR-ES-007 §6.7 + §19, the Agentic
Operations concept record MUST have an `authority_context` property
of type `reference` with `required: true`.

Test:

```python
def test_aop_authority_context_required():
    record = load_concept('agentic-operations')
    auth_props = [p for p in record['properties']
                  if p['name'] == 'authority_context']
    assert len(auth_props) == 1
    assert auth_props[0]['type'] == 'reference'
    assert auth_props[0]['required'] is True
```

## AOP-CON-004 ;; Operational behavior governed by policies

Per CR-ES-007 §7 + §23 + ADR-ES-007 §6.7, the Agentic Operations
concept record MUST have a `policy_context` property of type
`reference` with `required: true`.

Test:

```python
def test_aop_policy_context_required():
    record = load_concept('agentic-operations')
    policy_props = [p for p in record['properties']
                    if p['name'] == 'policy_context']
    assert len(policy_props) == 1
    assert policy_props[0]['type'] == 'reference'
    assert policy_props[0]['required'] is True
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-007 §7 + ADR-ES-007 §19