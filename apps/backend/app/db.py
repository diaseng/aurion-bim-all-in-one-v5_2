
from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .settings import settings

_engine: Optional[AsyncEngine] = None
_Session: Optional[sessionmaker] = None

def get_engine() -> Optional[AsyncEngine]:
    global _engine
    if _engine is None and settings.DATABASE_URL:
        _engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
    return _engine

def get_sessionmaker() -> Optional[sessionmaker]:
    global _Session
    eng = get_engine()
    if eng and _Session is None:
        _Session = sessionmaker(eng, expire_on_commit=False, class_=AsyncSession)
    return _Session
