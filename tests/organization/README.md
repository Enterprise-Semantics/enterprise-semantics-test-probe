# Organization Conformance Tests

Per CR-ES-022 section 9 + section 10 + ADR-ES-022 section 13.

## Coverage

This directory contains:

- 1 README (this file)
- 16 positive tests (ORG-CON-001 .. ORG-CON-016) per CR-ES-022 section 9
- 14 negative tests (ORG-NEG-001 .. ORG-NEG-014) per CR-ES-022 section 10

## Foundational Status

Organization is a foundational concept per ADR-ES-022 section 1.
There is no dependency gate (no BLOCKED test). This CR resolves
the dependency documented in ADR-ES-020.

## Authoring

Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-24).

## Cardinal Rules

- Zero en-dash (U+2013)
- Zero em-dash (U+2014)
- Zero horizontal-ellipsis divider (U+2E3B)
- Zero inline 3-semicolon dividers (replace with comma)
- Zero vendor-specific embargoed references
- Cardinal author signature on every file

## Positive Tests (CR-ES-022 section 9)

| ID | Subject | CR Section |
|---|---|---|
| ORG-CON-001 | pursues Organizational Intent | section 9.1 |
| ORG-CON-002 | coordinates Actor | section 9.2 |
| ORG-CON-003 | allocates Role | section 9.3 |
| ORG-CON-004 | allocates Responsibility | section 9.4 |
| ORG-CON-005 | delegates Authority | section 9.5 |
| ORG-CON-006 | marshals Resource | section 9.6 |
| ORG-CON-007 | undertakes Activity | section 9.7 |
| ORG-CON-008 | operates within Authority | section 9.8 |
| ORG-CON-009 | is governed by Policy | section 9.9 |
| ORG-CON-010 | observes Constraints | section 9.10 |
| ORG-CON-011 | operates under Governance | section 9.11 |
| ORG-CON-012 | is accountable under Accountability | section 9.12 |
| ORG-CON-013 | produces Organizational Outcome | section 9.13 |
| ORG-CON-014 | supports Escalation | section 9.14 |
| ORG-CON-015 | retains Agentic/Autonomous orthogonality | section 9.15 |
| ORG-CON-016 | contains provenance | section 9.16 |

## Negative Tests (CR-ES-022 section 10)

| ID | Subject | CR Section |
|---|---|---|
| ORG-NEG-001 | Organization is-a Enterprise | section 10.1 |
| ORG-NEG-002 | Organization is-a Process | section 10.2 |
| ORG-NEG-003 | Organization is-a Activity | section 10.3 |
| ORG-NEG-004 | Organization is-a Capability | section 10.4 |
| ORG-NEG-005 | Organization is-a Value Stream | section 10.5 |
| ORG-NEG-006 | Organization is-a Operations | section 10.6 |
| ORG-NEG-007 | Organization is-a Agent | section 10.7 |
| ORG-NEG-008 | Enterprise is-a Organization | section 10.8 |
| ORG-NEG-009 | Process is-a Organization | section 10.9 |
| ORG-NEG-010 | Activity is-a Organization | section 10.10 |
| ORG-NEG-011 | Capability is-a Organization | section 10.11 |
| ORG-NEG-012 | Value Stream is-a Organization | section 10.12 |
| ORG-NEG-013 | Operations is-a Organization | section 10.13 |
| ORG-NEG-014 | Agent is-a Organization | section 10.14 |
