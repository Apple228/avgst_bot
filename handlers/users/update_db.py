import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from aiogram.utils.markdown import hcode

from keyboards.default import contact_buttons, menu, cancel
from loader import dp, db


@dp.message_handler(Command("username"))
async def change_username(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне свой новый username")
    await state.set_state("username")

@dp.message_handler(state="username")
async def enter_username(message: types.Message, state: FSMContext):
    await db.update_user_username(username=message.text, telegram_id=message.from_user.id)
    user = await db.select_user(telegram_id=message.from_user.id)
    user = dict(user)
    await message.answer("Данные обновлены. Запись в БД:\n" +
                         hcode(f"{user=}"))
    await state.reset_state()


@dp.message_handler(Command("email"))
async def update_user_email(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне свой новый email")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    await db.update_user_email(email=message.text, telegram_id=message.from_user.id)
    await state.reset_state()
    await message.answer("Твой email сохранён")


@dp.message_handler(Command("number"))
async def share_number(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}.\n"
                         f"передай свой номер, нажав кнопку ниже",
                         reply_markup=contact_buttons.phone_number)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    phone_number = contact.phone_number
    await db.update_user_phone_number(phone_number=phone_number, telegram_id=message.from_user.id)
    # user = await db.select_user(id=message.from_user.id)
    await message.answer(f"Спасибо, {contact.full_name}.\n"
                         f"Твой номер {contact.phone_number} был получен.\n"
                         f"Рекомендуется ввести свою почту командой /email",
                         reply_markup=menu)


@dp.message_handler(text="📢Объявление для всех")
async def ad(message: types.Message, state: FSMContext):
    await message.answer("Введите текст объявления", reply_markup=cancel)
    await state.set_state("ad")


@dp.message_handler(state="ad")
async def enter_ad(message: types.Message, state: FSMContext):
    users_id = await db.select_all_telegram_id()
    count = await db.count_users()
    for i in range(0, count):
        logging.info(users_id[i][0])
        await dp.bot.send_message(users_id[i][0], f"{message.from_user.full_name} делает объявление: \n"
                                                  f"{message.text}")
    await message.answer("Объявление сделано!", reply_markup=menu)
    await state.reset_state()

