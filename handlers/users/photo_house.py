import os

from aiogram import types
from aiogram.types import MediaGroup, CallbackQuery, InputFile

from loader import dp


@dp.callback_query_handler(text="Барн M")
async def barnM(call: CallbackQuery):
    content = os.listdir('photo/houses/barnM/')
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False
    for file in content:
        if int(file.split(".")[0])<=10:
            album1.attach_photo(InputFile(path_or_bytesio=f'photo/houses/barnM/{file}'))
        elif 10<int(file.split(".")[0])<=20:
            album2.attach_photo(InputFile(path_or_bytesio=f'photo/houses/barnM/{file}'))
            have_album2 = True
        elif 20<int(file.split(".")[0])<=30:
            album3.attach_photo(InputFile(path_or_bytesio=f'photo/houses/barnM/{file}'))
            have_album3 = True
    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Барн L")
async def barnM(call: CallbackQuery):
    content = os.listdir('photo/houses/barnL/')
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False
    for file in content:
        if int(file.split(".")[0])<=10:
            album1.attach_photo(InputFile(path_or_bytesio=f'photo/houses/barnL/{file}'))
        elif 10<int(file.split(".")[0])<=20:
            album2.attach_photo(InputFile(path_or_bytesio=f'photo/houses/barnL/{file}'))
            have_album2 = True
        elif 20<int(file.split(".")[0])<=30:
            album3.attach_photo(InputFile(path_or_bytesio=f'photo/houses/barnL/{file}'))
            have_album3 = True
    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)



@dp.callback_query_handler(text="Прованс 28")
async def provans28(call: CallbackQuery):
    album = MediaGroup()
    files = ["AgACAgIAAxkBAAId1WENDLt9r74xm_zlpiJ-HjXrghE7AAILtjEbl3BQSP8xF850UNgUAQADAgADeQADIAQ",
             'AgACAgIAAxkBAAId12ENDOsgzPDgUpZ_YST3UbpYzisNAAIJtjEbl3BQSEWM64rgLwy_AQADAgADeQADIAQ',
             "AgACAgIAAxkBAAId2WENDPfwEWMVLLmjKIUp2Cl1Q37ZAAIItjEbl3BQSM1YC72KZWTaAQADAgADeQADIAQ",
             "AgACAgIAAxkBAAId22ENDQK308iecu3VhLtq9Xb8tcz7AAIHtjEbl3BQSDujxyM1393yAQADAgADeQADIAQ",
             "AgACAgIAAxkBAAId3WENDUTJO_azVIaREIERoWSd_pblAAIGtjEbl3BQSJj1yiNELJLFAQADAgADeQADIAQ",
             "AgACAgIAAxkBAAId32ENDVOLw_d63Yi9xu-uQZ8sBeslAAIFtjEbl3BQSL1_9wRhfSGjAQADAgADeQADIAQ",
             "AgACAgIAAxkBAAId4WENDWWrTPC3VtREnkJImsHgs1RlAAK7tzEb0cpYSD9Y_OfEKoqbAQADAgADeQADIAQ",
             "AgACAgIAAxkBAAId42ENDXCmIj5m5U12cGkZfNu2L951AAIDtjEbl3BQSKGycDN7oR8fAQADAgADeQADIAQ",
             "AgACAgIAAxkBAAId5WENDX-tcWhBIA2hrCv1svF6G34dAAK8tzEb0cpYSK0_cLfSbCntAQADAgADeQADIAQ",
             "AgACAgIAAxkBAAId52ENDYsjA-H99b-dFo8N6nfqmgVjAAIBtjБарнEbl3BQSIzsmHYpM__1AQADAgADeQADIAQ",
             # "AgACAgIAAxkBAAIL4GELp9VI11vpDmql3F2d8B4J2_krAAICtjEbl3BQSEgvXsFsUUopAQADAgADeQADIAQ",
             # "AgACAgIAAxkBAAIL4mELp99LKOu7P2qnBtegDUkfgWMPAAK9tzEb0cpYSM3DHll21HkqAQADAgADeQADIAQ",
             # "AgACAgIAAxkBAAIL5GELp-7F_dcCqrOg-yTDxWrFhbUtAAK-tzEb0cpYSP9Tlrif-N8HAQADAgADeQADIAQ",
             # "AgACAgIAAxkBAAIL5mELqAcIqTgxEXAtox4fEqVW_gH1AAK_tzEb0cpYSEig4E4_3bjKAQADAgADeQADIAQ",
             ]
    for file in files:
        album.attach_photo(file)
    await call.message.answer_media_group(media=album)
    await call.message.answer("Это Прованс 28")




