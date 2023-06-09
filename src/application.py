from http import HTTPStatus

from fastapi import FastAPI

from src.api import routers
from src.api.exception_handlers import internal_server_error_handler


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(routers.student_router)
    app.include_router(routers.teacher_router)
    app.include_router(routers.course_router)
    app.include_router(routers.grade_router)

    app.add_exception_handler(
        HTTPStatus.INTERNAL_SERVER_ERROR,
        internal_server_error_handler
    )

    return app
