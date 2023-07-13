import os

from aiogram.types import MediaGroup, CallbackQuery, InputFile

from loader import dp


@dp.callback_query_handler(text="Финляндия M")
async def barnM(call: CallbackQuery):
    path = 'photo/houses/finM/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Барн L")
async def barnM(call: CallbackQuery):
    path = 'photo/houses/barnL/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Модульный 49")
async def barnM(call: CallbackQuery):
    path = 'photo/houses/mod49/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Модульная Дом-Баня")
async def barnM(call: CallbackQuery):
    path = 'photo/houses/ModDom_ban/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)

@dp.callback_query_handler(text="Фото посёлка")
async def barnM(call: CallbackQuery):
    path = 'photo/Village/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)
    await call.message.answer('3D тур поселка https://6481fc89b9d3e315553d1233--frolicking-heliotrope-01e7ac.netlify.app/')


@dp.callback_query_handler(text="Фото посёлка")
async def barnM(call: CallbackQuery):
    path = 'photo/Village/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Наружные коммуникации")
async def barnM(call: CallbackQuery):
    path = 'photo/com/Comm_outside/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Электрика")
async def barnM(call: CallbackQuery):
    path = 'photo/com/Electricity/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Фото с завода")
async def barnM(call: CallbackQuery):
    path = 'photo/Фото_с_завода/фото_с_завода/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Отопление")
async def barnM(call: CallbackQuery):
    path = 'photo/com/Comm_WarmFloor/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Шведский L")
async def barnM(call: CallbackQuery):
    path = 'photo/houses/ShvedskiyL/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Прованс XL")
async def barnM(call: CallbackQuery):
    path = 'photo/houses/ProvansXL/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Шведский 3")
async def barnM(call: CallbackQuery):
    path = 'photo/houses/Шведский_3/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Финляндия XL")
async def barnM(call: CallbackQuery):
    path = 'photo/houses/FinXL/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    album4 = MediaGroup()
    have_album2 = False
    have_album3 = False
    have_album4 = False
    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True
        elif 30 < i <= 40:
            album4.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album4 = True
    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)
    if have_album4:
        await call.message.answer_media_group(media=album4)


@dp.callback_query_handler(text="Финляндия L")
async def barnM(call: CallbackQuery):
    path = 'photo/houses/FinL/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Сборка домов")
async def barnM(call: CallbackQuery):
    path = 'photo/Фото_с_завода/сборка_домов/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Норвегия L")
async def barnM(call: CallbackQuery):
    path = 'photo//houses/NorvL/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)



@dp.callback_query_handler(text="Шведский M")
async def shvedM(call: CallbackQuery):
    path = 'photo/houses/Shvedskiy M/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)

@dp.callback_query_handler(text="Барн XL")
async def barnXL(call: CallbackQuery):
    path = 'photo/houses/Barn XL/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)


@dp.callback_query_handler(text="Модульный 38")
async def mod38(call: CallbackQuery):
    path = 'photo/houses/Mod38/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)



@dp.callback_query_handler(text="Норвегия XL")
async def norvXL(call: CallbackQuery):
    path = 'photo/houses/Norv XL/'
    content = os.listdir(path)
    size = 0
    for file in content:
        if size < int(file.split(".")[0]):
            size = int(file.split(".")[0])
    album1 = MediaGroup()
    album2 = MediaGroup()
    album3 = MediaGroup()
    have_album2 = False
    have_album3 = False

    for i in range(1, size + 1):
        if i <= 10:
            album1.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
        elif 10 < i <= 20:
            album2.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album2 = True
        elif 20 < i <= 30:
            album3.attach_photo(InputFile(path_or_bytesio=f'{path}{i}.jpg'))
            have_album3 = True

    await call.message.answer_media_group(media=album1)
    if have_album2:
        await call.message.answer_media_group(media=album2)
    if have_album3:
        await call.message.answer_media_group(media=album3)