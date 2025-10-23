
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str = "production"
    PORT: int = 10000
    DATABASE_URL: str | None = None  # ex: postgresql+asyncpg://user:pass@host/db
    METRICS_ENABLED: bool = True

settings = Settings()
