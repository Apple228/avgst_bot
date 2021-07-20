# import logging
#
# from aiogram import types
# from aiogram.types import CallbackQuery
#
# from data.config import HR_SUPPORT
# from keyboards.default import cancel, menu
# from keyboards.inline.reference import reference
# from loader import dp
#
#
#
# @dp.message_handler(text="📄Заказать справку")
# async def hr_support(message: types.Message):
#     await message.answer("Выберите услугу из меню ниже", reply_markup=reference)
#     # await It_support.name_id.set()
#
#
# @dp.callback_query_handler(text="doc_3")
# async def download_3NDFL(call: CallbackQuery):
#     file_id = "BQACAgIAAxkBAAIRjmCbpM_9S94QzHjS8HuBprPWcUuzAAKcCwAC5-HYSGpw39ufffVwHwQ"
#     id = call.from_user.id
#     await dp.bot.send_document(chat_id=id, document=file_id)
