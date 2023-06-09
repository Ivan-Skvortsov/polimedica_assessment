from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from src.api.schemas.request.student import (StudentCreateRequest,
                                             StudentUpdateRequest)
from src.api.schemas.response.student import StudentResponse
from src.db.crud.student import StudentCRUD
from src.db.models import Student

router = APIRouter(prefix="/students", tags=["Students"])


@router.post(
    "/",
    response_model=StudentResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.CREATED,
    summary="Создать нового студента.",
    response_description="Информация о созданном студенте."
)
async def create_student(
    student_data: StudentCreateRequest,
    student_crud: StudentCRUD = Depends()
) -> StudentResponse:
    """Создать нового студента."""  # TODO описание
    student = Student(**student_data.dict())
    return await student_crud.create(student)


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Получить информацию о студенте по его id.",
    response_description="Информация о студенте."
)
async def get_student(
    student_id: UUID,
    student_crud: StudentCRUD = Depends()
) -> StudentResponse:
    """Получить информацию о студенте по его id.

    - **id**: уникальный иднетификатор студента
    - **name**: имя студента
    - **surname**: фамилия студента
    - **patronymic**: отчество студента (при наличии)
    - **gender**: пол студента
    - **date_of_birth**: дата рождения студента
    - **group_id**: ИД группы, в которой обучается студент (при наличии)
    - **year_of_entry**: год поступления в ВУЗ
    """
    return await student_crud.get(student_id)


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Обновить информацию о студенте.",
    response_description="Обновленная информация о студенте."
)
async def update_student(
    student_id: UUID,
    student_data: StudentUpdateRequest,
    student_crud: StudentCRUD = Depends()
) -> StudentResponse:
    """Обновить информацию о студенте."""  # TODO описание
    student = Student(**student_data.dict())
    return await student_crud.update(student_id, student)


@router.delete(
    "/{student_id}",
    status_code=HTTPStatus.NO_CONTENT,
    summary="Удалить студента.",
)
async def delete_student(
    student_id: UUID,
    student_crud: StudentCRUD = Depends()
) -> None:
    """Удалить студента."""  # TODO описание
    return await student_crud.delete(student_id)
