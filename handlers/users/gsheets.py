import asyncio
import logging
import random

import gspread_asyncio
import gspread_formatting
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from datetime import datetime

from aiogram.types import CallbackQuery
from google.oauth2.service_account import Credentials
from aiogram.dispatcher.filters.builtin import Command

from keyboards.inline.gsheets_timer import gsheets_timer

from loader import dp





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


#встреч/показов
@dp.message_handler(Command("data"))
async def update_data(dp:Dispatcher):
    await dp.bot.send_message(624523030, "Ежедневный сбор статистики в таблицу", reply_markup=gsheets_timer)




@dp.callback_query_handler(text="ввести данные в таблицу")
async def update_data_gsheets(call: CallbackQuery, state: FSMContext):

    await call.message.answer("Введите количество встреч")
    await state.set_state("Количество встреч")


@dp.message_handler(state="Количество встреч")
async def update_data_gsheets(message: types.Message, state: FSMContext):
    spreadsheet_id = '1hocu-OWJdIDiTmy1WlteqprXhYPn7sIKkNUi8vdjXfQ'
    # spreadsheet_id = '1Dyffryz2Yc0uPhbSjf3zsapWlP9AMpXCgIo3UlwoF4c'
    path = r'C:\Users\aleks\PycharmProjects\MultiLevelMenu\creds.json'
    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(path))
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)
    # worksheet = await add_worksheet(async_spreadsheet, 'Лист2')
    worksheet = await async_spreadsheet.worksheet('Статистика от бота')
    current_datetime = datetime.now()
    values = []
    data = str(current_datetime.day) + "." + str(current_datetime.month) + "." + \
           str(current_datetime.year) + " " + str(current_datetime.hour) + ":" + \
           str(current_datetime.minute)
    values.append(data)
    values.append(message.from_user.first_name+" "+message.from_user.last_name)
    values.append(message.text)
    logging.info(list(values))
    await worksheet.append_row(values)
    await message.answer("Сохранено")


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
