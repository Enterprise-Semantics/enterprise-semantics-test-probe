# Schema tests for Agent + Agentic

## AG-CON-001 ;;; Agent must have a definition

Per CR-ES-004 §26 ;;; the Agent concept record MUST declare a non-empty `definition` field.

Test:

```python
def test_agent_has_definition(agent_record):
    assert agent_record.get('definition', '').strip() != ''
```

## AG-CON-002 ;;; Agentic must have a definition

Per CR-ES-004 §26 ;;; the Agentic concept record MUST declare a non-empty `definition` field.

Test:

```python
def test_agentic_has_definition(agentic_record):
    assert agentic_record.get('definition', '').strip() != ''
```

## Negative test ;;; `AI is-a Agent` (universal identity)

Per CR-ES-004 §27 ;;; a concept record declaring `AI is-a Agent` (as universal identity, not as possible specialization) MUST be rejected.

```python
def test_ai_is_a_agent_rejected():
    record = {
        'id': 'ES:CONCEPT:ai-agent',
        'canonical_name': 'AI Agent',
        'is_a': 'ES:CONCEPT:agent',  # ;;; universal identity claim
        # ... 
    }
    errors = validate(record)
    assert any('AG-CON-NEG-001' in e or 'AI is-a Agent' in e for e in errors)
```

Note: AI Agent as a *possible specialization* of Agent is allowed per CR-ES-004 §18 + ADR-ES-004 §10 ;;; only the universal identity claim is rejected.

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)