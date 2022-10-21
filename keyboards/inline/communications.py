from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

communications_keyboard = InlineKeyboardMarkup(row_width=2,
                                               inline_keyboard=[
                                                   [
                                                       InlineKeyboardButton(
                                                           text="Отопление",
                                                           callback_data="Отопление"
                                                       ),
                                                       InlineKeyboardButton(
                                                           text="Электрика",
                                                           callback_data="Электрика"
                                                       ),
                                                   ],
                                                   [
                                                       InlineKeyboardButton(
                                                           text="ВК",
                                                           callback_data="ВК"
                                                       ),
                                                       InlineKeyboardButton(
                                                           text="Вентиляция",
                                                           callback_data="Вентиляция"
                                                       )
                                                   ],
                                                   [
                                                       InlineKeyboardButton(
                                                           text="Наружные коммуникации",
                                                           callback_data="Наружные коммуникации"
                                                       ),

                                                   ],

                                               ])

heating_keyboard = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="Теплый пол",
                                                    callback_data="Теплый пол"
                                                ),
                                            ],

                                        ])
