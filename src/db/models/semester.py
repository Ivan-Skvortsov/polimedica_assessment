from sqlalchemy import SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class Semester(Base):
    """Семестр."""

    __tablename__ = "semester"

    number: Mapped[int] = mapped_column(SmallInteger)
