from typing import Optional, TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.exceptions import DatabaseObjectNotFound

DatabaseModel = TypeVar("DatabaseModel")


class BaseCRUD:
    """Базовый класс, реализующий работу с БД."""

    def __init__(self, session: AsyncSession, model: DatabaseModel) -> None:
        self._session = session
        self._model = model

    async def create(self, instance: DatabaseModel) -> DatabaseModel:
        """Создает объект в БД."""
        self._session.add(instance)
        await self._session.commit()
        await self._session.refresh(instance)
        return instance

    async def get_one_or_none(self, id_: UUID) -> Optional[DatabaseModel]:
        """Получает объект из БД. Если его не существует, возвращает None."""
        db_obj = await self._session.execute(
            select(self._model).where(self._model.id == id_)
        )
        return db_obj.scalars().first()

    async def get(self, id_: UUID) -> DatabaseModel:
        """Получает объект из БД. Если его не существует, бросает ошибку."""
        db_obj = await self.get_one_or_none(id_)
        if not db_obj:
            raise DatabaseObjectNotFound(
                f"Объект {self._model.__name__} c ID {id_} не найден."
            )
        return db_obj

    async def get_all(self) -> list[DatabaseModel]:
        """Получет все объекты из БД."""
        db_objects = await self._session.scalars(select(self._model))
        return db_objects.all()

    async def update(self, id_: UUID, instance: DatabaseModel) -> DatabaseModel:  # noqa
        """Обновляет информацию о объекте в БД."""
        instance.id = id_
        instance = await self._session.merge(instance)
        await self._session.commit()
        return instance

    async def delete(self, id_: UUID) -> None:
        """Удаляет объект из БД."""
        db_obj = await self.get_one_or_none(id_)
        if not db_obj:
            raise DatabaseObjectNotFound(
                f"Объект {self._model.__name__} c ID {id_} не найден."
            )
        await self._session.delete(db_obj)
        await self._session.commit()
        await self._session.flush()
