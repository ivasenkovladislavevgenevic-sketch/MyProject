"""Tests for ORM models."""

import pytest
from datetime import date
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from src.database import Base
from src.models import Employee, Correspondent, Document, Task


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


def test_create_employee(session):
    emp = Employee(full_name="Иванов И.И.", position="Начальник", phone="123", email="a@b.ru")
    session.add(emp)
    session.commit()
    assert emp.id is not None
    assert emp.full_name == "Иванов И.И."


def test_create_correspondent_internal(session):
    corr = Correspondent(type="INTERNAL", department="Бухгалтерия", official_name="Петров П.П.")
    session.add(corr)
    session.commit()
    assert corr.id is not None
    assert corr.type == "INTERNAL"


def test_create_correspondent_external(session):
    corr = Correspondent(type="EXTERNAL", code="ORG-001", organization_name="ООО Тест")
    session.add(corr)
    session.commit()
    assert corr.organization_name == "ООО Тест"


def test_create_document_with_tasks(session):
    emp = Employee(full_name="Тестов Т.Т.", position="Тестер")
    session.add(emp)
    session.flush()

    doc = Document(
        number="DOC-001", name="Тестовый документ",
        document_type="INCOMING",
        creation_date=date(2026, 1, 1),
        registration_date=date(2026, 1, 2),
        resolution_author_id=emp.id,
        controller_id=emp.id
    )
    session.add(doc)
    session.flush()

    task = Task(
        code="T-001", name="Тестовая задача",
        deadline=date(2026, 2, 1),
        document_id=doc.id, executor_id=emp.id
    )
    session.add(task)
    session.commit()

    assert len(doc.tasks) == 1
    assert doc.tasks[0].executor.full_name == "Тестов Т.Т."


def test_task_unique_code_per_document(session):
    emp = Employee(full_name="Тест", position="Тест")
    session.add(emp)
    session.flush()

    doc = Document(
        number="DOC-002", name="Документ 2",
        document_type="INTERNAL",
        creation_date=date(2026, 1, 1),
        registration_date=date(2026, 1, 1)
    )
    session.add(doc)
    session.flush()

    t1 = Task(code="T-001", name="Задача 1", deadline=date(2026, 3, 1),
              document_id=doc.id, executor_id=emp.id)
    t2 = Task(code="T-001", name="Задача дубль", deadline=date(2026, 3, 1),
              document_id=doc.id, executor_id=emp.id)
    session.add(t1)
    session.flush()
    session.add(t2)

    with pytest.raises(Exception):
        session.flush()
