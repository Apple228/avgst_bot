from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="☎Контакты"),
            KeyboardButton(text="🏡Домики")
        ],
        [
            KeyboardButton(text="📢Объявление для всех"),
            KeyboardButton(text="💡Сделать опрос", request_poll=types.KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text="📊Новая задача"),
            KeyboardButton(text="📝Список задач")
        ],
        [
            KeyboardButton(text="📄Документы"),
            KeyboardButton(text="💻IT Поддержка"),

        ]
    ],
    resize_keyboard=True
)

incoming_and_outgoing = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📤Исходящие")
        ],
        [
            KeyboardButton(text="📥Входящие")
        ]

    ],
    resize_keyboard=True
)
