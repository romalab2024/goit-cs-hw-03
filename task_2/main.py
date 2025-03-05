from pymongo import MongoClient

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Перевірка з’єднання
try:
    client.server_info()  # Спроба отримати інформацію про сервер
    print("З'єднання з MongoDB успішне!")
except Exception as e:
    print(f"Помилка підключення: {e}")

db = client["cat_database"]
collection = db["cats"]

# Перевірка наявності колекції
if "cats" in db.list_collection_names():
    print("Колекція 'cats' знайдена!")
else:
    print("Колекція 'cats' не знайдена.")

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cat_database"]
collection = db["cats"]

def insert_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Кіт {name} успішно доданий з ID: {result.inserted_id}")
    except Exception as e:
        print(f"Помилка при додаванні кота: {e}")

# Додавання котів
insert_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
insert_cat("murzik", 5, ["муркоче голосно", "чорний", "любить рибу"])

# Функція для виведення всіх записів із колекції
def show_all_cats():
    try:
        cats = collection.find()
        print("Всі коти у базі даних:")
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка при виведенні котів: {e}")

# Функція для виведення інформації про кота за іменем
def find_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(f"Знайдено кота: {cat}")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при пошуку кота: {e}")

        # Виклики функцій для перевірки
show_all_cats()
find_cat_by_name("barsik")
find_cat_by_name("unknown_cat")

# Функція для оновлення віку кота за ім'ям
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Вік кота {name} успішно оновлено до {new_age} років.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при оновленні віку кота: {e}")

        # Функція для додавання нової характеристики до списку features за ім'ям
def add_feature_to_cat(name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"Характеристика '{new_feature}' успішно додана коту {name}.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")

        # Перевірка роботи функцій
update_cat_age("barsik", 4)
add_feature_to_cat("barsik", "любить спати на сонці")

# Функція для видалення кота за ім'ям
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт з ім'ям {name} успішно видалений.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при видаленні кота: {e}")

        # Функція для видалення всіх записів із колекції
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Успішно видалено {result.deleted_count} котів.")
    except Exception as e:
        print(f"Помилка при видаленні всіх котів: {e}")

        # Перевірка роботи функцій
delete_cat_by_name("murzik")
delete_all_cats()

insert_cat("simba", 2, ["любить м'ясо", "пухнастий", "грайливий"])
insert_cat("tiger", 4, ["сірий", "мисливець", "спокійний"])
insert_cat("leo", 5, ["рудий", "сміливий", "лідер"])

show_all_cats()
