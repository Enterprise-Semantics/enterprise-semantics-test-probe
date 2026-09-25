# Semantic Integrity Conformance Tests

Per CR-ES-022 section 11 + ADR-ES-022.

## Coverage

This directory contains:

- 1 README (this file)
- 20 positive tests (AAI-CON-001 .. AAI-CON-020) per CR-ES-022 section 11
- 15 negative tests (AAI-NEG-001 .. AAI-NEG-015) per CR-ES-022 section 11

## Authoring

Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-24).

## Cardinal Rules

- Zero en-dash (U+2013)
- Zero em-dash (U+2014)
- Zero horizontal-ellipsis divider (U+2E3B)
- Zero inline 3-semicolon dividers (replace with comma)
- Zero vendor-specific embargoed references
- Cardinal author signature on every file

## Positive Tests (CR-ES-022 section 11)

| ID | Subject |
|---|---|
| AAI-CON-001 | coverage registry validity |
| AAI-CON-002 | four-state characterization |
| AAI-CON-003 | independent dimensions (Agentic vs Autonomous) |
| AAI-CON-004 | specialization metadata completeness |
| AAI-CON-005 | dependency declaration |
| AAI-CON-006 | semantic delta documentation |
| AAI-CON-007 | materiality declaration |
| AAI-CON-008 | reusable cross-cutting vocabulary |
| AAI-CON-009 | candidate disposition (canonical) |
| AAI-CON-010 | candidate disposition (investigate) |
| AAI-CON-011 | candidate disposition (profile) |
| AAI-CON-012 | candidate disposition (deferred) |
| AAI-CON-013 | candidate disposition (rejected) |
| AAI-CON-014 | established family validation |
| AAI-CON-015 | Agentic pattern evaluation |
| AAI-CON-016 | Autonomous pattern evaluation |
| AAI-CON-017 | orthogonality preservation |
| AAI-CON-018 | specialization gate enforcement |
| AAI-CON-019 | dependency gate enforcement |
| AAI-CON-020 | mechanical symmetry prohibition |

## Negative Tests (CR-ES-022 section 11)

| ID | Subject |
|---|---|
| AAI-NEG-001 | automatic Agentic inheritance |
| AAI-NEG-002 | automatic Autonomous inheritance |
| AAI-NEG-003 | AI equivalence (Agentic implies AI) |
| AAI-NEG-004 | AI equivalence (Autonomous implies AI) |
| AAI-NEG-005 | Automation equivalence (Autonomous implies Automation) |
| AAI-NEG-006 | Automation equivalence (Agentic implies Automation) |
| AAI-NEG-007 | missing base concept |
| AAI-NEG-008 | missing semantic delta |
| AAI-NEG-009 | undocumented specialization |
| AAI-NEG-010 | mechanical symmetry canonicalization |
| AAI-NEG-011 | unauthorized canonicalization |
| AAI-NEG-012 | Agentic + AI conflation |
| AAI-NEG-013 | Autonomous + Automation conflation |
| AAI-NEG-014 | implicit base concept creation |
| AAI-NEG-015 | cross-cutting vocabulary divergence |
