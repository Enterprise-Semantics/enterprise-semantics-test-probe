#!/usr/bin/env python3
"""validate.py ;;; Enterprise-Semantics conformance gate.

Phase 5 (PLAN §Phase 5.1-5.2): this harness is the CI gate applied to
enterprise-semantics and enterprise-semantics-mappings. It does NOT duplicate
the source-of-truth schema and harness in enterprise-semantics/conformance/;
instead it imports those modules (or invokes them via subprocess) so a single
change to the schema or harness automatically takes effect on every
consumer.

Run modes:
- `--mode profile`        ;; invoke conformance/check.py in enterprise-semantics
- `--mode concepts`       ;; invoke conformance/check_concepts.py
- `--mode all` (default)  ;; run both, fail if either fails
- `--source PATH`         ;; optional override of authority repo path
                           ;; (default: ../enterprise-semantics)
- `--pytest PATH`         ;; also invoke pytest at PATH (relative to source)

Exit code 0 on NO_DRIFT, non-zero on DRIFT_DETECTED or harness error.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def find_authority_source(start: Path) -> Path:
    """Locate the enterprise-semantics authority repo. Search order:
    1. `--source PATH` if provided
    2. `../enterprise-semantics` (sibling of test-probe in the workspace)
    3. CWD/enterprise-semantics
    4. The current directory if it contains `conformance/check.py`
    """
    here = Path(__file__).resolve().parent  # tools/
    test_probe = here.parent                  # repo root of test-probe
    workspace = test_probe.parent             # parent of test-probe, e.g. .../repos
    for candidate in (workspace / "enterprise-semantics",
                      test_probe / "enterprise-semantics",
                      Path.cwd() / "enterprise-semantics",
                      Path.cwd()):
        if (candidate / "conformance" / "check.py").is_file():
            return candidate
    raise FileNotFoundError(
        "enterprise-semantics authority repo not found. "
        "Pass --source PATH or place this repo as a sibling of "
        "enterprise-semantics."
    )


def run_harness(source: Path, script: str) -> tuple[int, str]:
    cmd = [sys.executable, str(source / "conformance" / script)]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=source)
    output = (proc.stdout + proc.stderr).strip()
    return proc.returncode, output


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise-Semantics CI gate")
    parser.add_argument("--mode", choices=["profile", "concepts", "all"],
                        default="all")
    parser.add_argument("--source", type=Path, default=None,
                        help="Path to enterprise-semantics authority repo")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    source = args.source or find_authority_source(here)
    print(f"source: {source}")

    failures: list[str] = []

    if args.mode in ("profile", "all"):
        rc, out = run_harness(source, "check.py")
        print(f"[profile] exit={rc}\n{out}")
        if rc != 0 or "DRIFT_DETECTED" in out:
            failures.append("profile")

    if args.mode in ("concepts", "all"):
        rc, out = run_harness(source, "check_concepts.py")
        print(f"[concepts] exit={rc}\n{out}")
        if rc != 0 or "DRIFT_DETECTED" in out:
            failures.append("concepts")

    if failures:
        print(f"FAIL: {', '.join(failures)} drift detected", file=sys.stderr)
        return 1
    print("PASS: NO_DRIFT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
