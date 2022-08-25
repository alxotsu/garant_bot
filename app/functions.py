import re
from decimal import Decimal

from web3 import Web3
from web3.middleware import geth_poa_middleware

from app import config
from app.bot import bot
from models import queries


def check_admin_permission(chat_id):
    return chat_id in (config.ADMIN_FIRST_CHAT_ID, config.ADMIN_SECOND_CHAT_ID)


def check_user_blocks(user):
    if user.banned:
        return "⛔️ К сожалению, Вы получили блокировку!"
    if user.customer_deal is not None or user.seller_deal is not None:
        return "⛔️ Вы не можете взаимодействовать с ботом, пока не завершите сделку!"


def search_second_user(message):
    if message.text.startswith("-") or not message.text.isdigit():
        bot.send_message(message.chat.id, text="Отмена...")
        return

    if int(message.text) == message.chat.id:
        bot.send_message(message.chat.id, text="⛔️Нельзя начать сделку с самим собой.")
        return

    second_user = queries.get_user(int(message.text))
    if second_user is None:
        bot.send_message(
            message.chat.id, text="⛔️Пользователь с введённым ChatID не найден."
        )
        return

    if second_user.banned:
        bot.send_message(
            message.chat.id, text="⛔️Пользователь с введённым ChatID заблокирован."
        )
        return

    if second_user.customer_deal is not None or second_user.seller_deal is not None:
        bot.send_message(
            message.chat.id,
            text="⛔️Пользователь с введённым ChatID в данный момент уже участвует в сделке.",
        )
        return

    return second_user


def ban_or_unban_user(message, ban):
    if not check_admin_permission(message.chat.id):
        return
    if message.text.startswith("-") or not message.text.isdigit():
        bot.send_message(message.chat.id, text="Отмена...")
        return

    user = queries.get_user(int(message.text))
    if user is None:
        bot.send_message(
            message.chat.id, text="⛔️Пользователь с введённым ChatID не найден."
        )
        return
    user.banned = ban
    user.save()
    return True


def solve_dispute(message, customer_solve):
    if not check_admin_permission(message.chat.id):
        return
    if message.text.startswith("-") or not message.text.isdigit():
        bot.send_message(message.chat.id, text="Отмена...")
        return

    deal = queries.get_deal(int(message.text))
    if deal is None:
        bot.send_message(message.chat.id, text="⛔️Сделка не найдена. Отмена...")
        return
    if customer_solve:
        bot.send_message(deal.customer_id, "✅ Вердикт был вынесен в вашу пользу.")
        bot.send_message(deal.customer_id, "✅ Вердикт был вынесен в пользу покупателя.")
        bot.send_message(message.chat.id, "✅ Вердикт был вынесен в пользу покупателя.")
        deal.customer.balance += deal.amount
        deal.customer.save()
    else:
        bot.send_message(deal.customer_id, "✅ Вердикт был вынесен в пользу продавца.")
        bot.send_message(deal.customer_id, "✅ Вердикт был вынесен в вашу пользу.")
        bot.send_message(message.chat.id, "✅ Вердикт был вынесен в пользу продавца.")
        deal.seller.balance += deal.amount
        deal.seller.save()
    deal.delete()


def format_user_info(user):
    return (
        f"❕ ChatID - <b><code>{user.chat_id}</code></b>\n"
        f"❕ Имя пользователя - @{bot.get_chat(user.chat_id).username}\n"
        f"❕ Проведенных сделок - {len(user.customer_offers) + len(user.seller_offers)}"
    )


def format_deal_info(deal):
    seller_username = bot.get_chat(deal.seller.chat_id).username
    customer_username = bot.get_chat(deal.customer.chat_id).username

    return (
        f"№{deal.id}\n"
        f"❕ Покупатель - @{customer_username} (ChatID <b><code>{deal.customer_id}</code></b>)\n"
        f"❕ Продавец - @{seller_username} (ChatID <b><code>{deal.seller_id}</code></b>)\n"
        f"💰 Сумма сделки - {deal.amount} USDT\n"
        f"📊 Статус сделки - {deal.status.value}"
    )


def get_web3_remote_provider():
    web3 = Web3(Web3.HTTPProvider(config.METAMASK_NETWORK_LINK))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    web3.eth.default_account = config.METAMASK_ADDRESS
    web3.eth.account.privateKeyToAccount = config.METAMASK_PRIVATE_KEY

    return web3


def get_token_contract(web3, abi):
    addr = web3.toChecksumAddress(config.TOKEN_ADDRESS)
    return web3.eth.contract(address=addr, abi=abi)


def monitor_payments():
    pass


def process_withdrawal(withdrawal):
    pass


def is_wallet_amount(text):
    return bool(re.fullmatch(r"\d+(\.[0-9]{1,2})?", text))


def get_system_balance():
    web3 = get_web3_remote_provider()

    abi = [
        {
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "payable": False,
            "type": "function",
        }
    ]

    contract = get_token_contract(web3, abi)

    balance = contract.functions.balanceOf(config.METAMASK_ADDRESS).call()

    return Decimal(balance) / 10**18
