-- АИС «Делопроизводство» - Database Schema
-- Automated Document Registration System

PRAGMA foreign_keys = ON;

-- Сотрудники предприятия (исполнители, авторы резолюций, контролёры)
CREATE TABLE IF NOT EXISTS employee (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name   TEXT    NOT NULL,
    position    TEXT    NOT NULL,
    phone       TEXT,
    email       TEXT
);

-- Корреспонденты (внутренние и внешние)
CREATE TABLE IF NOT EXISTS correspondent (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    type              TEXT NOT NULL CHECK (type IN ('INTERNAL', 'EXTERNAL')),
    department        TEXT,     -- для внутренних
    official_name     TEXT,     -- для внутренних (должностное лицо)
    code              TEXT,     -- для внешних
    organization_name TEXT      -- для внешних (название организации)
);

-- Документы (входящие, исходящие, внутренние)
CREATE TABLE IF NOT EXISTS document (
    id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    number               TEXT NOT NULL UNIQUE,
    name                 TEXT NOT NULL,
    document_type        TEXT NOT NULL CHECK (document_type IN ('INCOMING', 'OUTGOING', 'INTERNAL')),
    creation_date        DATE NOT NULL,
    registration_date    DATE NOT NULL,
    correspondent_id     INTEGER REFERENCES correspondent(id),
    resolution_author_id INTEGER REFERENCES employee(id),
    controller_id        INTEGER REFERENCES employee(id)
);

-- Задачи документов
CREATE TABLE IF NOT EXISTS task (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    code        TEXT    NOT NULL,
    name        TEXT    NOT NULL,
    deadline    DATE    NOT NULL,
    document_id INTEGER NOT NULL REFERENCES document(id) ON DELETE CASCADE,
    executor_id INTEGER NOT NULL REFERENCES employee(id),
    UNIQUE(document_id, code)
);

-- Индексы для ускорения отчётов
CREATE INDEX IF NOT EXISTS idx_task_deadline ON task(deadline);
CREATE INDEX IF NOT EXISTS idx_task_document ON task(document_id);
CREATE INDEX IF NOT EXISTS idx_task_executor ON task(executor_id);
CREATE INDEX IF NOT EXISTS idx_document_type ON document(document_type);
