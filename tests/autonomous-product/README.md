# Autonomous Product Conformance Tests

Per CR-ES-017 §10 + §9 + ADR-ES-017 §17.

## Coverage

This directory contains:

- 1 README (this file)
- 21 positive tests (APROD-AUTO-CON-001 .. APROD-AUTO-CON-021) per CR-ES-017 §10
- 16 negative tests (APROD-AUTO-NEG-001 .. APROD-AUTO-NEG-016) per CR-ES-017 §9

## Authoring

Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-24).

## Test Pattern

Each test file is a stub following the format established by prior tranches (ES-012/013/014/015/016). Each test file:

1. References its CR section number and ADR section number in the file header
2. States the test assertion in human-readable form
3. Provides the expected conformance / non-conformance verdict
4. Names the validator behavior required (per CR-ES-017 §8 + §10)

## Cardinal Rules

- Zero en-dash (U+2013)
- Zero em-dash (U+2014)
- Zero horizontal-ellipsis divider (U+2E3B)
- Zero inline 3-semicolon dividers (replace with comma)
- Zero vendor-specific embargoed references
- Cardinal author signature on every file

## Positive Tests (CR-ES-017 §10)

| ID | Subject | CR Section |
|---|---|---|
| APROD-AUTO-CON-001 | specializes Product | §10.1 |
| APROD-AUTO-CON-002 | retains Product semantics | §10.2 |
| APROD-AUTO-CON-003 | demonstrates material autonomy | §10.3 |
| APROD-AUTO-CON-004 | has defined product objective | §10.4 |
| APROD-AUTO-CON-005 | has bounded decision scope | §10.5 |
| APROD-AUTO-CON-006 | has bounded action scope | §10.6 |
| APROD-AUTO-CON-007 | operates within authority | §10.7 |
| APROD-AUTO-CON-008 | respects policy | §10.8 |
| APROD-AUTO-CON-009 | respects constraints | §10.9 |
| APROD-AUTO-CON-010 | operates within governance | §10.10 |
| APROD-AUTO-CON-011 | observes outcomes | §10.11 |
| APROD-AUTO-CON-012 | may adapt | §10.12 |
| APROD-AUTO-CON-013 | supports escalation | §10.13 |
| APROD-AUTO-CON-014 | permits human intervention | §10.14 |
| APROD-AUTO-CON-015 | does not require AI | §10.15 |
| APROD-AUTO-CON-016 | does not require automation | §10.16 |
| APROD-AUTO-CON-017 | may use Workflow | §10.17 |
| APROD-AUTO-CON-018 | may use Agentic Workflow | §10.18 |
| APROD-AUTO-CON-019 | may use Autonomous Operations | §10.19 |
| APROD-AUTO-CON-020 | preserves Agentic/Autonomous orthogonality | §10.20 |
| APROD-AUTO-CON-021 | contains complete provenance | §10.21 |

## Negative Tests (CR-ES-017 §9)

| ID | Subject | CR Section |
|---|---|---|
| APROD-AUTO-NEG-001 | Autonomous Product is-a Agentic Product | §9.1 |
| APROD-AUTO-NEG-002 | Autonomous Product is-a Autonomous Service | §9.2 |
| APROD-AUTO-NEG-003 | Autonomous Product is-a Autonomous Capability | §9.3 |
| APROD-AUTO-NEG-004 | Autonomous Product is-a Autonomous Operations | §9.4 |
| APROD-AUTO-NEG-005 | Autonomous Product is-a Autonomous Value Stream | §9.5 |
| APROD-AUTO-NEG-006 | Autonomous Product requires AI | §9.6 |
| APROD-AUTO-NEG-007 | AI automatically establishes Autonomous Product | §9.7 |
| APROD-AUTO-NEG-008 | Automation automatically establishes Autonomous Product | §9.8 |
| APROD-AUTO-NEG-009 | Product containing an Agent automatically becomes Autonomous Product | §9.9 |
| APROD-AUTO-NEG-010 | Autonomous Product requires elimination of humans | §9.10 |
| APROD-AUTO-NEG-011 | Autonomous Product has unlimited authority | §9.11 |
| APROD-AUTO-NEG-012 | Autonomous Product has no governance boundary | §9.12 |
| APROD-AUTO-NEG-013 | Autonomous Operations automatically makes every Product autonomous | §9.13 |
| APROD-AUTO-NEG-014 | Autonomous Value Stream automatically makes every Product autonomous | §9.14 |
| APROD-AUTO-NEG-015 | Autonomous Product implies Autonomous Enterprise | §9.15 |
| APROD-AUTO-NEG-016 | Autonomous Product requires every product action to be autonomous | §9.16 |
