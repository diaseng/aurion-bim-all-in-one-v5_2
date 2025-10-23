
from alembic import context
from sqlalchemy import engine_from_config, pool
import os

config = context.config
target_metadata = None

def run_migrations_offline():
    url = os.getenv("DATABASE_URL_SYNC", "")
    if not url:
        async_url = os.getenv("DATABASE_URL", "")
        if async_url.startswith("postgresql+asyncpg://"):
            url = async_url.replace("postgresql+asyncpg://", "postgresql://")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    url = os.getenv("DATABASE_URL_SYNC", "")
    if not url:
        async_url = os.getenv("DATABASE_URL", "")
        if async_url.startswith("postgresql+asyncpg://"):
            url = async_url.replace("postgresql+asyncpg://", "postgresql://")
    connectable = engine_from_config({"sqlalchemy.url": url}, prefix="", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
