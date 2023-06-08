from datetime import date
from uuid import UUID

from sqlalchemy import DATE, Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class IndependentAssignment(Base):
    """Самостоятельное задание."""

    __tablename__ = "independent_assignment"

    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(Text)
    date_created: Mapped[date] = mapped_column(DATE, index=True)
    date_due: Mapped[date] = mapped_column(DATE)
    is_completed: Mapped[bool] = mapped_column(Boolean)
    student_id: Mapped[UUID] = mapped_column(ForeignKey("student.id"))
    grade_id: Mapped[UUID] = mapped_column(ForeignKey("grade.id"))
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey("teacher.id"))
    course_id: Mapped[UUID] = mapped_column(ForeignKey("course.id"))
