"""Tests for report generation."""

import pytest
from datetime import date
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from src.database import Base
from src.services import add_employee, register_document
from src.reports import get_overdue_documents, get_approaching_deadlines


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


@pytest.fixture
def sample_data(session):
    emp1 = add_employee(session, "Иванов Иван Иванович", "Начальник", "+7-111", "ivanov@test.ru")
    emp2 = add_employee(session, "Петрова Анна Сергеевна", "Специалист", "+7-222", "petrova@test.ru")

    # Document with overdue task (deadline 2026-03-15)
    register_document(
        session, "DOC-001", "Приказ о проверке", "INTERNAL",
        date(2026, 3, 1), date(2026, 3, 1),
        tasks_data=[
            {"code": "T1", "name": "Провести проверку", "deadline": date(2026, 3, 15), "executor_id": emp1.id},
        ]
    )

    # Document with approaching deadline (2026-04-05)
    register_document(
        session, "DOC-002", "Запрос от партнёра", "INCOMING",
        date(2026, 3, 20), date(2026, 3, 20),
        tasks_data=[
            {"code": "T2", "name": "Подготовить ответ", "deadline": date(2026, 4, 5), "executor_id": emp2.id},
        ]
    )

    # Document with future deadline (2026-05-01)
    register_document(
        session, "DOC-003", "Плановый отчёт", "OUTGOING",
        date(2026, 3, 25), date(2026, 3, 25),
        tasks_data=[
            {"code": "T3", "name": "Составить отчёт", "deadline": date(2026, 5, 1), "executor_id": emp1.id},
        ]
    )

    return {"emp1": emp1, "emp2": emp2}


def test_overdue_documents(session, sample_data):
    # As of 2026-04-01, DOC-001 (deadline 2026-03-15) should be overdue
    results = get_overdue_documents(session, date(2026, 4, 1))
    assert len(results) == 1
    assert results[0]["number"] == "DOC-001"
    assert results[0]["document_type"] == "INTERNAL"


def test_overdue_documents_none(session, sample_data):
    # As of 2026-03-01, nothing should be overdue
    results = get_overdue_documents(session, date(2026, 3, 1))
    assert len(results) == 0


def test_approaching_deadlines(session, sample_data):
    # As of 2026-04-01 with 7 days window -> DOC-002 task (deadline 2026-04-05)
    results = get_approaching_deadlines(session, date(2026, 4, 1), 7)
    assert len(results) == 1
    assert results[0]["doc_number"] == "DOC-002"
    assert results[0]["task_name"] == "Подготовить ответ"
    assert results[0]["executor_name"] == "Петрова Анна Сергеевна"
    assert results[0]["executor_position"] == "Специалист"


def test_approaching_deadlines_wider_window(session, sample_data):
    # As of 2026-04-01 with 35 days -> should include DOC-002 and DOC-003
    results = get_approaching_deadlines(session, date(2026, 4, 1), 35)
    assert len(results) == 2
    numbers = {r["doc_number"] for r in results}
    assert numbers == {"DOC-002", "DOC-003"}


def test_approaching_deadlines_none(session, sample_data):
    # As of 2026-06-01 -> all deadlines are in the past
    results = get_approaching_deadlines(session, date(2026, 6, 1), 7)
    assert len(results) == 0