@dp.callback_query_handler(text="Шведский 24")
async def Shvedskiy24(call: CallbackQuery):
    album = MediaGroup()
    files = ["AgACAgIAAxkBAAIobWFkY2zHKbi7FF93ikZzo3R8qtbrAAJ8tjEbljsoSxypZyEElosoAQADAgADeQADIQQ",
             'AgACAgIAAxkBAAIocWFkY6SraM8qiVw-2w2XXKiQEH36AAJftjEbYqEgSzwBIQgjA6FWAQADAgADeQADIQQ',
             "AgACAgIAAxkBAAIoc2FkY7R4yDxAYiEUXKFRrGYSGWKpAAJhtjEbYqEgSyLG7yiUh66wAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIodWFkY9BMg9EAAdt4Ap-VxYqKBTuWoQACYrYxG2KhIEvpVz9ap_EhGQEAAwIAA3kAAyEE",
             "AgACAgIAAxkBAAIod2FkY-Pm4n0pkNYXJYLR39JXk-SEAAJktjEbYqEgS8d6JcLTsyW3AQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIoeWFkY_k0x0Nh4p_Fzj2Z5s3QdtQHAAJltjEbYqEgS1k6hsSuy1omAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIoe2FkZA30xTeAK-zHsBljL6W74ZyaAAJmtjEbYqEgS2oWFMZaA_GbAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIofWFkZCN7c7EErSgqGaLfw6mgHM4lAAJotjEbYqEgSzhkDY7LqsBVAQADAgADeQADIQQ",
             # "AgACAgIAAxkBAAIoe2FkZA30xTeAK-zHsBljL6W74ZyaAAJmtjEbYqEgS2oWFMZaA_GbAQADAgADeQADIQQ",
             # "AgACAgIAAxkBAAIofWFkZCN7c7EErSgqGaLfw6mgHM4lAAJotjEbYqEgSzhkDY7LqsBVAQADAgADeQADIQQ",
             ]
    for file in files:
        album.attach_photo(file)
    await call.message.answer_media_group(media=album)
    await call.message.answer("Это Шведский 24")


