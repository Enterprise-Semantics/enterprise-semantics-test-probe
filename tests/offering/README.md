# Offering Conformance Tests

Per CR-ES-021 section 9 + section 10 + ADR-ES-021 section 13.

## Coverage

This directory contains:

- 1 README (this file)
- 15 positive tests (OFFR-CON-001 .. OFFR-CON-015) per CR-ES-021 section 9
- 12 negative tests (OFFR-NEG-001 .. OFFR-NEG-012) per CR-ES-021 section 10

## Foundational Status

Offering is a foundational concept per ADR-ES-021 section 1. There
is no dependency gate (no BLOCKED test). This CR resolves the
dependency documented in ADR-ES-018 + ADR-ES-019.

## Authoring

Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-24).

## Cardinal Rules

- Zero en-dash (U+2013)
- Zero em-dash (U+2014)
- Zero horizontal-ellipsis divider (U+2E3B)
- Zero inline 3-semicolon dividers (replace with comma)
- Zero vendor-specific embargoed references
- Cardinal author signature on every file

## Positive Tests (CR-ES-021 section 9)

| ID | Subject | CR Section |
|---|---|---|
| OFFR-CON-001 | addresses Customer Need | section 9.1 |
| OFFR-CON-002 | composes Product | section 9.2 |
| OFFR-CON-003 | composes Service | section 9.3 |
| OFFR-CON-004 | exercises Capability | section 9.4 |
| OFFR-CON-005 | has offering objective | section 9.5 |
| OFFR-CON-006 | operates within Authority | section 9.6 |
| OFFR-CON-007 | is governed by Policy | section 9.7 |
| OFFR-CON-008 | observes Constraints | section 9.8 |
| OFFR-CON-009 | is under Governance | section 9.9 |
| OFFR-CON-010 | progresses through Fulfillment | section 9.10 |
| OFFR-CON-011 | produces Customer Outcome | section 9.11 |
| OFFR-CON-012 | realizes Value | section 9.12 |
| OFFR-CON-013 | supports Escalation | section 9.13 |
| OFFR-CON-014 | retains Agentic/Autonomous orthogonality | section 9.14 |
| OFFR-CON-015 | contains provenance | section 9.15 |

## Negative Tests (CR-ES-021 section 10)

| ID | Subject | CR Section |
|---|---|---|
| OFFR-NEG-001 | Offering is-a Product | section 10.1 |
| OFFR-NEG-002 | Offering is-a Service | section 10.2 |
| OFFR-NEG-003 | Offering is-a Capability | section 10.3 |
| OFFR-NEG-004 | Offering is-a Value Stream | section 10.4 |
| OFFR-NEG-005 | Offering is-a Enterprise | section 10.5 |
| OFFR-NEG-006 | Offering is-a Customer Need | section 10.6 |
| OFFR-NEG-007 | Offering is-a Fulfillment Process | section 10.7 |
| OFFR-NEG-008 | Product is-a Offering | section 10.8 |
| OFFR-NEG-009 | Service is-a Offering | section 10.9 |
| OFFR-NEG-010 | Capability is-a Offering | section 10.10 |
| OFFR-NEG-011 | Value Stream is-a Offering | section 10.11 |
| OFFR-NEG-012 | Enterprise is-a Offering | section 10.12 |
