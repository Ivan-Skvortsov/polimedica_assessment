from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models import Base


class Course(Base):
    """Курс."""

    __tablename__ = "course"

    name: Mapped[str] = mapped_column(String(100))
    hours: Mapped[int] = mapped_column(SmallInteger)

    timetables: Mapped[list["TimeTable"]] = relationship()  # noqa
