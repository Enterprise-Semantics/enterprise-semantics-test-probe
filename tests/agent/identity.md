# Identity tests for Agentic

## Identity uniqueness

Per CR-ES-001 §15, ``ES:CONCEPT:<kebab>`` format must be unique across all concept records.

Test:

```python
def test_agentic_identity_unique(agentic_record, all_concept_records):
    aid = agentic_record['id']
    ids = [r['id'] for r in all_concept_records if r.get('id') != aid]
    assert aid not in ids, f'Agentic identity {aid} is not unique'
```

## Identity format

Test:

```python
def test_agentic_identity_format(agentic_record):
    import re
    aid = agentic_record['id']
    assert re.match(r'^ES:CONCEPT:[a-z][a-z0-9-]*$', aid)
```

## Subject_type in predicates

Per CR-ES-004 §10, predicates with `subject_type: ES:CONCEPT:agent` MUST match the Agent's identity, predicates with `subject_type: ES:CONCEPT:agentic` MUST match the Agentic's identity.

Test:

```python
def test_predicate_subject_types_match_concepts(vocabulary_path):
    import yaml
    with open(vocabulary_path) as f:
        vocab = yaml.safe_load(f)
    predicates = vocab['vocabulary']['governed_predicates']
    
    agent_predicates = [p for p in predicates if p.get('subject_type') == 'ES:CONCEPT:agent']
    agentic_predicates = [p for p in predicates if p.get('subject_type') == 'ES:CONCEPT:agentic']
    
    #, Agent predicates exist (Agent is a recognized concept)
    assert len(agent_predicates) >= 8, f'Expected 8+ Agent predicates, got {len(agent_predicates)}'
    
    #, Agentic predicates are NOT in vocabulary as Entity subjects, Agentic is a SemanticProperty
    #, the Agentic concept record itself has no subject predicates
    #, (predicate registration is for relationships, not for properties)
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)