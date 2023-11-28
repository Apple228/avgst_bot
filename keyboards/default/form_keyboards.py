from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [
                                             KeyboardButton(text="Запустить анкету"),
                                         ]
                                     ])

location_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [
                                                KeyboardButton(text="Московская область"),

                                            ]
                                        ])

interesting_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                           keyboard=[
                                               [
                                                   KeyboardButton(text="Готовый дом")
                                               ],
                                               [
                                                   KeyboardButton(text="Стройка, своя земля"),
                                                   KeyboardButton(text="Стройка, нет земли"),
                                               ]
                                           ])

planing_build_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                             keyboard=[
                                                 [
                                                     KeyboardButton(text="2023"),
                                                     KeyboardButton(text="1-я половина 2024"),
                                                 ],
                                                 [
                                                     KeyboardButton(text="2025"),
                                                     KeyboardButton(text="2-я половина 2024")
                                                 ]
                                             ])
target_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [
                                              KeyboardButton(text="ПМЖ"),
                                              KeyboardButton(text="Дача"),
                                          ]
                                      ])

square_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [
                                              KeyboardButton(text="50-100м2"),
                                              KeyboardButton(text="100-150м2")
                                          ],
                                          [
                                              KeyboardButton(text="150-200м2"),
                                              KeyboardButton(text="200+м2"),
                                          ]
                                      ])

count_room_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                          keyboard=[
                                              [
                                                  KeyboardButton(text="1"),
                                                  KeyboardButton(text="2"),

                                              ],
                                              [
                                                  KeyboardButton(text="3"),
                                                  KeyboardButton(text="4"),

                                              ]
                                          ])
equipment_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                         keyboard=[
                                             [
                                                 KeyboardButton(text="Базовая"),
                                                 KeyboardButton(text="Под ключ"),
                                             ],
                                             [
                                                 KeyboardButton(text="white box"),
                                             ]
                                         ])

project_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton(text="Барн L"),
                                               KeyboardButton(text="Норвегия L"),
                                               KeyboardButton(text="Норвегия XL"),
                                           ],
                                           [
                                               KeyboardButton(text="Финляндия XL"),
                                               KeyboardButton(text="Шведский L"),
                                           ],
                                           [
                                               KeyboardButton(text="Модульный 49"),
                                               KeyboardButton(text="Модульный 57"),
                                           ],


                                       ])

budget_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [
                                              KeyboardButton(text="до 5 млн"),
                                              KeyboardButton(text="до 10 млн"),
                                          ],
                                          [
                                              KeyboardButton(text="до 15 млн"),
                                              KeyboardButton(text="больше 15 млн"),
                                          ]

                                      ])
payment_method_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                              keyboard=[
                                                  [
                                                      KeyboardButton(text="Наличные"),
                                                      KeyboardButton(text="Ипотека"),
                                                  ],
                                                  [
                                                      KeyboardButton(text="Продажа квартиры")
                                                  ]
                                              ])
komplekt_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [KeyboardButton(text="Теплый контур(Премиум)"),
                                             KeyboardButton(text="WB")],
                                            [
                                                KeyboardButton(text="Под ключ")
                                            ]
                                        ])
comment_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton(text="Нет комментария"),

                                           ],
                                           [
                                               KeyboardButton(text="B2B"),
                                               KeyboardButton(text="Горячий"),
                                           ]

                                       ])
clent_from_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                          keyboard=[
                                              [
                                                  KeyboardButton(text="ВК"),
                                                  KeyboardButton(text="Inst"),
                                              ],
                                              [
                                                  KeyboardButton(text="Сайт поселка"),
                                                  KeyboardButton(text="Авито фейк")
                                              ]
                                          ])