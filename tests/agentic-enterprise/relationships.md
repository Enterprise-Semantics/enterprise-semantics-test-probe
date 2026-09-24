# Relationship tests for Agentic Enterprise

## AE-CON-004 ; Agentic Enterprise realises through Agentic Value Streams

Per CR-ES-010 §4 + ADR-ES-010 §14 + AE-CON-004, the Agentic
Enterprise concept record MUST declare an
`enterprise-realizes-through` relationship to Agentic Value Streams.

Test:

```python
def test_ae_enterprise_realizes_through():
    record = load_concept('agentic-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'enterprise-realizes-through']
    assert any(r['object'] == 'ES:CONCEPT:agentic-value-stream' for r in rels)
```

## AE-CON-005 ; Agentic Enterprise operates through Agentic Operations

Per CR-ES-010 §4 + ADR-ES-010 §15 + AE-CON-005, the Agentic
Enterprise concept record MUST declare an
`enterprise-operates-through` relationship to Agentic Operations.

Test:

```python
def test_ae_enterprise_operates_through():
    record = load_concept('agentic-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'enterprise-operates-through']
    assert any(r['object'] == 'ES:CONCEPT:agentic-operations' for r in rels)
```

## AE-CON-006 ; Agentic Enterprise uses Agentic Workflows

Per CR-ES-010 §4 + ADR-ES-010 §16 + AE-CON-006, the Agentic
Enterprise concept record MAY declare a `uses` relationship to
Agentic Workflows.

Test:

```python
def test_ae_uses_agentic_workflow():
    record = load_concept('agentic-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'uses']
    assert any(r['object'] == 'ES:CONCEPT:agentic-workflow' for r in rels)
```

## AE-NEG-011 ; Agentic Enterprise is NOT Agentic Operations

Per CR-ES-010 §22 + AE-NEG-011. The Agentic Enterprise concept
record MUST NOT declare an identity relationship with Agentic
Operations.

Test:

```python
def test_ae_not_identity_with_agentic_operations():
    record = load_concept('agentic-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-operations'

def test_ae_no_identity_relationship():
    record = load_concept('agentic-enterprise')
    # verify no predicate claims identity (is-a) with Agentic Operations
    identity_predicates = ['is-a', 'isa', 'is']
    for r in record['relationships']:
        assert r['predicate'] not in identity_predicates
```

## AE-NEG-012 ; Agentic Enterprise is NOT Agentic Value Stream

Per CR-ES-010 §22 + AE-NEG-012. The Agentic Enterprise concept
record MUST NOT declare an identity relationship with Agentic Value
Streams.

Test:

```python
def test_ae_not_identity_with_agentic_value_stream():
    record = load_concept('agentic-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-value-stream'
```

## AE-NEG-013 ; Agentic Enterprise is NOT Agentic Workflow

Per CR-ES-010 §22 + AE-NEG-013. The Agentic Enterprise concept
record MUST NOT declare an identity relationship with Agentic
Workflows.

Test:

```python
def test_ae_not_identity_with_agentic_workflow():
    record = load_concept('agentic-enterprise')
    specializes_rels = [r for r in record['relationships']
                        if r['predicate'] == 'specializes']
    for r in specializes_rels:
        assert r['object'] != 'ES:CONCEPT:agentic-workflow'
```

## AE-NEG-014 ; Agentic Operations does NOT automatically establish Agentic Enterprise

Per CR-ES-010 §22 + AE-NEG-014. Agentic Operations alone do not
establish Agentic Enterprise.

Test:

```python
def test_ae_not_automatic_from_agentic_operations():
    record = load_concept('agentic-enterprise')
    # verify no relationship declares automatic entailment from
    # Agentic Operations to Agentic Enterprise
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'automatic' not in rationale or 'agentic enterprise' not in rationale
```

## AE-NEG-015 ; Agentic Value Stream does NOT automatically establish Agentic Enterprise

Per CR-ES-010 §22 + AE-NEG-015. Agentic Value Streams alone do not
establish Agentic Enterprise.

Test:

```python
def test_ae_not_automatic_from_agentic_value_stream():
    record = load_concept('agentic-enterprise')
    # verify the enterprise-realizes-through relationship is
    # qualified as enterprise-realisation-via-value-stream, NOT
    # automatic-entailment
    for r in record['relationships']:
        if r['predicate'] == 'enterprise-realizes-through':
            assert r.get('qualification', '') != 'automatic-entailment'
```
