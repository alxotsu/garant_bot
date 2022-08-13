from os import environ

DATABASE_URL = environ["DATABASE_URL"]
BOT_TOKEN = environ["TOKEN"]
ADMIN_FIRST_CHAT_ID = int(environ["ADMIN_1"])
ADMIN_SECOND_CHAT_ID = int(environ.setdefault("ADMIN_2", environ["ADMIN_1"]))
BOT_CHAT_LINK = environ["BOT_CHAT_LINK"]
INSTRUCTION = environ["INSTRUCTION_LINK"]
ADMIN_USERNAME = environ["ADMIN_USERNAME"]
PERCENT = int(environ["PERCENT"])
QIWI_ID = environ["QIWI_ID"]
QIWI_TOKEN = environ["QIWI_TOKEN"]

REPLENISH = (
    "⚠️ Пополнение баланса\n\n"
    "🥝 Qiwi \n\n"
    f"👉 Номер(Qiwi) - <b><code>{QIWI_ID}</code>\n"
    "👉 Коментарий - <code>{code}</code></b>\n"
    "👉 До 15 000 рублей!"
)

