"""CLI interface for АИС Делопроизводство."""

from datetime import date, datetime
from src.database import init_db, get_session
from src.services import (
    add_employee, add_correspondent, register_document,
    modify_task, get_all_employees, get_all_correspondents,
    get_all_documents, get_document_tasks
)
from src.reports import get_overdue_documents, get_approaching_deadlines


def print_header(title: str):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


def input_date(prompt: str) -> date:
    while True:
        val = input(f"{prompt} (ГГГГ-ММ-ДД): ").strip()
        try:
            return datetime.strptime(val, "%Y-%m-%d").date()
        except ValueError:
            print("Неверный формат даты. Попробуйте снова.")


def menu_add_employee(session):
    print_header("Добавление сотрудника")
    full_name = input("ФИО: ").strip()
    position = input("Должность: ").strip()
    phone = input("Телефон: ").strip() or None
    email = input("Email: ").strip() or None
    emp = add_employee(session, full_name, position, phone, email)
    print(f"Сотрудник добавлен (ID: {emp.id})")


def menu_add_correspondent(session):
    print_header("Добавление корреспондента")
    corr_type = input("Тип (INTERNAL/EXTERNAL): ").strip().upper()
    if corr_type == "INTERNAL":
        dept = input("Отдел: ").strip()
        official = input("Должностное лицо: ").strip()
        corr = add_correspondent(session, "INTERNAL", department=dept, official_name=official)
    elif corr_type == "EXTERNAL":
        code = input("Код организации: ").strip()
        org_name = input("Название организации: ").strip()
        corr = add_correspondent(session, "EXTERNAL", code=code, organization_name=org_name)
    else:
        print("Неверный тип.")
        return
    print(f"Корреспондент добавлен (ID: {corr.id})")


def menu_register_document(session):
    print_header("Регистрация документа")

    number = input("Номер документа: ").strip()
    name = input("Название документа: ").strip()

    print("Тип: 1-Входящий, 2-Исходящий, 3-Внутренний")
    type_map = {"1": "INCOMING", "2": "OUTGOING", "3": "INTERNAL"}
    doc_type = type_map.get(input("Выбор: ").strip())
    if not doc_type:
        print("Неверный тип.")
        return

    creation_date = input_date("Дата создания")
    registration_date = date.today()

    # Show correspondents
    correspondents = get_all_correspondents(session)
    if correspondents:
        print("\nКорреспонденты:")
        for c in correspondents:
            label = f"{c.department} ({c.official_name})" if c.type == "INTERNAL" else f"{c.code} - {c.organization_name}"
            print(f"  {c.id}: [{c.type}] {label}")
    corr_id = input("ID корреспондента (или Enter для пропуска): ").strip()
    corr_id = int(corr_id) if corr_id else None

    # Show employees
    employees = get_all_employees(session)
    if employees:
        print("\nСотрудники:")
        for e in employees:
            print(f"  {e.id}: {e.full_name} - {e.position}")

    author_id = input("ID автора резолюции (или Enter): ").strip()
    author_id = int(author_id) if author_id else None

    ctrl_id = input("ID контролёра (или Enter): ").strip()
    ctrl_id = int(ctrl_id) if ctrl_id else None

    # Tasks
    tasks_data = []
    while True:
        add_task = input("\nДобавить задачу? (да/нет): ").strip().lower()
        if add_task != "да":
            break
        code = input("  Код задачи: ").strip()
        task_name = input("  Название задачи: ").strip()
        deadline = input_date("  Срок исполнения")
        exec_id = int(input("  ID исполнителя: ").strip())
        tasks_data.append({
            "code": code, "name": task_name,
            "deadline": deadline, "executor_id": exec_id
        })

    doc = register_document(
        session, number, name, doc_type, creation_date, registration_date,
        corr_id, author_id, ctrl_id, tasks_data
    )
    print(f"\nДокумент зарегистрирован: {doc.number} (ID: {doc.id})")


def menu_modify_task(session):
    print_header("Изменение поручения")

    documents = get_all_documents(session)
    if not documents:
        print("Нет зарегистрированных документов.")
        return

    print("Документы:")
    for d in documents:
        print(f"  {d.id}: [{d.document_type}] {d.number} - {d.name}")

    doc_id = int(input("ID документа: ").strip())
    tasks = get_document_tasks(session, doc_id)
    if not tasks:
        print("У документа нет задач.")
        return

    print("\nЗадачи:")
    for t in tasks:
        print(f"  {t.id}: {t.code} - {t.name} (срок: {t.deadline}, исполнитель: {t.executor.full_name})")

    task_id = int(input("ID задачи: ").strip())

    print("\n1 - Перенести срок")
    print("2 - Назначить нового исполнителя")
    print("3 - Оба действия")
    action = input("Выбор: ").strip()

    new_deadline = None
    new_executor_id = None

    if action in ("1", "3"):
        new_deadline = input_date("Новый срок исполнения")
    if action in ("2", "3"):
        employees = get_all_employees(session)
        for e in employees:
            print(f"  {e.id}: {e.full_name} - {e.position}")
        new_executor_id = int(input("ID нового исполнителя: ").strip())

    task = modify_task(session, task_id, new_deadline, new_executor_id)
    print(f"Задача обновлена: {task.code} - {task.name}")


def menu_overdue_report(session):
    print_header("Отчёт: Просроченные документы")
    as_of = input_date("Контрольная дата")

    results = get_overdue_documents(session, as_of)
    if not results:
        print("Просроченных документов не найдено.")
        return

    type_labels = {"INCOMING": "Входящий", "OUTGOING": "Исходящий", "INTERNAL": "Внутренний"}
    print(f"\n{'Номер':<20} {'Название':<30} {'Тип':<15}")
    print("-" * 65)
    for r in results:
        print(f"{r['number']:<20} {r['name']:<30} {type_labels.get(r['document_type'], r['document_type']):<15}")


def menu_deadline_notifications(session):
    print_header("Уведомления: Приближающиеся сроки исполнения")
    as_of = input_date("Контрольная дата")
    n_days = int(input("Количество дней: ").strip())

    results = get_approaching_deadlines(session, as_of, n_days)
    if not results:
        print("Задач с приближающимися сроками не найдено.")
        return

    print(f"\n{'Номер док.':<15} {'Документ':<25} {'Задача':<25} {'Исполнитель':<25} {'Должность':<20}")
    print("-" * 110)
    for r in results:
        print(f"{r['doc_number']:<15} {r['doc_name']:<25} {r['task_name']:<25} {r['executor_name']:<25} {r['executor_position']:<20}")


def main():
    init_db()
    session = get_session()

    while True:
        print_header("АИС «Делопроизводство»")
        print("  1. Регистрация документа")
        print("  2. Изменение поручения (перенос срока / смена исполнителя)")
        print("  3. Добавить сотрудника")
        print("  4. Добавить корреспондента")
        print("  5. Отчёт: Просроченные документы")
        print("  6. Уведомления: Приближающиеся сроки исполнения")
        print("  0. Выход")

        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            menu_register_document(session)
        elif choice == "2":
            menu_modify_task(session)
        elif choice == "3":
            menu_add_employee(session)
        elif choice == "4":
            menu_add_correspondent(session)
        elif choice == "5":
            menu_overdue_report(session)
        elif choice == "6":
            menu_deadline_notifications(session)
        elif choice == "0":
            print("Выход из системы.")
            break
        else:
            print("Неверный выбор.")

    session.close()


if __name__ == "__main__":
    main()
