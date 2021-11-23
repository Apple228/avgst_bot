from environs import Env
import pathlib
from pathlib import Path

# Теперь вместо библиотеки python-dotenv библиотека environs

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IT_SUPPORT = env.list("IT_SUPPORT")
# HR_SUPPORT = env.list("HR_SUPPORT")
# PATH = r'C:\Users\aleks\PycharmProjects\MultiLevelMenu\creds.json'
PATH = Path(pathlib.Path.cwd(), 'creds.json')

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
# USER_GSHEETS = [624523030, 1257825667]

DEPARTMENT_OF_READY_HOUSES = [364700552, 1062255366, 1014182764, 96908874]#96908874, новая таблица
SALES_DEPARTMENT = [226606977, 1009851780, 706556502, 549911734, 1970286517] # старая


USER_GSHEETS2 = [226606977, 1009851780, 706556502, 549911734, 1970286517]
# я, Меркушев, Саша, Николаев, Цветков, Инишев, Дёмин

ALL_TG_ID = [1970286517, 226606977,364700552,96908874,549911734,1062255366,
             706556502,545084722,1209926925,314120760, 1009851780]

TEST_COFEE = [624523030, 1257825667]