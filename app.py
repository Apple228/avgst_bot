import logging
from datetime import datetime

from aiogram import executor, Dispatcher

from loader import dp, db, tm, scheduler
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def send_message_to_admin(dp:Dispatcher):
    current_datetime = datetime.now()
    await dp.bot.send_message(624523030, f"{current_datetime.day}-{current_datetime.month}-{current_datetime.year}  {current_datetime.hour}:{current_datetime.minute}")


def scheduler_jobs():
    scheduler.add_job(send_message_to_admin, "cron", day_of_week="mon-fri", hour=17, minute=53, end_date="2022-05-30", args=(dp,))

async def on_startup(dispatcher):
    # Уведомляет про запуск
    logging.info("Создаем подключение к базе данных")
    await db.create_users()
    await tm.create_tasks()
    # await db.drop_users()

    logging.info("Создаем таблицу пользователей")
    await db.create_table_users()
    logging.info("Готово.")
    logging.info("Создаем таблицу задач")
    await tm.create_table_tasks()
    logging.info("Готово.")
    await on_startup_notify(dispatcher)
    scheduler_jobs()

if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
