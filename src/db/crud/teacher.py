from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.db import get_session
from src.db.crud.base import BaseCRUD
from src.db.models import Teacher


class TeacherCRUD(BaseCRUD):
    """Класс, реализующий работу БД с сущностю Teacher."""

    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        super().__init__(session, Teacher)
