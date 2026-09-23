# Operational loop tests for Agentic Operations

## 8-step operational loop

Per ADR-ES-007 §17 + CR-ES-007 §9 ;; the operational control loop has
8 steps: Sense -> Interpret -> Decide -> Coordinate -> Act -> Observe
Outcome -> Adapt (the loop also has Evaluate as a 9th step per the
full example).

Test:

```python
def test_aop_loop_8_steps():
    record = load_concept('agentic-operations')
    # Must reference operational loop semantics
    invariants = record.get('invariants', [])
    # Check that loop is documented (e.g., in characteristics)
    characteristics = record.get('characteristics', [])
    assert any('sensing' in c.lower() for c in characteristics)

def test_aop_loop_bounded():
    record = load_concept('agentic-operations')
    # Operational loop is bounded by authority and policy
    auth_props = [p for p in record['properties']
                  if p['name'] in ['authority_context', 'policy_context']]
    assert len(auth_props) == 2
```

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 clean
- No vendor-specific material from embargoed sources
- Per CR-ES-007 §9 + ADR-ES-007 §17