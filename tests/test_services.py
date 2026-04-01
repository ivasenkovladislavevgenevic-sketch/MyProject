"""Tests for business logic services."""

import pytest
from datetime import date
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from src.database import Base
from src.services import (
    add_employee, add_correspondent, register_document, modify_task
)


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")

    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    Base.metadata.create_all(engine)
    _Session = sessionmaker(bind=engine)
    sess = _Session()
    yield sess
    sess.close()


def test_add_employee(session):
    emp = add_employee(session, "Тестов Т.Т.", "Инженер", "+7-000", "test@test.ru")
    assert emp.id is not None
    assert emp.position == "Инженер"


def test_add_correspondent(session):
    corr = add_correspondent(session, "EXTERNAL", code="EXT-01", organization_name="ООО Тест")
    assert corr.id is not None
    assert corr.type == "EXTERNAL"


def test_register_document_with_tasks(session):
    emp = add_employee(session, "Исполнитель", "Специалист")
    corr = add_correspondent(session, "INTERNAL", department="IT", official_name="Шеф")

    doc = register_document(
        session,
        number="DOC-100", name="Приказ", document_type="INTERNAL",
        creation_date=date(2026, 3, 1), registration_date=date(2026, 3, 1),
        correspondent_id=corr.id, resolution_author_id=emp.id,
        controller_id=emp.id,
        tasks_data=[
            {"code": "T1", "name": "Задача 1", "deadline": date(2026, 4, 1), "executor_id": emp.id},
            {"code": "T2", "name": "Задача 2", "deadline": date(2026, 4, 15), "executor_id": emp.id},
        ]
    )
    assert doc.id is not None
    assert len(doc.tasks) == 2


def test_modify_task_deadline(session):
    emp = add_employee(session, "Исполнитель", "Специалист")
    doc = register_document(
        session, "DOC-200", "Тест", "INCOMING",
        date(2026, 1, 1), date(2026, 1, 1),
        tasks_data=[{"code": "T1", "name": "Задача", "deadline": date(2026, 2, 1), "executor_id": emp.id}]
    )
    task = doc.tasks[0]
    new_date = date(2026, 3, 15)
    modified = modify_task(session, task.id, new_deadline=new_date)
    assert modified.deadline == new_date


def test_modify_task_executor(session):
    emp1 = add_employee(session, "Первый", "Специалист")
    emp2 = add_employee(session, "Второй", "Инженер")
    doc = register_document(
        session, "DOC-300", "Тест", "OUTGOING",
        date(2026, 1, 1), date(2026, 1, 1),
        tasks_data=[{"code": "T1", "name": "Задача", "deadline": date(2026, 2, 1), "executor_id": emp1.id}]
    )
    task = doc.tasks[0]
    modified = modify_task(session, task.id, new_executor_id=emp2.id)
    assert modified.executor_id == emp2.id


def test_modify_task_not_found(session):
    with pytest.raises(ValueError):
        modify_task(session, 9999, new_deadline=date(2026, 5, 1))
