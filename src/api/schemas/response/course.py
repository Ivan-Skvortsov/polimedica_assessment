from uuid import UUID

from pydantic import BaseModel


class CourseResponse(BaseModel):
    """Схема для отображения информаци о курсе."""

    id: UUID
    name: str
    hours: int

    class Config:
        orm_mode = True
