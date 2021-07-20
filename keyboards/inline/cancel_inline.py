from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel_inline = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(
                                                 text="Отмена",
                                                 callback_data="Отмена"
                                             ),



                                             InlineKeyboardButton(
                                                 text="Назад",
                                                 callback_data="Назад"
                                             )
                                         ]
                                     ])
