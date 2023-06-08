from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models import Base


class Department(Base):
    """Отделение."""

    __tablename__ = "department"

    name: Mapped[str] = mapped_column(String(20))

    groups: Mapped[list["Group"]] = relationship()  # noqa
