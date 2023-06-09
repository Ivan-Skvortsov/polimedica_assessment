from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from src.api.schemas.request.exam import ExamCreateRequest, ExamUpdateRequest
from src.api.schemas.response.exam import ExamResponse
from src.db.crud.exam import ExamCRUD
from src.db.models import Exam

router = APIRouter(prefix="/grades", tags=["Grades"])


@router.post(
    "/",
    response_model=ExamResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.CREATED,
    summary="Создать новую оценку студенту по курсу (экзамен).",
    response_description="Информация об оценке студента за курс (экзамен)."
)
async def create_exam(
    exam_data: ExamCreateRequest,
    exam_crud: ExamCRUD = Depends()
) -> ExamResponse:
    """Создаёт оценку студенту за курс.

    Итоговая оценка студента за курс есть оценка за финальный экзамен.

    - **exam_date**: дата проведения экзамена
    - **student_id**: уникальный идентификатор студента
    - **grade_id**: уникальный идентификатор оценки
    - **course_id**: уникальный идентификатор курса
    - **semester_id**: уникальный идентификатор семестра
    - **teacher_id**: уникальный идентификатор преподавателя.
    """
    exam = Exam(**exam_data.dict())
    return await exam_crud.create(exam)


@router.put(
    "/{grade_id}",
    response_model=ExamResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Обновить оценку студенту по курсу (экзамен).",
    response_description="Информация об оценке студента за курс (экзамен)."
)
async def update_exam(
    grade_id: UUID,
    exam_data: ExamUpdateRequest,
    exam_crud: ExamCRUD = Depends()
) -> ExamResponse:
    """Обновляет оценку студенту за курс.

    Итоговая оценка студента за курс есть оценка за финальный экзамен.

    - **exam_date**: дата проведения экзамена
    - **student_id**: уникальный идентификатор студента
    - **grade_id**: уникальный идентификатор оценки
    - **course_id**: уникальный идентификатор курса
    - **semester_id**: уникальный идентификатор семестра
    - **teacher_id**: уникальный идентификатор преподавателя.
    """
    exam = Exam(**exam_data.dict())
    return await exam_crud.update(grade_id, exam)
