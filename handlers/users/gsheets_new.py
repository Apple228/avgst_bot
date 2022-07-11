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
    #     if (await db.check_gsheets_today(telegram_id=user_gsheets) == 0):
            await dp.bot.send_message(user_gsheets, "Ежедневный сбор статистики в таблицу",
                                      reply_markup=gsheets_timer_finished_house)
            username = await db.select_full_name(user_gsheets)
            await dp.bot.send_message(624523030, f"Сообщение отправлено для {username}")


@dp.callback_query_handler(text="Отдел готовых домов")
async def state_data_gsheets(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Заинтересовал Барн 7", reply_markup=numbers)
    await state.set_state("Заинтересовал Барн 7")


@dp.message_handler(state="Заинтересовал Барн 7")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_Barn7 = message.text
    try:
        await state.update_data(interested_in_Barn7=int(interested_in_Barn7))
        await message.answer("Заинтересовал Барн 10", reply_markup=numbers)
        await state.set_state("Заинтересовал Барн 10")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал Барн 7")


@dp.message_handler(state="Заинтересовал Барн 10")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_Barn10 = message.text
    try:
        await state.update_data(interested_in_Barn10=int(interested_in_Barn10))
        await message.answer("Заинтересовал Шведский 2", reply_markup=numbers)
        await state.set_state("Заинтересовал Шведский 2")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал Барн 10")



@dp.message_handler(state="Заинтересовал Шведский 2")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_Swedish2 = message.text
    try:

        await state.update_data(interested_in_Swedish2=int(interested_in_Swedish2))
        await message.answer("Заинтересовал Барн 11", reply_markup=numbers)
        await state.set_state("Заинтересовал Барн 11")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал Шведский 2")

@dp.message_handler(state="Заинтересовал Барн 11")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_Barn11 = message.text
    try:

        await state.update_data(interested_in_Barn11=int(interested_in_Barn11))
        await message.answer("Заинтересовал другой проект", reply_markup=numbers)
        await state.set_state("Заинтересовал другой проект")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал Барн 11")


@dp.message_handler(state="Заинтересовал другой проект")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    interested_in_an_other_project = message.text
    try:

        await state.update_data(interested_in_an_other_project=int(interested_in_an_other_project))
        await message.answer("Кол-во показов Барн 10", reply_markup=numbers)
        await state.set_state("Кол-во показов Барн 10")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Заинтересовал другой проект")

@dp.message_handler(state="Кол-во показов Барн 10")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    number_of_impressions_Barn_10 = message.text
    try:

        await state.update_data(
            number_of_impressions_Barn_10=int(number_of_impressions_Barn_10))
        await message.answer("Кол-во показов в продажу домов", reply_markup=numbers)
        await state.set_state("Кол-во показов в продажу домов")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Кол-во показов в продажу домов")


@dp.message_handler(state="Кол-во показов в продажу домов")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    number_of_impressions_in_the_sale_of_houses = message.text
    try:

        await state.update_data(
            number_of_impressions_in_the_sale_of_houses=int(number_of_impressions_in_the_sale_of_houses))
        await message.answer("Кол-во показов в стройку", reply_markup=numbers)
        await state.set_state("Кол-во показов в стройку")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Кол-во показов в продажу домов")



@dp.message_handler(state="Кол-во показов в стройку")
async def save_data_gsheets(message: types.Message, state: FSMContext):
    number_of_impressions_in_construction = message.text
    try:
        number_of_impressions_in_construction = int(number_of_impressions_in_construction)
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
    values.append(int(data.get("interested_in_Barn7")))
    values.append(int(data.get("interested_in_Barn10")))
    values.append(int(data.get("interested_in_Swedish2")))
    values.append(int(data.get("interested_in_Barn11")))
    # values.append(data.get("interested_in_Barn6"))
    # values.append(data.get("interested_in_Barn3"))
    values.append(int(data.get("interested_in_an_other_project")))
    values.append(int(data.get("number_of_impressions_Barn_10")))
    values.append(int(data.get("number_of_impressions_in_the_sale_of_houses")))

    values.append(number_of_impressions_in_construction)
    # values.append(data.get("number_of_concluded_contracts"))
    # values.append(the_amount_of_concluded_contracts)
    logging.info(values)
    await dp.bot.send_message(624523030, f"{values}")
    await dp.bot.send_sticker(message.from_user.id,
                              'CAACAgIAAxkBAAIQLWEk1jSoIIEBvFImzG43r2pSNer3AAIQDwACQvzYS_tsLq_GpJXBIAQ',
                              reply_markup=menu)
    worksheet = await async_spreadsheet.worksheet('БОТ ГД3')
    await worksheet.append_row(values)
    await state.reset_state()
    await db.update_gsheets_today(telegram_id=message.from_user.id)


@dp.message_handler(text="Напоминание про таблицу")
async def check_gsheet_finished_house(message: types.Message):
    # logging.info(await db.check_gsheets_today(telegram_id=message.from_user.id))
    for user_gsheets in DEPARTMENT_OF_READY_HOUSES:
        if (await db.check_gsheets_today(telegram_id=user_gsheets) == 0):
            await dp.bot.send_message(user_gsheets, "Напоминаю, что нужно заполнить статистику",
                                      reply_markup=gsheets_timer_finished_house)
            username = await db.select_full_name(user_gsheets)
            await dp.bot.send_message(624523030, f"Таблицу не заполнил {username}")


@dp.callback_query_handler(text="Заполнить нулями готовые дома")
async def state_data_gsheets(call: CallbackQuery, state: FSMContext):
    spreadsheet_id = '1hocu-OWJdIDiTmy1WlteqprXhYPn7sIKkNUi8vdjXfQ'
    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(PATH))
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)
    # worksheet = await add_worksheet(async_spreadsheet, 'Лист2')
    await dp.bot.send_sticker(call.from_user.id,
                              "CAACAgIAAxkBAAIQJmEk1FkF6Cp75JJwbDSwKW1j7e8LAAJaDwACg1TYS2Vw3nymTXs9IAQ")
    worksheet = await async_spreadsheet.worksheet('БОТ ГД3')

    values = []

    today = datetime.date.today()
    data_time = today.strftime('%d.%m.%y')

    values.append(data_time)
    values.append(call.from_user.first_name + " " + call.from_user.last_name)
    values.append(0)
    values.append(0)
    values.append(0)
    values.append(0)
    values.append(0)
    values.append(0)
    values.append(0)
    logging.info(values)
    await dp.bot.send_message(624523030, f"{values}")
    await worksheet.append_row(values)
    await db.update_gsheets_today(telegram_id=call.from_user.id)
