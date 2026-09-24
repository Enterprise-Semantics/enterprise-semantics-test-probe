# Agentic Capability negative conformance tests (ACAP-NEG-001..014)

Per CR-ES-012 §24.

The following negative tests must all FAIL when the Agentic
Capability semantic model is correctly applied. Each represents a
rejected interpretation per ADR-ES-012 §24.

## ACAP-NEG-001: Agentic Capability is-a Agent

Assert that Agentic Capability is-a Agent returns False.

```python
def test_agentic-capability-is-agent_must_fail():
    assert False, 'ACAP-NEG-001 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-002: Agent is-a Agentic Capability

Assert that Agent is-a Agentic Capability returns False.

```python
def test_agent-is-agentic-capability_must_fail():
    assert False, 'ACAP-NEG-002 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-003: Agentic Capability is-a Agentic Workflow

Assert that Agentic Capability is-a Agentic Workflow returns False.

```python
def test_agentic-capability-is-agentic-workflow_must_fail():
    assert False, 'ACAP-NEG-003 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-004: Agentic Workflow is-a Agentic Capability

Assert that Agentic Workflow is-a Agentic Capability returns False.

```python
def test_agentic-workflow-is-agentic-capability_must_fail():
    assert False, 'ACAP-NEG-004 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-005: Agentic Capability is-a Agentic Operations

Assert that Agentic Capability is-a Agentic Operations returns False.

```python
def test_agentic-capability-is-agentic-operations_must_fail():
    assert False, 'ACAP-NEG-005 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-006: Agentic Operations is-a Agentic Capability

Assert that Agentic Operations is-a Agentic Capability returns False.

```python
def test_agentic-operations-is-agentic-capability_must_fail():
    assert False, 'ACAP-NEG-006 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-007: Agentic Capability is-a Agentic Value Stream

Assert that Agentic Capability is-a Agentic Value Stream returns False.

```python
def test_agentic-capability-is-agentic-value-stream_must_fail():
    assert False, 'ACAP-NEG-007 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-008: Agentic Value Stream is-a Agentic Capability

Assert that Agentic Value Stream is-a Agentic Capability returns False.

```python
def test_agentic-value-stream-is-agentic-capability_must_fail():
    assert False, 'ACAP-NEG-008 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-009: Agentic Capability requires AI

Assert that an AI-less realization still qualifies as Agentic Capability if behavior is material.

```python
def test_agentic-capability-requires-ai_must_fail():
    assert False, 'ACAP-NEG-009 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-010: AI automatically establishes Agentic Capability

Assert that adding AI to a Capability does not automatically make it Agentic.

```python
def test_ai-automatically-establishes-agentic-capability_must_fail():
    assert False, 'ACAP-NEG-010 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-011: Automation automatically establishes Agentic Capability

Assert that automating a Capability does not automatically make it Agentic.

```python
def test_automation-automatically-establishes-agentic-capability_must_fail():
    assert False, 'ACAP-NEG-011 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-012: Agentic Capability automatically implies Autonomous Capability

Assert that Agentic Capability is-a Autonomous Capability returns False.

```python
def test_agentic-implies-autonomous_must_fail():
    assert False, 'ACAP-NEG-012 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-013: Agentic Capability automatically establishes Agentic Enterprise

Assert that a single Agentic Capability does not establish Agentic Enterprise.

```python
def test_agentic-establishes-agentic-enterprise_must_fail():
    assert False, 'ACAP-NEG-013 pending implementation per CR-ES-012 §24'
```

## ACAP-NEG-014: Agentic Capability requires removal of humans

Assert that human participation patterns (Human, Human+Agent, Human+System) are valid in Agentic Capability realizations.

```python
def test_agentic-removes-humans_must_fail():
    assert False, 'ACAP-NEG-014 pending implementation per CR-ES-012 §24'
```

