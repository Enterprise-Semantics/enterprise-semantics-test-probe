# Boundaries tests for Autonomous Operations

## AOP-AUTO-CON-013 ;; Autonomous Operations is distinct from Agentic Operations

Per CR-ES-008 §10 + ADR-ES-008 §9 + §10 + §22, the relationship
`Autonomous Operations is-a Agentic Operations` MUST be invalid.

Test:

```python
def test_auto_is_not_agentic_operations():
    record = load_concept('autonomous-operations')
    aop_refs = [r for r in record['relationships']
                if r['object'] == 'ES:CONCEPT:agentic-operations']
    for r in aop_refs:
        assert r['predicate'] not in ['is-a', 'specializes']
```

## AOP-AUTO-CON-014 ;; Autonomous Operations is distinct from Agentic Workflow

Per CR-ES-008 §12 + ADR-ES-008 §12 + §22, the relationship
`Autonomous Operations is-a Agentic Workflow` MUST be invalid.

Test:

```python
def test_auto_is_not_agentic_workflow():
    record = load_concept('autonomous-operations')
    awf_refs = [r for r in record['relationships']
                if r['object'] == 'ES:CONCEPT:agentic-workflow']
    for r in awf_refs:
        assert r['predicate'] != 'specializes'
        # May only use (not specialise)
```

## AOP-AUTO-CON-015 ;; Autonomous Operations is distinct from Agentic Value Stream

Per ADR-ES-008 §13 + AOP-AUTO-CON-015, Autonomous Operations
MUST NOT specialise Agentic Value Stream.

Test:

```python
def test_auto_is_not_agentic_value_stream():
    record = load_concept('autonomous-operations')
    avs_refs = [r for r in record['relationships']
                if 'value-stream' in str(r['object']).lower()]
    for r in avs_refs:
        assert r['predicate'] != 'specializes'
```

## AOP-AUTO-CON-010 ;; Autonomous Operations does not require AI

Per ADR-ES-008 §19 + AOP-AUTO-CON-010, the concept record MUST
NOT declare AI as a semantic requirement.

Test:

```python
def test_auto_does_not_require_ai():
    record = load_concept('autonomous-operations')
    # No AI vendor mentioned in definition
    definition = record['definition'].lower()
    assert 'ai' not in definition.split() or \
           'ai-based' in definition or \
           'ai-augmented' in definition  # allowed forms
```

## Material participation criterion

Per ADR-ES-008 §7 + §28, autonomous behaviour must materially
participate in operational decision and action.

Test:

```python
def test_auto_material_participation():
    record = load_concept('autonomous-operations')
    # Must have all 8 characteristics
    assert len(record['characteristics']) >= 8
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-008 §25 + ADR-ES-008 §23