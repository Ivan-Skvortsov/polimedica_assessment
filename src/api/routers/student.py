from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from src.api.schemas.request.student import StudentCreateRequest
from src.api.schemas.response.student import StudentResponse
from src.db.crud.student import StudentCRUD  # TODO

router = APIRouter(prefix="/students", tags=["Students"])


@router.post(
    "/",
    response_model=StudentResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.CREATED,
    summary="Создать нового студента.",
    response_description="Информация о созданном студенте."
)
async def create_student(student: StudentCreateRequest) -> StudentResponse:
    """Создать нового студента."""
    return {"Hello": "World!"}  # TODO


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Получить информацию о студенте по его id.",
    response_description="Информация о созданном студенте."
)
async def get_student(
    student_id: UUID,
    student_crud: StudentCRUD = Depends()
) -> StudentResponse:
    """Получить информацию о студенте по его id."""
    return await student_crud.get_one_or_none(student_id)
