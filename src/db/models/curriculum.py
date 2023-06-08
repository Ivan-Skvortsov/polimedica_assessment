from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class Curriculum(Base):
    """Учебный план."""

    __tablename__ = "curriculum"

    group_id: Mapped[UUID] = mapped_column(ForeignKey("group.id"))
    course_id: Mapped[UUID] = mapped_column(ForeignKey("course.id"))
    semester_id: Mapped[UUID] = mapped_column(ForeignKey("semester.id"))