@dp.callback_query_handler(text="Шведский 28")
async def Shvedskiy28(call: CallbackQuery):
    album1 = MediaGroup()
    file1 = ["AgACAgIAAxkBAAIof2FkZWSjWauvmw8lM3GB4J5qpzq6AAJutjEbYqEgS336YkRbiXHqAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIogWFkZXOhBMzGp8i_4Jy5N2g1FSJQAAJvtjEbYqEgS_ALyHpliMK-AQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIog2FkZYY67pfnlg_3L2LdZ1pYxCEkAAJwtjEbYqEgS1B0LF8PovR5AQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIohWFkZZ3nXwiQo_zPMVnGp-ggI4E2AAJxtjEbYqEgSwUOaYXRROYHAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIoh2FkZawmgBUJMzg3B9tWUlQBJciRAAJytjEbYqEgSymhLr0O7ufWAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIoiWFkZbs9Dn3h8UGUOE4tGAW-V8tVAAJztjEbYqEgS4F1TUQcfO4UAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIoi2FkZiGrUnbrteui4D7M5HeWsq3-AAJ2tjEbYqEgS52odU7FpZtMAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIojWFkZjDEZ4JBXGyqcXGjSrjxjAvtAAJ3tjEbYqEgS6IFjoCC9J1WAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIoj2FkZkN-NDfYjiTFccNGgRnGEF48AAJ5tjEbYqEgS4L9UoeH3JpfAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIokWFkZlfoIrLE5FLK6TLf8jdYk5lDAAJ6tjEbYqEgSyN2L4XhsYx_AQADAgADeQADIQQ"]
    for file in file1:
        album1.attach_photo(file)
    await call.message.answer_media_group(media=album1)
    album2 = MediaGroup()
    file2 = ["AgACAgIAAxkBAAIok2FkZmia3RXSzmKX783tXfJIHs_0AAJ7tjEbYqEgS6Hh3b-cGtpmAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIolWFkZnjhlVCILyJeYd-rKGcoZdBDAAJ8tjEbYqEgS0M5H-gJl7tsAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIol2FkZoq95blDxE4kkM-ox-BXuV2CAAJ-tjEbYqEgSzAHvI7RXp9rAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIomWFkZplUOZLjeeFYF7hSUuysCobjAAJ_tjEbYqEgS2SX0x025Ha-AQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIom2FkZq3FkMUgF_RXED_mrVlQRkRmAAKAtjEbYqEgS-W5kgWm2TBxAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIonWFkZrwyC__bDxiTA_jm35E15hO_AAKBtjEbYqEgS-jjERDh5jRaAQADAgADeQADIQQ"]
    for file in file2:
        album2.attach_photo(file)
    await call.message.answer_media_group(media=album2)
    await call.message.answer("Это Шведский 28")


@dp.callback_query_handler(text="Шведский 23")
async def Shvedskiy23(call: CallbackQuery):
    album = MediaGroup()
    fileswed23 = ["AgACAgIAAxkBAAIpXWFkdYYv-hbt4NBCBT1IGz366fXMAALEtjEbYqEgSxXKDls49PTpAQADAgADeQADIQQ",
                  "AgACAgIAAxkBAAIpX2FkdZiILHZNfn7LufdUFhDpdLSvAALFtjEbYqEgSzHUkX-zTlNkAQADAgADeQADIQQ",
                  "AgACAgIAAxkBAAIpYWFkdaxClvdya6aPF6ht1vY9MJoCAALGtjEbYqEgS_ft8ZUnWqc5AQADAgADeQADIQQ",
                  "AgACAgIAAxkBAAIpY2FkdcDJ8ytkCIJ4-Q9iuDJqKOFRAALHtjEbYqEgS7dTJ9UyCjsoAQADAgADeQADIQQ",
                  "AgACAgIAAxkBAAIpZWFkdc7nFG8QgPJwyBzNppmaxgdnAALJtjEbYqEgS-nqGMFsXTc2AQADAgADeQADIQQ",
                  "AgACAgIAAxkBAAIpZ2FkdeFAh7a70ckDnoK6Cqb9ZGWeAALKtjEbYqEgSzNPcaN0UmvGAQADAgADeQADIQQ",
                  "AgACAgIAAxkBAAIpaWFkdfREBNVKNNlTcXaXvPXRWL0UAALLtjEbYqEgS_HmCWSSbIMnAQADAgADeQADIQQ"]
    for file in fileswed23:
        album.attach_photo(file)
    await call.message.answer_media_group(media=album)
    await call.message.answer("Это Шведский 23")


