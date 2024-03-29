import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()
    await db.create_users()

    print("Создаем таблицу Пользователей...")

    await db.create_table_users()
    print("Готово")

    print("Добавляем пользователей")

    await db.add_user("One", "onetwol", 123)
    await db.add_user("Vasya", "vv_alakaz", 1234)
    await db.add_user("1", "1", 131231)
    await db.add_user("1", "1", 23324234)
    await db.add_user("John", "JohnDoe", 4388229)
    print("Готово")

    users = await db.select_all_users()
    print(f"Получил всех пользователей: {users}")

    user = await db.select_user(id=5)
    print(f"Получил пользователя: {user}")



