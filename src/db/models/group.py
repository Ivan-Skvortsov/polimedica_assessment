from uuid import UUID

from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models import Base


class Group(Base):
    """Группа."""

    __tablename__ = "group"

    name: Mapped[str] = mapped_column(String(20))
    year_of_entry: Mapped[int] = mapped_column(SmallInteger)
    faculty_id: Mapped[UUID] = mapped_column(ForeignKey("faculty.id"))
    department_id: Mapped[UUID] = mapped_column(ForeignKey("department.id"))

    students: Mapped[list["Student"]] = relationship()  # noqa
