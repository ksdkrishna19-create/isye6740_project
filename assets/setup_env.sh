#!/usr/bin/env bash
# One-shot environment setup for this project.
# Usage: bash assets/setup_env.sh   (run from the project root, or anywhere)
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment at .venv ..."
    python3 -m venv .venv
fi

echo "Installing Python dependencies from requirements.txt ..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

# xgboost on macOS needs the libomp OpenMP runtime, which is a system
# library (not installable via pip). Check for it and warn if missing.
if [[ "$(uname)" == "Darwin" ]]; then
    if ! .venv/bin/python -c "import xgboost" >/dev/null 2>&1; then
        echo
        echo "xgboost failed to import. On macOS this is almost always a"
        echo "missing OpenMP runtime. Fix with Homebrew:"
        echo "    brew install libomp"
        echo "(Install Homebrew first from https://brew.sh if you don't have it.)"
    fi
fi

echo
echo "Setup complete. Activate the environment with:"
echo "    source .venv/bin/activate"
