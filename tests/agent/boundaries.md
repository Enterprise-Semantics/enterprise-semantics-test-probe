# Boundaries tests for Agentic

## AG-CON-003, Agentic must identify its semantic characteristics

Per CR-ES-004 §26, the Agentic concept record MUST declare its 6 semantic characteristics (delegated intent, contextual interpretation, action selection, bounded authority, outcome orientation, adaptation).

Test:

```python
def test_agentic_characteristics(agentic_record):
    characteristics = agentic_record.get('characteristics', [])
    expected = {'delegated-intent', 'contextual-interpretation', 'action-selection', 'bounded-authority', 'outcome-orientation', 'contextual-adaptation'}
    actual = {c['id'] for c in characteristics}
    assert expected.issubset(actual), f'Missing characteristics: {expected - actual}'
```

## AG-CON-004, Agentic must not be defined as AI

Per CR-ES-004 §26 + ADR-ES-004 §10 + AG-INV-001, the Agentic definition MUST NOT include "AI" as a synonym or equivalence claim.

Test:

```python
def test_agentic_not_ai(agentic_record):
    definition = agentic_record.get('definition', '').lower()
    #, the definition should not say "agentic IS AI" or "agentic = AI" or "agentic means AI"
    forbidden_phrases = [
        'agentic is ai',
        'agentic = ai',
        'agentic means ai',
        'agentic describes ai',
        'agentic is the same as ai',
    ]
    for phrase in forbidden_phrases:
        assert phrase not in definition, f'Agentic definition contains forbidden phrase: {phrase}'
```

## AG-CON-005, Agentic must not be defined as Automation

Per CR-ES-004 §26 + ADR-ES-004 §8 + AG-INV-002, the Agentic definition MUST NOT include "Automation" as a synonym or equivalence claim.

Test:

```python
def test_agentic_not_automation(agentic_record):
    definition = agentic_record.get('definition', '').lower()
    forbidden_phrases = [
        'agentic is automation',
        'agentic = automation',
        'agentic means automation',
        'agentic describes automation',
    ]
    for phrase in forbidden_phrases:
        assert phrase not in definition
```

## AG-CON-006, Agentic must not be defined as Autonomous

Per CR-ES-004 §26 + ADR-ES-004 §9 + AG-INV-003, the Agentic definition MUST NOT include "Autonomous" as a synonym or equivalence claim.

Test:

```python
def test_agentic_not_autonomous(agentic_record):
    definition = agentic_record.get('definition', '').lower()
    forbidden_phrases = [
        'agentic is autonomous',
        'agentic = autonomous',
        'agentic means autonomous',
        'agentic describes autonomous',
    ]
    for phrase in forbidden_phrases:
        assert phrase not in definition
```

## Negative tests

Per CR-ES-004 §27:

- `AI is-a Agent` (universal identity), rejected, see schema.md
- `Agentic is-a Autonomous`, rejected
- `Automation is-a Agentic`, rejected

```python
def test_agentic_is_a_autonomous_rejected():
    record = {
        'id': 'ES:CONCEPT:agentic',
        'is_a': 'ES:CONCEPT:autonomous',  #, equivalence claim
        # ...
    }
    errors = validate(record)
    assert any('AG-CON-006' in e or 'Agentic is-a Autonomous' in e for e in errors)
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)