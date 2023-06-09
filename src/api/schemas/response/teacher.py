from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TeacherResponse(BaseModel):
    """Схема для отображения информаци о студенте."""

    id: UUID
    name: str
    surname: str
    patronymic: Optional[str]
    degree: str
    faculty_id: Optional[UUID]

    class Config:
        orm_mode = True
