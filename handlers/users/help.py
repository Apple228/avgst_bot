from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp, Command

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/email - Ввести свою почту',
        '/data - объявляет сбор статистики в таблицу',
        'Регламент заездов - ',
        'Фото Прованс 28'

    ]
    await message.answer('\n'.join(text))


