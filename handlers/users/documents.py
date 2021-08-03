from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.docs import docs, requisites, contract_Grishatkin, contract_Lifanov
from loader import dp


@dp.message_handler(text="📄Документы")
async def document(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=docs)


@dp.callback_query_handler(text="Реквизиты")
async def document(call: CallbackQuery):
    await call.message.edit_text(text="Вы находитесь в разделе реквизиты")
    await call.message.edit_reply_markup(reply_markup=requisites)


@dp.callback_query_handler(text="Реквизиты Гришаткин")
async def document(call: CallbackQuery):
    id = call.from_user.id
    file_id_1 = "BQACAgIAAxkBAAIVF2DLtt1gD4mwbWwFjlAUFr727U9-AAKsDQAC-dlZSno56K-grKY5HwQ"
    await dp.bot.send_document(chat_id=id, document=file_id_1)


@dp.callback_query_handler(text="Реквизиты Лифанов")
async def document(call: CallbackQuery):
    id = call.from_user.id
    file_id_1 = "BQACAgIAAxkBAAIVGWDLty3Rk25ZvHatdpPW9U3ua1SsAAKXDAACozVYSitVc_uPBkjUHwQ"
    await dp.bot.send_document(chat_id=id, document=file_id_1)


@dp.callback_query_handler(text="Договора Гришаткин")
async def document(call: CallbackQuery):
    await call.message.edit_text(text="Вы находитесь в договора Гришаткин")
    await call.message.edit_reply_markup(reply_markup=contract_Grishatkin)


@dp.callback_query_handler(text="Договора Лифанов")
async def document(call: CallbackQuery):
    await call.message.edit_text(text="Вы находитесь в договора Лифанов")
    await call.message.edit_reply_markup(reply_markup=contract_Lifanov)


@dp.callback_query_handler(text="Договор баня Гришаткин")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIVSmDLw_88E8QVcbccKPBwW3gk0SNQAAJvDAACozVYSo4Uw4gvMLZTHwQ"
    file_id_2 = "BQACAgIAAxkBAAIVTGDLxBuLv6Sr4qKm3LtnY530ZXHLAAJwDAACozVYSoAKT8aFQxSmHwQ"
    file_id_3 = "BQACAgIAAxkBAAIZDWDUOMMpiwh93PuyiiCmTXC5Xbj5AAJPDwAC4VWZSkxjDBikBDptHwQ"  # Приложение 4
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)
    await dp.bot.send_document(chat_id=id, document=file_id_3)


@dp.callback_query_handler(text="Договор дача Гришаткин")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIVUGDLxJPhaZbuKFje1mbty8zXuwaAAAJyDAACozVYSmWraMw1yI48HwQ"
    file_id_2 = "BQACAgIAAxkBAAIZDWDUOMMpiwh93PuyiiCmTXC5Xbj5AAJPDwAC4VWZSkxjDBikBDptHwQ"  # Приложение 4
    file_id_3 = "BQACAgIAAxkBAAIVVGDLxLzYBPrIDHO9KSkndN1Qo1F3AAJ0DAACozVYSuiqVERerMrtHwQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)
    await dp.bot.send_document(chat_id=id, document=file_id_3)


@dp.callback_query_handler(text="Договор дом без дроби Гришаткин")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIcy2EJjvP9X74Pzx9nfFcGWzDQONkcAAKXEAACKThISIgJWkTRxw1tIAQ"
    file_id_2 = "BQACAgIAAxkBAAIczWEJjxa6rxI9g47BATFfjkxYdxtLAAKYEAACKThISKRwk9GreA2SIAQ"
    file_id_3 = "BQACAgIAAxkBAAIcz2EJjzq-SrKarTZkOl7deqFhyvYpAAKZEAACKThISCvrlHHUMHzMIAQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)
    await dp.bot.send_document(chat_id=id, document=file_id_3)


@dp.callback_query_handler(text="Договор Коммуникации Гришаткин без")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIc0WEJj2dozuYsxkj-i2-3m7wT_mYcAAKaEAACKThISHHtVfHxBsIKIAQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)


@dp.callback_query_handler(text="Договор дом с дробью Гришаткин")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIc02EJj4nrEqKzTZYnfFTlb_IepbFxAAKbEAACKThISAJ_DAIkjc9NIAQ"
    file_id_2 = "BQACAgIAAxkBAAIc1WEJj55LUwVgoHtUeNXh7cysDHbOAAKcEAACKThISFShfRarrSd-IAQ"
    file_id_3 = "BQACAgIAAxkBAAIc12EJj7E-4SFTw-KUORj2XM4h37uMAAKdEAACKThISPG4hSNiUAtSIAQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)
    await dp.bot.send_document(chat_id=id, document=file_id_3)


