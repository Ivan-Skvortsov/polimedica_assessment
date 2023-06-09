from http import HTTPStatus
from typing import Any

from fastapi import HTTPException


class BaseApplicationException(HTTPException):

    status_code: int = None
    detail: str = "Упс! Что-то пошло не так. Пожалуйста, попробуйте позже."
    headers: dict[str, Any] = None

    def __init__(self):
        super().__init__(
            status_code=self.status_code,
            detail=self.detail,
            headers=self.headers
        )


class DatabaseObjectNotFound(BaseApplicationException):

    def __init__(self, detail: str):
        self.detail = detail
        self.status_code = HTTPStatus.NOT_FOUND
