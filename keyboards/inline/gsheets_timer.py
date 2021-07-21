from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

gsheets_timer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Ввести данные",
                callback_data="ввести данные в таблицу"
            )
        ],
        # [
        #     InlineKeyboardButton(
        #         text="Напомнить через час",
        #         callback_data="через час"
        #     )
        # ]
    ]
)