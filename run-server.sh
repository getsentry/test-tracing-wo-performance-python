#!/usr/bin/env bash

set -euo pipefail

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

export SENTRY_USE_ENVIRONMENT=True
export SENTRY_TRACE=ybcabcabcabcabcabcabcabcabcabcab-1231231231231231-1 
printenv | grep SENTRY

python server.py
