from aiogram import types
from aiogram.types import CallbackQuery


from keyboards.inline.video_list import video_list, tyr3DBarn10_keyboard, houses_video
from loader import dp


@dp.message_handler(text="📹Видео")
async def send_keyboard_list(message: types.Message):
    await message.answer("Выбери нужный раздел", reply_markup=video_list)

@dp.callback_query_handler(text="3D туры")
async def tyr3D(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=tyr3DBarn10_keyboard)

@dp.callback_query_handler(text="Видео домов")
async def tyr3D(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=houses_video)

@dp.callback_query_handler(text="Барн 10 3D тур")
async def tyr3DBarn10(call: CallbackQuery):
    await call.message.edit_text("https://zima360.ru/wp-content/uploads/2022/07/1stageAvanStNN/")


@dp.callback_query_handler(text="Прованс 24 видео")
async def videoProvans24(call: CallbackQuery):
    await call.message.edit_text("Пока нет ссылки")

