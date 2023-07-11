from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.docs import docs, requisites, contract_Grishatkin, contract_Lifanov
from loader import dp


@dp.message_handler(text="📄Документы")
async def document(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=docs)


@dp.callback_query_handler(text="Реквизиты")
async def document(call: CallbackQuery):
    await call.message.edit_text(text="Вы находитесь в разделе реквизиты")
    await call.message.edit_reply_markup(reply_markup=requisites)


@dp.callback_query_handler(text="Реквизиты Гришаткин")
async def document(call: CallbackQuery):
    id = call.from_user.id
    file_id_1 = "BQACAgIAAxkBAAJvdWSt1KnPNGwLPbILwbxLDLs7dJhuAAIxKAAC4xExSaNTh8YxF6xCLwQ"
    await dp.bot.send_document(chat_id=id, document=file_id_1)

@dp.callback_query_handler(text="Реквизиты АС Каркас")
async def document(call: CallbackQuery):
    id = call.from_user.id
    file_id_1 = "BQACAgIAAxkBAAJvd2St1PUdLZRrpqicWBu-TrjTl5ACAALiMgACPH5hSXJ-xbFPchejLwQ"
    await dp.bot.send_document(chat_id=id, document=file_id_1)


@dp.callback_query_handler(text="Реквизиты Якущенко")
async def document(call: CallbackQuery):
    id = call.from_user.id
    file_id_1 = "BQACAgIAAxkBAAJveWSt1SNSp3XGtl6BxloLp1pfyj_dAALjMgACPH5hSdxjDBjLTS5YLwQ"
    await dp.bot.send_document(chat_id=id, document=file_id_1)


@dp.callback_query_handler(text="Реквизиты Лифанов")
async def document(call: CallbackQuery):
    id = call.from_user.id
    file_id_1 = "BQACAgIAAxkBAAIywWGWNn5R4ELEC8N_MzVTNtlKMsU9AAIEDgACUdqwSWGzzpOGAS4_IgQ"
    await dp.bot.send_document(chat_id=id, document=file_id_1)








@dp.callback_query_handler(text="Назад в документы")
async def document(call: CallbackQuery):
    await call.message.edit_text(text="Выберите раздел")
    await call.message.edit_reply_markup(reply_markup=docs)


