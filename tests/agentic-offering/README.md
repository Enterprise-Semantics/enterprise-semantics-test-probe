# Agentic Offering Conformance Tests

Per CR-ES-018 §14 + ADR-ES-018 §17.

## Coverage

This directory contains:

- 1 README (this file)
- 20 positive tests (AOFF-CON-001 .. AOFF-CON-020) per CR-ES-018 §14
- 15 negative tests (AOFF-NEG-001 .. AOFF-NEG-015) per CR-ES-018 §14

## Foundational Dependency Gate

Per ADR-ES-018 §16 + CR-ES-018 §2, the implementation depends on the
parent Offering concept being canonical in Enterprise-Semantics.
As of 2026-09-25, the parent Offering concept is NOT yet canonical.
Per user directive message 1552900782440058902 ("Proceed with 18"),
implementation proceeded with the dependency documented.

The conformance tests verify the Agentic Offering specialization
semantics independently of whether the parent Offering concept is
canonical. The blocking test for the dependency is:

- AOFF-NEG-BLOCKED-001: Agentic Offering depends on Offering canonical

This test is marked BLOCKED until ADR-ES-019 (Offering canonical
grounding) is filed and Accepted.

## Authoring

Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-24).

## Test Pattern

Each test file is a stub following the format established by prior
tranches (ES-012/013/014/015/016/017).

## Cardinal Rules

- Zero en-dash (U+2013)
- Zero em-dash (U+2014)
- Zero horizontal-ellipsis divider (U+2E3B)
- Zero inline 3-semicolon dividers (replace with comma)
- Zero vendor-specific embargoed references
- Cardinal author signature on every file

## Positive Tests (CR-ES-018 §14)

| ID | Subject | CR Section |
|---|---|---|
| AOFF-CON-001 | specializes Offering | §14.1 |
| AOFF-CON-002 | retains Offering semantics | §14.2 |
| AOFF-CON-003 | material agentic behavior exists | §14.3 |
| AOFF-CON-004 | stakeholder intent may be interpreted | §14.4 |
| AOFF-CON-005 | context may influence realization | §14.5 |
| AOFF-CON-006 | configuration may be dynamically selected | §14.6 |
| AOFF-CON-007 | composition may be dynamically selected | §14.7 |
| AOFF-CON-008 | coordination may occur | §14.8 |
| AOFF-CON-009 | adaptation may occur | §14.9 |
| AOFF-CON-010 | authority boundary exists | §14.10 |
| AOFF-CON-011 | policy/constraint boundary exists | §14.11 |
| AOFF-CON-012 | outcome orientation exists | §14.12 |
| AOFF-CON-013 | human intervention is permitted | §14.13 |
| AOFF-CON-014 | Agentic Product may participate | §14.14 |
| AOFF-CON-015 | Agentic Service may participate | §14.15 |
| AOFF-CON-016 | Agentic Workflow may participate | §14.16 |
| AOFF-CON-017 | AI is not required | §14.17 |
| AOFF-CON-018 | automation is not sufficient | §14.18 |
| AOFF-CON-019 | Agentic does not imply Autonomous | §14.19 |
| AOFF-CON-020 | provenance is complete | §14.20 |

## Negative Tests (CR-ES-018 §14)

| ID | Subject | CR Section |
|---|---|---|
| AOFF-NEG-001 | Agentic Offering is-a Agent | §14.21 |
| AOFF-NEG-002 | Agentic Offering is-a Agentic Product | §14.22 |
| AOFF-NEG-003 | Agentic Offering is-a Agentic Service | §14.23 |
| AOFF-NEG-004 | Agentic Offering is-a Agentic Workflow | §14.24 |
| AOFF-NEG-005 | Agentic Offering is-a Agentic Operations | §14.25 |
| AOFF-NEG-006 | Agentic Offering is-a Agentic Value Stream | §14.26 |
| AOFF-NEG-007 | Agentic Offering requires AI | §14.27 |
| AOFF-NEG-008 | AI automatically establishes Agentic Offering | §14.28 |
| AOFF-NEG-009 | Automation automatically establishes Agentic Offering | §14.29 |
| AOFF-NEG-010 | Offering containing an Agent automatically becomes Agentic Offering | §14.30 |
| AOFF-NEG-011 | Agentic Offering automatically becomes Autonomous Offering | §14.31 |
| AOFF-NEG-012 | Agentic Offering requires removal of humans | §14.32 |
| AOFF-NEG-013 | Agentic Offering has unlimited authority | §14.33 |
| AOFF-NEG-014 | Agentic Product automatically makes the whole Offering agentic | §14.34 |
| AOFF-NEG-015 | Agentic Service automatically makes the whole Offering agentic | §14.35 |

## Foundational Dependency Block Test

| ID | Subject | Status |
|---|---|---|
| AOFF-NEG-BLOCKED-001 | Agentic Offering depends on Offering canonical | BLOCKED until ADR-ES-019 Accepted |
