from uuid import UUID

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.db import get_session
from src.db.crud.base import BaseCRUD
from src.db.models import Course, Group, Student, TimeTable


class CourseCRUD(BaseCRUD):
    """Класс, реализующий работу БД с сущностю Course."""

    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        super().__init__(session, Course)

    async def get_course_students(self, course_id: UUID) -> list[Student]:
        """Получить список студентов, обучающихся на курсе."""
        statement = (
            select(Student).join(Group)
                           .join(TimeTable)
                           .join(Course)
                           .where(Course.id == course_id)
        )
        students = await self._session.execute(statement)
        return students.scalars().all()
