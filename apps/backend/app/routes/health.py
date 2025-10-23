
from fastapi import APIRouter
from ..settings import settings
from ..db import get_engine
router = APIRouter()
@router.get("/ping")
async def ping():
    return {"status":"ok","service":"aurion-api","version":"5.2","env":settings.ENVIRONMENT}
@router.get("/db")
async def db_status():
    eng = get_engine()
    return {"database": "configured" if eng else "not_configured"}
@router.get("/live")
async def live():
    return {"live": True}
@router.get("/ready")
async def ready():
    return {"ready": True}
