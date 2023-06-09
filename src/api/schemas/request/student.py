from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Extra, Field

from src.db.models import Student


class StudentCreateRequest(BaseModel):
    """Схема для создания нового студента."""

    surname: str = Field(..., min_length=2, max_length=30)
    name: str = Field(..., min_length=2, max_length=30)
    patronymic: Optional[str] = Field(min_length=2, max_length=30)
    gender: Student.Gender
    date_of_birth: date
    year_of_entry: int = Field(
        ..., gt=1900, description="Год поступления не может быть меньше 1900"
    )

    class Config:
        extra = Extra.forbid


class StudentUpdateRequest(StudentCreateRequest):
    """Схема для обновления информации о студенте."""

    group_id: Optional[UUID]
