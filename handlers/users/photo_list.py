from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.communications import communications_keyboard
from keyboards.inline.houses import houses
from keyboards.inline.photo_list import photo_list
from keyboards.inline.production import production_keyboard
from loader import dp


@dp.message_handler(text="📷Фото")
async def send_keyboard_list(message: types.Message):
    await message.answer("Выбери нужный раздел", reply_markup=photo_list)

@dp.callback_query_handler(text="Фото домов")
async def send_keyboard_home(call: CallbackQuery):
    await call.message.edit_text(text="Выбери нужный дом")
    await call.message.edit_reply_markup(reply_markup=houses)


@dp.callback_query_handler(text="Фото коммуникации")
async def send_keyboard_home(call: CallbackQuery):
    await call.message.edit_text(text="Выбери нужный раздел")
    await call.message.edit_reply_markup(reply_markup=communications_keyboard)

@dp.callback_query_handler(text="Фото производства")
async def send_keyboard_home(call: CallbackQuery):
    await call.message.edit_text(text="Выбери нужный раздел")
    await call.message.edit_reply_markup(reply_markup=production_keyboard)


