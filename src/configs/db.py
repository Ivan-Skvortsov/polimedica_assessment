from typing import Generator

from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from .environment import settings

engine = create_async_engine(settings.database_url, echo=True)


async def get_session() -> Generator[AsyncSession, None, None]:
    """Генератор сессий."""
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    async with async_session() as session:
        yield session
