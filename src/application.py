from http import HTTPStatus

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import routers
from src.api.exception_handlers import internal_server_error_handler


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(routers.student_router)
    app.include_router(routers.teacher_router)
    app.include_router(routers.course_router)

    # TODO
    origins = ["*"]

    app.add_exception_handler(
        HTTPStatus.INTERNAL_SERVER_ERROR,
        internal_server_error_handler
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "DELETE"],
        allow_headers=[
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin"
        ]
    )
    return app
