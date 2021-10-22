from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

update_birthday = InlineKeyboardMarkup(inline_keyboard=
    [
        InlineKeyboardButton(
            text="Ввести дату",
            callback_data="День рождения"
        )
    ])