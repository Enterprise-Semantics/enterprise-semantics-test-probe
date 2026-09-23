# Relationships tests for Agentic Operations

## AOP-CON-001 ;; Agentic Operations specialises Operations (relationship)

Per CR-ES-007 §21 + ADR-ES-007 §21 + §27 ;;; the Agentic Operations
record MUST declare 9 canonical relationships.

Test:

```python
def test_aop_required_relationships():
    record = load_concept('agentic-operations')
    predicates = [r['predicate'] for r in record['relationships']]
    required = ['specializes', 'engages', 'responds-to',
                'operates-within', 'governed-by', 'coordinates',
                'uses', 'produces', 'adapts-to']
    for p in required:
        assert p in predicates
```

## AOP-CON-007 ;; Agentic Operations uses Agentic Workflows

Per CR-ES-007 §8.7 + ADR-ES-007 §9 + §21 ;;; the Agentic Operations
MUST use Agentic Workflow.

Test:

```python
def test_aop_uses_agentic_workflow():
    record = load_concept('agentic-operations')
    uses = [r for r in record['relationships']
            if r['predicate'] == 'uses']
    assert any(r['object'] == 'ES:CONCEPT:agentic-workflow' for r in uses)
```

## AOP-CON-008 ;; Agentic Operations coordinates Processes

Per CR-ES-007 §8.6 + ADR-ES-007 §10 ;;; the Agentic Operations MUST
coordinate Process.

Test:

```python
def test_aop_coordinates_process():
    record = load_concept('agentic-operations')
    coords = [r for r in record['relationships']
              if r['predicate'] == 'coordinates']
    assert any('process' in str(r['object']).lower() for r in coords)
```

## AOP-CON-006 ;; Agentic Operations engages Agents

Per CR-ES-007 §8.2 + ADR-ES-007 §11 ;;; the Agentic Operations MUST
engage Agent.

Test:

```python
def test_aop_engages_agent():
    record = load_concept('agentic-operations')
    engages = [r for r in record['relationships']
               if r['predicate'] == 'engages']
    assert any(r['object'] == 'ES:CONCEPT:agent' for r in engages)
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-007 §21 + ADR-ES-007 §21 + §27