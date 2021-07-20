from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.cancel_inline import cancel_inline

from loader import dp, db
from states import Id

cb_users = CallbackData("set", "name", "id")


async def inline_users():
    markup = InlineKeyboardMarkup(row_width=2)
    count = await db.count_users()
    users = await db.select_full_name_id()
    for i in range(count):
        markup.insert(
            InlineKeyboardButton(text=users[i][0], callback_data=cb_users.new(name=users[i][0], id=users[i][1]))
        )
    return markup


@dp.message_handler(text="📊Новая задача")
async def new_task(message: types.Message):
    markup = await inline_users()
    await message.answer(text="Выберите сотрудника", reply_markup=markup)


@dp.callback_query_handler(text="Назад", state="*")
async def new_task(call: CallbackQuery, state: FSMContext):
    markup = await inline_users()
    await state.reset_state()
    await call.message.edit_text(text="Выберите сотрудника")
    await call.message.edit_reply_markup(reply_markup=markup)


@dp.callback_query_handler(cb_users.filter())
async def set_name_for_task(call: CallbackQuery, callback_data: dict, state: FSMContext):
    name = callback_data.get("name")
    id_for = callback_data.get("id")

    await call.message.edit_text(text=f"Введите текст задачи для {name}. 📝📝📝 \n"
                                      f"Если передумали, то нажмите отмена. "
                                      f"Если хотите выбрать другого человека, то назад.")
    await call.message.edit_reply_markup(reply_markup=cancel_inline)

    await state.update_data(id_for=id_for,
                            name=name)  # если находим, то меняем стейт и идём в следующий хендлер
    await Id.id.set()


@dp.callback_query_handler(text="Отмена", state="*")
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Отменено")
    await state.reset_state()
