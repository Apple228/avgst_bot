from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

video_list = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text="3D туры",
                                              callback_data="3D туры"
                                          ),
                                          InlineKeyboardButton(
                                              text="Видео домов",
                                              callback_data="Видео домов"
                                          )
                                      ]

                                  ])

tyr3DBarn10_keyboard = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text="Барн 10",
                                                        callback_data="Барн 10 3D тур"
                                                    ),
                                                ]

                                            ])

houses_video = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Прованс 24",
                                                callback_data="Прованс 24 видео"
                                            )
                                        ]

                                    ])
