# Identity tests for Agentic Workflow

## Identity uniqueness

Per CR-ES-001 §15 ;; `ES:CONCEPT:<kebab>` format must be unique
across all concept records.

Test:

```python
def test_awf_identity_unique():
    all_ids = [c['id'] for c in all_concepts()]
    assert all_ids.count('ES:CONCEPT:agentic-workflow') == 1

def test_awf_id_format():
    record = load_concept('agentic-workflow')
    assert record['id'] == 'ES:CONCEPT:agentic-workflow'
    assert re.match(r'^ES:CONCEPT:[a-z][a-z0-9-]*$', record['id'])
```

## Identity form

Per ADR-ES-002 §11 ;; the canonical identity form is `ES:CONCEPT:<k>`
in lowercase kebab-case. The CR-ES-006 §5 verbatim text uses
`ES:CONCEPT:AGENTIC_WORKFLOW` ;; which is canonicalised to the
lowercase form.

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-006 §5 + ADR-ES-002 §11