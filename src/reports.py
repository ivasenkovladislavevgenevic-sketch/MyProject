"""Report generation for АИС Делопроизводство."""

from datetime import date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_
from src.models import Document, Task, Employee


def get_overdue_documents(session: Session, as_of_date: date) -> list[dict]:
    """Get documents with overdue tasks as of the given date.

    Returns list of dicts: {number, name, document_type}
    """
    results = (
        session.query(
            Document.number,
            Document.name,
            Document.document_type
        )
        .join(Task, Document.id == Task.document_id)
        .filter(Task.deadline < as_of_date)
        .distinct()
        .all()
    )

    return [
        {
            "number": r.number,
            "name": r.name,
            "document_type": r.document_type
        }
        for r in results
    ]


def get_approaching_deadlines(session: Session, as_of_date: date,
                              n_days: int) -> list[dict]:
    """Get tasks with approaching deadlines (within n_days from as_of_date).

    Returns list of dicts: {doc_number, doc_name, task_name, executor_name, executor_position}
    """
    end_date = as_of_date + timedelta(days=n_days)

    results = (
        session.query(
            Document.number.label("doc_number"),
            Document.name.label("doc_name"),
            Task.name.label("task_name"),
            Employee.full_name.label("executor_name"),
            Employee.position.label("executor_position")
        )
        .join(Task, Document.id == Task.document_id)
        .join(Employee, Task.executor_id == Employee.id)
        .filter(and_(
            Task.deadline >= as_of_date,
            Task.deadline <= end_date
        ))
        .order_by(Task.deadline)
        .all()
    )

    return [
        {
            "doc_number": r.doc_number,
            "doc_name": r.doc_name,
            "task_name": r.task_name,
            "executor_name": r.executor_name,
            "executor_position": r.executor_position
        }
        for r in results
    ]
