# Relationships tests for Agentic Workflow

## AWF-CON-001 ;; Agentic Workflow specialises Workflow (relationship)

Per CR-ES-006 §5 + §18 + ADR-ES-006 §2 + §18 ;;; the Agentic Workflow
record MUST declare 8 canonical relationships.

Test:

```python
def test_awf_required_relationships():
    record = load_concept('agentic-workflow')
    predicates = [r['predicate'] for r in record['relationships']]
    required = ['specializes', 'engages', 'interprets',
                'operates-within', 'coordinates', 'produces']
    for p in required:
        assert p in predicates

def test_awf_specializes_workflow():
    record = load_concept('agentic-workflow')
    specializes = [r for r in record['relationships']
                   if r['predicate'] == 'specializes']
    assert any(r['object'] == 'ES:CONCEPT:workflow' for r in specializes)
```

## AWF-CON-007 ;; Agentic Workflow engages Agents

Per CR-ES-006 §11 + ADR-ES-006 §8 + §18 ;;; the Agentic Workflow
MUST engage Agent (inherited from CR-ES-004 + ADR-ES-004).

Test:

```python
def test_awf_engages_agent():
    record = load_concept('agentic-workflow')
    engages = [r for r in record['relationships']
               if r['predicate'] == 'engages']
    assert any(r['object'] == 'ES:CONCEPT:agent' for r in engages)
```

## AWF-CON-006 ;; Agentic Workflow coordinates Activities and Tasks

Per CR-ES-006 §10 + ADR-ES-006 §18 ;;; the Agentic Workflow MUST
coordinate Activities (and Tasks).

Test:

```python
def test_awf_coordinates_activities():
    record = load_concept('agentic-workflow')
    coords = [r for r in record['relationships']
              if r['predicate'] == 'coordinates']
    objects = [r['object'] for r in coords]
    assert any('activity' in str(o).lower() for o in objects)
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-006 §18 + ADR-ES-006 §18 + §23