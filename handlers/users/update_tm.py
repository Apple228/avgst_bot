import logging
import re
from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.types import CallbackQuery

from keyboards.default import menu, cancel

from keyboards.inline.task_inline import task
from loader import dp, db, tm
from states import Id


# @dp.message_handler(text="📊Новая задача")
# async def get_name(message: types.Message):
#     await message.answer("Пришли имя и фамилию сотрудника, для которого будет поставлена задача",
#                          reply_markup=cancel)
#     await Id.name_id.set()


@dp.message_handler(state=Id.name_id)
async def search_name(message: types.Message, state: FSMContext):
    name = message.text
    names = await db.select_full_name_id()  # SELECT full_name, telegram_id FROM Users
    user_data = list(names)
    count = await db.count_users()
    for i in range(0, count):
        if name == user_data[i][0]:
            await message.answer("Введите текст задачи")
            id_for = user_data[i][1]
            await state.update_data(id_for=id_for,
                                    name=user_data[i][0],
                                    reply_markup=cancel)  # если находим, то меняем стейт и идём в следующий хендлер
            await Id.next()
            break
    else:
        await message.answer("Такого человека нет в базе",
                             reply_markup=menu)  # если нет, то сбрасываем стейт, можно сделать возврат на предыдущий
        await state.reset_state()


@dp.message_handler(state=Id.id)
async def insert_task(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id_for = int(data.get("id_for"))

    task_for = data.get("name")

    await tm.add_task(task_for=task_for, task_for_telegram_id=id_for, task_from_telegram_id=message.from_user.id,
                      task_from=message.from_user.full_name, text_tasks=message.text, status="Задача поставлена")
    id_task = await tm.select_id()  # получаем id у задачи, которую только что поставили)))

    await dp.bot.send_message(id_for, f"{id_task[0]}.Поступила новая задача: {message.text}\n"
                                      f"Отправитель:{message.from_user.full_name}", reply_markup=task)

    await message.answer("Задача поставлена", reply_markup=menu)
    await state.reset_state()


@dp.callback_query_handler(text="completed")
async def task_completed(call: CallbackQuery, state: FSMContext):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы выполнили задачу", show_alert=True)
    text_message = call.message.text  # текст сообщения
    num = re.findall(r'\d+', text_message)
    num = [int(i) for i in num]
    task = await tm.task_for_user(id=num[0])  # task_for, task_from, task_from_telegram_id, text_task

    await tm.update_status(status="Выполнена✅", id=num[0])
    await call.message.edit_text(f"Задача:{task[3]} была выполнена ✅✅✅")
    await dp.bot.send_message(task[2], f"{task[0]} выполнил(а) задачy: \n"
                                       f"{task[3]} \n"
                                       f" ✅✅✅")
    # Вариант 1 - Отправляем пустую клавиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)

    # await state.update_data(task_for=task[0], task_from=task[1],
    #                         task_from_telegram_id=task[2], text_task=task[3])


@dp.callback_query_handler(text="not_completed")
async def task_not_completed(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы не выполнили задачу", show_alert=True)
    text_message = call.message.text  # текст сообщения, его потом редактируем исполнителя таски
    num = re.findall(r'\d+', text_message)
    num = [int(i) for i in num]
    task = await tm.task_for_user(id=num[0])  # task_for, task_from, task_from_telegram_id, text_tasks
    await tm.update_status(status="Не выполнена❌", id=num[0])
    await call.message.edit_text(f"Задача:{task[3]} была не выполнена ❌❌❌")
    await dp.bot.send_message(task[2], f"{task[0]} не выполнил(а) задачy: \n"
                                       f"{task[3]} \n"
                                       f"❌❌❌")
    # Вариант 1 - Отправляем пустую клавиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(text="📥Входящие")
async def get_task_for_user(message: types.Message):
    tasks = await tm.tasks_for_user(
        task_for_telegram_id=message.from_user.id)  # id, task_for, task_from, text_tasks, status
    t = list(tasks)
    count = len(t)
    for i in range(count):
        await message.answer(f"{t[i][0]}.Для:{t[i][1]} От:{t[i][2]} \n"
                             f"Текст: {t[i][3]}\n"
                             f"Статус: {t[i][4]}", reply_markup=task)
    await message.answer(f"Всего {count} задач" + (
        '' if count % 10 == 0 or 4 < count % 10 < 10 or 10 < count % 100 < 15 else 'и'
        if 1 < count % 10 < 5 else 'а'), reply_markup=menu)


@dp.message_handler(text="📤Исходящие")
async def get_task_for_user(message: types.Message):
    # id, task_for, task_from, text_tasks, status
    tasks = await tm.tasks_from_user(task_from_telegram_id=message.from_user.id)
    t = list(tasks)
    count = len(t)
    for i in range(count):
        await message.answer(f"{t[i][0]}.Для:{t[i][1]} От:{t[i][2]} \n"
                             f"Текст: {t[i][3]}\n"
                             f"Статус: {t[i][4]}", reply_markup=task)
    await message.answer(f"Всего {count} задач" + (
        '' if count % 10 == 0 or 4 < count % 10 < 10 or 10 < count % 100 < 15 else 'и'
        if 1 < count % 10 < 5 else 'а'), reply_markup=menu)
