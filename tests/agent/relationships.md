# Relationships tests for Agent + Agentic

## AG-CON-007, Agent must have an authority relationship when modeled as acting agentically

Per CR-ES-004 §26, if a concept record declares an Agent that operates agentically, the Agent MUST have an `acts-within` relationship to a defined Authority.

Test:

```python
def test_agent_authority_relationship(agent_record):
    if is_agentic(agent_record):
        rels = agent_record.get('relationships', [])
        assert any(
            r.get('subject') == 'ES:CONCEPT:agent' and
            r.get('predicate') == 'acts-within' and
            r.get('object') == 'ES:CONCEPT:authority'
            for r in rels
        ), 'Agent modeled as acting agentically must have acts-within authority relationship'
```

## AG-CON-008, Agentic execution must have an intent or objective

Per CR-ES-004 §26, an Agentic execution MUST include an Intent or objective, the Agent MUST have an `interprets` or `receives` relationship to an Intent.

Test:

```python
def test_agentic_has_intent(agentic_record):
    agent = get_agent_record()
    rels = agent.get('relationships', [])
    assert any(
        r.get('predicate') in ('interprets', 'receives') and
        r.get('object') == 'ES:CONCEPT:intent'
        for r in rels
    ), 'Agentic execution must have an intent or objective'
```

## AG-CON-009, Agentic execution must support action selection

Per CR-ES-004 §26, Agentic execution MUST support Action Selection, the Agent MUST have a `selects` relationship to an Action.

Test:

```python
def test_agentic_action_selection(agent_record):
    rels = agent_record.get('relationships', [])
    assert any(
        r.get('predicate') == 'selects' and
        r.get('object') == 'ES:CONCEPT:action'
        for r in rels
    ), 'Agentic execution must support action selection'
```

## AG-CON-010, Agentic execution must be outcome-oriented

Per CR-ES-004 §26, Agentic execution MUST be outcome-oriented, the Agent MUST have an `agent-produces` (or equivalent) relationship to an Outcome.

Test:

```python
def test_agentic_outcome_oriented(agent_record):
    rels = agent_record.get('relationships', [])
    produces_rels = [r for r in rels if r.get('predicate', '').endswith('produces') or r.get('predicate') == 'produces']
    assert any(
        r.get('object', '').endswith('outcome')
        for r in produces_rels
    ), 'Agentic execution must be outcome-oriented'
```

## Reference resolution

Per CR-ES-004 §25, references must resolve. Test:

```python
def test_relationships_resolve(agent_record):
    rels = agent_record.get('relationships', [])
    for r in rels:
        subject = r.get('subject')
        object = r.get('object')
        assert subject in canonical_ids() or subject.startswith('external:')
        assert object in canonical_ids() or object.startswith('external:')
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)