import logging

import pathlib
from pathlib import Path

import gspread_asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from datetime import datetime

from aiogram.types import CallbackQuery
from google.oauth2.service_account import Credentials
from aiogram.dispatcher.filters.builtin import Command

from data.config import PATH, USER_GSHEETS
from keyboards.default import cancel, menu
from keyboards.inline.gsheets_timer import gsheets_timer

from loader import dp, db


def get_scoped_credentials(path: str):
    creds = Credentials.from_service_account_file(path)

    def prepare_scoped_credentials():
        return creds.with_scopes(
            ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        )

    return prepare_scoped_credentials


async def create_spreadsheet(client, spreadsheet_name) -> gspread_asyncio.AsyncioGspreadSpreadsheet:
    spreadsheet = await client.create(spreadsheet_name)
    spreadsheet = await client.open_by_key(spreadsheet.id)
    return spreadsheet


async def add_worksheet(async_spreadsheet: gspread_asyncio.AsyncioGspreadSpreadsheet, worksheet_name):
    worksheet = await async_spreadsheet.add_worksheet(worksheet_name, 500, 500)
    worksheet = await async_spreadsheet.worksheet(worksheet.title)
    return worksheet


# количество новых встреч, количество повторных встреч, количество показов
@dp.message_handler(Command("data"))
async def update_data_gsheet(dp: Dispatcher):
    for user_gsheets in USER_GSHEETS:
        if (await db.check_gsheets_today(telegram_id=user_gsheets) == 0):
            await dp.bot.send_message(user_gsheets, "Ежедневный сбор статистики в таблицу", reply_markup=gsheets_timer)


@dp.callback_query_handler(text="Гугл таблица")
async def state_data_gsheets(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите количество новых встреч за сегодня", reply_markup=cancel)
    await state.set_state("Количество новых встреч")


@dp.message_handler(state="Количество новых встреч")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    number_of_new_meetings = message.text
    try:
        int(number_of_new_meetings)
        await state.update_data(number_of_new_meetings=number_of_new_meetings)
        await message.answer("Введите количество повторных встреч за сегодня", reply_markup=cancel)
        await state.set_state("Количество повторных встреч")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Количество новых встреч")





@dp.message_handler(state="Количество повторных встреч")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    number_of_recurring_meetings = message.text
    try:
        int(number_of_recurring_meetings)
        await state.update_data(number_of_recurring_meetings=number_of_recurring_meetings)
        await message.answer("Введите количество показов за сегодня", reply_markup=cancel)
        await state.set_state("Количество показов")
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Количество повторных встреч")




@dp.message_handler(state="Количество показов")
async def save_data_gsheets(message: types.Message, state: FSMContext):
    number_of_impressions = message.text
    try:
        int(number_of_impressions)
    except:
        await message.answer("Введено не целое число, давай ещё раз")
        await state.set_state("Количество показов")
    data = await state.get_data()
    number_of_recurring_meetings = data.get("number_of_recurring_meetings")
    number_of_new_meetings = data.get("number_of_new_meetings")
    # await message.answer("Запись в таблицу..")
    await state.reset_state()
    await dp.bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAIQLWEk1jSoIIEBvFImzG43r2pSNer3AAIQDwACQvzYS_tsLq_GpJXBIAQ')
    ####################################################################
    spreadsheet_id = '1hocu-OWJdIDiTmy1WlteqprXhYPn7sIKkNUi8vdjXfQ'
    # spreadsheet_id = '1Dyffryz2Yc0uPhbSjf3zsapWlP9AMpXCgIo3UlwoF4c'   #ссылка на мою таблицу
    # path = r'C:\Users\aleks\PycharmProjects\MultiLevelMenu\creds.json'
    # path = Path(pathlib.Path.cwd(), 'creds.json')

    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(PATH))  # импорт из конфига
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)
    # worksheet = await add_worksheet(async_spreadsheet, 'Лист2')
    worksheet = await async_spreadsheet.worksheet('Статистика от бота')
    current_datetime = datetime.now()
    values = []
    data_time = str(current_datetime.day) + "." + str(current_datetime.month) + "." + \
                str(current_datetime.year)
                # + " " + str(current_datetime.hour + 3) + ":" + \
                # str(current_datetime.minute)
    values.append(data_time)
    values.append(message.from_user.first_name + " " + message.from_user.last_name)
    values.append(int(number_of_new_meetings))
    values.append(int(number_of_recurring_meetings))
    values.append(int(number_of_impressions))
    logging.info(values)
    # await worksheet.append_row(values)  # не забудь раскоментить!
    await db.update_gsheets_today(telegram_id=message.from_user.id)
    await message.answer(f"{data_time}\n"
                         f"Количество новых встреч: {number_of_new_meetings}\n"
                         f"Количество повторных встреч: {number_of_recurring_meetings}\n"
                         f"Количество показов: {number_of_impressions}",
                         reply_markup=menu)
    experience = (values[2]+values[3]+values[4])*10
    await db.update_experience(experience=experience, telegram_id=message.from_user.id)



