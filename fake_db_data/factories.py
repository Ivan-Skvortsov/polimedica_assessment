import factory
from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker

from src.configs.environment import settings
from src.db import models

engine = create_engine(settings.database_url.replace("+asyncpg", "+psycopg2"))
session = scoped_session(sessionmaker(bind=engine))


def lazy_fk_ids(model):
    """Выгружает id модели из БД для использования их в качестве внешних ключей."""  # noqa
    yield from (session.scalars(select(model.id)))


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Базовая фабрика для моделей."""

    id = factory.Faker("uuid4")

    class Meta:
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"


class DepartmentFactory(BaseFactory):
    """Фабрика для модели Department (отделение)."""

    name = factory.Iterator(["Очное", "Заочное", "Вечернее"])

    class Meta:
        model = models.Department


class BuildingFactory(BaseFactory):
    """Фабрика для модели Building (здание)."""

    name = factory.Sequence(lambda n: f"Корпус №{n + 1}")
    city = factory.Faker("city_name")
    street = factory.Faker("street_name")
    house = factory.Sequence(lambda n: n + 1)
    postal_code = factory.Sequence(lambda n: 111111 + n)

    class Meta:
        model = models.Building


class FacultyFactory(BaseFactory):
    """Фабрика для модели Faculty (факультет)."""

    name = factory.Faker("text", max_nb_chars=100)
    phone_number = factory.Sequence(lambda n: f"+7(999)999-99-{n + 10}")
    building_id = factory.Iterator(lazy_fk_ids(models.Building))

    class Meta:
        model = models.Faculty


class GroupFactory(BaseFactory):
    """Фабрика для модели Group (группа)."""

    name = factory.Sequence(lambda n: f"ГРУППА-{n + 10}")
    year_of_entry = factory.Faker("pyint", min_value=1950, max_value=2023)
    faculty_id = factory.Iterator(lazy_fk_ids(models.Faculty))
    department_id = factory.Iterator(lazy_fk_ids(models.Department))

    class Meta:
        model = models.Group


class StudentFactory(BaseFactory):
    """Фабрика для модели Student (студент)."""

    name = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    patronymic = factory.Faker("middle_name")
    gender = factory.Iterator([gender for gender in models.Student.Gender])
    date_of_birth = factory.Faker("date")
    year_of_entry = factory.Faker("pyint", min_value=1950, max_value=2023)
    group_id = factory.Iterator(lazy_fk_ids(models.Group))

    class Meta:
        model = models.Student


class TeacherFactory(BaseFactory):
    """Фабрика для модели Teacher (преподаватель)."""

    name = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    patronymic = factory.Faker("middle_name")
    degree = factory.Faker("text", max_nb_chars=20)
    faculty_id = factory.Iterator(lazy_fk_ids(models.Faculty))

    class Meta:
        model = models.Teacher


class CourseFactory(BaseFactory):
    """Фабрика для модели Course (курс)."""

    name = factory.Faker("text", max_nb_chars=100)
    hours = factory.Faker("pyint", min_value=10, max_value=210)

    class Meta:
        model = models.Course


class GradeFactory(BaseFactory):
    """Фабрика для модели Grade (оценка)."""

    score = factory.Iterator(list(range(1, 5)))

    class Meta:
        model = models.Grade


class ClassRoomFactory(BaseFactory):
    """Фабрика для модели ClassRoom (аудитория)."""

    number = factory.Faker("pyint", min_value=101, max_value=599)
    building_id = factory.Iterator(lazy_fk_ids(models.Building))

    class Meta:
        model = models.ClassRoom


class TimeTableFactory(BaseFactory):
    """Фабрика для модели TimeTable (расписание)."""

    group_id = factory.Iterator(lazy_fk_ids(models.Group))
    day_of_week = factory.Iterator(list(range(1, 6)))
    lesson_number = factory.Iterator(list(range(1, 6)))
    course_id = factory.Iterator(lazy_fk_ids(models.Course))
    teacher_id = factory.Iterator(lazy_fk_ids(models.Teacher))
    classroom_id = factory.Iterator(lazy_fk_ids(models.ClassRoom))

    class Meta:
        model = models.TimeTable


class SemesterFactory(BaseFactory):
    """Фабрика для модели Semester (семестр)."""

    number = factory.Iterator(list(range(1, 11)))

    class Meta:
        model = models.Semester


class ExamFactory(BaseFactory):
    """Фабрика для модели Exam (экзамен)."""

    exam_date = factory.Faker("date")
    student_id = factory.Iterator(lazy_fk_ids(models.Student))
    grade_id = factory.Iterator(lazy_fk_ids(models.Grade))
    course_id = factory.Iterator(lazy_fk_ids(models.Course))
    semester_id = factory.Iterator(lazy_fk_ids(models.Semester))
    teacher_id = factory.Iterator(lazy_fk_ids(models.Teacher))

    class Meta:
        model = models.Exam


class IndependentAssignmentFactory(BaseFactory):
    """Фабрика для модели IndependentAssignment (самостоятельное задание)."""

    title = factory.Faker("text", max_nb_chars=30)
    description = factory.Faker("text", max_nb_chars=300)
    date_created = factory.Faker("date")
    date_due = factory.Faker("date")
    is_completed = factory.Faker("boolean")
    student_id = factory.Iterator(lazy_fk_ids(models.Student))
    grade_id = factory.Iterator(lazy_fk_ids(models.Grade))
    teacher_id = factory.Iterator(lazy_fk_ids(models.Teacher))
    course_id = factory.Iterator(lazy_fk_ids(models.Course))

    class Meta:
        model = models.IndependentAssignment


class CourseProgrammeFactory(BaseFactory):
    """Фабрика для модели CourseProgramme (программа курса)."""

    course_id = factory.Iterator(lazy_fk_ids(models.Course))
    title = factory.Faker("text", max_nb_chars=100)
    descritpion = factory.Faker("text", max_nb_chars=300)
    hours = factory.Faker("pyint", min_value=10, max_value=110)
    semester_id = factory.Iterator(lazy_fk_ids(models.Semester))

    class Meta:
        model = models.CourseProgramme


class CurriculumFactory(BaseFactory):
    """Фабрика для модели Curriculum (учебный план)."""

    group_id = factory.Iterator(lazy_fk_ids(models.Group))
    course_id = factory.Iterator(lazy_fk_ids(models.Course))
    semester_id = factory.Iterator(lazy_fk_ids(models.Semester))

    class Meta:
        model = models.Curriculum
