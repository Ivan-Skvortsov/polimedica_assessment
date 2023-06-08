from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class Building(Base):
    """Здание."""

    __tablename__ = "building"

    name: Mapped[str] = mapped_column(String(20), unique=True)
    city: Mapped[str] = mapped_column(String(20))
    street: Mapped[str] = mapped_column(String(100))
    house: Mapped[int] = mapped_column(SmallInteger)
    postal_code: Mapped[int] = mapped_column()
