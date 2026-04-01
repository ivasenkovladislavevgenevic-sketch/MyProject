"""ORM models for АИС Делопроизводство."""

import enum
from sqlalchemy import (
    Column, Integer, String, Date, ForeignKey, UniqueConstraint, CheckConstraint
)
from sqlalchemy.orm import relationship
from src.database import Base


class DocumentType(enum.Enum):
    INCOMING = "INCOMING"
    OUTGOING = "OUTGOING"
    INTERNAL = "INTERNAL"


class CorrespondentType(enum.Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"


class Employee(Base):
    """Сотрудник предприятия (исполнитель, автор резолюции, контролёр)."""
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.full_name}')>"


class Correspondent(Base):
    """Корреспондент (внутренний или внешний)."""
    __tablename__ = "correspondent"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    department = Column(String)
    official_name = Column(String)
    code = Column(String)
    organization_name = Column(String)

    __table_args__ = (
        CheckConstraint("type IN ('INTERNAL', 'EXTERNAL')"),
    )

    def __repr__(self):
        if self.type == "INTERNAL":
            return f"<Correspondent(internal, dept='{self.department}')>"
        return f"<Correspondent(external, org='{self.organization_name}')>"


class Document(Base):
    """Деловой документ (входящий, исходящий, внутренний)."""
    __tablename__ = "document"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    document_type = Column(String, nullable=False)
    creation_date = Column(Date, nullable=False)
    registration_date = Column(Date, nullable=False)
    correspondent_id = Column(Integer, ForeignKey("correspondent.id"))
    resolution_author_id = Column(Integer, ForeignKey("employee.id"))
    controller_id = Column(Integer, ForeignKey("employee.id"))

    __table_args__ = (
        CheckConstraint("document_type IN ('INCOMING', 'OUTGOING', 'INTERNAL')"),
    )

    correspondent = relationship("Correspondent", foreign_keys=[correspondent_id])
    resolution_author = relationship("Employee", foreign_keys=[resolution_author_id])
    controller = relationship("Employee", foreign_keys=[controller_id])
    tasks = relationship("Task", back_populates="document", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Document(number='{self.number}', name='{self.name}')>"


class Task(Base):
    """Задача документа с привязкой к исполнителю."""
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    deadline = Column(Date, nullable=False)
    document_id = Column(Integer, ForeignKey("document.id", ondelete="CASCADE"), nullable=False)
    executor_id = Column(Integer, ForeignKey("employee.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("document_id", "code", name="uq_task_document_code"),
    )

    document = relationship("Document", back_populates="tasks")
    executor = relationship("Employee", foreign_keys=[executor_id])

    def __repr__(self):
        return f"<Task(code='{self.code}', name='{self.name}')>"
