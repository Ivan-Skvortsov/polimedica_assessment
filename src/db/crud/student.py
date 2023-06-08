from typing import Optional
from uuid import UUID

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.db import get_session
from src.db.models import Student


class StudentCRUD:
    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self.__session = session

    async def get_one_or_none(self, id_: UUID) -> Optional[Student]:
        db_obj = await self.__session.execute(
            select(Student).where(Student.id == id_)
        )
        return db_obj.scalars().first()

    async def get(self, id_: UUID) -> Student:
        db_obj = await self.get_one_or_none(id_)
        if not db_obj:
            raise LookupError  # TODO
        return db_obj
