# Autonomous Organization Conformance Tests

Per CR-ES-021 section 15 + ADR-ES-021 section 18.

## Coverage

This directory contains:

- 1 README (this file)
- 21 positive tests (AORG-AUTO-CON-001 .. AORG-AUTO-CON-021) per CR-ES-021 section 15
- 16 negative tests (AORG-AUTO-NEG-001 .. AORG-AUTO-NEG-016) per CR-ES-021 section 15

## Foundational Status

Per CR-ES-021 section 2 + ADR-ES-021 section 16, Autonomous
Organization depends on the parent Organization concept being
canonical in Enterprise-Semantics. Per ADR-ES-022 + CR-ES-022
Accepted, the dependency is resolved at the governance level.
The parent Organization concept lives on the
docs/cr-es-022-vs-a-organization-concepts branch (not yet merged
to origin/main).

## Authoring

Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-24).

## Cardinal Rules

- Zero en-dash (U+2013)
- Zero em-dash (U+2014)
- Zero horizontal-ellipsis divider (U+2E3B)
- Zero inline 3-semicolon dividers (replace with comma)
- Zero vendor-specific embargoed references
- Cardinal author signature on every file

## Positive Tests (CR-ES-021 section 15)

| ID | Subject | CR Section |
|---|---|---|
| AORG-AUTO-CON-001 | specializes Organization | section 15.1 |
| AORG-AUTO-CON-002 | has organizational objective | section 15.2 |
| AORG-AUTO-CON-003 | has autonomy scope | section 15.3 |
| AORG-AUTO-CON-004 | has decision scope | section 15.4 |
| AORG-AUTO-CON-005 | has action scope | section 15.5 |
| AORG-AUTO-CON-006 | has coordination scope | section 15.6 |
| AORG-AUTO-CON-007 | supports adaptation | section 15.7 |
| AORG-AUTO-CON-008 | operates within authority | section 15.8 |
| AORG-AUTO-CON-009 | governed by policy | section 15.9 |
| AORG-AUTO-CON-010 | observes constraints | section 15.10 |
| AORG-AUTO-CON-011 | operates under governance | section 15.11 |
| AORG-AUTO-CON-012 | accountable under accountability | section 15.12 |
| AORG-AUTO-CON-013 | supports intervention model | section 15.13 |
| AORG-AUTO-CON-014 | supports escalation | section 15.14 |
| AORG-AUTO-CON-015 | supports observation | section 15.15 |
| AORG-AUTO-CON-016 | demonstrates material autonomy | section 15.16 |
| AORG-AUTO-CON-017 | permits human participation | section 15.17 |
| AORG-AUTO-CON-018 | preserves Agentic/Autonomous orthogonality | section 15.18 |
| AORG-AUTO-CON-019 | supports autonomous operational use | section 15.19 |
| AORG-AUTO-CON-020 | supports workflow use | section 15.20 |
| AORG-AUTO-CON-021 | OTCHERE example validity | section 15.21 |

## Negative Tests (CR-ES-021 section 15)

| ID | Subject | CR Section |
|---|---|---|
| AORG-AUTO-NEG-001 | Autonomous Organization is-a Agentic Organization | section 15.N1 |
| AORG-AUTO-NEG-002 | Autonomous Organization is-a Autonomous Enterprise | section 15.N2 |
| AORG-AUTO-NEG-003 | Autonomous Organization is-a Autonomous Operations | section 15.N3 |
| AORG-AUTO-NEG-004 | Autonomous Organization is-a Autonomous Service | section 15.N4 |
| AORG-AUTO-NEG-005 | Autonomous Organization is-a Autonomous Product | section 15.N5 |
| AORG-AUTO-NEG-006 | Autonomous Organization requires AI | section 15.N6 |
| AORG-AUTO-NEG-007 | Automation establishes Autonomous Organization | section 15.N7 |
| AORG-AUTO-NEG-008 | Autonomous Organization prohibits humans | section 15.N8 |
| AORG-AUTO-NEG-009 | Autonomous Organization has unlimited authority | section 15.N9 |
| AORG-AUTO-NEG-010 | Autonomous Organization has no governance | section 15.N10 |
| AORG-AUTO-NEG-011 | Autonomous Organization has no accountability | section 15.N11 |
| AORG-AUTO-NEG-012 | Autonomous Organization has no escalation | section 15.N12 |
| AORG-AUTO-NEG-013 | Autonomous Organization is-a Autonomous Offering | section 15.N13 |
| AORG-AUTO-NEG-014 | Autonomous Organization is-a Autonomous Workflow | section 15.N14 |
| AORG-AUTO-NEG-015 | Autonomous component establishes Autonomous Organization | section 15.N15 |
| AORG-AUTO-NEG-016 | Autonomous Organization requires Agentic behavior | section 15.N16 |
