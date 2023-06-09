from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from src.api.schemas.request.course import CourseCreateRequest
from src.api.schemas.response.course import CourseResponse
from src.db.crud.course import CourseCRUD
from src.db.models import Course

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post(
    "/",
    response_model=CourseResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.CREATED,
    summary="Создать новый курс.",
    response_description="Информация созданном курсе."
)
async def create_course(
    course_data: CourseCreateRequest,
    course_crud: CourseCRUD = Depends()
) -> CourseResponse:
    """Создаёт новый курс."""  # TODO описание
    course = Course(**course_data.dict())
    return await course_crud.create(course)


@router.get(
    "/{course_id}",
    response_model=CourseResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Получить информацию о курсе по его id.",
    response_description="Информация о курсе."
)
async def get_student(
    course_id: UUID,
    course_crud: CourseCRUD = Depends()
) -> CourseResponse:
    """Получить информацию о курсе по его id."""  # TODO описание
    return await course_crud.get(course_id)
