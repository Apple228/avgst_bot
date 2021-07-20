from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

task = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text="✅",
                                        callback_data="completed"
                                    ),
                                    InlineKeyboardButton(
                                        text="❌",
                                        callback_data="not_completed"
                                    )
                                ]
                            ])





