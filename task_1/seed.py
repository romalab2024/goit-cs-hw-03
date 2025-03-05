import psycopg2
from faker import Faker
import random

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="task_management",
    user="postgres",
    password="Ramstein1979.", 
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Ініціалізація Faker
fake = Faker()

# Додавання статусів (якщо їх ще немає)
status_list = ['new', 'in progress', 'completed']
for status in status_list:
    cursor.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING", (status,))

# Додавання випадкових користувачів
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT DO NOTHING", (fullname, email))

# Отримання id користувачів та статусів
cursor.execute("SELECT id FROM users")
user_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM status")
status_ids = [row[0] for row in cursor.fetchall()]

# Додавання випадкових завдань
for _ in range(20):
    title = fake.sentence(nb_words=5)
    description = fake.paragraph(nb_sentences=3)
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id)
    )

# Підтвердження змін та закриття підключення
conn.commit()
cursor.close()
conn.close()

print("Дані успішно додані!")
