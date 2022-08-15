from os import environ

DATABASE_URL = environ["DATABASE_URL"]
BOT_TOKEN = environ["TOKEN"]
ADMIN_FIRST_CHAT_ID = int(environ["ADMIN_1"])
ADMIN_SECOND_CHAT_ID = int(environ.setdefault("ADMIN_2", environ["ADMIN_1"]))
BOT_CHAT_LINK = environ["BOT_CHAT_LINK"]
INSTRUCTION = environ["INSTRUCTION_LINK"]
ADMIN_USERNAME = environ["ADMIN_USERNAME"]
PERCENT = int(environ["PERCENT"])
METAMASK_ADDRESS = environ["METAMASK_ADDRESS"]
QIWI_TOKEN = environ["QIWI_TOKEN"]

if PERCENT >= 100:
    raise Exception("Комиссия за вывод не может быть выше 100%")
