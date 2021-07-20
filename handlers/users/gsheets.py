import asyncio
import logging
import random

import gspread_asyncio
import gspread_formatting
from aiogram import types
from aiogram.dispatcher import FSMContext


from google.oauth2.service_account import Credentials
from aiogram.dispatcher.filters.builtin import Command
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



@dp.message_handler(Command("data"))
async def update_data(message: types.Message, state: FSMContext):
    await message.answer("Введите количество встреч за сегодня")
    await state.set_state("get_count_gsheets")


@dp.message_handler(state="get_count_gsheets")
async def update_data_gsheets(message: types.Message, state: FSMContext):
    spreadsheet_id = '1Dyffryz2Yc0uPhbSjf3zsapWlP9AMpXCgIo3UlwoF4c'
    path = r'C:\Users\aleks\PycharmProjects\MultiLevelMenu\creds.json'
    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(path))
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)
    # worksheet = await add_worksheet(async_spreadsheet, 'Лист2')
    worksheet = await async_spreadsheet.worksheet('Лист2')
    logging.info(message.text)
    # await worksheet.append_row(message.text)
    values = []
    values.append(message.text)
    await worksheet.append_row(values)
    logging.info(list(values))

    await state.reset_state()
    # await worksheet.append_row(values)

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
