# Autonomy integrity tests for Agentic Enterprise

## AE-CON-007 ; Authority boundary

Per AE-CON-007 + ADR-ES-010 §1 + §17, the Agentic Enterprise
operates within defined authority.

Test:

```python
def test_ae_authority_field_present():
    record = load_concept('agentic-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'operates-within']
    assert any(r['object'] == 'ES:CONCEPT:authority' for r in rels)

def test_ae_authority_not_unrestricted():
    """An Agentic Enterprise instance with authority = unrestricted
    fails conformance per AE-CON-018."""
    record = load_concept('agentic-enterprise')
    # verify the rationale does not declare unrestricted authority
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'unrestricted' not in rationale or 'fail' in rationale
```

## AE-CON-008 ; Policy governance boundary

Per AE-CON-008 + ADR-ES-010 §17, the Agentic Enterprise operates
within defined policy and governance boundaries.

Test:

```python
def test_ae_governed_by_policy():
    record = load_concept('agentic-enterprise')
    rels = [r for r in record['relationships']
            if r['predicate'] == 'governed-by']
    assert any('policy' in r.get('object', '').lower() for r in rels)
```

## AE-CON-009 ; Human participation remains valid

Per AE-CON-009 + ADR-ES-010 §10, human participation is permitted
in an Agentic Enterprise.

Test:

```python
def test_ae_human_participation_valid():
    """The Agentic Enterprise must NOT require elimination of humans
    per AE-NEG-009."""
    record = load_concept('agentic-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'elimination of humans' not in rationale
        assert 'human-free' not in rationale
```

## AE-CON-010 ; AI is not required

Per AE-CON-010 + ADR-ES-010 §11, AI is not required for the Agentic
Enterprise.

Test:

```python
def test_ae_ai_not_required():
    """The Agentic Enterprise must NOT require AI per AE-CON-010 +
    AE-NEG-002."""
    record = load_concept('agentic-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        # AI may be an implementation mechanism, but not a requirement
        assert 'requires ai' not in rationale
```

## AE-NEG-003 ; Agentic Enterprise is NOT Autonomous Enterprise

Per ADR-ES-011 §11 + AE-NEG-003, Agentic Enterprise and Autonomous
Enterprise are orthogonal.

Test:

```python
def test_ae_not_autonomous_enterprise():
    record = load_concept('agentic-enterprise')
    # verify no identity predicate with Autonomous Enterprise
    for r in record['relationships']:
        if r.get('object') == 'ES:CONCEPT:autonomous-enterprise':
            assert r['predicate'] not in ('is-a', 'specializes', 'isa')
```

## AE-NEG-004 ; Agentic Enterprise does NOT require Autonomous Operations

Per CR-ES-010 §22 + AE-NEG-004. Agentic Enterprise does not require
Autonomous Operations.

Test:

```python
def test_ae_does_not_require_autonomous_operations():
    record = load_concept('agentic-enterprise')
    # verify no relationship declares Autonomous Operations as a
    # mandatory dependency
    for r in record['relationships']:
        if r.get('object') == 'ES:CONCEPT:autonomous-operations':
            assert r.get('qualification', '') != 'mandatory'
            assert r.get('rationale', '').lower().find('requires autonomous') == -1
```

## AE-NEG-005 ; Agentic Enterprise does NOT require every Value Stream to be agentic

Per CR-ES-010 §22 + AE-NEG-005. Mixed-mode is valid.

Test:

```python
def test_ae_not_all_value_streams_agentic():
    record = load_concept('agentic-enterprise')
    # verify the rationale does not claim every value stream must be
    # agentic
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'every value stream must be agentic' not in rationale
```

## AE-NEG-006 ; Agentic Enterprise does NOT require every Process to be agentic

Per CR-ES-010 §22 + AE-NEG-006. Mixed-mode is valid.

Test:

```python
def test_ae_not_all_processes_agentic():
    record = load_concept('agentic-enterprise')
    # verify the rationale does not claim every process must be agentic
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'every process must be agentic' not in rationale
```

## AE-NEG-007 ; Agentic Enterprise is NOT established by possessing an Agent

Per CR-ES-010 §22 + AE-NEG-007. Merely possessing Agents does not
establish Agentic Enterprise.

Test:

```python
def test_ae_not_established_by_agent_possession():
    record = load_concept('agentic-enterprise')
    # verify no relationship claims that possessing an Agent
    # establishes Agentic Enterprise
    for r in record['relationships']:
        if r.get('object') == 'ES:CONCEPT:agent':
            rationale = r.get('rationale', '').lower()
            assert 'establishes agentic enterprise' not in rationale
            assert 'possession of agents' not in rationale
```

## AE-NEG-008 ; Agentic Enterprise is NOT established by using automation

Per CR-ES-010 §22 + AE-NEG-008. Automation alone does not establish
Agentic Enterprise.

Test:

```python
def test_ae_not_established_by_automation():
    record = load_concept('agentic-enterprise')
    # verify no relationship claims automation establishes
    # Agentic Enterprise
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'automation establishes agentic enterprise' not in rationale
        assert 'use of automation' not in rationale
```

## AE-NEG-009 ; Agentic Enterprise does NOT require elimination of humans

Per CR-ES-010 §22 + AE-NEG-009. Human governance is required.

Test:

```python
def test_ae_human_governance_required():
    record = load_concept('agentic-enterprise')
    # verify the rationale does NOT claim humans are eliminated
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'humans are eliminated' not in rationale
        assert 'no human' not in rationale or 'no human intervention for every decision' in rationale
```

## AE-NEG-010 ; Agentic Enterprise implies unlimited authority (FALSE)

Per CR-ES-010 §22 + AE-NEG-010. Authority is bounded.

Test:

```python
def test_ae_authority_is_bounded():
    record = load_concept('agentic-enterprise')
    # verify the rationale does NOT claim unlimited authority
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'unlimited authority' not in rationale or 'fails conformance' in rationale
```

## AE-NEG-017 ; Agentic Enterprise is NOT Autonomous Operations

Per CR-ES-010 §22 + AE-NEG-017.

Test:

```python
def test_ae_not_autonomous_operations_identity():
    record = load_concept('agentic-enterprise')
    for r in record['relationships']:
        if r.get('object') == 'ES:CONCEPT:autonomous-operations':
            assert r['predicate'] != 'specializes'
            assert r.get('qualification', '') != 'identity'
```

## AE-NEG-018 ; Agentic Enterprise is NOT Autonomous Value Stream

Per CR-ES-010 §22 + AE-NEG-018.

Test:

```python
def test_ae_not_autonomous_value_stream_identity():
    record = load_concept('agentic-enterprise')
    for r in record['relationships']:
        if r.get('object') == 'ES:CONCEPT:autonomous-value-stream':
            assert r['predicate'] != 'specializes'
            assert r.get('qualification', '') != 'identity'
```
