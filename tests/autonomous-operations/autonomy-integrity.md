# Autonomy integrity tests for Autonomous Operations

## 6-field integrity

Per CR-ES-008 §28 ;;; an asserted Autonomous Operations instance MUST
demonstrate at least 6 integrity fields:

- Defined operational objective
- Defined authority
- Defined autonomous decision scope
- Defined autonomous action scope
- Defined policy/constraint boundary
- Defined escalation boundary

An instance that merely contains AI/Agent/Automation/Workflow
SHALL NOT pass Autonomous Operations conformance.

Test:

```python
def test_auto_integrity_6_fields():
    record = load_concept('autonomous-operations')
    # 1. operational_objective
    obj_props = [p for p in record['properties']
                 if p['name'] == 'operational_objective']
    assert len(obj_props) == 1
    assert obj_props[0]['required'] is True

    # 2. authority_context
    auth_props = [p for p in record['properties']
                  if p['name'] == 'authority_context']
    assert len(auth_props) == 1
    assert auth_props[0]['required'] is True

    # 3. decision_scope
    decision_props = [p for p in record['properties']
                      if p['name'] == 'decision_scope']
    assert len(decision_props) == 1

    # 4. action_scope
    action_props = [p for p in record['properties']
                    if p['name'] == 'action_scope']
    assert len(action_props) == 1

    # 5. policy_context + constraint_context
    policy_props = [p for p in record['properties']
                    if p['name'] in ['policy_context', 'constraint_context']]
    assert len(policy_props) == 2

    # 6. escalation_boundary
    esc_props = [p for p in record['properties']
                 if p['name'] == 'escalation_boundary']
    assert len(esc_props) == 1
    assert esc_props[0]['required'] is True
```

## Negative test ;; Mere Agent / AI / Workflow presence is insufficient

Per CR-ES-008 §28 ;;; an instance that merely contains AI/Agent/
Automation/Workflow SHALL NOT pass Autonomous Operations conformance.

Test:

```python
def test_auto_mere_agent_presence_insufficient():
    record = load_concept('autonomous-operations')
    # Must have all 8 characteristics
    assert len(record['characteristics']) >= 8
    # autonomy_scope must be present
    auto_props = [p for p in record['properties']
                  if p['name'] == 'autonomy_scope']
    assert len(auto_props) == 1
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-008 §28