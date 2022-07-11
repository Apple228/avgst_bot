import logging
from datetime import datetime

from aiogram import executor, Dispatcher

from handlers.users.birthday import birthday_today
from handlers.users.coffee_random import coffee_random_choice
from handlers.users.gsheets import update_data_gsheet, check_gsheets_today, zeroing_gsheets_today
from handlers.users.gsheets_new import update_data_gsheet_finished_house, check_gsheet_finished_house
from loader import dp, db, tm, scheduler
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


def scheduler_jobs():
    scheduler.add_job(update_data_gsheet, "cron", day_of_week="mon-fri", hour=18, minute=10,
                      end_date="2023-05-30", args=(dp,))
    scheduler.add_job(update_data_gsheet_finished_house, "cron", day_of_week="mon-fri", hour=18, minute=10,
                      end_date="2023-05-30", args=(dp,))
    # scheduler.add_job(update_data_gsheet, "cron", day_of_week="sat", hour=13, minute=00, args=(dp,))
    # scheduler.add_job(check_gsheets_today, "cron", day_of_week="mon-sat", hour=17, minute=00, args=(dp,))

    # scheduler.add_job(check_gsheet_finished_house, "cron", day_of_week="mon-sat", hour=16, minute=30, args=(dp,))

    # scheduler.add_job(zeroing_gsheets_today, "cron", day_of_week="mon-sat", hour=21, minute=20, args=(dp,))
    scheduler.add_job(birthday_today, "cron", day_of_week="mon-sun", hour=6, minute=00, args=(dp,))
    # scheduler.add_job(coffee_random_choice, "cron" , day_of_week="mon-fri", hour=6, minute=30, args=(dp,))



async def on_startup(dispatcher):
    # Уведомляет про запуск
    logging.info("Создаем подключение к базе данных")
    await db.create_users()
    await tm.create_tasks()
    # await ep.create_employees()
    # await db.drop_users()

    logging.info("Создаем таблицу пользователей")
    await db.create_table_users()
    logging.info("Готово.")
    logging.info("Создаем таблицу задач")
    await tm.create_table_tasks()
    logging.info("Готово.")
    await on_startup_notify(dispatcher)
    scheduler_jobs()
    await set_default_commands(dp)


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
