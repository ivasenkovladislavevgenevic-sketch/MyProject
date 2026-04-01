"""Database connection and session management for АИС Делопроизводство."""

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///document_system.db"

engine = create_engine(DATABASE_URL, echo=False)


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def init_db():
    """Create all tables from ORM metadata."""
    from src.models import Employee, Correspondent, Document, Task  # noqa: F401
    Base.metadata.create_all(engine)


def get_session():
    """Return a new database session."""
    return Session()
