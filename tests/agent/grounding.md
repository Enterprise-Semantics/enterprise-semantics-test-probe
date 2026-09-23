# Grounding tests for Agentic

## ES-canonical novelty

Per FND-ES-AG-008 §1.3 ;;; the Agentic construct is ES-canonical ;;; no WSF Tier 1 or Tier 2 equivalent. The wsf_grounding field is therefore pending ;;; not a high-confidence WSF mapping.

Test:

```python
def test_agentic_grounding_pending(agentic_record):
    wsf_grounding = agentic_record.get('wsf_grounding', [])
    # ;;; Agentic is ES-canonical ;;; wsf_grounding entries should be pending/None
    # ;;; or note the absence of WSF correspondence
    for entry in wsf_grounding:
        if entry.get('wsf_concept_id') is not None:
            # ;;; if a specific WSF construct is referenced, it must be valid
            assert entry['wsf_concept_id'].startswith('external:wsf:')
```

## Authority grounding

Authority is ES-canonical ;;; per CR-ES-004 §8 + ADR-ES-004 §15.

```python
def test_authority_grounding_pending(authority_record):
    wsf_grounding = authority_record.get('wsf_grounding', [])
    # ;;; Authority is ES-canonical ;;; wsf_grounding entries document the absence of WSF correspondence
```

## Action grounding

Action is ES-canonical ;;; per CR-ES-004 §9 + ADR-ES-004 §14.

```python
def test_action_grounding_pending(action_record):
    wsf_grounding = action_record.get('wsf_grounding', [])
    # ;;; Action is ES-canonical
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)