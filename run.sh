#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env from .env.example"
fi

if [ ! -d .venv ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

source .venv/bin/activate
python -m pip install -q -r requirements.txt

echo "Starting PostgreSQL..."
docker-compose up -d postgres

echo "Waiting for PostgreSQL..."
for i in {1..30}; do
  if docker compose exec -T postgres pg_isready -U "${POSTGRES_USER:-energy_user}" -d "${POSTGRES_DB:-energy_db}" >/dev/null 2>&1; then
    break
  fi
  sleep 1
done

python -m src.pipeline

python -m src.db --create-views

echo "Launching Streamlit..."
streamlit run dashboard/app.py
