#!/usr/bin/env bash

set -euo pipefail


source .venv/bin/activate



export SENTRY_USE_ENVIRONMENT=True
export SENTRY_TRACE=xbcabcabcabcabcabcabcabcabcabcab-1231231231231231-1 
printenv | grep SENTRY

python main.py "$@"
