import datetime

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove

from data.config import PATH
from keyboards.default import menu
from keyboards.default.form_keyboards import location_keyboard, interesting_keyboard, target_keyboard, square_keyboard, \
    count_room_keyboard, equipment_keyboard, project_keyboard, budget_keyboard, payment_method_keyboard, \
    clent_from_keyboard, komplekt_keyboard, comment_keyboard
from loader import dp
from google.oauth2.service_account import Credentials
import gspread_asyncio
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


@dp.message_handler(text='📝Новый лид')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Имя клиента", reply_markup=ReplyKeyboardRemove())
    await state.set_state("Имя клиента")




@dp.message_handler(state="Имя клиента")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    if message.text == "/stop":
        await message.answer("Нужно ввести имя, если нет такой инфы, то /cancel")
        await state.set_state("Имя клиента")
    else:
        client_name = message.text
        await state.update_data(client_name=client_name)
        await message.answer("Номер телефона")
        await state.set_state("Номер телефона")


@dp.message_handler(state="Номер телефона")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    if message.text == "/stop":
        await message.answer("Нужно ввести номер клиента, если нет никакой инфы, то /cancel")
        await state.set_state("Номер телефона")
    else:
        client_phone_number = message.text
        await state.update_data(client_phone_number=client_phone_number)
        await message.answer("Название проекта", reply_markup=project_keyboard)
        await state.set_state("Название проекта")

@dp.message_handler(state="Название проекта")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_project = message.text
    await state.update_data(client_project=client_project)
    await message.answer("Количество комнат", reply_markup=count_room_keyboard)
    await state.set_state("Количество комнат")


@dp.message_handler(state="Количество комнат")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_room = message.text
    await state.update_data(client_room=client_room)
    await message.answer("Бюджет", reply_markup=ReplyKeyboardRemove())
    await state.set_state("Бюджет")

@dp.message_handler(state="Бюджет")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_budget = message.text
    await state.update_data(client_budget=client_budget)
    await message.answer("Комплектация", reply_markup=komplekt_keyboard)
    await state.set_state("Комплектация")

@dp.message_handler(state="Комплектация")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_komplekt = message.text
    await state.update_data(client_komplekt=client_komplekt)
    await message.answer("Способ оплаты", reply_markup=payment_method_keyboard)
    await state.set_state("Способ оплаты")

@dp.message_handler(state="Способ оплаты")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    payment_method = message.text
    await state.update_data(payment_method=payment_method)
    await message.answer("Откуда пришли", reply_markup=clent_from_keyboard)
    await state.set_state("Откуда пришли")

@dp.message_handler(state="Откуда пришли")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_from = message.text
    await state.update_data(client_from=client_from)
    await message.answer("Комментарий", reply_markup=comment_keyboard)
    await state.set_state("Комментарий")


@dp.message_handler(Command("stop"), state='*')
@dp.message_handler(state="Комментарий")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    if message.text == "/stop":
        comment = ""
    else:
        comment = message.text
    await state.update_data(comment=comment)

    data = await state.get_data()
    today = datetime.date.today()

    await message.answer(f"1. {message.from_user.full_name}\n"
                         f"2. {today.strftime('%d.%m.%y')}\n"
                         f"3. {data.get('client_name')}\n"
                         f"4. {data.get('client_phone_number')}\n"
                         f"5. {data.get('client_project')}\n"
                         f"6. {data.get('client_room')}\n"
                         f"7. {data.get('client_budget')}\n"
                         f"8. {data.get('client_komplekt')}\n"
                         # f"8. {data.get('client_target')}\n"
                         # f"9. {data.get('client_square')}\n"
                         # f"10. {data.get('count_room')}\n"
                         # f"11. {data.get('equipment')}\n"
                         # f"12. {data.get('project')}\n"
                         # f"13. {data.get('budget')}\n"
                         f"9. {data.get('payment_method')}\n"
                         f"10. {data.get('client_from')}\n"
                         f"11. {data.get('comment')}\n",
                         reply_markup=menu)
    await state.reset_state()
    spreadsheet_id = '1RDCvRLVibW0cGEqS8RtCgI0bmsLM5EN-CKYmToyBciA'
    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(PATH))  # импорт из конфига
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)

    worksheet = await async_spreadsheet.worksheet('БОТ КП Авангард')
    values = [message.from_user.full_name, today.strftime('%d.%m.%y'), data.get('client_name'),
              data.get('client_phone_number'), data.get('client_project'),data.get('client_room'), data.get('client_budget'),
              data.get('client_komplekt'),
              data.get('payment_method'),
              data.get('client_from'),
              # data.get('client_target'), data.get('client_square'), data.get('count_room'),
              # data.get('equipment'), data.get('project'), data.get('budget'),
              data.get('comment')]
    await worksheet.append_row(values)
