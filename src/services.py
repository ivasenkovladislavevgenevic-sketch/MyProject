"""Business logic layer for АИС Делопроизводство."""

from datetime import date
from typing import Optional
from sqlalchemy.orm import Session
from src.models import Employee, Correspondent, Document, Task


def add_employee(session: Session, full_name: str, position: str,
                 phone: str = None, email: str = None) -> Employee:
    """Add a new employee."""
    emp = Employee(full_name=full_name, position=position, phone=phone, email=email)
    session.add(emp)
    session.commit()
    return emp


def add_correspondent(session: Session, corr_type: str, department: str = None,
                      official_name: str = None, code: str = None,
                      organization_name: str = None) -> Correspondent:
    """Add a new correspondent (INTERNAL or EXTERNAL)."""
    corr = Correspondent(
        type=corr_type, department=department, official_name=official_name,
        code=code, organization_name=organization_name
    )
    session.add(corr)
    session.commit()
    return corr


def register_document(session: Session, number: str, name: str, document_type: str,
                      creation_date: date, registration_date: date,
                      correspondent_id: int = None, resolution_author_id: int = None,
                      controller_id: int = None,
                      tasks_data: list[dict] = None) -> Document:
    """Register a new document with tasks.

    tasks_data: list of dicts with keys: code, name, deadline, executor_id
    """
    doc = Document(
        number=number, name=name, document_type=document_type,
        creation_date=creation_date, registration_date=registration_date,
        correspondent_id=correspondent_id,
        resolution_author_id=resolution_author_id,
        controller_id=controller_id
    )
    session.add(doc)
    session.flush()  # get doc.id

    if tasks_data:
        for td in tasks_data:
            task = Task(
                code=td["code"], name=td["name"],
                deadline=td["deadline"], executor_id=td["executor_id"],
                document_id=doc.id
            )
            session.add(task)

    session.commit()
    return doc


def modify_task(session: Session, task_id: int,
                new_deadline: Optional[date] = None,
                new_executor_id: Optional[int] = None) -> Task:
    """Modify a task: reschedule deadline and/or reassign executor."""
    task = session.get(Task, task_id)
    if task is None:
        raise ValueError(f"Task with id={task_id} not found")

    if new_deadline is not None:
        task.deadline = new_deadline
    if new_executor_id is not None:
        task.executor_id = new_executor_id

    session.commit()
    return task


def get_all_employees(session: Session) -> list[Employee]:
    """Return all employees."""
    return session.query(Employee).order_by(Employee.full_name).all()


def get_all_correspondents(session: Session) -> list[Correspondent]:
    """Return all correspondents."""
    return session.query(Correspondent).order_by(Correspondent.id).all()


def get_all_documents(session: Session) -> list[Document]:
    """Return all documents."""
    return session.query(Document).order_by(Document.registration_date.desc()).all()


def get_document_tasks(session: Session, document_id: int) -> list[Task]:
    """Return all tasks for a given document."""
    return session.query(Task).filter(Task.document_id == document_id).all()
