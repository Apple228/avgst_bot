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
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text="Видео с производства",
                                              callback_data="Видео с производства"
                                          ),
                                          InlineKeyboardButton(
                                              text="Видео посёлка",
                                              callback_data="Видео посёлка"
                                          )
                                      ],

                                  ])

tyr3DBarn10_keyboard = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text="Барн L",
                                                        callback_data="Барн L 3D тур"
                                                    ),
                                                    InlineKeyboardButton(
                                                        text="Барн XL",
                                                        callback_data="Барн XL 3D тур"
                                                    ),

                                                ]

                                            ])

houses_video = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Барн XL",
                                                callback_data="Барн XL видео"
                                            ),
                                            InlineKeyboardButton(
                                                text="Прованс 24",
                                                callback_data="Прованс 24 видео"
                                            ),
                                        ],

                                    ])
