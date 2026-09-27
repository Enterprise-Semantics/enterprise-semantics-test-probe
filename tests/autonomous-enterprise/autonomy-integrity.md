# Autonomy integrity tests for Autonomous Enterprise

## AE-AUTO-CON-005 ; Authority boundary

Per AE-AUTO-CON-005 + ADR-ES-011 §10, the Autonomous Enterprise
operates within defined authority.

Test:

```python
def test_ae_authority_field_present():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'operates-within']
    assert any(r['object'] == 'ES:CONCEPT:authority' for r in rels)

def test_ae_authority_not_unrestricted():
    """An Autonomous Enterprise instance with authority = unrestricted
    fails conformance per AE-AUTO-CON-018."""
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'unrestricted' not in rationale or 'fail' in rationale
```

## AE-AUTO-CON-006 ; Policy governance boundary

Per AE-AUTO-CON-006 + ADR-ES-011 §15.

Test:

```python
def test_ae_governed_by_policy():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'governed-by']
    assert any('policy' in r.get('object', '').lower() for r in rels)

def test_ae_constrained_by_constraint():
    record = load_concept('autonomous-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'constrained-by']
    assert any('constraint' in r.get('object', '').lower() for r in rels)
```

## AE-AUTO-CON-010 ; Human participation remains valid

Per AE-AUTO-CON-010 + ADR-ES-011 §9.

Test:

```python
def test_ae_human_participation_valid():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'elimination of humans' not in rationale
        assert 'human-free' not in rationale
```

## AE-AUTO-CON-011 ; AI is not required

Per AE-AUTO-CON-011 + ADR-ES-011 §16.

Test:

```python
def test_ae_ai_not_required():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'requires ai' not in rationale
```

## AE-AUTO-NEG-005 ; AI does NOT automatically establish Autonomous Enterprise

Per AE-AUTO-NEG-005.

Test:

```python
def test_ae_ai_does_not_establish():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'ai establishes autonomous enterprise' not in rationale
```

## AE-AUTO-NEG-006 ; Automation does NOT automatically establish Autonomous Enterprise

Per AE-AUTO-NEG-006 + AE-AUTO-CON-012.

Test:

```python
def test_ae_automation_does_not_establish():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'automation establishes autonomous enterprise' not in rationale
        assert 'automation is sufficient' not in rationale
```

## AE-AUTO-NEG-007 ; Autonomous Operations do NOT automatically establish Autonomous Enterprise

Per AE-AUTO-NEG-007 + AE-AUTO-CON-015.

Test:

```python
def test_ae_autonomous_operations_not_automatic():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'autonomous operations establishes autonomous enterprise' not in rationale
        assert 'autonomous operations automatically' not in rationale
```

## AE-AUTO-NEG-008 ; Autonomous Value Streams do NOT automatically establish Autonomous Enterprise

Per AE-AUTO-NEG-008 + AE-AUTO-CON-016.

Test:

```python
def test_ae_autonomous_value_stream_not_automatic():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'autonomous value stream establishes autonomous enterprise' not in rationale
```

## AE-AUTO-NEG-012 ; Autonomous Enterprise does NOT require elimination of humans

Per AE-AUTO-NEG-012 + AE-AUTO-NEG-013.

Test:

```python
def test_ae_human_governance_required():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'eliminate humans' not in rationale
        assert 'no human intervention' not in rationale or 'not required for every' in rationale
```

## AE-AUTO-NEG-014 ; Autonomous Enterprise implies unlimited authority (FALSE)

Per AE-AUTO-NEG-014 + AE-AUTO-CON-018.

Test:

```python
def test_ae_authority_is_bounded():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'unlimited authority' not in rationale or 'fails conformance' in rationale
```

## AE-AUTO-NEG-015 ; Autonomous Enterprise implies Autonomous Workflow (FALSE)

Per AE-AUTO-NEG-015 + AE-AUTO-CON-020. Autonomous Workflow is held as
a future concept per CR-ES-011 §27.

Test:

```python
def test_ae_does_not_imply_autonomous_workflow():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'autonomous workflow' not in rationale or 'future concept' in rationale or 'not established' in rationale
```

## AE-AUTO-NEG-016 ; Autonomous Enterprise implies Autonomous Agent (FALSE)

Per AE-AUTO-NEG-016 + AE-AUTO-CON-021.

Test:

```python
def test_ae_does_not_imply_autonomous_agent():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'autonomous agent' not in rationale or 'future concept' in rationale or 'not established' in rationale
```
