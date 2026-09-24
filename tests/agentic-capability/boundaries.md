# Agentic Capability boundary conformance tests (ACAP-CON-005..013)

Per ADR-ES-012 §23 + CR-ES-012 §23.

## ACAP-CON-005: Agentic Capability may engage an Agent

Assert that engages -> Agent relationship is valid.

```python
def test_engages-agent(agentic_capability_record):
    assert False, 'ACAP-CON-005 pending implementation per ADR-ES-012 §23 + CR-ES-012 §23'
```

## ACAP-CON-006: Agentic Capability may be realized through Agentic Workflow

Assert that realized-through -> Agentic Workflow relationship is valid.

```python
def test_realized-through-agentic-workflow(agentic_capability_record):
    assert False, 'ACAP-CON-006 pending implementation per ADR-ES-012 §23 + CR-ES-012 §23'
```

## ACAP-CON-007: Agentic Capability may be supported by Agentic Operations

Assert that supported-by -> Agentic Operations relationship is valid.

```python
def test_supported-by-agentic-operations(agentic_capability_record):
    assert False, 'ACAP-CON-007 pending implementation per ADR-ES-012 §23 + CR-ES-012 §23'
```

## ACAP-CON-008: Agentic Capability may enable Agentic Value Stream realization

Assert that enables -> Agentic Value Stream relationship is valid.

```python
def test_enables-agentic-value-stream(agentic_capability_record):
    assert False, 'ACAP-CON-008 pending implementation per ADR-ES-012 §23 + CR-ES-012 §23'
```

## ACAP-CON-009: Agentic Capability does not require AI

Assert that Agentic Capability qualification does not require AI ; an AI-less realization still qualifies if behavior is material.

```python
def test_ai-not-required(agentic_capability_record):
    assert False, 'ACAP-CON-009 pending implementation per ADR-ES-012 §23 + CR-ES-012 §23'
```

## ACAP-CON-010: Automation does not establish Agentic Capability

Assert that automated_capability is not equal to agentic_capability.

```python
def test_automation-not-sufficient(agentic_capability_record):
    assert False, 'ACAP-CON-010 pending implementation per ADR-ES-012 §23 + CR-ES-012 §23'
```

## ACAP-CON-011: Agentic Capability does not imply autonomy

Assert that an Agentic Capability may be non-autonomous, partially autonomous, or fully autonomous ; autonomy is not inferred.

```python
def test_autonomy-not-implied(agentic_capability_record):
    assert False, 'ACAP-CON-011 pending implementation per ADR-ES-012 §23 + CR-ES-012 §23'
```

## ACAP-CON-012: Agentic Capability does not imply Agentic Enterprise

Assert that a single Agentic Capability does not establish Agentic Enterprise.

```python
def test_agentic-enterprise-not-implied(agentic_capability_record):
    assert False, 'ACAP-CON-012 pending implementation per ADR-ES-012 §23 + CR-ES-012 §23'
```

## ACAP-CON-013: Agent is not a subtype of Capability

Assert that Agent is-a Capability returns False.

```python
def test_agent-not-subtype-of-capability(agentic_capability_record):
    assert False, 'ACAP-CON-013 pending implementation per ADR-ES-012 §23 + CR-ES-012 §23'
```

