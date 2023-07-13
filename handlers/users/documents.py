import os

from aiogram import types
from aiogram.types import CallbackQuery, InputFile


from keyboards.inline.docs import docs, requisites, contract_Grishatkin, contract_Lifanov, price_tables_keyboard, \
    kp_keyboard
from loader import dp


@dp.message_handler(text="📄Документы")
async def document(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=docs)


@dp.message_handler(text="📈Таблицы цен")
async def document(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=price_tables_keyboard)


@dp.message_handler(text="📊КПшки")
async def document(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=kp_keyboard)
@dp.callback_query_handler(text="Реквизиты")
async def document(call: CallbackQuery):
    await call.message.edit_text(text="Вы находитесь в разделе реквизиты")
    await call.message.edit_reply_markup(reply_markup=requisites)

@dp.callback_query_handler(text="Цены для НН")
async def document(call: CallbackQuery):
    path1 = 'docs/ИЮЛЬ 2023 дома.xlsx'
    path2 = 'docs/ИЮЛЬ 2023 модули.xlsx'
    await call.message.answer_document(document=types.InputFile(path1))
    await call.message.answer_document(document=types.InputFile(path2))

@dp.callback_query_handler(text="Цены для МСК")
async def document(call: CallbackQuery):
    path1 = 'docs/ИЮНЬ 2023 дома МСК.xlsx'
    path2 = 'docs/ИЮНЬ 2023 модули МСК.xlsx'
    await call.message.answer_document(document=types.InputFile(path1))
    await call.message.answer_document(document=types.InputFile(path2))


@dp.callback_query_handler(text="Договора АС Каркас")
async def document(call: CallbackQuery):
    path = "docs/Договора АС Каркас"
    content = os.listdir(path)
    for file in content:
        await call.message.answer_document(document=types.InputFile(f"{path}/{file}"))

@dp.callback_query_handler(text="Договора Нижний Новгород")
async def document(call: CallbackQuery):
    path = "docs/Договора Нижний Новгород"
    content = os.listdir(path)
    for file in content:
        await call.message.answer_document(document=types.InputFile(f"{path}/{file}"))

@dp.callback_query_handler(text="КПшки для НН")
async def document(call: CallbackQuery):
    await call.message.answer("Их нет")
    path1 = ''
    path2 = ''
    # await call.message.answer_document(document=types.InputFile(path1))
    # await call.message.answer_document(document=types.InputFile(path2))


@dp.callback_query_handler(text="КПшки для МСК")
async def document(call: CallbackQuery):
    path = "docs/КПшки МСК"
    content = os.listdir(path)
    for file in content:
        await call.message.answer_document(document=types.InputFile(f"{path}/{file}"))

@dp.callback_query_handler(text="Реквизиты Гришаткин")
async def document(call: CallbackQuery):
    path = 'docs/Карточка_ООО_Авангард_Строй_Нижний_Новгород_Примсоцбанк.docx'
    await call.message.answer_document(document=types.InputFile(path))

@dp.callback_query_handler(text="Реквизиты АС Каркас")
async def document(call: CallbackQuery):
    path = 'docs/Карточка_ООО АС Каркас.docx'
    await call.message.answer_document(document=types.InputFile(path))

@dp.callback_query_handler(text="Реквизиты Якущенко")
async def document(call: CallbackQuery):
    path = 'docs/Карточка_организации_ИП_Якущенко.pdf'
    await call.message.answer_document(document=types.InputFile(path))

@dp.callback_query_handler(text="Реквизиты Лифанов")
async def document(call: CallbackQuery):
    path = 'docs/Карточка ООО Авангард строй НН.docx'
    await call.message.answer_document(document=types.InputFile(path))


@dp.callback_query_handler(text="Регламент ОГД")
async def document(call: CallbackQuery):
    path = 'docs/Регламент ведения клиента.docx'
    await call.message.answer_document(document=types.InputFile(path))







@dp.callback_query_handler(text="Назад в документы")
async def document(call: CallbackQuery):
    await call.message.edit_text(text="Выберите раздел")
    await call.message.edit_reply_markup(reply_markup=docs)


