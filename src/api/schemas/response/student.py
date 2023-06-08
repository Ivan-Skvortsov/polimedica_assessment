from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.db.models import Student


class StudentResponse(BaseModel):
    """Схема для отображения информаци о студенте."""

    id: UUID
    name: str
    surname: str
    patronymic: Optional[str]
    gender: Student.Gender
    date_of_birth: date
    group_id: Optional[UUID]
    year_of_entry: int

    class Config:
        orm_mode = True
