from datetime import date
from uuid import UUID

from sqlalchemy import DATE, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class Exam(Base):
    """Экзамен."""

    __tablename__ = "exam"

    exam_date: Mapped[date] = mapped_column(DATE, index=True)
    student_id: Mapped[UUID] = mapped_column(ForeignKey("student.id"))
    grade_id: Mapped[UUID] = mapped_column(ForeignKey("grade.id"))
    course_id: Mapped[UUID] = mapped_column(ForeignKey("course.id"))
    semester_id: Mapped[UUID] = mapped_column(ForeignKey("semester.id"))
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey("teacher.id"))
