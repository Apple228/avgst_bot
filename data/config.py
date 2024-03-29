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
# DEPARTMENT_OF_READY_HOUSES = [624523030, 1257825667]
DEPARTMENT_OF_READY_HOUSES = [364700552, 772189661, 2074802977, 624523030] # новая таблица
SALES_DEPARTMENT = [1009851780, 706556502, 549911734,  624523030] # старая
#SALES_DEPARTMENT = [624523030, 1257825667] # старая

USER_GSHEETS2 = [ 1009851780, 706556502, 549911734, 1970286517]
# я, Саша, Николаев, Цветков, Инишев, Дёмин

ALL_TG_ID = [1970286517, 364700552,549911734,
             706556502,545084722,1209926925,314120760, 1009851780]

TEST_COFFEE = [624523030, 1257825667]