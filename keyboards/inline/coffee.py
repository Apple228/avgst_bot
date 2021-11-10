from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

coffee = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="☕",
            callback_data="Кофе"
        )
    ]
])