@dp.callback_query_handler(text="Заполнить нулями")
async def state_data_gsheets(call: CallbackQuery, state: FSMContext):
    spreadsheet_id = '1hocu-OWJdIDiTmy1WlteqprXhYPn7sIKkNUi8vdjXfQ'
    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(PATH))
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)
    # worksheet = await add_worksheet(async_spreadsheet, 'Лист2')
    await dp.bot.send_sticker(call.from_user.id,
                              "CAACAgIAAxkBAAIQJmEk1FkF6Cp75JJwbDSwKW1j7e8LAAJaDwACg1TYS2Vw3nymTXs9IAQ")
    worksheet = await async_spreadsheet.worksheet('Статистика от бота')
    current_datetime = datetime.now()
    values = []
    data_time = str(current_datetime.day) + "." + str(current_datetime.month) + "." + \
                str(current_datetime.year)
                # + " " + str(current_datetime.hour + 3) + ":" + \
                # str(current_datetime.minute)
    values.append(data_time)
    values.append(call.from_user.first_name + " " + call.from_user.last_name)
    values.append(0)
    values.append(0)
    values.append(0)
    logging.info(values)
    await worksheet.append_row(values)
    await db.update_gsheets_today(telegram_id=call.from_user.id)

    # await call.message.answer("Сохранено нулями", reply_markup=menu)
    await call.answer("Сохранено")

@dp.message_handler(text="Напоминание про таблицу")
async def check_gsheets_today(message: types.Message):
    # logging.info(await db.check_gsheets_today(telegram_id=message.from_user.id))
    for user_gsheets in USER_GSHEETS:
        if (await db.check_gsheets_today(telegram_id=user_gsheets) == 0):
            await dp.bot.send_message(user_gsheets, "Напоминаю, что нужно заполнить статистику", reply_markup=gsheets_timer)

@dp.message_handler(Command("switch_on"))
@dp.message_handler(text="Напоминать сегодня про таблицу")
async def zeroing_gsheets(message: types.Message):
    await message.answer("Окей, сегодня напомню по таймеру или же вызвать сбор сейчас по команде /data")
    # logging.info(await db.check_gsheets_today(telegram_id=message.from_user.id))
    for user_gsheets in USER_GSHEETS:
        await db.zeroing_gsheets_today(telegram_id=user_gsheets)


@dp.message_handler(text="Обнуление таймера")
async def zeroing_gsheets_today(message: types.Message):
    # logging.info(await db.check_gsheets_today(telegram_id=message.from_user.id))
    for user_gsheets in USER_GSHEETS:
        await db.zeroing_gsheets_today(telegram_id=user_gsheets)

@dp.message_handler(Command("switch_off"))
@dp.message_handler(text="Не напоминать сегодня про таблицу")
async def one_gsheets_today(message: types.Message):
    await message.answer("Окей, сегодня без рассылки")
    for user_gsheets in USER_GSHEETS:
        await db.update_gsheets_today(telegram_id=user_gsheets)

# @dp.message_handler(state="Количество встреч")
# async def update_data_gsheets(message: types.Message, state: FSMContext):
#     spreadsheet_id = '1hocu-OWJdIDiTmy1WlteqprXhYPn7sIKkNUi8vdjXfQ'
#     # spreadsheet_id = '1Dyffryz2Yc0uPhbSjf3zsapWlP9AMpXCgIo3UlwoF4c'
#     # path = r'C:\Users\aleks\PycharmProjects\MultiLevelMenu\creds.json'
#     path = Path(pathlib.Path.cwd(), 'creds.json')
#     # path = r'/home/ubuntu/pythonProject/creds.json'
#     client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(path))
#     client = await client.authorize()
#     async_spreadsheet = await client.open_by_key(spreadsheet_id)
#     # worksheet = await add_worksheet(async_spreadsheet, 'Лист2')
#     worksheet = await async_spreadsheet.worksheet('Статистика от бота')
#     current_datetime = datetime.now()
#     values = []
#     data = str(current_datetime.day) + "." + str(current_datetime.month) + "." + \
#            str(current_datetime.year) + " " + str(current_datetime.hour) + ":" + \
#            str(current_datetime.minute)
#     values.append(data)
#     values.append(message.from_user.first_name + " " + message.from_user.last_name)
#     values.append(message.text)
#     logging.info(list(values))
#     await worksheet.append_row(values)
#     await message.answer("Сохранено")

#
# async def main():
#     spreadsheet_id = '1Dyffryz2Yc0uPhbSjf3zsapWlP9AMpXCgIo3UlwoF4c'
#     # 'https://docs.google.com/spreadsheets/d/1Dyffryz2Yc0uPhbSjf3zsapWlP9AMpXCgIo3UlwoF4c'
#
#     path = r'C:\Users\aleks\PycharmProjects\MultiLevelMenu\creds.json'
#     client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(path))
#     client = await client.authorize()
#     async_spreadsheet = await client.open_by_key(spreadsheet_id)
#     worksheet = await add_worksheet(async_spreadsheet, 'Лист номер 1')
#     worksheet = await async_spreadsheet.worksheet('Лист номер 1')
#     # url = async_spreadsheet.ss.url
#
#     # await async_spreadsheet.share('alekse.lazarev.01@gmail.com', perm_type='user', role='writer')
#     headers = ['ID', 'Имя Клиента', "Номер телефона", "Адрес", "Сумма выполненных заказов"]
#     await create_header(worksheet, headers)
#
#     fake = Faker()
#     Faker.seed(0)
#
#     ids = [num for num in range(1, 101)]
#     names = [fake.first_name() for _ in range(100)]
#     phone_numbers = [fake.phone_number() for _ in range(100)]
#     address = [fake.address() for _ in range(100)]
#     orders_sum = [random.randint(100, 1000) for _ in range(100)]
#
#     values = list(zip(ids, names, phone_numbers, address, orders_sum))
#     await worksheet.append_rows(values)
#
#
# asyncio.run(main())
