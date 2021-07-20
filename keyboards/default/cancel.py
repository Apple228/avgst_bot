from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Отмена")
        ]

    ],
    resize_keyboard=True
)
