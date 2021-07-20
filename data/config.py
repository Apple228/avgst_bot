from environs import Env

# Теперь вместо библиотеки python-dotenv библиотека environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IT_SUPPORT = env.list("IT_SUPPORT")
# HR_SUPPORT = env.list("HR_SUPPORT")


DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")

