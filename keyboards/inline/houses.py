from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
houses = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text="Прованс 28",
                                        callback_data="Прованс 28"
                                    ),
                                    InlineKeyboardButton(
                                        text="Шведский 28",
                                        callback_data="Шведский 28"
                                    ),
                                    InlineKeyboardButton(
                                        text="Шведский 24",
                                        callback_data="Шведский 24"
                                    ),
                                    InlineKeyboardButton(
                                        text="Прованс 6",
                                        callback_data="Прованс 6"
                                    )
                                ]
                            ])


