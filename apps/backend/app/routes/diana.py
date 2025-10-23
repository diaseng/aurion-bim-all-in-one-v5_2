
from fastapi import APIRouter
router = APIRouter()
@router.get("/ping")
def ping():
    return {"module":"diana","status":"ok"}
