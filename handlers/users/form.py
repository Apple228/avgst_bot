import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove

from data.config import PATH
from keyboards.default import menu
from keyboards.default.form_keyboards import location_keyboard, interesting_keyboard, target_keyboard, square_keyboard, \
    count_room_keyboard, equipment_keyboard, project_keyboard, budget_keyboard, payment_method_keyboard, \
    mortgage_advice_keyboard, start_keyboard
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

@dp.message_handler(Command("cancel"), state="*")
@dp.message_handler(text="Отмена", state="*")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Отменено", reply_markup=start_keyboard)
    await state.reset_state()


@dp.message_handler(state="Имя клиента")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_name = message.text
    await state.update_data(client_name=client_name)
    await message.answer("Номер телефона")
    await state.set_state("Номер телефона")


@dp.message_handler(state="Номер телефона")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_phone_number = message.text
    await state.update_data(client_phone_number=client_phone_number)
    await message.answer("Какую локацию рассматриваете? (если не Мск, то написать регион)", reply_markup=location_keyboard)
    await state.set_state("Какую локацию рассматриваете?")


@dp.message_handler(state="Какую локацию рассматриваете?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_location = message.text
    await state.update_data(client_location=client_location)
    await message.answer("Что интересует?", reply_markup=interesting_keyboard)
    await state.set_state("Что интересует?")


@dp.message_handler(state="Что интересует?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_interesting = message.text
    await state.update_data(client_interesting=client_interesting)
    await message.answer("Как используем дом?", reply_markup=target_keyboard)
    await state.set_state("Как используем дом?")


@dp.message_handler(state="Как используем дом?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_target = message.text
    await state.update_data(client_target=client_target)
    await message.answer("Площадь?", reply_markup=square_keyboard)
    await state.set_state("Площадь?")


@dp.message_handler(state="Площадь?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_square = message.text
    await state.update_data(client_square=client_square)
    await message.answer("Сколько комнат?", reply_markup=count_room_keyboard)
    await state.set_state("Сколько комнат?")

@dp.message_handler(state="Сколько комнат?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    count_room = message.text
    await state.update_data(count_room=count_room)
    await message.answer("Комплектация?", reply_markup=equipment_keyboard)
    await state.set_state("Комплектация?")


@dp.message_handler(state="Комплектация?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    equipment = message.text
    await state.update_data(equipment=equipment)
    await message.answer("Проект?", reply_markup=project_keyboard)
    await state.set_state("Проект?")


@dp.message_handler(state="Проект?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    project = message.text
    await state.update_data(project=project)
    await message.answer("Бюджет?", reply_markup=budget_keyboard)
    await state.set_state("Бюджет?")



@dp.message_handler(state="Бюджет?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    budget = message.text
    await state.update_data(budget=budget)
    await message.answer("Способ оплаты?", reply_markup=payment_method_keyboard)
    await state.set_state("Способ оплаты?")


@dp.message_handler(state="Способ оплаты?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    payment_method = message.text
    await state.update_data(payment_method=payment_method)
    await message.answer("Нужна ли консультация по ипотеке?", reply_markup=mortgage_advice_keyboard)
    await state.set_state("Нужна ли консультация по ипотеке?")


@dp.message_handler(state="Нужна ли консультация по ипотеке?")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    mortgage_advice = message.text
    today = datetime.date.today()
    await state.update_data(mortgage_advice=mortgage_advice)
    data = await state.get_data()

    await message.answer(f"1. {message.from_user.full_name}\n"
                         f"2. {today.strftime('%d.%m.%y')}\n"
                         f"3. {data.get('client_name')}\n"
                         f"4. {data.get('client_phone_number')}\n"
                         f"5. {data.get('client_location')}\n"
                         f"6. {data.get('client_interesting')}\n"
                         f"7. {data.get('client_target')}\n"
                         f"8. {data.get('client_square')}\n"
                         f"9. {data.get('count_room')}\n"
                         f"10. {data.get('equipment')}\n"
                         f"11. {data.get('project')}\n"
                         f"12. {data.get('budget')}\n"
                         f"13. {data.get('payment_method')}\n"
                         f"14. {data.get('mortgage_advice')}\n",
                         reply_markup=menu)
    await state.reset_state()
    spreadsheet_id = '1hocu-OWJdIDiTmy1WlteqprXhYPn7sIKkNUi8vdjXfQ'
    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(PATH))  # импорт из конфига
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)

    worksheet = await async_spreadsheet.worksheet('Опросник выставка лето 2023')
    values = [message.from_user.full_name, today.strftime('%d.%m.%y'), data.get('client_name'),
              data.get('client_phone_number'), data.get('client_location'),data.get('client_interesting'),
              data.get('client_target'), data.get('client_square'), data.get('count_room'),
              data.get('equipment'), data.get('project'), data.get('budget'), data.get('payment_method'),
              data.get('mortgage_advice')]
    await worksheet.append_row(values)