@dp.callback_query_handler(text="Барн 7")
async def Barn7(call: CallbackQuery):
    album1 = MediaGroup()
    filebarn1 = ["AgACAgIAAxkBAAIvKmGD7YQpuJyEih_EjXCsMC9rSgZaAAIHuDEbaiMgSA-eUspdMzsuAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIvLGGD7aqn2bPebRjY1rN2b-4hAzM3AAIIuDEbaiMgSBPr_wLfjENkAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIvLmGD7b3bvnVaCq4HhzyybefVayb5AAIJuDEbaiMgSIdejg8BjWJyAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIvMGGD7eE5TAfL6QGOGDycuKmxLBhvAAIKuDEbaiMgSECACzoyL_DLAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIvMmGD7fELK-G8KJQ_fYSfrzFHB4H3AAILuDEbaiMgSOVxxsRNETNeAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIvNmGD7iy381wZ2m9VpK3vz9-X2zN6AAIOuDEbaiMgSJIiQgv0VcjWAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIvOGGD7kAVDExboSFYGCyOpaMPD4iMAAIPuDEbaiMgSPVkN3oFY3OVAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIvOmGD7lCTmyQJnFGSszkq2G_gPUNoAAIQuDEbaiMgSM1mQ5EkcvX6AQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIvPGGD7mGes6LHS3OEEVfcLsKIZpjKAAIRuDEbaiMgSL9pVNHN-E_BAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIvPmGD7nGiSgv3U_ezrhojl3b4GIBHAAISuDEbaiMgSF5gIKeW2QS9AQADAgADeQADIQQ"]
    for file in filebarn1:
        album1.attach_photo(file)
    await call.message.answer_media_group(media=album1)
    await call.message.answer("Это Барн 7 снаружи")

    album2 = MediaGroup()
    filebarn2 = ["AgACAgIAAxkBAAIo3WFkbjWV0uJipdpVXFtwEIacq4cKAAKYtjEbYqEgS2TO2qEBFozYAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo32Fkbkip9DyHsvVhHGMjH_NylkRxAAKatjEbYqEgS4LuZsb9P5LoAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo4WFkbmFWyX1xukb2DV8G7Slq77fkAAKbtjEbYqEgS33ICkHL7o0iAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo42FkbnQFW8uq6jGsrWF_tyhB8lVVAAKetjEbYqEgS_PcSWuTgvw1AQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo5WFkboQkaM3jRqI4yM5os-PGeeSfAAKftjEbYqEgS9oGwn1XKUpBAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo52Fkbpok2m6NW_EqwPlwSasJYJqbAAKgtjEbYqEgS1DCMWhZcTmkAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo6WFkbqy2nfz6ZywMpOYjGUCmooeWAAKhtjEbYqEgS-BAGDInrvA_AQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo62Fkbr2tFSVo7Mmah8ENttQYl7P_AAKitjEbYqEgS1oyeG4QotibAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo7WFkbtAFfROpMG35FfpIu-RMLSM0AAKjtjEbYqEgS0WDfjezyv-OAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo72FkbuUzBEYII3xR70JUPrWTaWbUAAKktjEbYqEgSxzKr_57ghWQAQADAgADeQADIQQ"]
    for file in filebarn2:
        album2.attach_photo(file)
    await call.message.answer_media_group(media=album2)
    album3 = MediaGroup()
    filebarn3 = ["AgACAgIAAxkBAAIo8WFkby2Ol6JRBNCMqbXa9CsKSVuUAAKltjEbYqEgS5WiG972sTAfAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo22FkbdWQsTMgvDMRBpCPAQEEQeGWAAKWtjEbYqEgS920OLE3iJmtAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo82Fkb0Ez73DUMteTrwMCWIFArfcPAAKmtjEbYqEgS549PfkRx9xjAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo9WFkb1AwsoGDOeDuMnTrDjLvPuq7AAKntjEbYqEgS8voV_BjjQPkAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIo92Fkb2BYseebDemFxdMEUTrPEcEpAAKotjEbYqEgSzTIYKQr7HgUAQADAgADeQADIQQ"]
    for file in filebarn3:
        album3.attach_photo(file)
    await call.message.answer_media_group(media=album3)
    await call.message.answer("Это Барн 7 внутри")


