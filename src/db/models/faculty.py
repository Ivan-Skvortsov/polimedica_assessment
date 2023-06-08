from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models import Base


class Faculty(Base):
    """Факультет."""

    __tablename__ = "faculty"

    name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(16))
    building_id: Mapped[UUID] = mapped_column(ForeignKey("building.id"))

    teachers: Mapped[list["Teacher"]] = relationship()  # noqa
