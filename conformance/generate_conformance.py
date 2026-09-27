#!/usr/bin/env python3
"""conformance/generate_conformance.py

CI-generated conformance section per ES-ADR-030 + ES-CR-030 (DP3 = C).
Reads all tests/kits/*/kit.yaml manifests, renders the conformance section
into an output directory (default: rendered-conformance/). Never hand-edited.

Author: Emmanuel A. Otchere (cardinal author rule, 2026-09-24)
"""
import sys
import yaml
from pathlib import Path

KIT_GLOB = "tests/kits/*/kit.yaml"

def load_kits(root: Path):
    kits = []
    for kf in sorted(root.glob(KIT_GLOB)):
        kits.append(yaml.safe_load(kf.read_text()))
    return kits

def render_index(kits):
    lines = [
        "# Conformance ; Enterprise-Semantics",
        "",
        "> CI-generated per ES-ADR-030 + ES-CR-030. Do not hand-edit.",
        f"> Concepts covered: {len(kits)}",
        "",
        "## Coverage Matrix",
        "",
    ]
    for k in kits:
        cov = k.get("coverage", {})
        lines.append(f"### {k.get('canonical_name')} (`{k.get('concept')}`)")
        lines.append("")
        lines.append(f"- Status: {k.get('status')}")
        lines.append(f"- Version: {k.get('version')}")
        lines.append(f"- Base concept: {k.get('base_concept')}")
        lines.append(f"- Concept repo: {k.get('concept_repo')}")
        lines.append(f"- Tests: {cov.get('total', 0)} (positive {cov.get('positive', 0)} ; negative {cov.get('negative', 0)} ; integrity {cov.get('integrity', 0)} ; other {cov.get('other', 0)})")
        lines.append(f"- Boundary assertions covered: {len(k.get('boundary_assertions_covered', []))}")
        lines.append("")
    lines.append("## Author")
    lines.append("")
    lines.append("Emmanuel A. Otchere (cardinal author rule, 2026-09-24)")
    return "\n".join(lines) + "\n"

def render_page(k):
    cov = k.get("coverage", {})
    lines = [
        f"# Conformance ; {k.get('canonical_name')}",
        "",
        "> CI-generated per ES-ADR-030 + ES-CR-030. Do not hand-edit.",
        "",
        f"- Concept: `{k.get('concept')}`",
        f"- Base concept: {k.get('base_concept')}",
        f"- Status: {k.get('status')}",
        f"- Version: {k.get('version')}",
        f"- Concept repo: {k.get('concept_repo')}",
        f"- Test path: {k.get('test_path', 'tests/' + k.get('concept', '').split(':')[-1] + '/')}",
        f"- Test source branch: {k.get('test_source_branch', 'n/a')}",
        "",
        "## Coverage",
        "",
        f"- Positive: {cov.get('positive', 0)}",
        f"- Negative: {cov.get('negative', 0)}",
        f"- Integrity: {cov.get('integrity', 0)}",
        f"- Other: {cov.get('other', 0)}",
        f"- Total: {cov.get('total', 0)}",
        "",
        "## Boundary Assertions Covered",
        "",
    ]
    for a in k.get("boundary_assertions_covered", []):
        lines.append(f"- {a}")
    prov = k.get("provenance", {})
    lines += ["", "## Provenance", ""]
    for key, val in prov.items():
        lines.append(f"- {key}: {', '.join(val) if isinstance(val, list) else val}")
    lines += ["", "## Author", "", "Emmanuel A. Otchere (cardinal author rule, 2026-09-24)"]
    return "\n".join(lines) + "\n"

def main():
    root = Path(__file__).resolve().parent.parent
    outdir = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "rendered-conformance"
    outdir.mkdir(parents=True, exist_ok=True)
    kits = load_kits(root)
    (outdir / "README.md").write_text(render_index(kits))
    for k in kits:
        slug = k.get("id", "").split(":")[-1]
        (outdir / f"{slug}.md").write_text(render_page(k))
    print(f"generated {len(kits)} concept pages + index into {outdir}")

if __name__ == "__main__":
    main()
