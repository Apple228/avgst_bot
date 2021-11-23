from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create_users(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,  # этот фетч означает, что хотим забрать все данные
                      fetchval: bool = False,  # доставать одно значение
                      fetchrow: bool = False,  # данные в одной строке
                      execute: bool = False  # никакие данные возвращать не надо
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(55) NOT NULL,
        username varchar(55) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        email varchar(55),
        phone_number VARCHAR(15),
        birthday date,
        gsheets_today INT default 0,
        lvl INT default 0,
        experience INT default 0
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):  #?
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def select_full_name(self, telegram_id):   #получаю имя для кофе
        sql = "SELECT full_name  FROM Users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def update_user_email(self, email, telegram_id):
        sql = "UPDATE Users SET email=$1 where telegram_id=$2"
        return await self.execute(sql, email, telegram_id, execute=True)

    async def update_user_phone_number(self, phone_number, telegram_id):
        sql = "UPDATE Users SET phone_number=$1 where telegram_id=$2"
        return await self.execute(sql, phone_number, telegram_id, execute=True)

    # async def drop_users(self):
    #     await self.execute("DROP TABLE Users", execute=True)

    async def select_contacts(self, **kwargs):
        sql = "SELECT full_name, phone_number, email, username FROM Users"
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetch=True)

    async def select_full_name_id(self):
        sql = "SELECT full_name, telegram_id FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_full_name_all_users(self):
        sql = "SELECT full_name FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_all_telegram_id(self):
        sql = "SELECT telegram_id FROM Users"
        return await self.execute(sql, fetch=True)

    async def update_gsheets_today(self, telegram_id):
        sql = "UPDATE Users SET gsheets_today=1 where telegram_id=$1"
        return await self.execute(sql, telegram_id, execute=True)

    async def zeroing_gsheets_today(self, telegram_id):
        sql = "UPDATE Users SET gsheets_today=0 where telegram_id=$1"
        return await self.execute(sql, telegram_id, execute=True)

    async def check_gsheets_today(self, telegram_id):
        sql = "SELECT gsheets_today from Users where telegram_id = $1"
        return await self.execute(sql, telegram_id, fetchval=True)

    async def update_experience(self, experience, telegram_id):
        sql = "UPDATE Users SET experience = experience+$1 where telegram_id=$2"
        return await self.execute(sql, experience, telegram_id, execute=True)

    async def update_birthday(self, date, telegram_id):
        sql = "UPDATE Users SET birthday=$1 WHERE telegram_id=$2"
        return await self.execute(sql, date, telegram_id, execute=True)


# _________________________________________________________________________________________________
class TaskManager:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create_tasks(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,  # этот фетч означает, что хотим забрать все данные
                      fetchval: bool = False,  # доставать одно значение
                      fetchrow: bool = False,  # данные в одном списке
                      execute: bool = False  # никакие данные возвращать не надо
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_tasks(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Tasks (
        id SERIAL PRIMARY KEY,   
        task_for VARCHAR(55) NOT NULL,
        task_for_telegram_id BIGINT NOT NULL,
        task_from VARCHAR(55) NOT NULL,
        task_from_telegram_id BIGINT NOT NULL,
        text_tasks VARCHAR(2000),
        status VARCHAR(55)
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_task(self, task_for, task_for_telegram_id, task_from,  # новая таска
                       task_from_telegram_id, text_tasks, status):
        sql = "INSERT INTO tasks (task_for, task_for_telegram_id, " \
              "task_from, task_from_telegram_id, text_tasks, status) " \
              "VALUES($1, $2, $3, $4, $5, $6) returning *"
        return await self.execute(sql, task_for, task_for_telegram_id, task_from, task_from_telegram_id, text_tasks,
                                  status, execute=True)

    async def tasks_for_user(self, task_for_telegram_id):  # все таски для юзера
        sql = "SELECT id, task_for, task_from, text_tasks, status from tasks " \
              "where task_for_telegram_id=$1"
        return await self.execute(sql, task_for_telegram_id, fetch=True)

    async def tasks_from_user(self, task_from_telegram_id):  # все таски от юзера
        sql = "SELECT id, task_for, task_from, text_tasks, status from tasks " \
              "where task_from_telegram_id=$1"
        return await self.execute(sql, task_from_telegram_id, fetch=True)

    async def select_id(self):  # получаем айди задачи
        sql = "SELECT id FROM tasks ORDER BY id DESC LIMIT 1"
        return await self.execute(sql, fetchrow=True)

    async def update_status(self, status, id):  # меняем статус таски
        sql = "UPDATE tasks SET status=$1 where id=$2"
        return await self.execute(sql, status, id, execute=True)

    async def select_task_from_telegram_id(self, id):  # получаем tg_id того, кто поставил таску
        sql = "SELECT task_from_telegram_id FROM tasks where id =$1"
        return await self.execute(sql, id, fetchrow=True)

    async def task_for_user(self, id):  # таска для юзера
        sql = "SELECT task_for, task_from, task_from_telegram_id, text_tasks from tasks " \
              "where id=$1"
        return await self.execute(sql, id, fetchrow=True)


# _________________________________________________________________________________________________
# class Employees:
#
#     def __init__(self):
#         self.pool: Union[Pool, None] = None
#
#     async def create_employees(self):
#         self.pool = await asyncpg.create_pool(
#             user=config.DB_USER,
#             password=config.DB_PASS,
#             host=config.DB_HOST,
#             database=config.DB_NAME
#         )
#
#     async def execute(self, command, *args,
#                       fetch: bool = False,  # этот фетч означает, что хотим забрать все данные
#                       fetchval: bool = False,  # доставать одно значение
#                       fetchrow: bool = False,  # данные в одном списке
#                       execute: bool = False  # никакие данные возвращать не надо
#                       ):
#         async with self.pool.acquire() as connection:
#             connection: Connection
#             async with connection.transaction():
#                 if fetch:
#                     result = await connection.fetch(command, *args)
#                 elif fetchval:
#                     result = await connection.fetchval(command, *args)
#                 elif fetchrow:
#                     result = await connection.fetchrow(command, *args)
#                 elif execute:
#                     result = await connection.execute(command, *args)
#             return result
#
#
#     async def create_table_employees(self):
#         sql = """
#              CREATE TABLE IF NOT EXISTS Tasks (
#             id SERIAL PRIMARY KEY,
#             fullname VARCHAR(60) NOT NULL,
#             post VARCHAR(40),
#             date_birthday date
#
#          );
#         """
#         await self.execute(sql, execute=True)

    # @staticmethod
    # def format_args(sql, parameters: dict):
    #     sql += " AND ".join([
    #         f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
    #                                                       start=1)
    #     ])
