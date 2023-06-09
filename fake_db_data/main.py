import logging

import factory
import sqlalchemy

from fake_db_data import factories

logging.basicConfig(
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


def fill_db_with_fake_data():
    """Очищает БД и заполняет её фейковыми данными."""
    msg = (
        "ВНИМАНИЕ! Дальнейшее действие приведет к удалению ВСЕХ существующих данных из БД!\n"  # noqa
        "Продолжить? (y/n): "
    )
    if input(msg).lower().strip() not in ("y", "yes"):
        return
    truncate_tables()
    generate_fake_data()


def generate_fake_data():
    """Генерирует фейковые данные БД."""
    with factory.Faker.override_default_locale("ru_RU"):
        logger.info("Создание отделений...")
        factories.DepartmentFactory.create_batch(3)
        logger.info("Создание зданий...")
        factories.BuildingFactory.create_batch(3)
        logger.info("Создание факультетов...")
        factories.FacultyFactory.create_batch(10)
        logger.info("Создание групп...")
        factories.GroupFactory.create_batch(20)
        logger.info("Создание студентов...")
        factories.StudentFactory.create_batch(100)
        logger.info("Создание преподавателей...")
        factories.TeacherFactory.create_batch(30)
        logger.info("Создание курсов...")
        factories.CourseFactory.create_batch(30)
        logger.info("Создание оценок...")
        factories.GradeFactory.create_batch(5)
        logger.info("Создание аудиторий...")
        factories.ClassRoomFactory.create_batch(50)
        logger.info("Создание расписаний...")
        factories.TimeTableFactory.create_batch(30)
        logger.info("Создание семестров...")
        factories.SemesterFactory.create_batch(10)
        logger.info("Создание экзаменов...")
        factories.ExamFactory.create_batch(200)
        logger.info("Создание самостоятельных заданий...")
        factories.IndependentAssignmentFactory.create_batch(200)
        logger.info("Создание программ курсов...")
        factories.CourseProgrammeFactory.create_batch(90)
        logger.info("Создание учебных планов...")
        factories.CurriculumFactory.create_batch(50)
    logger.info("Создание фейковых данных завершено.")


def truncate_tables():
    """Удаляет существующие данные из БД."""
    logger.info("Удаление существующих данных...")
    factories.session.execute(sqlalchemy.text(
        """TRUNCATE TABLE
            building,
            classroom,
            course_programme,
            course_teacher,
            course,
            curriculum,
            department,
            exam,
            faculty,
            grade,
            "group",
            independent_assignment,
            semester,
            student,
            teacher,
            timetable
        """)
    )
    factories.session.commit()


if __name__ == "__main__":
    fill_db_with_fake_data()
