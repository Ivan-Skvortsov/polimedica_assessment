from uuid import UUID

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовый класс для моделей."""

    id: Mapped[UUID] = mapped_column(primary_key=True)
