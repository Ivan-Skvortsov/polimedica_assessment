from uuid import UUID

from sqlalchemy import ForeignKey, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class CourseProgramme(Base):
    """Программа курса."""

    __tablename__ = "course_programme"
    course_id: Mapped[UUID] = mapped_column(
        ForeignKey("course.id", ondelete="CASCADE")
    )
    title: Mapped[str] = mapped_column(String(100))
    descritpion: Mapped[str] = mapped_column(Text)
    hours: Mapped[int] = mapped_column(SmallInteger)
    semester_id: Mapped[UUID] = mapped_column(ForeignKey("semester.id"))
