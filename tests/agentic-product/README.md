# Agentic Product Conformance Tests

Per CR-ES-016 §23 + §24 + ADR-ES-016 §17.

## Coverage

This directory contains:

- 1 README (this file)
- 20 positive tests (APROD-CON-001 .. APROD-CON-020) per CR-ES-016 §23
- 16 negative tests (APROD-NEG-001 .. APROD-NEG-016) per CR-ES-016 §24

## Authoring

Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-24).

## Test Pattern

Each test file is a stub following the format established by prior tranches (ES-012/013/014/015). Each test file:

1. References its CR section number and ADR section number in the file header
2. States the test assertion in human-readable form
3. Provides the expected conformance / non-conformance verdict
4. Names the validator behavior required (per CR-ES-016 §25 + §26)

## Cardinal Rules

- Zero en-dash (U+2013)
- Zero em-dash (U+2014)
- Zero horizontal-ellipsis divider (U+2E3B)
- Zero inline 3-semicolon dividers (replace with comma)
- Zero vendor-specific embargoed references
- Cardinal author signature on every file

## Positive Tests (CR-ES-016 §23)

| ID | Subject | CR Section |
|---|---|---|
| APROD-CON-001 | Agentic Product specializes Product | §23.1 |
| APROD-CON-002 | Product semantics are retained | §23.2 |
| APROD-CON-003 | Material agentic realization exists | §23.3 |
| APROD-CON-004 | Product realization is outcome-oriented | §23.4 |
| APROD-CON-005 | Intent interpretation is supported | §23.5 |
| APROD-CON-006 | Contextual interpretation is supported | §23.6 |
| APROD-CON-007 | Action selection may occur | §23.7 |
| APROD-CON-008 | Coordination may occur | §23.8 |
| APROD-CON-009 | Adaptation may occur | §23.9 |
| APROD-CON-010 | Authority boundary exists | §23.10 |
| APROD-CON-011 | Policy/constraint boundary exists | §23.11 |
| APROD-CON-012 | Human intervention is permitted | §23.12 |
| APROD-CON-013 | Agentic Workflow may support realization | §23.13 |
| APROD-CON-014 | Agent may participate | §23.14 |
| APROD-CON-015 | Agentic Product may support Capability | §23.15 |
| APROD-CON-016 | Agentic Product may participate in Value Stream | §23.16 |
| APROD-CON-017 | AI is not required | §23.17 |
| APROD-CON-018 | Automation is not sufficient | §23.18 |
| APROD-CON-019 | Agentic does not imply Autonomous | §23.19 |
| APROD-CON-020 | Provenance and grounding are present | §23.20 |

## Negative Tests (CR-ES-016 §24)

| ID | Subject | CR Section |
|---|---|---|
| APROD-NEG-001 | Agentic Product is-a Agent | §24.1 |
| APROD-NEG-002 | Agentic Product is-a Agentic Capability | §24.2 |
| APROD-NEG-003 | Agentic Product is-a Agentic Service | §24.3 |
| APROD-NEG-004 | Agentic Product is-a Agentic Workflow | §24.4 |
| APROD-NEG-005 | Agentic Product is-a Agentic Operations | §24.5 |
| APROD-NEG-006 | Agentic Product is-a Agentic Value Stream | §24.6 |
| APROD-NEG-007 | Agentic Product requires AI | §24.7 |
| APROD-NEG-008 | AI-enabled Product automatically becomes Agentic Product | §24.8 |
| APROD-NEG-009 | Automated Product automatically becomes Agentic Product | §24.9 |
| APROD-NEG-010 | Product containing an Agent automatically becomes Agentic Product | §24.10 |
| APROD-NEG-011 | Agentic Product automatically becomes Autonomous Product | §24.11 |
| APROD-NEG-012 | Agentic Product requires elimination of humans | §24.12 |
| APROD-NEG-013 | Agentic Product has unlimited authority | §24.13 |
| APROD-NEG-014 | Agentic Product requires every product action to be agentic | §24.14 |
| APROD-NEG-015 | Agentic Product automatically establishes Agentic Value Stream | §24.15 |
| APROD-NEG-016 | Agentic Product automatically establishes Agentic Enterprise | §24.16 |
