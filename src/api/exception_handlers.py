import logging
from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse


async def internal_server_error_handler(request: Request, exc: Exception):
    logging.exception(f"Необработанное исключение: {exc}")
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={
            "detail": "Упс! Что-то пошло не так. Пожалуйста, попробуйте позже."
        }
    )
