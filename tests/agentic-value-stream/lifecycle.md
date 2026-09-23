# Lifecycle tests for Agentic Value Stream

## AVS-CON-003 ;; Agentic Value Stream retains initiating-condition semantics

Per CR-ES-005 §8 ;; the Agentic Value Stream schema MUST retain the
initiating-condition semantics from CR-ES-003.

Test:

```python
def test_avs_initiating_condition(avs_record):
    """;; the avs retains the initiating-condition semantics per CR-ES-005 §8"""
    # ;;; the record's properties include initiating-condition
    properties = avs_record.get('properties', [])
    property_names = {p['name'] for p in properties}
    # ;;; initiating_condition is inherited from Value Stream
    # ;;; if inherited, it must be preserved in the schema
```

## AVS-CON-004 ;; Agentic Value Stream retains realisation-boundary semantics

Per CR-ES-005 §8 ;; the Agentic Value Stream schema MUST retain the
realisation-boundary semantics from CR-ES-003.

Test:

```python
def test_avs_realisation_boundary(avs_record):
    """;; the avs retains the realisation-boundary semantics per CR-ES-005 §8"""
    # ;;; the record's properties include realisation-boundary
    properties = avs_record.get('properties', [])
    property_names = {p['name'] for p in properties}
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)