@dp.callback_query_handler(text="Договор дом с дробью Лифанов")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIVfGDLxhaJCAO-ydyemxelzymE0x7qAAKFDAACozVYSh4jgrnNcDjoHwQ"
    file_id_2 = "BQACAgIAAxkBAAIZJ2DUOsvna8Ka8pDuxRR_03N_6Av6AAJQDwAC4VWZStb7H3XrH6qHHwQ"
    file_id_3 = "BQACAgIAAxkBAAIVgGDLxkBpbsGw0HWGsnBK0qdt86TpAAKHDAACozVYSk20eCP2_akHHwQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)
    await dp.bot.send_document(chat_id=id, document=file_id_3)


@dp.callback_query_handler(text="Договор дом без дроби Лифанов")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIVgmDLxquw-D3Q9Pfr4TssS_bRjS1zAAKIDAACozVYSq2qiR_SVvtWHwQ"
    file_id_2 = "BQACAgIAAxkBAAIZJ2DUOsvna8Ka8pDuxRR_03N_6Av6AAJQDwAC4VWZStb7H3XrH6qHHwQ"
    file_id_3 = "BQACAgIAAxkBAAIVhmDLxtBJB6CTj5iiLIxyeC06WTWHAAKKDAACozVYSgMpHjkWPF1CHwQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)
    await dp.bot.send_document(chat_id=id, document=file_id_3)


@dp.callback_query_handler(text="Договор дача Лифанов")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIViGDLxvLDA0ydiC6lp2j8DqVbouEwAAKLDAACozVYSg3Cf9vSh1ddHwQ"
    file_id_2 = "BQACAgIAAxkBAAIZDWDUOMMpiwh93PuyiiCmTXC5Xbj5AAJPDwAC4VWZSkxjDBikBDptHwQ"     # Приложение 4
    file_id_3 = "BQACAgIAAxkBAAIVjGDLxxK2W6ON3JBfW8DXx67veLgEAAKNDAACozVYSu9Ij1Cl8dzpHwQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)
    await dp.bot.send_document(chat_id=id, document=file_id_3)


@dp.callback_query_handler(text="Договор баня Лифанов")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIVjmDLxzVVMG_IQVj6ZPXRNQuwIpdqAAKODAACozVYShD-Fa3Sm5bEHwQ"
    file_id_2 = "BQACAgIAAxkBAAIZDWDUOMMpiwh93PuyiiCmTXC5Xbj5AAJPDwAC4VWZSkxjDBikBDptHwQ"     # Приложение 4
    file_id_3 = "BQACAgIAAxkBAAIVkmDLx09ljihjAR3fHQrvJUNS9rd1AAKQDAACozVYShhTMjsBPpFhHwQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)
    await dp.bot.send_document(chat_id=id, document=file_id_3)


@dp.callback_query_handler(text="Договор коммуникации Лифанов")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAIVlGDLx4EvAAH4Y9Eweqv1rm4kaMeFCwACfQwAAqM1WErus5akHG9V7R8E"

    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)


@dp.callback_query_handler(text="Акции")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAITv2C6DK2KwoVurYg3LffLT2aI2_KJAAK7CwACYQS4SefY9xzL12g9HwQ"
    file_id_2 = "BQACAgIAAxkBAAITwWC6DNaq5VMeKfLDZaMyj5vghUa2AAK8CwACYQS4SURtIvFzvqvfHwQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)


@dp.callback_query_handler(text="Регламенты")
async def document(call: CallbackQuery):
    file_id_1 = "BQACAgIAAxkBAAITxGC6D5S_l4Xe9fk2s8vbvki7JHpeAAK9CwACYQS4SS8yzqf5Z5TbHwQ"
    file_id_2 = "BQACAgIAAxkBAAITxmC6D6R17GKajKm6vQOKlo6G4SOJAAK-CwACYQS4SUBMHNBasUNkHwQ"
    file_id_3 = "BQACAgIAAxkBAAITyGC6D7JMmKzwkbG_YjfJuTWjRp2xAAK_CwACYQS4SccJcoY-gYkpHwQ"
    file_id_4 = "BQACAgIAAxkBAAITymC6D8XVkEKIP4XLT1tbMnMwsN7mAALACwACYQS4SQABmo0s9PobqR8E"
    file_id_5 = "BQACAgIAAxkBAAITzGC6D9LbpR96mWLdtw6c5t5KlE04AALBCwACYQS4Sckk16IirCUjHwQ"
    file_id_6 = "BQACAgIAAxkBAAITzmC6D-HcypY37w7_W6zFKGCK_v7qAALCCwACYQS4SXhDYHbv6rxEHwQ"
    id = call.from_user.id
    await dp.bot.send_document(chat_id=id, document=file_id_1)
    await dp.bot.send_document(chat_id=id, document=file_id_2)
    await dp.bot.send_document(chat_id=id, document=file_id_3)
    await dp.bot.send_document(chat_id=id, document=file_id_4)
    await dp.bot.send_document(chat_id=id, document=file_id_5)
    await dp.bot.send_document(chat_id=id, document=file_id_6)


@dp.callback_query_handler(text="Назад в документы")
async def document(call: CallbackQuery):
    await call.message.edit_text(text="Выберите раздел")
    await call.message.edit_reply_markup(reply_markup=docs)
