#!/usr/bin/env bash
# One-time setup for the FitAnalysis extraction tooling.
# Creates a project-local Python virtual environment (.venv) and installs the
# libraries scripts/extract.py needs. Safe to re-run.
#
# Usage:  bash scripts/setup.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "==> Creating virtual environment at .venv"
python3 -m venv .venv

echo "==> Installing extraction dependencies"
.venv/bin/pip install --quiet --upgrade pip
.venv/bin/pip install --quiet -r scripts/requirements.txt

echo "==> Done. Extractor ready:"
echo "    .venv/bin/python scripts/extract.py <path-to-document>"
