from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from src.api.schemas.request.course import CourseCreateRequest
from src.api.schemas.response.course import CourseResponse
from src.api.schemas.response.student import StudentResponse
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
    """Создаёт новый курс.

    - **name**: название курса
    - **hours**: количество часов в курсе.
    """
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
async def get_course(
    course_id: UUID,
    course_crud: CourseCRUD = Depends()
) -> CourseResponse:
    """Получает информацию о курсе по его id.

    - **id**: уникальный идентификатор курса
    - **name**: название курса
    - **hours**: количество часов в курсе.
    """
    return await course_crud.get(course_id)


@router.get(
    "/{course_id}/students",
    response_model=list[StudentResponse],
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Получить список всех студентов на курсе.",
    response_description="Информация о студентах курса."
)
async def get_student(
    course_id: UUID,
    course_crud: CourseCRUD = Depends()
) -> list[StudentResponse]:
    """Получает список всех студентов на курсе.

    - **id**: уникальный иднетификатор студента
    - **name**: имя студента
    - **surname**: фамилия студента
    - **patronymic**: отчество студента (при наличии)
    - **gender**: пол студента
    - **date_of_birth**: дата рождения студента
    - **group_id**: ИД группы, в которой обучается студент (при наличии)
    - **year_of_entry**: год поступления в ВУЗ.
    """
    return await course_crud.get_course_students(course_id)
