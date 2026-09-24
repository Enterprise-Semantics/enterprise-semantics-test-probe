# Boundaries tests for Agentic Workflow

## AWF-CON-011 ;; Agentic Workflow is not a Process

Per CR-ES-006 §9 + ADR-ES-006 §6 + §24.4, the relationship
`Agentic Workflow is-a Process` MUST be invalid.

Test:

```python
def test_awf_is_not_process():
    record = load_concept('agentic-workflow')
    # No "is-a" or equivalent predicate to process
    invalid = [r for r in record['relationships']
               if r['object'] == 'ES:CONCEPT:process'
               or r['object'] == 'external:concept:process']
    for r in invalid:
        assert r['predicate'] not in ['is-a', 'specializes']
```

## AWF-CON-012 ;; Agentic Workflow is not a Value Stream

Per ADR-ES-006 §15 + §24.6 + AWF-CON-012, the relationship
`Agentic Workflow is-a Value Stream` MUST be invalid.

Test:

```python
def test_awf_is_not_value_stream():
    record = load_concept('agentic-workflow')
    value_stream_refs = [r for r in record['relationships']
                         if 'value-stream' in str(r['object']).lower()]
    for r in value_stream_refs:
        assert r['predicate'] not in ['is-a']
```

## AWF-CON-013 ;; Agentic Workflow is not an Agent

Per ADR-ES-006 §8 + AWF-CON-013, the relationship
`Agentic Workflow is-a Agent` MUST be invalid.

Test:

```python
def test_awf_is_not_agent():
    record = load_concept('agentic-workflow')
    # Agent is engaged, not is-a
    agent_refs = [r for r in record['relationships']
                  if r['object'] == 'ES:CONCEPT:agent']
    for r in agent_refs:
        assert r['predicate'] in ['engages']  # only engagement allowed
```

## AWF-CON-009 ;; Agentic Workflow does not require AI

Per ADR-ES-006 §14 + AWF-CON-009, the concept record MUST NOT
declare AI as a semantic requirement.

Test:

```python
def test_awf_does_not_require_ai():
    record = load_concept('agentic-workflow')
    # No AI vendor mentioned in definition
    assert 'ai' not in record['definition'].lower().split() or \
           'not necessarily' in record['definition'].lower() or \
           'ai-based' in record['definition'].lower()  # allowed forms
```

## AWF-CON-010 ;; Agentic Workflow does not imply autonomy

Per ADR-ES-006 §17 + AWF-CON-010, the concept record MUST NOT
declare Autonomous Workflow semantics.

Test:

```python
def test_awf_does_not_imply_autonomy():
    record = load_concept('agentic-workflow')
    assert 'autonomous' not in record['canonical_name'].lower()
    # Definition should reference bounded authority, not autonomy
    assert 'autonomous' not in record['definition'].lower() or \
           'autonomous workflow' not in record['definition'].lower()
```

## Negative test ;; Workflow merely containing an Agent

Per ADR-ES-006 §10 + §24.5, the material-participation criterion
is enforced.

Test:

```python
def test_awf_material_participation():
    record = load_concept('agentic-workflow')
    # Must have all 8 characteristics
    assert len(record['characteristics']) >= 8
    # Must reference material participation in definition
    definition = record['definition'].lower()
    assert 'interpret' in definition or 'select' in definition or \
           'agentic behavior' in definition
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-006 §28 + §29 + ADR-ES-006 §23