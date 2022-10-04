from os import environ

DATABASE_URL = environ["DATABASE_URI"]
BOT_TOKEN = environ["BOT_TOKEN"]
ADMIN_FIRST_CHAT_ID = int(environ["ADMIN_1"])
ADMIN_SECOND_CHAT_ID = int(environ.setdefault("ADMIN_2", environ["ADMIN_1"]))
BOT_CHAT_LINK = environ["BOT_CHAT_LINK"]
INSTRUCTION_LINK = environ["INSTRUCTION_LINK"]
ADMIN_EMAIL = environ["ADMIN_EMAIL"]
ADMIN_USERNAME = environ["ADMIN_USERNAME"]
TAX_PERCENT = float(environ["TAX_PERCENT"])
REFERRAL_TAX_SALE = float(environ["REFERRAL_TAX_SALE"])
REFERRAL_BONUS = float(environ["REFERRAL_BONUS"])
SYSTEM_WALLET_ADDRESS = environ["SYSTEM_WALLET_ADDRESS"]
SYSTEM_WALLET_PRIVATE_KEY = environ["SYSTEM_WALLET_PRIVATE_KEY"]
BLOCKCHAIN_RPC_LINK = environ["BLOCKCHAIN_RPC_LINK"]
BLOCKCHAIN_ID = int(environ["BLOCKCHAIN_ID"])
BLOCKCHAIN_TOKEN_ADDRESS = environ["BLOCKCHAIN_TOKEN_ADDRESS"]
OUTPUT_GAS_COUNT = int(environ["OUTPUT_GAS_COUNT"])
