from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Extra

from src.db.models import Student


class StudentCreateRequest(BaseModel):
    """Схема для создания нового студента."""

    surname: str
    name: str
    patronymic: Optional[str]
    gender: Student.Gender
    date_of_birth: date
    year_of_entry: int  # TODO валидация

    class Config:
        extra = Extra.forbid


class StudentUpdateRequest(StudentCreateRequest):
    """Схема для обновления информации о студенте."""

    group_id: Optional[UUID]
