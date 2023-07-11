from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

photo_list = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text="Фото коммуникации",
                                              callback_data="Фото коммуникации"
                                          ),
                                          InlineKeyboardButton(
                                              text="Фото производства",
                                              callback_data="Фото производства"
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text="Фото посёлка",
                                              callback_data="Фото посёлка"
                                          ),
                                          InlineKeyboardButton(
                                              text="Фото домов",
                                              callback_data="Фото домов"
                                          ),
                                      ]

                                  ])
