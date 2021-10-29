from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

numbers = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="0")
        ],
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2")
        ],
        [
            KeyboardButton(text="3"),
            KeyboardButton(text="4")
        ]
    ],
    resize_keyboard=True
)