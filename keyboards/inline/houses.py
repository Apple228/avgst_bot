from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
houses = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text="Барн 10",
                                        callback_data="Барн 10"
                                    ),
                                    InlineKeyboardButton(
                                        text="Барн M",
                                        callback_data="Барн M"
                                    ),
                                ],
                                [
                                    InlineKeyboardButton(
                                        text="Барн L",
                                        callback_data="Барн L"
                                    ),
                                    InlineKeyboardButton(
                                        text="Барн XL",
                                        callback_data="Барн XL"
                                    )
                                ],
                                [
                                    InlineKeyboardButton(
                                        text="Барн 7",
                                        callback_data="Барн 7"
                                    ),
                                    InlineKeyboardButton(
                                        text="Шведский 23",
                                        callback_data="Шведский 23"
                                    ),
                                ],
                                [
                                    InlineKeyboardButton(
                                        text="Шведский 2",
                                        callback_data="Шведский 2"
                                    ),
                                    InlineKeyboardButton(
                                        text="Модульная дом-баня",
                                        callback_data="Модульная дом-баня"
                                    ),
                                ],
                                [
                                    InlineKeyboardButton(
                                        text="Прованс 24",
                                        callback_data="Прованс 24"
                                    ),


                                    InlineKeyboardButton(
                                        text="Прованс 6",
                                        callback_data="Прованс 6"
                                    ),
                                ],
                                [
                                    InlineKeyboardButton(
                                        text="Шведский 3",
                                        callback_data="Шведский 3"
                                    ),


                                    InlineKeyboardButton(
                                        text="Премьер 4",
                                        callback_data="Премьер 4"
                                    ),
                                ]
                            ])


