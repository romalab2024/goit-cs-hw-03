-- 📌 Створення таблиці користувачів
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- 📌 Створення таблиці статусів
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- 📌 Створення таблиці завдань із зовнішніми ключами
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (status_id) REFERENCES status (id),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- 📌 Вибір всіх завдань для користувача з id = 1
SELECT * FROM tasks WHERE user_id = 1;

-- 📌 Вибір всіх завдань зі статусом "new"
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 📌 Оновлення статусу завдання з id = 7 на "in progress"
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 7;

-- 📌 Вибір користувачів, у яких немає жодного завдання
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- 📌 Додавання нового завдання для користувача з id = 2
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Нове завдання', 'Опис нового завдання', 1, 2);

-- 📌 Видалення завдання з id = 2
DELETE FROM tasks WHERE id = 2;

-- 📌 Вибір всіх користувачів, які мають email на gmail.com
SELECT * FROM users WHERE email LIKE '%@gmail.com';

-- 📌 Вибір інформації про користувача з id = 1
SELECT * FROM users WHERE id = 1;

-- 📌 Підрахунок кількості завдань у кожному статусі
SELECT s.name AS статус, COUNT(t.id) AS кількість_завдань
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

-- 📌 Вибір завдань для користувачів із доменом email "example.com"
SELECT t.*
FROM tasks t
INNER JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

-- 📌 Вибір завдань, у яких опис є порожнім (NULL)
SELECT * FROM tasks WHERE description IS NULL;

-- 📌 Вибір завдань у статусі "in progress" із іменами користувачів
SELECT u.fullname, t.title, t.description
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- 📌 Підрахунок кількості завдань для кожного користувача
SELECT u.fullname, COUNT(t.id) AS кількість_завдань
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
