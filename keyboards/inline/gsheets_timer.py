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
                text="Нихуя не работал",
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

gsheets_timer_finished_house = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Ввести данные",
                callback_data="Отдел готовых домов"
            )
        ],
        [
            InlineKeyboardButton(
                text="Нихуя не работал",
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