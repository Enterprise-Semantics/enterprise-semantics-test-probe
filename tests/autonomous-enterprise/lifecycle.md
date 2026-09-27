# Lifecycle tests for Autonomous Enterprise

## AE-AUTO-CON-017 ; Mixed-mode enterprise operation

Per AE-AUTO-CON-017 + ADR-ES-011 §19, the Autonomous Enterprise
does NOT require every enterprise activity to be autonomous.

Test:

```python
def test_ae_mixed_mode_valid():
    """The Autonomous Enterprise does not require every enterprise
    activity to be autonomous per AE-AUTO-CON-017."""
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'every value stream must be autonomous' not in rationale
        assert 'every operation must be autonomous' not in rationale
```

## AE-AUTO-NEG-009 ; Agentic Enterprise does NOT automatically become Autonomous

Per AE-AUTO-NEG-009.

Test:

```python
def test_ae_agentic_not_automatic():
    record = load_concept('autonomous-enterprise')
    for r in record['relationships']:
        rationale = r.get('rationale', '').lower()
        assert 'agentic enterprise becomes autonomous' not in rationale
```
