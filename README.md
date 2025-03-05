# goit-cs-hw-03
Homework for the module "Introduction to the study of database management systems"

Task 1

# Task Management System — це проста система управління завданнями, яка дозволяє:
- Додавати, редагувати, видаляти завдання.
- Фільтрувати завдання за статусом та користувачами.
- Переглядати статистику кількості завдань у різних статусах.
---
# Інструкції по запуску

  1. Встановлення залежностей
Переконайтеся, що у вас встановлено:
- **Python 3** (для `seed.py`)
- **PostgreSQL** (для бази даних)
- **DBeaver** або будь-який інший клієнт для SQL

  2. Створення бази даних
У PostgreSQL створіть базу даних `task_management`:
```sql CREATE DATABASE task_management;

  3. Відновлення бази даних з резервної копії
 bash psql -U postgres -d task_management -f task_management_backup.sql

  4. Заповнення таблиць випадковими даними
Запустіть seed.py для автоматичного додавання даних:
python seed.py
  5. Виконання SQL-запитів
Відкрийте файл queries.sql у DBeaver або іншому клієнті SQL.
Виконуйте запити по черзі для перевірки функціоналу.

  Як протестувати?
Відновіть базу даних.
Запустіть seed.py для генерації даних.
Виконуйте SQL-запити з queries.sql, щоб протестувати функціонал.
