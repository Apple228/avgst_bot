from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.birthday import update_birthday
from loader import dp
import datetime
d ={
    'Лифанов Павел':'29.10',
}

@dp.message_handler(text="День рождения")
async def birthday_today(message: types.Message):
    today = datetime.date.today()
    print(today.strftime('%d.%m'))
    for name, date in d.items():
        if date == today.strftime('%d.%m'):
            await message.answer(f'Сегодня день рождения у {name}')

# @dp.message_handler(text="День рождения")
# async def birthday1(message:types.Message):
#     await message.answer("+", reply_markup=update_birthday)
#
#
# @dp.callback_query_handler(text="День рождения")
# async def birthday(call: CallbackQuery, state: FSMContext):
#     await call.message.answer("Введите дату вашего рождения в формате ГГГГ-ММ-ДД")
#     await state.set_state("Ввод даты дня рождения")
#
# @dp.message_handler(state="Ввод даты дня рождения")
# async def birthday(message: types.Message):
#     await message.answer("+")