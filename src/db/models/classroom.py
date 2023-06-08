from uuid import UUID

from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class ClassRoom(Base):
    """Аудитория."""

    __tablename__ = "classroom"

    number: Mapped[int] = mapped_column(SmallInteger)
    building_id: Mapped[UUID] = mapped_column(
        ForeignKey("building.id", ondelete="CASCADE")
    )
