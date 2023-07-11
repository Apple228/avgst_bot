from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

docs = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Реквизиты",
            callback_data="Реквизиты"
        ),
        InlineKeyboardButton(
            text="Регламент ОГД",
            callback_data="Регламент ОГД"
        )
    ],
    [
        InlineKeyboardButton(
            text="Договора Гришаткин",
            callback_data="Договора Гришаткин"
        ),
        InlineKeyboardButton(
            text="Договора Лифанов",
            callback_data="Договора Лифанов"
        )
    ],

])

requisites = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Реквизиты Гришаткин",
            callback_data="Реквизиты Гришаткин"
        ),
        InlineKeyboardButton(
            text="Реквизиты Лифанов",
            callback_data="Реквизиты Лифанов"
        ),
    ],
    [
        InlineKeyboardButton(
            text="Реквизиты АС Каркас",
            callback_data="Реквизиты АС Каркас"
        ),
        InlineKeyboardButton(
            text="Реквизиты Якущенко",
            callback_data="Реквизиты Якущенко"
        ),
    ],
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="Назад в документы"
        )
    ]
])

contract_Grishatkin = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Договора баня без дроби",
            callback_data="Договор баня Гришаткин без дроби"

        )
    ],
    [
        InlineKeyboardButton(
            text="Договора баня с дробью",
            callback_data="Договор баня Гришаткин с дробью"

        )
    ],
    [
        InlineKeyboardButton(
            text="Договор дача без дроби",
            callback_data="Договор дача Гришаткин без дроби"

        )
    ],
    [
        InlineKeyboardButton(
            text="Договор дача с дробью",
            callback_data="Договор дача Гришаткин с дробью"

        )
    ],
    [
        InlineKeyboardButton(
            text="Договор дом с дробью",
            callback_data="Договор дом с дробью Гришаткин"
        )
    ],
    [
        InlineKeyboardButton(
            text="Договор дом без дроби",
            callback_data="Договор дом без дроби Гришаткин"
        )
    ],
    [
        InlineKeyboardButton(
            text="Договор Коммуникации",
            callback_data="Договор Коммуникации Гришаткин"
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="Назад в документы"
        )
    ],

])

contract_Lifanov = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Договор баня",
            callback_data="Договор баня Лифанов"

        )
    ],
    [
        InlineKeyboardButton(
            text="Договор дача",
            callback_data="Договор дача Лифанов"

        )
    ],
    [
        InlineKeyboardButton(
            text="Договор дом с дробью",
            callback_data="Договор дом с дробью Лифанов"
        )
    ],
    [
        InlineKeyboardButton(
            text="Договор дом без дроби",
            callback_data="Договор дом без дроби Лифанов"
        )
    ],
    [
        InlineKeyboardButton(
            text="Договор коммуникации Лифанов",
            callback_data="Договор коммуникации Лифанов"
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="Назад в документы"
        )
    ]
])
