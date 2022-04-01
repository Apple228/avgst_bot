import logging

import gspread_asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
import datetime
from aiogram.types import CallbackQuery
from google.oauth2.service_account import Credentials
from aiogram.dispatcher.filters.builtin import Command

from data.config import DEPARTMENT_OF_READY_HOUSES, PATH
from handlers.users.gsheets import get_scoped_credentials
from keyboards.default import menu
from keyboards.default.numbers_for_gsheets import numbers
from keyboards.inline.gsheets_timer import gsheets_timer_finished_house
from loader import dp, db

@dp.message_handler(Command("data_new"))
async def update_data_gsheet_finished_house(dp: Dispatcher):
    for user_gsheets in DEPARTMENT_OF_READY_HOUSES:
        if (await db.check_gsheets_today(telegram_id=user_gsheets) == 0):
            await dp.bot.send_message(user_gsheets, "Ежедневный сбор статистики в таблицу", reply_markup=gsheets_timer_finished_house)


@dp.callback_query_handler(text="Отдел готовых домов")
async def state_data_gsheets(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Заинтересовал Барн 7", reply_markup=numbers)
    await state.set_state("Заинтересовал Барн 7")

@dp.message_handler(state="Заинтересовал Барн 7")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_Barn7 = message.text
    try:
        int(interested_in_Barn7)
        await state.update_data(interested_in_Barn7=interested_in_Barn7)
        await message.answer("Заинтересовал Шведский 2", reply_markup=numbers)
        await state.set_state("Заинтересовал Шведский 2")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал Барн 7")



@dp.message_handler(state="Заинтересовал Шведский 2")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_Swedish2 = message.text
    try:
        int(interested_in_Swedish2)
        await state.update_data(interested_in_Swedish2=interested_in_Swedish2)
        await message.answer("Заинтересовал Прованс 24", reply_markup=numbers)
        await state.set_state("Заинтересовал Прованс 24")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал Шведский 2")

@dp.message_handler(state="Заинтересовал Прованс 24")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_Provence_24 = message.text
    try:
        int(interested_in_Provence_24)
        await state.update_data(interested_in_Provence_24=interested_in_Provence_24)
        await message.answer("Заинтересовал Барн 6", reply_markup=numbers)
        await state.set_state("Заинтересовал Барн 6")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал Прованс 24")


@dp.message_handler(state="Заинтересовал Барн 6")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_Barn6 = message.text
    try:
        int(interested_in_Barn6)
        await state.update_data(interested_in_Barn6=interested_in_Barn6)
        await message.answer("Заинтересовал Барн 3", reply_markup=numbers)
        await state.set_state("Заинтересовал Барн 3")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал Барн 6")


@dp.message_handler(state="Заинтересовал Барн 3")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_Barn3 = message.text
    try:
        int(interested_in_Barn3)
        await state.update_data(interested_in_Barn3=interested_in_Barn3)
        await message.answer("Заинтересовал индивидуальный проект", reply_markup=numbers)
        await state.set_state("Заинтересовал индивидуальный проект")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал Барн 3")

@dp.message_handler(state="Заинтересовал индивидуальный проект")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_an_individual_project = message.text
    try:
        int(interested_in_an_individual_project)
        await state.update_data(interested_in_an_individual_project=interested_in_an_individual_project)
        await message.answer("Кол-во показов", reply_markup=numbers)
        await state.set_state("Кол-во показов")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал индивидуальный проект")


@dp.message_handler(state="Кол-во показов")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    number_of_impressions_new = message.text
    try:
        int(number_of_impressions_new)
        await state.update_data(number_of_impressions_new=number_of_impressions_new)
        await message.answer("Кол-во повторных встреч", reply_markup=numbers)
        await state.set_state("Кол-во повторных встреч")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Кол-во показов")



@dp.message_handler(state="Кол-во повторных встреч")
async def save_data_gsheets(message: types.Message, state: FSMContext):
    number_of_repeated_meetings_new = message.text
    try:
        int(number_of_repeated_meetings_new)
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Сумма заключенных договоров (готовые дома)")
    data = await state.get_data()
    spreadsheet_id = '1hocu-OWJdIDiTmy1WlteqprXhYPn7sIKkNUi8vdjXfQ'
    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(PATH))  # импорт из конфига
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)


    values = []
    today = datetime.date.today()
    data_time = today.strftime('%d.%m.%y')

    values.append(data_time)
    values.append(message.from_user.first_name + " " + message.from_user.last_name)
    values.append(data.get("interested_in_Barn7"))
    values.append(data.get("interested_in_Swedish2"))
    values.append(data.get("interested_in_Provence_24"))
    values.append(data.get("interested_in_Barn6"))
    values.append(data.get("interested_in_Barn3"))
    values.append(data.get("interested_in_an_individual_project"))
    values.append(data.get("number_of_impressions_new"))
    values.append(number_of_repeated_meetings_new)
    # values.append(data.get("number_of_concluded_contracts"))
    # values.append(the_amount_of_concluded_contracts)
    logging.info(values)
    await dp.bot.send_sticker(message.from_user.id,
                              'CAACAgIAAxkBAAIQLWEk1jSoIIEBvFImzG43r2pSNer3AAIQDwACQvzYS_tsLq_GpJXBIAQ', reply_markup=menu)
    worksheet = await async_spreadsheet.worksheet('БОТ ГД')
    await worksheet.append_row(values)
    await state.reset_state()
    await db.update_gsheets_today(telegram_id=message.from_user.id)