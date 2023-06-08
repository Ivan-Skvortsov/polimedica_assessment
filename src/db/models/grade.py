from sqlalchemy import SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class Grade(Base):
    """Оценка."""

    __tablename__ = "grade"
    score: Mapped[int] = mapped_column(SmallInteger)
