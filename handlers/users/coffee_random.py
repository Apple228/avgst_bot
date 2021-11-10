import random
# from pytrovich.enums import NamePart, Gender, Case
# from pytrovich.maker import PetrovichDeclinationMaker

from aiogram import types
from aiogram.types import CallbackQuery

from data.config import ALL_TG_ID, USER_GSHEETS
from keyboards.inline.coffee import coffee
from loader import dp, db

random_user_which_coffee = 0
random_user_makes_coffee = 0


@dp.message_handler(text="Кофе")
async def coffee_random_choice(message: types.Message):
    global random_user_which_coffee
    random_user_which_coffee = random.choice(ALL_TG_ID)
    # random_user_which_coffee = random.choice(USER_GSHEETS)
    await dp.bot.send_message(random_user_which_coffee, "Доброе утро!\nСегодня тебе повезло и у тебя есть возможность "
                                                        "получить кофе, который будет сделан случайно выбранным человеком "
                                                        "после нажатия на кнопку!", reply_markup=coffee)


@dp.callback_query_handler(text="Кофе")
async def coffee_random_choice_2(call: CallbackQuery):
    global random_user_makes_coffee
    global random_user_which_coffee
    random_user_makes_coffee = random.choice(ALL_TG_ID)
    fullname_user_which_coffee = await db.select_full_name(telegram_id=random_user_which_coffee)
    # firstname, lastname = fullname_user_which_coffee.split()
    # print(firstname)
    # print(lastname)
    # maker = PetrovichDeclinationMaker()
    # print(maker.make(NamePart.FIRSTNAME, Gender.MALE, Case.GENITIVE, "Алексей"))
    # print(maker.make(NamePart.LASTNAME, Gender.MALE, Case.GENITIVE, "Лазарев"))
    await dp.bot.send_message(random_user_makes_coffee,
                              text=f"Доброе утро!\nУдача выбрала тебя и поэтому тебе нужно сделать кофе "
                                   f"для {fullname_user_which_coffee}. Возможно завтра напиток будут делать тебе :)")
    await dp.bot.send_message(624523030, f"{random_user_makes_coffee} для {fullname_user_which_coffee}")
