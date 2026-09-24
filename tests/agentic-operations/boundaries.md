# Boundaries tests for Agentic Operations

## AOP-CON-013 ;; Agentic Operations is not Agentic Workflow

Per CR-ES-007 §10 + ADR-ES-007 §7 + §24.3, the relationship
`Agentic Operations is-a Agentic Workflow` MUST be invalid.

Test:

```python
def test_aop_is_not_agentic_workflow():
    record = load_concept('agentic-operations')
    awf_refs = [r for r in record['relationships']
                if r['object'] == 'ES:CONCEPT:agentic-workflow']
    for r in awf_refs:
        assert r['predicate'] not in ['is-a', 'specializes']
```

## AOP-CON-014 ;; Agentic Operations is not Agentic Value Stream

Per ADR-ES-007 §8 + §24.4 + AOP-CON-014, the relationship
`Agentic Operations is-a Agentic Value Stream` MUST be invalid.

Test:

```python
def test_aop_is_not_agentic_value_stream():
    record = load_concept('agentic-operations')
    avs_refs = [r for r in record['relationships']
                if 'value-stream' in str(r['object']).lower()]
    for r in avs_refs:
        assert r['predicate'] not in ['is-a']
```

## AOP-CON-012 ;; Agentic Operations does not imply Autonomous Operations

Per ADR-ES-007 §15 + §24.5 + AOP-CON-012, the relationship
`Agentic Operations implies Autonomous Operations` MUST be invalid.

Test:

```python
def test_aop_does_not_imply_autonomy():
    record = load_concept('agentic-operations')
    assert 'autonomous' not in record['canonical_name'].lower()
    # No relationship implies Autonomous Operations
    autonomous_refs = [r for r in record['relationships']
                       if 'autonomous' in str(r['object']).lower()]
    assert len(autonomous_refs) == 0
```

## AOP-CON-011 ;; Agentic Operations does not require AI

Per ADR-ES-007 §14 + §24.1 + AOP-CON-011, the concept record MUST
NOT declare AI as a semantic requirement.

Test:

```python
def test_aop_does_not_require_ai():
    record = load_concept('agentic-operations')
    # No AI vendor mentioned in definition
    definition = record['definition'].lower()
    assert 'ai' not in definition.split() or \
           'ai-based' in definition or \
           'ai-augmented' in definition  # allowed forms
```

## Negative test ;; Material participation criterion

Per ADR-ES-007 §28.6, mere Agent presence does not establish
material agentic operational behavior.

Test:

```python
def test_aop_material_participation():
    record = load_concept('agentic-operations')
    # Must have all 8 characteristics
    assert len(record['characteristics']) >= 8
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-007 §23 + §24 + ADR-ES-007 §27