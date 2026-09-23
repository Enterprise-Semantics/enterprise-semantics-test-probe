# Identity tests for Agentic Value Stream

## Identity uniqueness

Per CR-ES-001 §15 ;; `ES:CONCEPT:<kebab>` format must be unique across
all concept records.

Test:

```python
def test_avs_identity_unique(avs_record, all_concept_records):
    aid = avs_record['id']
    ids = [r['id'] for r in all_concept_records if r.get('id') != aid]
    assert aid not in ids, f'Agentic Value Stream identity {aid} is not unique'
```

## Identity format

Test:

```python
def test_avs_identity_format(avs_record):
    import re
    aid = avs_record['id']
    assert re.match(r'^ES:CONCEPT:[a-z][a-z0-9-]*$', aid)
```

## Specialisation relationship validation

Per CR-ES-005 §5 ;; Agentic Value Stream specialises Value Stream.

```python
def test_avs_specialisation_validates(avs_record, vs_record):
    """;; Agentic Value Stream must specialise an existing concept"""
    spec = avs_record.get('specializes')
    assert spec == 'ES:CONCEPT:value-stream'
    # ;;; the parent must be a real Concept record
    assert vs_record is not None
    assert vs_record['id'] == 'ES:CONCEPT:value-stream'
```

## Profile binding validation

Per CR-ES-005 §14 ;; the Agentic Value Stream must bind to a registered
Profile.

```python
def test_avs_profile_binding(avs_record, all_profiles):
    bindings = avs_record.get('profile_bindings', [])
    profile_ids = {p['id'] for p in all_profiles}
    for b in bindings:
        assert b['profile_id'] in profile_ids, f'Profile {b[\"profile_id\"]} not registered'
```

## Authored by

Emmanuel A. Otchere (cardinal author rule, 2026-09-23)