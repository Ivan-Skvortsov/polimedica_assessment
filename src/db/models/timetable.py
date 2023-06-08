from uuid import UUID

from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class TimeTable(Base):
    """Расписание."""

    __tablename__ = "timetable"

    group_id: Mapped[UUID] = mapped_column(ForeignKey("group.id"))
    day_of_week: Mapped[int] = mapped_column(SmallInteger)
    lesson_number: Mapped[int] = mapped_column(SmallInteger)
    course_id: Mapped[UUID] = mapped_column(ForeignKey("course.id"))
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey("teacher.id"))
    classroom_id: Mapped[UUID] = mapped_column(ForeignKey("classroom.id"))
