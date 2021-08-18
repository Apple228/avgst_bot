from aiogram import types
from aiogram.types import MediaGroup

from loader import dp


@dp.message_handler(text="Фото Прованс 28")
async def sendMediaGroup(message: types.Message):
    album = MediaGroup()
    files =["AgACAgIAAxkBAAId1WENDLt9r74xm_zlpiJ-HjXrghE7AAILtjEbl3BQSP8xF850UNgUAQADAgADeQADIAQ",
            'AgACAgIAAxkBAAId12ENDOsgzPDgUpZ_YST3UbpYzisNAAIJtjEbl3BQSEWM64rgLwy_AQADAgADeQADIAQ',
            "AgACAgIAAxkBAAId2WENDPfwEWMVLLmjKIUp2Cl1Q37ZAAIItjEbl3BQSM1YC72KZWTaAQADAgADeQADIAQ",
            "AgACAgIAAxkBAAId22ENDQK308iecu3VhLtq9Xb8tcz7AAIHtjEbl3BQSDujxyM1393yAQADAgADeQADIAQ",
            "AgACAgIAAxkBAAId3WENDUTJO_azVIaREIERoWSd_pblAAIGtjEbl3BQSJj1yiNELJLFAQADAgADeQADIAQ",
            "AgACAgIAAxkBAAId32ENDVOLw_d63Yi9xu-uQZ8sBeslAAIFtjEbl3BQSL1_9wRhfSGjAQADAgADeQADIAQ",
            "AgACAgIAAxkBAAId4WENDWWrTPC3VtREnkJImsHgs1RlAAK7tzEb0cpYSD9Y_OfEKoqbAQADAgADeQADIAQ",
            "AgACAgIAAxkBAAId42ENDXCmIj5m5U12cGkZfNu2L951AAIDtjEbl3BQSKGycDN7oR8fAQADAgADeQADIAQ",
            "AgACAgIAAxkBAAId5WENDX-tcWhBIA2hrCv1svF6G34dAAK8tzEb0cpYSK0_cLfSbCntAQADAgADeQADIAQ",
            "AgACAgIAAxkBAAId52ENDYsjA-H99b-dFo8N6nfqmgVjAAIBtjEbl3BQSIzsmHYpM__1AQADAgADeQADIAQ",
            # "AgACAgIAAxkBAAIL4GELp9VI11vpDmql3F2d8B4J2_krAAICtjEbl3BQSEgvXsFsUUopAQADAgADeQADIAQ",
            # "AgACAgIAAxkBAAIL4mELp99LKOu7P2qnBtegDUkfgWMPAAK9tzEb0cpYSM3DHll21HkqAQADAgADeQADIAQ",
            # "AgACAgIAAxkBAAIL5GELp-7F_dcCqrOg-yTDxWrFhbUtAAK-tzEb0cpYSP9Tlrif-N8HAQADAgADeQADIAQ",
            # "AgACAgIAAxkBAAIL5mELqAcIqTgxEXAtox4fEqVW_gH1AAK_tzEb0cpYSEig4E4_3bjKAQADAgADeQADIAQ",
            ]
    for file in files:
        album.attach_photo(file)
    await message.answer_media_group(media=album)


@dp.message_handler(text="Проект Прованс 28")
async def sendInfoProect(message: types.Message):
    await message.answer(""" Дачные дома с отделкой без коммуникаций:
На сваях - 2мес.
На ростверке - 2,5мес.
На плите - 3мес.
Дачные дома с коммуникациями 
Внутренние коммуникации +1мес.
Наружные коммуникации +0,5 мес.
Электрика + 0,5 мес.
Чистовые отделки + 1 мес. ( ламинат, плитка, натяжные потолки, обои, металлические лестницы)
Покраска 3го слоя +0,5мес.

Жилой дом без отделки размерами 6*8, 8*8 без учёта террас и крылечек: 
На сваях - 3мес.
На ростверке - 3,5мес.
На плите - 4мес.

Жилой дом с отделкой размерами 6*8, 8*8 без учёта террас и крылечек: 
На сваях - 3мес.
На ростверке - 3,5мес.
На плите - 4мес.
Внутренние коммуникации +1мес.
Наружные коммуникации +0,5 мес.
Электрика + 0,5 мес.
Чистовые отделки + 1 мес. ( ламинат, плитка, натяжные потолки, обои, металлические лестницы)
Покраска 3го слоя +0,5 мес.

Жилой дом без отделки, размерами до 10*10  без учёта террас и крылечек: 
На сваях - 3мес.
На ростверке - 3,5мес.
На плите - 4мес.

Жилой дом с отделкой, размерами до 10*10  без учёта террас и крылечек: 
На сваях - 4мес.
На ростверке - 4,5мес.
На плите - 5мес.
Внутренние коммуникации +1мес.
Наружные коммуникации +0,5 мес.
Электрика + 0,5 мес.
 Чистовые отделки + 1 мес. ( ламинат, плитка, натяжные потолки, обои, металлические лестницы)
Покраска 3го слоя +1мес.

Жилой дом без отделки, размерами более чем 10*10 без учёта террас и крылечек: 
На сваях - 4мес.
На ростверке - 4,5мес.
На плите - 5мес.

Жилой дом с отделкой, размерами более чем 10*10 без учёта террас и крылечек: 
На сваях - 5мес.
На ростверке - 6мес.
На плите - 6,5мес.
Внутренние коммуникации +1мес.
Наружные коммуникации +0,5 мес.
Электрика + 0,5 мес.
 Чистовые отделки + 1 мес. ( ламинат, плитка, натяжные потолки, обои, металлические лестницы)
Покраска 3го слоя +1мес.""")