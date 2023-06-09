from pydantic import BaseModel, Extra


class CourseCreateRequest(BaseModel):
    """Схема для создания нового курса."""

    name: str
    hours: int

    class Config:
        extra = Extra.forbid
