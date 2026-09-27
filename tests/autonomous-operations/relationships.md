# Relationships tests for Autonomous Operations

## AOP-AUTO-CON-001 ;; Autonomous Operations specialises Operations (relationship)

Per CR-ES-008 §24 + ADR-ES-008 §22, the Autonomous Operations
record MUST declare 10 canonical relationships.

Test:

```python
def test_auto_required_relationships():
    record = load_concept('autonomous-operations')
    predicates = [r['predicate'] for r in record['relationships']]
    required = [
        'specializes', 'operates-within', 'governed-by', 'pursues',
        'responds-to', 'produces', 'adapts-to', 'escalates-to', 'uses'
    ]
    for p in required:
        assert p in predicates
    # Note: 'uses' appears twice (workflow + agentic-workflow)
    assert predicates.count('uses') >= 2
```

## AOP-AUTO-CON-009 ;; Autonomous Operations escalates to Human / Authority

Per CR-ES-008 §9.7 + ADR-ES-008 §7.8 + §8 + §17, the Autonomous
Operations MUST escalate to Human / Authority.

Test:

```python
def test_auto_escalates_to():
    record = load_concept('autonomous-operations')
    escalates = [r for r in record['relationships']
                 if r['predicate'] == 'escalates-to']
    assert len(escalates) >= 1
```

## AOP-AUTO-CON-013 ;; Autonomous Operations is distinct from Agentic Operations

Per CR-ES-008 §24 + ADR-ES-008 §9 + §10 + §22, Autonomous
Operations MUST NOT specialise Agentic Operations.

Test:

```python
def test_auto_not_subtype_agentic_operations():
    record = load_concept('autonomous-operations')
    specializes = [r for r in record['relationships']
                   if r['predicate'] == 'specializes']
    for r in specializes:
        assert r['object'] != 'ES:CONCEPT:agentic-operations'
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-008 §9 + §24 + ADR-ES-008 §17 + §22