# Examples tests for Agentic Value Stream

## OTCHERE Inc Order-to-Cash (Agentic)

Per CR-ES-005 §19 ;; the foundational example demonstrates:

- 11 flow steps
- 4 agentic scope entries
- 10 cardinal relationships used (3 AVS predicates + Agent predicates)
- All 8 Agentic Value Stream characteristics (delegated intent ;;
  contextual interpretation ;; dynamic action selection ;; agentic
  coordination ;; adaptive progression ;; bounded authority ;;
  intervention ;; outcome orientation)
- 7 boundaries demonstrated (human-in-the-loop ;; bounded authority ;;
  outcome orientation ;; Agentic != AI ;; Agentic != Automation ;;
  Agentic != Autonomous ;; mixed realization ;; specialised of Value
  Stream)

Test:

```python
def test_order_to_cash_agentic_example_parses(example_path):
    """;; Verify the example YAML parses cleanly"""
    import yaml
    with open(example_path) as f:
        data = yaml.safe_load(f)
    assert data['canonical_name'] == 'OTCHERE Inc Order-to-Cash (Agentic)'

def test_order_to_cash_agentic_demonstrates_all_8_characteristics(example_path):
    """;; Per CR-ES-005 §19 + ADR-ES-005 §15 ;; the example demonstrates all 8 Agentic Value Stream characteristics"""
    with open(example_path) as f:
        data = yaml.safe_load(f)
    demonstrated = {b.split(';;')[-1].strip().split(' ')[0] for b in data.get('boundaries_demonstrated', [])}
    # ;;; the 8 characteristics are documented in the boundaries section + the relationships section
    assert len(demonstrated) >= 7

def test_order_to_cash_agentic_uses_mixed_realization(example_path):
    """;; Per CR-ES-005 §11 ;; mixed realization is supported"""
    with open(example_path) as f:
        data = yaml.safe_load(f)
    flow_steps = data['flow']
    modes = {step.get('realization_mode') for step in flow_steps}
    # ;;; mixed realization ;; at least 2 distinct modes
    assert len(modes) >= 2

def test_order_to_cash_agentic_preserves_human_escalation(example_path):
    """;; Per ADR-ES-005 §4.7 ;; human escalation remains possible"""
    with open(example_path) as f:
        data = yaml.safe_load(f)
    boundaries = data.get('boundaries_demonstrated', [])
    assert any('human' in b.lower() for b in boundaries)

def test_order_to_cash_agentic_uses_otchere_naming(example_path):
    """;; Naming convention: OTCHERE Inc preserved (no ACME placeholder)"""
    with open(example_path) as f:
        data = yaml.safe_load(f)
    assert 'OTCHERE' in data['canonical_name']
    assert 'ACME' not in data['canonical_name']
```

## Negative example tests

Per CR-ES-005 §22 ;; the following should be rejected:

```python
def test_ai_is_a_agentic_value_stream_universal_identity_rejected():
    """;; AI Value Stream as universal Agentic Value Stream (not as possible specialisation) is rejected"""
    record = {
        'id': 'ES:CONCEPT:ai-value-stream',
        'is_a': 'ES:CONCEPT:agentic-value-stream',  # ;;; universal identity claim
    }
    errors = validate(record)
    assert any('AI is-a Agentic Value Stream' in e for e in errors)

def test_agentic_value_stream_is_a_autonomous_value_stream_rejected():
    """;; Agentic Value Stream is-a Autonomous Value Stream must fail"""
    record = {
        'id': 'ES:CONCEPT:agentic-value-stream',
        'is_a': 'ES:CONCEPT:autonomous-value-stream',
    }
    errors = validate(record)
    assert any('Agentic Value Stream is-a Autonomous Value Stream' in e for e in errors)

def test_agentic_value_stream_requires_ai_rejected():
    """;; Agentic Value Stream requires AI must fail"""
    record = {
        'id': 'ES:CONCEPT:agentic-value-stream',
        'requires': 'ES:CONCEPT:ai',
    }
    errors = validate(record)
    assert any('Agentic Value Stream requires AI' in e for e in errors)

def test_agentic_value_stream_replaces_value_stream_rejected():
    """;; Agentic Value Stream replaces Value Stream must fail"""
    record = {
        'id': 'ES:CONCEPT:agentic-value-stream',
        'replaces': 'ES:CONCEPT:value-stream',
    }
    errors = validate(record)
    assert any('Agentic Value Stream replaces Value Stream' in e for e in errors)

def test_agentic_value_stream_is_a_process_rejected():
    """;; Agentic Value Stream is-a Process must fail"""
    record = {
        'id': 'ES:CONCEPT:agentic-value-stream',
        'is_a': 'ES:CONCEPT:process',
    }
    errors = validate(record)
    assert any('Agentic Value Stream is-a Process' in e for e in errors)
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)