from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("stop", "Закончить анкету (с сохранением)"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("menu", "Возврат в меню"),
        types.BotCommand("cancel", "Отмена"),
        types.BotCommand("/get_stats_today", "Подсчет статистики за сегодня"),


    ])
