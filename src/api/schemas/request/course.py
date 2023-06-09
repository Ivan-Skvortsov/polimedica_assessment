from pydantic import BaseModel, Extra, Field


class CourseCreateRequest(BaseModel):
    """Схема для создания нового курса."""

    name: str = Field(..., min_length=2, max_length=100)
    hours: int

    class Config:
        extra = Extra.forbid
