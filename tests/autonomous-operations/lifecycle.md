# Lifecycle tests for Autonomous Operations

## AOP-AUTO-CON-006 ;; Autonomous Operations is outcome-oriented

Per CR-ES-008 §7 + §24 + ADR-ES-008 §7.6 + §22 ;;; the Autonomous
Operations concept record MUST have an `operational_objective`
property of type `reference` with `required: true`.

Test:

```python
def test_auto_operational_objective_required():
    record = load_concept('autonomous-operations')
    obj_props = [p for p in record['properties']
                 if p['name'] == 'operational_objective']
    assert len(obj_props) == 1
    assert obj_props[0]['type'] == 'reference'
    assert obj_props[0]['required'] is True
```

## AOP-AUTO-CON-004 ;; Autonomous Operations operates within explicit authority

Per CR-ES-008 §7 + §24 + ADR-ES-008 §5 + §7.4 + §22 ;;; the
Autonomous Operations concept record MUST have an
`authority_context` property of type `reference` with `required: true`.

Test:

```python
def test_auto_authority_context_required():
    record = load_concept('autonomous-operations')
    auth_props = [p for p in record['properties']
                  if p['name'] == 'authority_context']
    assert len(auth_props) == 1
    assert auth_props[0]['type'] == 'reference'
    assert auth_props[0]['required'] is True
```

## AOP-AUTO-CON-005 ;; Autonomous Operations is governed by policies

Per CR-ES-008 §7 + §24 + ADR-ES-008 §14 + §22 ;;; the Autonomous
Operations concept record MUST have a `policy_context` property of
type `reference` with `required: true` AND a `constraint_context`
property of type `reference` with `required: true`.

Test:

```python
def test_auto_policy_context_required():
    record = load_concept('autonomous-operations')
    policy_props = [p for p in record['properties']
                    if p['name'] == 'policy_context']
    assert len(policy_props) == 1
    assert policy_props[0]['required'] is True

def test_auto_constraint_context_required():
    record = load_concept('autonomous-operations')
    constraint_props = [p for p in record['properties']
                        if p['name'] == 'constraint_context']
    assert len(constraint_props) == 1
    assert constraint_props[0]['required'] is True
```

## AOP-AUTO-CON-008 ;; Autonomous Operations provides escalation boundary

Per CR-ES-008 §7 + §24 + ADR-ES-008 §7.8 + §16 + §22 ;;; the
Autonomous Operations concept record MUST have an
`escalation_boundary` property of type `reference_set` with
`required: true`.

Test:

```python
def test_auto_escalation_boundary_required():
    record = load_concept('autonomous-operations')
    esc_props = [p for p in record['properties']
                 if p['name'] == 'escalation_boundary']
    assert len(esc_props) == 1
    assert esc_props[0]['required'] is True
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-008 §7 + ADR-ES-008 §7 + §22