import logging

from aiogram import types


from loader import dp, bot, db


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Начни что-то писать",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не обязательно жать при этом на кнопку",
                    parse_mode="HTML"
                ),
            ),
        ],

        cache_time=5)


@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    user = query.from_user.id
    allowed_users = await db.select_all_telegram_id()
    count = await db.count_users()
    list_allowed_users = []
    for i in range(count):
        list_allowed_users.append(allowed_users[i][0])
    if user not in list_allowed_users:
        await query.answer(
            results=[],
            switch_pm_text="Бот недоступен, поскольку вас нет в базе данных",
            switch_pm_parameter="connect_user",
            cache_time=5)
        return

    await query.answer(
        results=[
            types.InlineQueryResultCachedDocument(
                id="1",
                title="Реквизиты компании",
                document_file_id="BQACAgIAAxkBAAIVF2DLtt1gD4mwbWwFjlAUFr727U9-AAKsDQAC-dlZSno56K-grKY5HwQ",
                description="Реквизиты Гришаткин"
            ),
            types.InlineQueryResultCachedDocument(
                id="2",
                title="Реквизиты компании",
                document_file_id="BQACAgIAAxkBAAIVGWDLty3Rk25ZvHatdpPW9U3ua1SsAAKXDAACozVYSitVc_uPBkjUHwQ",
                description="Реквизиты Лифанов"
            ),
            # types.InlineQueryResultCachedDocument(
            #     id="3",
            #     title="Договор подряда Баня",
            #     document_file_id="BQACAgIAAxkBAAIX9GDM0unQ_IO8p_tBpp1Eh5OJ1dS6AAJvDAACozVYSo4Uw4gvMLZTHwQ",
            #     description="Договор баня Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="4",
            #     title="Приложение 3",
            #     document_file_id="BQACAgIAAxkBAAIX9mDM0xv9m4YtrGnr_nZUTVpEWbCzAAJwDAACozVYSoAKT8aFQxSmHwQ",
            #     description="Договор баня Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="5",
            #     title="Приложение 4",
            #     document_file_id="BQACAgIAAxkBAAIX-GDM00uHgV1S-cgwCfHteEs17HhiAAJxDAACozVYSjCONM59uPdGHwQ",
            #     description="Договор баня Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="6",
            #     title="Приложение 3",
            #     document_file_id="BQACAgIAAxkBAAIX-mDM03coJtzD1VR42L26IEXP4GHtAAJyDAACozVYSmWraMw1yI48HwQ",
            #     description="Договор дача Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="7",
            #     title="Приложение 4",
            #     document_file_id="BQACAgIAAxkBAAIX_GDM050ndk8KFnsqV5pvpgal7fnGAAJzDAACozVYShadzWqG6lX_HwQ",
            #     description="Договор дача Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="8",
            #     title="Договор подряда Садовый дом",
            #     document_file_id="BQACAgIAAxkBAAIX_mDM08gmjAkPeLb9qBSTVIwRSgNdAAJ0DAACozVYSuiqVERerMrtHwQ",
            #     description="Договор дача Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="9",
            #     title="Договор подряда жилой",
            #     document_file_id="BQACAgIAAxkBAAIYAAFgzNP_QvogXKm4LiLtzHp2mh1sMAACdQwAAqM1WEpu9YRkGUgLTB8E",
            #     description="Договор дом без дроби Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="10",
            #     title="Приложение 4",
            #     document_file_id="BQACAgIAAxkBAAIYAmDM1C_OhsDV7yLy8jIInKit6oS4AAJ2DAACozVYSmcelbeMBWKPHwQ",
            #     description="Договор дом без дроби Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="11",
            #     title="Приложение 5",
            #     document_file_id="BQACAgIAAxkBAAIYBGDM1Gu7xPqeJ89g_DHLNIpbKb7mAAJ3DAACozVYSoyF1FyI9sb5HwQ",
            #     description="Договор дом без дроби Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="13",
            #     title="Приложение 3",
            #     document_file_id="BQACAgIAAxkBAAITsWC6CpY9EtQWmrQn_XBICoU8ZdF1AAK2CwACYQS4SbqfWbDHO4_qHwQ",
            #     description="Договор дача без дроби"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="14",
            #     title="Приложение 4",
            #     document_file_id="BQACAgIAAxkBAAITs2C6CsNUpjHlyzZjekGGh8HOgIKZAAK3CwACYQS4SZ3ed1MWnqD6HwQ",
            #     description="Договор дача без дроби"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="15",
            #     title="Договор подряда жилой дом",
            #     document_file_id="BQACAgIAAxkBAAIYBmDM1JUtLeBLWm5fsplsAAF37sW1hQACeAwAAqM1WEo2bf__xjxe6x8E",
            #     description="Договор дом с дробью Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="16",
            #     title="Приложение 4",
            #     document_file_id="BQACAgIAAxkBAAIYCGDM1MIe9WAa9ocY3G1FPuNx5fnYAAJ5DAACozVYSs2dU_Dkau-EHwQ",
            #     description="Договор дом с дробью Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="17",
            #     title="Приложение 5",
            #     document_file_id="BQACAgIAAxkBAAIYCmDM1O6S9tDvDpkXi5rRAAGhnb7a7QACegwAAqM1WEpR0Q7fuRSEvB8E",
            #     description="Договор дом с дробью Гришаткин"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="18",
            #     title="Договор_подряда_коммуникации,_без",
            #     document_file_id="BQACAgIAAxkBAAIYDGDM1SDA9q45iDAh77RQ4cOk9_DEAAJ9DAACozVYSu6zlqQcb1XtHwQ",
            #     description="Договор коммуникации Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="19",
            #     title="Приложение 4",
            #     document_file_id="BQACAgIAAxkBAAIYDmDM1VgaCqns4kArhXiDj7XXkxmTAAKFDAACozVYSh4jgrnNcDjoHwQ",
            #     description="Договор дом с дробью Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="20",
            #     title="Приложение 5",
            #     document_file_id="BQACAgIAAxkBAAIYEGDM1Y6K6BjfPr7EVa1BMlAcfihfAAKGDAACozVYSs2Gocgs75hZHwQ",
            #     description="Договор дом с дробью Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="21",
            #     title="Договор подряда жилой дом белый",
            #     document_file_id="BQACAgIAAxkBAAIYEmDM1cShI9wAAbjWUl6yvxfzNaCiBQAChwwAAqM1WEpNtHgj9v2pBx8E",
            #     description="Договор дом с дробью Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="22",
            #     title="Приложение 4",
            #     document_file_id="BQACAgIAAxkBAAIYFGDM1i_TrR4O9xeJfhvQaLmijfcgAAKIDAACozVYSq2qiR_SVvtWHwQ",
            #     description="Договор дом без дроби Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="23",
            #     title="Приложение 5",
            #     document_file_id="BQACAgIAAxkBAAIYFmDM1mNuM-oDL-2hZ5tQo3EWtzYMAAKJDAACozVYSichb8zUSonIHwQ",
            #     description="Договор дом без дроби Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="24",
            #     title="Договор подряда жилой",
            #     document_file_id="BQACAgIAAxkBAAIYGGDM1ppcSCtqxhGRnuofhoO58HPlAAKKDAACozVYSgMpHjkWPF1CHwQ",
            #     description="Договор дом без дроби Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="25",
            #     title="Приложение 3",
            #     document_file_id="BQACAgIAAxkBAAIYGmDM1teIxoVsuSJ9jtE9p0bqnb02AAKLDAACozVYSg3Cf9vSh1ddHwQ",
            #     description="Договор дача Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="26",
            #     title="Приложение 4",
            #     document_file_id="BQACAgIAAxkBAAIYHGDM1v0JuX3-QPuyEhitnp4yxoGMAAKMDAACozVYSlgoeO2h8x0CHwQ",
            #     description="Договор дача Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="27",
            #     title="Договор подряда Садовый дом",
            #     document_file_id="BQACAgIAAxkBAAIYHmDM15S3-y14hPlC54F145w3Tl6jAAKNDAACozVYSu9Ij1Cl8dzpHwQ",
            #     description="Договор дача Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="28",
            #     title="Приложение 3",
            #     document_file_id="BQACAgIAAxkBAAIYIGDM1-HATdFh6R_f1WgQtQ2dVp-BAAKODAACozVYShD-Fa3Sm5bEHwQ",
            #     description="Договор баня Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="29",
            #     title="Приложение 4",
            #     document_file_id="BQACAgIAAxkBAAIYImDM2A_qj6bPUq98XTaunDDKT-t_AAKPDAACozVYSo3B1giE_2EcHwQ",
            #     description="Договор баня Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="30",
            #     title="Договор подряда  Баня",
            #     document_file_id="BQACAgIAAxkBAAIYJGDM2DIIB1l-tVoFz3QlAAEOn2_vwQACkAwAAqM1WEoYUzI7AT6RYR8E",
            #     description="Договор баня Лифанов"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="31",
            #     title="Акции ДАЧИ от 01.06.2021",
            #     document_file_id="BQACAgIAAxkBAAIYJmDM2VyluQABx13rfXBU07dUR7fG7gACuwsAAmEEuEnn2Pccy9doPR8E",
            #     description="Акции"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="32",
            #     title="Акции КАРКАС от 01.06.2021",
            #     document_file_id="BQACAgIAAxkBAAIYKGDM2ZRnOJRkpqaB_PG0V7qnKEzxAAK8CwACYQS4SURtIvFzvqvfHwQ",
            #     description="Акции"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="33",
            #     title="Регламент КАРКАС от 01.06.2021",
            #     document_file_id="BQACAgIAAxkBAAIYKmDM2cJSrAlBlOPOrzvlnkMy7psUAAK9CwACYQS4SS8yzqf5Z5TbHwQ",
            #     description="Регламент каркас"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="34",
            #     title="Регламент ДАЧИ от 01.06.2021",
            #     document_file_id="BQACAgIAAxkBAAIYLGDM2fRtZjN6JT9Q3fZhSBpMgy6mAAK-CwACYQS4SUBMHNBasUNkHwQ",
            #     description="Регламент дачи"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="35",
            #     title="Регламент ОЦБ и ПБ от 01.06.21",
            #     document_file_id="BQACAgIAAxkBAAIYLmDM2idiRG1r_ejPWZgW3fFh0-yJAAK_CwACYQS4SccJcoY-gYkpHwQ",
            #     description="Регламент ОЦБ"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="36",
            #     title="Регламент ОЦБ и ПБ от 01.06.21",
            #     document_file_id="BQACAgIAAxkBAAIYMGDM2nIDNbo7paxuj1esBmQb-SB4AALACwACYQS4SQABmo0s9PobqR8E",
            #     description="Регламент профбрус"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="37",
            #     title="ОЦБ и ПБ 2 этапы от 01.06.2021",
            #     document_file_id="BQACAgIAAxkBAAIYMmDM2sbZ_PqcFUV1QkiTWuFIxZCVAALBCwACYQS4Sckk16IirCUjHwQ",
            #     description="Регламент 2 этап"
            # ),
            # types.InlineQueryResultCachedDocument(
            #     id="38",
            #     title="Регламент Дома-бани",
            #     document_file_id="BQACAgIAAxkBAAIYNGDM2vtDynDSUV_FcZbldfpPVjP2AALCCwACYQS4SXhDYHbv6rxEHwQ",
            #     description="Регламент дома-бани"
            # ),
        ],
    )

