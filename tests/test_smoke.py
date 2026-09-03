"""Smoke test for the enterprise-semantics-test-probe harness.

Verifies that the harness correctly delegates to the authority repo's
conformance scripts. This test is runnable on CI only when the authority
repo is checked out as a sibling of test-probe (the default workspace
layout under /home/hermes/Projects/Enterprise-Semantics/repos/).

In CI on the authority repo itself, the test is skipped (the harness is
invoked via the GitHub Actions workflow, not via pytest).
"""
import shutil
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
HARNESS = HERE.parent / "tools" / "validate.py"


def authority_repo() -> Path | None:
    """Find the enterprise-semantics authority repo if it is available."""
    candidates = [
        HERE.parent / "enterprise-semantics",
        HERE.parent.parent / "enterprise-semantics",
    ]
    for c in candidates:
        if (c / "conformance" / "check.py").is_file():
            return c
    return None


def test_harness_help_runs():
    """The --help flag must always work, even without an authority repo."""
    if not HARNESS.is_file():
        # Skip if harness missing
        return
    r = subprocess.run([sys.executable, str(HARNESS), "--help"],
                       capture_output=True, text=True, timeout=30)
    assert r.returncode == 0, f"harness --help failed: {r.stderr}"
    assert "--mode" in r.stdout


def test_harness_passes_against_authority():
    """If the authority repo is reachable, the harness must report NO_DRIFT."""
    src = authority_repo()
    if src is None:
        # CI on the authority repo itself or on a separate test-probe clone
        # without a sibling authority repo ;; skip.
        return
    r = subprocess.run([sys.executable, str(HARNESS), "--mode", "all",
                        "--source", str(src)],
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 0, (
        f"harness failed: stdout={r.stdout!r} stderr={r.stderr!r}"
    )
    assert "NO_DRIFT" in r.stdout, r.stdout
