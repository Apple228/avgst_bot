import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import IT_SUPPORT
from keyboards.default import cancel, menu
from loader import dp
from states import It_support


@dp.message_handler(text="💻IT Поддержка")
async def it_support(message: types.Message):
    await message.answer("Введите описание проблемы.\n", reply_markup=cancel)
    await It_support.name_id.set()


@dp.message_handler(state=It_support.name_id)
async def text_it_support(message: types.Message, state: FSMContext):
    for it_support in IT_SUPPORT:
        try:
            await dp.bot.send_message(it_support, f"{message.from_user.full_name} оставил(а) заявку с текстом:\n"
                                                  f"{message.text} \n"
                                                  f"Связаться с @{message.from_user.username}")
        except Exception as err:
            logging.exception(err)
    await message.answer("Заявка оставлена", reply_markup=menu)
    await state.reset_state()
