from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

gsheets_timer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Ввести данные",
                callback_data="Гугл таблица"
            )
        ],
        [
            InlineKeyboardButton(
                text="Всё по нулям",
                callback_data="Заполнить нулями"
            )
        ]
        # [
        #     InlineKeyboardButton(
        #         text="Напомнить через час",
        #         callback_data="через час"
        #     )
        # ]
    ]
)