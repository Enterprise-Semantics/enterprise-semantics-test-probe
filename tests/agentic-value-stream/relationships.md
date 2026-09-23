# Relationships tests for Agentic Value Stream

## AVS-CON-005 ;; Agentic Value Stream identifies at least one material agentic characteristic

Per CR-ES-005 §21 + ADR-ES-005 §17 ;; the Agentic Value Stream concept
record MUST identify at least one material agentic characteristic
(from the 8: delegated intent ;; contextual interpretation ;; dynamic
action selection ;; agentic coordination ;; adaptive progression ;;
bounded authority ;; intervention ;; outcome orientation).

Test:

```python
def test_avs_has_agentic_characteristic(avs_record):
    characteristics = avs_record.get('characteristics', [])
    assert len(characteristics) >= 1, 'Agentic Value Stream must have at least one agentic characteristic'

def test_avs_characteristic_validates(avs_record):
    valid_ids = {
        'AG-VS-CHAR:delegated-intent',
        'AG-VS-CHAR:contextual-interpretation',
        'AG-VS-CHAR:dynamic-action-selection',
        'AG-VS-CHAR:agentic-coordination',
        'AG-VS-CHAR:adaptive-progression',
        'AG-VS-CHAR:bounded-authority',
        'AG-VS-CHAR:intervention',
        'AG-VS-CHAR:outcome-orientation',
    }
    actual_ids = {c['id'] for c in avs_record.get('characteristics', [])}
    assert actual_ids.issubset(valid_ids), f'Unknown characteristic IDs: {actual_ids - valid_ids}'
```

## AVS-CON-006 ;; Agentic participation is associated with delegated intent and bounded authority

Per CR-ES-005 §21 ;; agentic participation MUST be associated with
delegated intent and bounded authority.

Test:

```python
def test_avs_intent_authority_linkage(avs_record):
    properties = avs_record.get('properties', [])
    property_names = {p['name'] for p in properties}
    assert 'delegated_intent' in property_names
    assert 'authority_context' in property_names

def test_avs_engages_agent(avs_record):
    """;; per CR-ES-005 §7 ;; avs must engage an Agent"""
    rels = avs_record.get('relationships', [])
    assert any(
        r.get('predicate') == 'engages' and
        r.get('object') == 'ES:CONCEPT:agent'
        for r in rels
    )
```

## AVS-CON-007 ;; Agentic participation may apply to one or more stages

Per CR-ES-005 §21 ;; complete-stream agency is NOT required.

Test:

```python
def test_avs_agentic_scope_required(avs_record):
    """;; per CR-ES-005 §9 ;; agentic_scope is required"""
    properties = avs_record.get('properties', [])
    scope = next((p for p in properties if p['name'] == 'agentic_scope'), None)
    assert scope is not None
    assert scope.get('required') == True

def test_avs_mixed_realization_supported(avs_record):
    """;; per CR-ES-005 §11 ;; mixed realization is supported"""
    properties = avs_record.get('properties', [])
    mode = next((p for p in properties if p['name'] == 'realization_mode'), None)
    assert mode is not None
    valid_values = {'mixed', 'predominantly-agentic', 'agentic-partial', 'agentic-coordinated'}
    assert set(mode.get('values', [])).issubset(valid_values)
```

## Reference resolution

Per CR-ES-005 §25 ;; references must resolve.

Test:

```python
def test_avs_relationships_resolve(avs_record):
    rels = avs_record.get('relationships', [])
    for r in rels:
        subject = r.get('subject')
        object = r.get('object')
        assert subject in canonical_ids() or subject.startswith('external:')
        assert object in canonical_ids() or object.startswith('external:')
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)