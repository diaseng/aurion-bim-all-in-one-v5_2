
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, Float, Integer

Base = declarative_base()

class SinapiItem(Base):
    __tablename__ = "sinapi_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    description: Mapped[str] = mapped_column(String(512))
    unit: Mapped[str] = mapped_column(String(16))
    price: Mapped[float] = mapped_column(Float)
