from datetime import date
from uuid import UUID

from pydantic import BaseModel


class ExamResponse(BaseModel):
    """Схема для отображения информации об экзамене."""

    id: UUID
    exam_date: date
    student_id: UUID
    grade_id: UUID
    course_id: UUID
    semester_id: UUID
    teacher_id: UUID

    class Config:
        orm_mode = True
