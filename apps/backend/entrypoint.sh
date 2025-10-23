
#!/usr/bin/env bash
set -e

if [[ -n "$DATABASE_URL" && -z "$DATABASE_URL_SYNC" ]]; then
  export DATABASE_URL_SYNC="${DATABASE_URL/postgresql+asyncpg:\/\//postgresql://}"
fi

if [[ -n "$DATABASE_URL_SYNC" ]]; then
  echo "Running Alembic migrations..."
  alembic upgrade head || { echo 'Alembic failed'; exit 1; }
else
  echo "DATABASE_URL not set; skipping migrations."
fi

exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}
