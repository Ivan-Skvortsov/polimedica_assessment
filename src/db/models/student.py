import enum
from datetime import date
from typing import Optional
from uuid import UUID

from sqlalchemy import DATE, Enum, ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class Student(Base):
    """Студент."""

    class Gender(str, enum.Enum):
        """Пол."""

        MALE = "MALE"
        FEMALE = "FEMALE"

    __tablename__ = "student"

    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30), index=True)
    patronymic: Mapped[Optional[str]] = mapped_column(String(30))
    gender: Mapped[str] = mapped_column(
        Enum(Gender, name="student_gender", vallues_callable=lambda obj: [e.value for e in obj])  # noqa
    )
    date_of_birth: Mapped[date] = mapped_column(DATE)
    group_id: Mapped[UUID] = mapped_column(
        ForeignKey("group.id"), nullable=True
    )
    year_of_entry: Mapped[int] = mapped_column(SmallInteger)
