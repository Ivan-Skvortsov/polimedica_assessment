from sqlalchemy import Column, ForeignKey, Table

from src.db.models import Base

course_teacher = Table(
    "course_teacher",
    Base.metadata,
    Column("course_id", ForeignKey("course.id", ondelete="CASCADE")),
    Column("teacher_id", ForeignKey("teacher.id", ondelete="CASCADE")),
)
