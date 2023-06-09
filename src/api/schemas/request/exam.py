from datetime import date
from uuid import UUID

from pydantic import BaseModel, Extra


class ExamCreateRequest(BaseModel):
    """Схема для создания экзамена."""

    exam_date: date
    student_id: UUID
    grade_id: UUID
    course_id: UUID
    semester_id: UUID
    teacher_id: UUID

    class Config:
        extra = Extra.forbid


class ExamUpdateRequest(ExamCreateRequest):
    """Схема для обновления информации по экзамену."""

    pass
