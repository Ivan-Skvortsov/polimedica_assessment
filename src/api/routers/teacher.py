from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.api.schemas.response.teacher import TeacherResponse
from src.db.crud.teacher import TeacherCRUD

router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.get(
    "/",
    response_model=list[TeacherResponse],
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Список всех преподавателей.",
    response_description="Информация о всех преподавателях."
)
async def get_all_teachers(
    teacher_crud: TeacherCRUD = Depends()
) -> list[TeacherResponse]:
    """Получает список всех преподавателей.

    - **id**: уникальный идентификатор преподавателя
    - **surname**: фамилия преподавателя
    - **name**: имя преподавателя
    - **patronymic**: отчество преподавателя (при наличии)
    - **degree**: ученая степень преподавателя
    - **faculty_id**: уникальный идентификатор факультета (при наличии).
    """
    return await teacher_crud.get_all()