@dp.message_handler(text="Фото Прованс 28")
async def sendMediaGroup(message: types.Message):
    album = MediaGroup()
    files = ["AgACAgIAAxkBAAId1WENDLt9r74xm_zlpiJ-HjXrghE7AAILtjEbl3BQSP8xF850UNgUAQADAgADeQADIAQ",
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

@dp.callback_query_handler(text="Прованс 6")
async def Provans6(call: CallbackQuery):
    album1 = MediaGroup()
    fileProvans1 = ["AgACAgIAAxkBAAIqfGFmvePB92Co09jweJkZTBeKaiXDAAIpuDEbzR85S0XPxe9RB0IEAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIqfmFmvfilrNtp9fQ9nmyjL20f8QK6AAIquDEbzR85S21ix3V_ayzoAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIqgGFmvgu1MeFASPucW3RRsObsfbx6AAIruDEbzR85SyZxYnugzAABYQEAAwIAA3kAAyEE",
             "AgACAgIAAxkBAAIqgmFmvh1RqsUdlP41symjXNB4t9CQAAIsuDEbzR85SycYIoVQO32nAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIqhGFmvi20gMLfa8Rh6_FHF29pP3V_AAItuDEbzR85Sw26p62x5iLrAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIqhmFmvj-Ov4-PAm8VSxBeFOAgTD98AAIuuDEbzR85S3bqn9IlRdEOAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIqiGFmvlJtExdiSMFnnlbmO5pIZ_lKAAIwuDEbzR85S9-pGP83GuaJAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIqimFmvmME5qXw7X84INcFPRK-lhn8AAIxuDEbzR85S_7XjKVZshXqAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIqjGFmvnV6UyP1jCns-W7-nXlgksFkAAIzuDEbzR85S2Z_UOokaqrBAQADAgADeQADIQQ",
             "AgACAgIAAxkBAAIqjmFmvoU0MjmQH0Yn3hDuPB0PFoI9AAI0uDEbzR85S-tFx0QqCraeAQADAgADeQADIQQ"]
    for file in fileProvans1:
        album1.attach_photo(file)
    await call.message.answer_media_group(media=album1)

    album2 = MediaGroup()
    fileProvans2 = ["AgACAgIAAxkBAAIqkGFmv5I9lZGta5BOUi6VYSCFP74SAAI4uDEbzR85S7nvrv9xbB2_AQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIqkmFmv6yvaJfMQqsiDpQm-tWPsV_KAAI5uDEbzR85S410nkfBnmYeAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIqlGFmv7-P7ZfhxJI_hhOWNBxdiOeQAAI6uDEbzR85SzVz9Bwr3CR6AQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIqlmFmv89v5grmMXxfFtof26g0wNKHAAI-uDEbzR85S_U-nWk8-oGxAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIqmGFmv99WImlXdw91_qC5_NvQT6YSAAI_uDEbzR85SxOg7mwsffbjAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIqmmFmv_GWcrp8M4z9_xb5u6beHJ5yAAJBuDEbzR85S0OCb5nW42tcAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIqnGFmwAQQxAq73H1co2XroB6SnRYaAAJCuDEbzR85S-fAmwo0sG8tAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIqnmFmwBfUPTkDPjCfcZEYBL60F4DGAAJDuDEbzR85S0hUVQmSiqv-AQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAIqoGFmwCzn3YPh_XQMimCfT3yowH8AA0S4MRvNHzlLurwTRurInyMBAAMCAAN5AAMhBA"]
    for file in fileProvans2:
        album2.attach_photo(file)
    await call.message.answer_media_group(media=album2)
    await call.message.answer("https://www.youtube.com/watch?v=NvbMBwiftrY")
    await call.message.answer("Это Прованс 6")

@dp.callback_query_handler(text="Шведский 2")
async def Swedskiy2 (call: CallbackQuery):
    album1 = MediaGroup()
    fileSwed = ["AgACAgIAAxkBAAJlbmNPwB_rzUfGxI3QoYdmnJZtG1igAALjvzEbfbFwSvdWskTij8r5AQADAgADeQADKgQ",
                "AgACAgIAAxkBAAJlcGNPwEgGMfLCbvkAAUX6LF9I4YY_bQAC5L8xG32xcEq_o316is1ecgEAAwIAA3kAAyoE",
                "AgACAgIAAxkBAAJlcmNPwE6lVesP2PFpCKVafFsmNwAB5wAC5b8xG32xcErvKeJZ6mtsvQEAAwIAA3kAAyoE",
                "AgACAgIAAxkBAAJldGNPwFlghomk4jwg_lZ7WnsHg7u4AALmvzEbfbFwSjn0KpwHOcyKAQADAgADeQADKgQ",
                "AgACAgIAAxkBAAJldmNPwGaWqi5peoZisLry1C2Ec2knAALnvzEbfbFwSnvXbAcolPeTAQADAgADeQADKgQ",
                "AgACAgIAAxkBAAJleGNPwG8SV4o9zXjexuA4dSqzr1ipAALovzEbfbFwSgABBZIe41FhNgEAAwIAA3kAAyoE",
                "AgACAgIAAxkBAAJlemNPwHa-F_nrNPAt2euBteUPoNTEAALpvzEbfbFwSq1Ipn71PjJwAQADAgADeQADKgQ",
                "AgACAgIAAxkBAAJlfGNPwIFgnRbp7jeO4euZlefVVqeaAALrvzEbfbFwStLE3L_1lhihAQADAgADeQADKgQ",
    ]

    for file in fileSwed:
        album1.attach_photo(file)
    await call.message.answer_media_group(media=album1)
    await call.message.answer("Это Шведский 2")

@dp.callback_query_handler(text="Шведский 36")
async def Swedskiy36 (call: CallbackQuery):
    album1 = MediaGroup()
    fileSwed36 = ["AgACAgIAAxkBAAItpWF8AAH36InVMx0y58lFSGmMBo7D8gACz7UxG3l_4EsuTPu02Zqi6QEAAwIAA3kAAyEE",
                "AgACAgIAAxkBAAItp2F8ARSGtFonknv_pYvziX_L3ctvAALQtTEbeX_gS1uyIKj2El3TAQADAgADeQADIQQ",
                "AgACAgIAAxkBAAItqWF8AcDzOxnyYIFguCmeoUtclwd7AALRtTEbeX_gS7aekbMAAa7fswEAAwIAA3kAAyEE",
                "AgACAgIAAxkBAAItq2F8Afryr_NUrhCjpUI-boZjdBD-AALTtTEbeX_gS4TnkcU8oEFLAQADAgADeQADIQQ",
                "AgACAgIAAxkBAAItrWF8AhmjuiWlfn8ugOnF5menRxWvAALUtTEbeX_gS80j8mPUYTrvAQADAgADeQADIQQ",
                "AgACAgIAAxkBAAItr2F8Ai8v5IVI0ByFXJjcJHRrfwy4AALVtTEbeX_gS3NGMwF6U9N3AQADAgADeQADIQQ",
                "AgACAgIAAxkBAAItsWF8Akj6YL2h2vyuqZwyOSUWz5o9AALWtTEbeX_gSymY8kDebm5wAQADAgADeQADIQQ",
                "AgACAgIAAxkBAAIts2F8AmiAqr3Jg4XjWSqQaB67_3GLAALXtTEbeX_gS3c2xfBcpF2KAQADAgADeQADIQQ",
                "AgACAgIAAxkBAAIttWF8Ap3kgh4Q1r-rbY9Q4UtF8I5LAALZtTEbeX_gSxIrWa7NPuQUAQADAgADeQADIQQ",
                "AgACAgIAAxkBAAItt2F8Ar59nDDivhyb5S3UlpawfxS1AALatTEbeX_gS4eOGpu7qRH3AQADAgADeQADIQQ"]
    for file in fileSwed36:
        album1.attach_photo(file)
    await call.message.answer_media_group(media=album1)

    album2 = MediaGroup()
    fileSwed36_2 = ["AgACAgIAAxkBAAItuWF8AvdHBpOA7GmD1-EKlJOLgStoAALctTEbeX_gS2FWqn320hASAQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAItu2F8AwdjuHHe2pmFYpTNn8MNIPILAALdtTEbeX_gSyZx5WhebWd4AQADAgADeQADIQQ",
                 "AgACAgIAAxkBAAItvWF8Ax__cGRmBO03dtF_Xuy0h4BaAALetTEbeX_gS4S25HHl9i-4AQADAgADeQADIQQ"]
    for file in fileSwed36_2:
        album2.attach_photo(file)
    await call.message.answer_media_group(media=album2)

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

#
# @dp.callback_query_handler(text="Прованс 6")
# async def provans6(call: CallbackQuery):
#     await call.message.answer("https://www.youtube.com/watch?v=NvbMBwiftrY")


@dp.message_handler(text="Видео Прованс 6")
async def sendInfoProect(message: types.Message):
    await message.answer("https://www.youtube.com/watch?v=NvbMBwiftrY")


@dp.callback_query_handler(text="Модульная дом-баня")
async def provans28(call: CallbackQuery):
    album = MediaGroup()
    files = ["AgACAgIAAxkBAAJl3mNQ4n1oB17gh0TwmTn8t7NmpJwUAALUwjEbWFh4SufjtQYYCJ7wAQADAgADeQADKgQ",
             'AgACAgIAAxkBAAJl4GNQ4pTIwky5bT7cFxq0ssvZwEaEAALYwjEbWFh4SqZJpZ38OX74AQADAgADdwADKgQ',
             "AgACAgIAAxkBAAJl4mNQ4ptScZ7B7xW0JkgZSkACfySgAALWwjEbWFh4Ss8N5TSrRSZRAQADAgADdwADKgQ",
             "AgACAgIAAxkBAAJl5GNQ4qN15_B_525OrjEyyJkk3hmyAALXwjEbWFh4SvXcM2JDFpB7AQADAgADeQADKgQ",
             "AgACAgIAAxkBAAJl5mNQ4qkhiJgAAfKgnI-gqhVB7VTX7wAC1cIxG1hYeEoHZ8atoFQN4gEAAwIAA3cAAyoE",
             "AgACAgIAAxkBAAJl6GNQ4q-pYpoRph-tuIHNNyhaUffBAALbwjEbWFh4SqSNgNpFzuP9AQADAgADdwADKgQ",
             "AgACAgIAAxkBAAJl6mNQ4rW9KdhPHXe3EFIa5OGA_p3RAALZwjEbWFh4SmJYg9Ry-VBYAQADAgADdwADKgQ",
             "AgACAgIAAxkBAAJl7GNQ4rpSv2wm5qwkbZ8LGq7vEqFcAALcwjEbWFh4SuMP94CRVDI7AQADAgADdwADKgQ",
             "AgACAgIAAxkBAAJl7mNQ4sAoKNEBVjeh2fw-sgKDdCo1AALdwjEbWFh4Sr7VPvSzNZz-AQADAgADdwADKgQ",
             "AgACAgIAAxkBAAJl8GNQ4sUf27MDchxi3XSO4KQU5ar4AALawjEbWFh4StcJb4UaAmkKAQADAgADdwADKgQ",
             # "AgACAgIAAxkBAAIL4GELp9VI11vpDmql3F2d8B4J2_krAAICtjEbl3BQSEgvXsFsUUopAQADAgADeQADIAQ",
             # "AgACAgIAAxkBAAIL4mELp99LKOu7P2qnBtegDUkfgWMPAAK9tzEb0cpYSM3DHll21HkqAQADAgADeQADIAQ",
             # "AgACAgIAAxkBAAIL5GELp-7F_dcCqrOg-yTDxWrFhbUtAAK-tzEb0cpYSP9Tlrif-N8HAQADAgADeQADIAQ",
             # "AgACAgIAAxkBAAIL5mELqAcIqTgxEXAtox4fEqVW_gH1AAK_tzEb0cpYSEig4E4_3bjKAQADAgADeQADIAQ",
             ]
    for file in files:
        album.attach_photo(file)
    await call.message.answer_media_group(media=album)
    await call.message.answer("Это Модульная дом-баня")