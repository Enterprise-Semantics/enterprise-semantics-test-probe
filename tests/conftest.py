"""Pytest configuration for enterprise-semantics-test-probe.

Adds tools/ to sys.path so tests can import harness helpers if needed.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
