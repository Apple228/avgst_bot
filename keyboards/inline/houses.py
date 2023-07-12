from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

houses = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Барн L",
                                          callback_data="Барн L"
                                      ),
                                      InlineKeyboardButton(
                                          text="Финляндия M",
                                          callback_data="Финляндия M"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Модульный 49",
                                          callback_data="Модульный 49"
                                      ),
                                      InlineKeyboardButton(
                                          text="Модульная Дом-Баня",
                                          callback_data="Модульная Дом-Баня"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Прованс XL",
                                          callback_data="Прованс XL"
                                      ),
                                      InlineKeyboardButton(
                                          text="Шведский 3",
                                          callback_data="Шведский 3"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Шведский L",
                                          callback_data="Шведский L"
                                      ),
                                      InlineKeyboardButton(
                                          text="Финляндия XL",
                                          callback_data="Финляндия XL"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Финляндия L",
                                          callback_data="Финляндия L"
                                      ),
                                      InlineKeyboardButton(
                                          text="Норвегия L",
                                          callback_data="Норвегия L"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text = "Шведский M",
                                          callback_data="Шведский M"
                                      ),
                                      InlineKeyboardButton(
                                          text = "Барн XL",
                                          callback_data="Барн XL"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text = "Модульный 38",
                                          callback_data = "Модульный 38"
                                      ),
                                      InlineKeyboardButton(
                                          text = "Норвегия XL",
                                          callback_data="Норвегия XL"
                                      )
                                  ]


                              ])
