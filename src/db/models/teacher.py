from typing import Optional
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models import Base
from src.db.models.course_teacher import course_teacher


class Teacher(Base):
    """Преподаватель."""

    __tablename__ = "teacher"

    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30), index=True)
    patronymic: Mapped[Optional[str]] = mapped_column(String(30))
    degree: Mapped[str] = mapped_column(String(20))
    faculty_id: Mapped[Optional[UUID]] = mapped_column(ForeignKey("faculty.id"))  # noqa

    courses: Mapped[list["Course"]] = relationship(secondary=course_teacher)  # noqa
