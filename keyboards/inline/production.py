from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

production_keyboard = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Фото с завода",
                                          callback_data="Фото с завода"
                                      ),
                                      InlineKeyboardButton(
                                          text="Сборка домов",
                                          callback_data="Сборка домов"
                                      ),
                                  ],


                              ])


