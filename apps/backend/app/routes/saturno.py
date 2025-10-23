
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_sessionmaker
from ..models import SinapiItem

router = APIRouter()

class SinapiIn(BaseModel):
    code: str
    description: str
    unit: str
    price: float

class SinapiOut(SinapiIn):
    id: int

async def get_db() -> AsyncSession:
    Session = get_sessionmaker()
    if not Session:
        raise HTTPException(status_code=503, detail="Database not configured")
    async with Session() as s:
        yield s

@router.get("/ping")
async def ping():
    return {"module":"saturno","status":"ok"}

@router.post("/items", response_model=SinapiOut)
async def create_item(payload: SinapiIn, db: AsyncSession = Depends(get_db)):
    item = SinapiItem(code=payload.code, description=payload.description, unit=payload.unit, price=payload.price)
    db.add(item)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=409, detail="Item code already exists")
    await db.refresh(item)
    return SinapiOut(id=item.id, **payload.model_dict())

@router.get("/items", response_model=list[SinapiOut])
async def list_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(SinapiItem).order_by(SinapiItem.code))
    rows = result.scalars().all()
    return [SinapiOut(id=r.id, code=r.code, description=r.description, unit=r.unit, price=r.price) for r in rows]

@router.post("/mock/load")
async def mock_load(db: AsyncSession = Depends(get_db)):
    sample = [
        {"code":"ALV-0001","description":"Areia lavada média","unit":"m³","price":152.40},
        {"code":"CIM-0010","description":"Cimento CP-II 50kg","unit":"sc","price":38.90},
        {"code":"MAO-0100","description":"Servente de obra","unit":"h","price":12.75},
    ]
    inserted = 0
    for x in sample:
        exists = await db.execute(select(SinapiItem).where(SinapiItem.code==x["code"]))
        if not exists.scalar_one_or_none():
            db.add(SinapiItem(**x))
            inserted += 1
    await db.commit()
    return {"inserted": inserted, "total": len(sample)}
