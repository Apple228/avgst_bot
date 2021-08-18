import logging
from datetime import datetime

from aiogram import executor, Dispatcher

from handlers.users.gsheets import update_data_gsheets, check_gsheets_today, zeroing_gsheets_today
from loader import dp, db, tm, scheduler
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


def scheduler_jobs():
    scheduler.add_job(update_data_gsheets, "cron", day_of_week="mon-fri", hour=15, minute=10,
                      end_date="2022-05-30", args=(dp,))
    scheduler.add_job(update_data_gsheets, "cron", day_of_week="sat", hour=13, minute=0, args=(dp,))
    scheduler.add_job(check_gsheets_today, "cron", day_of_week="mon-sat", hour=18, minute=00, args=(dp,))
    scheduler.add_job(zeroing_gsheets_today, "cron", day_of_week="mon-sat", hour=20, minute=59, args=(dp,))



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
