from os import environ

DATABASE_URL = environ["DATABASE_URI"]
BOT_TOKEN = environ["TOKEN"]
ADMIN_FIRST_CHAT_ID = int(environ["ADMIN_1"])
ADMIN_SECOND_CHAT_ID = int(environ.setdefault("ADMIN_2", environ["ADMIN_1"]))
BOT_CHAT_LINK = environ["BOT_CHAT_LINK"]
INSTRUCTION = environ["INSTRUCTION_LINK"]
ADMIN_USERNAME = environ["ADMIN_USERNAME"]
PERCENT = int(environ["PERCENT"])
METAMASK_ADDRESS = environ["METAMASK_ADDRESS"]
METAMASK_PRIVATE_KEY = environ["METAMASK_PRIVATE_KEY"]
METAMASK_NETWORK_LINK = environ.setdefault(
    "METAMASK_NETWORK_LINK", "https://mainnet.infura.io/v3/"
)
TOKEN_ADDRESS = environ.setdefault(
    "TOKEN_ADDRESS", "0x55d398326f99059ff775485246999027b3197955"
)
GAS_COUNT = int(environ["GAS_COUNT"])

if PERCENT >= 100:
    raise Exception("Комиссия за вывод не может быть выше 100%")