# @dp.message_handler(state="Какую локацию рассматриваете?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     client_location = message.text
#     await state.update_data(client_location=client_location)
#     await message.answer("Что интересует?", reply_markup=interesting_keyboard)
#     await state.set_state("Что интересует?")
#     # await message.answer("Когда планируется стройка?", reply_markup=planing_build_keyboard)
#     # await state.set_state("Когда планируется стройка?")
#
# @dp.message_handler(state="Что интересует?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     client_interesting = message.text
#     await state.update_data(client_interesting=client_interesting)
#     await message.answer("Когда планируется стройка?", reply_markup=planing_build_keyboard)
#     await state.set_state("Когда планируется стройка?")
#
# @dp.message_handler(state="Когда планируется стройка?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     planing_build = message.text
#     await state.update_data(planing_build=planing_build)
#     await message.answer("Как используем дом?", reply_markup=target_keyboard)
#     await state.set_state("Как используем дом?")
#     # await message.answer("Комментарий", reply_markup=comment_keyboard)
#     # await state.set_state("Комментарий")
#
#
# @dp.message_handler(state="Как используем дом?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     client_target = message.text
#     await state.update_data(client_target=client_target)
#     await message.answer("Площадь?", reply_markup=square_keyboard)
#     await state.set_state("Площадь?")
#
#
# @dp.message_handler(state="Площадь?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     client_square = message.text
#     await state.update_data(client_square=client_square)
#     await message.answer("Сколько комнат?", reply_markup=count_room_keyboard)
#     await state.set_state("Сколько комнат?")
#
# @dp.message_handler(state="Сколько комнат?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     count_room = message.text
#     await state.update_data(count_room=count_room)
#     await message.answer("Комплектация?", reply_markup=equipment_keyboard)
#     await state.set_state("Комплектация?")
#
#
# @dp.message_handler(state="Комплектация?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     equipment = message.text
#     await state.update_data(equipment=equipment)
#     await message.answer("Проект?", reply_markup=project_keyboard)
#     await state.set_state("Проект?")
#
#
# @dp.message_handler(state="Проект?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     project = message.text
#     await state.update_data(project=project)
#     await message.answer("Бюджет?", reply_markup=budget_keyboard)
#     await state.set_state("Бюджет?")
#
# @dp.message_handler(state="Бюджет?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     budget = message.text
#     await state.update_data(budget=budget)
#     await message.answer("Способ оплаты?", reply_markup=payment_method_keyboard)
#     await state.set_state("Способ оплаты?")
#
#
# @dp.message_handler(state="Способ оплаты?")
# async def state_data_gsheets(message: types.Message, state: FSMContext):
#     payment_method = message.text
#     await state.update_data(payment_method=payment_method)
#     await message.answer("Комментарий", reply_markup=comment_keyboard)
#     await state.set_state("Комментарий")

#Ксюхины тесты
@dp.message_handler(text = "/get_stats_today")
async def get_records(message: types.message, state: FSMContext):

    spreadsheet_id = '1RDCvRLVibW0cGEqS8RtCgI0bmsLM5EN-CKYmToyBciA'
    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(PATH))  # импорт из конфига
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)
    worksheet = await async_spreadsheet.worksheet('БОТ КП Авангард')

    data = await worksheet.range(name = "A2:B2000")

    all_rows = []
    text = "|".join([cell.value for cell in data])
    text = text.split("|")
    for i in range(0, len(text)-1, 2):
        all_rows.append((text[i], text[i+1]))

    today = datetime.date.today()

    today_row = []
    for row in all_rows:
        if today.strftime('%d.%m.%y') in row:
            today_row.append(row[0])
    msg = f"Всего за сегодня {len(today_row)} лидов\n"
    d = {e: 0 for e in today_row}  # создаем словарь на основе списка с 0 значениями
    for key in today_row: d[key] += 1  # тупо считаем повторяющиеся
    for key, value in d.items():
        print(key, value)  # тупо выводим
        msg += f"{key} {value}\n"
    await message.answer(msg)