#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../apps/backend"; python -m venv .venv; source .venv/bin/activate; pip install -r requirements.txt; (uvicorn app.main:app --host 0.0.0.0 --port 8000) &
cd ../../apps/frontend; npm i; npm run dev
