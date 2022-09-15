from decimal import Decimal

from telebot import types
from web3.exceptions import TransactionNotFound

from app.bot import bot
from app import functions
from app import config
from app import keyboards
from models import queries, Deal


def ban_user(message):
    if functions.ban_or_unban_user(message, True):
        bot.send_message(message.chat.id, text="✅ Пользователь успешно забанен.")


def unban_user(message):
    if functions.ban_or_unban_user(message, False):
        bot.send_message(message.chat.id, text="✅ Пользователь успешно разбанен.")


def customer_solve_dispute(message):
    functions.solve_dispute(message, True)


def seller_solve_dispute(message):
    functions.solve_dispute(message, False)


def send_message_for_all_users(message):
    if not functions.check_admin_permission(message.chat.id):
        return

    if message.text == "-":
        bot.send_message(message.chat.id, text="Отмена...")
    else:
        users = queries.get_all_users()
        bot.send_message(message.chat.id, text="✅ Идёт рассылка...")
        count_all = 0
        count_success = 0
        for user in users:
            count_all += 1
            if message.chat.id == user.chat_id:
                continue
            try:
                bot.send_message(user.chat_id, message.text)
                count_success += 1
            except:
                pass
        bot.send_message(
            message.chat.id,
            text="✅ Рассылка завершена.\n"
            f"Сообщение получили {count_success} из {count_all} зарегистрированных пользователей.",
        )


def search_dispute(message):
    if not functions.check_admin_permission(message.chat.id):
        return

    if message.text.startswith("-") or not message.text.isdigit():
        bot.send_message(message.chat.id, text="Отмена...")
    else:
        deal = queries.get_deal(int(message.text))
        if deal is None:
            bot.send_message(message.chat.id, text="⛔️ Сделка не обнаружена!")
            return
        bot.send_message(
            message.chat.id,
            text=f"🧾 Информация о сделке "
            + functions.format_deal_info(deal)
            + f"\n\nКто прав в данном споре?",
            reply_markup=keyboards.solve_dispute,
            parse_mode="HTML",
        )


def output(message):
    if not functions.is_wallet_amount(message.text):
        bot.send_message(message.chat.id, text="Отмена...")
        return

    user = queries.get_user(message.chat.id)
    output_size = Decimal(message.text)

    if output_size > user.balance:
        bot.send_message(
            message.chat.id, text="⛔️ На балансе недостаточно средств для вывода!"
        )
        return

    if float(output_size) < 1:
        bot.send_message(
            message.chat.id,
            text="⛔️ Минимальная сумма для вывода 1 USDT",
        )
        return

    user.balance -= output_size
    user.save()
    bot.send_message(message.chat.id, text="✅ Запрос на вывод успешно отправлен!")
    queries.new_withdrawal(user.chat_id, user.metamask_address, output_size)


def register_transaction_hash(message):
    if message.text.startswith("-"):
        bot.send_message(message.chat.id, text="Отмена...")
        return

    hash_str = message.text[2:]

    if queries.get_transaction(hash_str) is not None:
        bot.send_message(
            message.chat.id, text="Эта транзакция уже была зарегистрирована в боте."
        )
        return

    web3 = functions.get_web3_remote_provider()
    try:
        transaction = web3.eth.get_transaction(bytes.fromhex(hash_str))
    except TransactionNotFound:
        bot.send_message(message.chat.id, text="Транзакция с таким ID не найдена.")
        return

    abi = [
        {
            "constant": False,
            "inputs": [
                {"name": "to", "type": "address"},
                {"name": "value", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "type": "function",
        }
    ]
    contract = functions.get_token_contract(web3, abi)
    transaction_info = contract.decode_function_input(transaction.input)[1]

    if transaction_info["to"] != config.SYSTEM_WALLET_ADDRESS:
        bot.send_message(
            message.chat.id, text="Перевод был совершён не на кошелёк сервиса."
        )
        return

    user = queries.get_user(message.chat.id)
    amount = Decimal(str(transaction_info["value"] / 10**18))
    queries.new_transaction(hash_str, user.chat_id, amount)
    user.balance += amount
    user.save()
    bot.send_message(
        message.chat.id, text=f"Баланс был успешно пополнен на {amount} USDT."
    )


def change_metamask(message):
    if message.text.startswith("-"):
        bot.send_message(message.chat.id, text="Отмена...")
        return

    user = queries.get_user(message.chat.id)
    user.metamask_address = message.text
    user.save()
    bot.send_message(message.chat.id, text="✅ Metamask установлен")


def search_seller_for_init(message):
    second_user = functions.search_second_user(message)

    if second_user is None:
        return

    queries.new_deal(message.chat.id, second_user.chat_id)

    bot.send_message(
        message.chat.id,
        "🧾 Профиль:\n\n"
        + functions.format_user_info(second_user)
        + "\n\n🔥В этой сделке вы будете покупателем.",
        reply_markup=keyboards.sentence_deal,
        parse_mode="HTML",
    )
    bot.send_message(
        chat_id=message.chat.id,
        text="Отключение клавиатуры...",
        reply_markup=types.ReplyKeyboardRemove(),
    )


def search_customer_for_init(message):
    second_user = functions.search_second_user(message)

    if second_user is None:
        return

    queries.new_deal(second_user.chat_id, message.chat.id)

    bot.send_message(
        message.chat.id,
        "🧾 Профиль:\n\n"
        + functions.format_user_info(second_user)
        + "\n\n🔥В этой сделке вы будете продавцом.",
        reply_markup=keyboards.sentence_deal,
        parse_mode="HTML",
    )
    bot.send_message(
        chat_id=message.chat.id,
        text="Отключение клавиатуры...",
        reply_markup=types.ReplyKeyboardRemove(),
    )


def set_price(message):
    if message.text.startswith("-") or not functions.is_wallet_amount(message.text):
        bot.send_message(message.chat.id, text="Отмена...")
        return

    deal = queries.get_user(message.chat.id).seller_deal
    if deal.amount != 0:
        return

    deal.amount = float(message.text)
    deal.save()

    bot.send_message(
        deal.seller_id,
        text=f"💥 Сумма сделки успешно изменена.\n\n💰 Сделка {functions.format_deal_info(deal)}",
        reply_markup=keyboards.seller_panel,
        parse_mode="HTML",
    )
    bot.send_message(
        deal.customer_id,
        text=f"💥 Была изменена сумма сделки.\n\n💰 Сделка {functions.format_deal_info(deal)}",
        reply_markup=keyboards.customer_panel,
        parse_mode="HTML",
    )


def add_review(message):
    deal = queries.get_user(message.chat.id).customer_deal
    if deal.status != Deal.Status.review:
        return

    if message.text == "-":
        bot.send_message(message.chat.id, text="Отмена...")
        review = None
        bot.send_message(
            deal.seller_id,
            text="❄️ Покупатель отказался оставлять отзыв.",
            reply_markup=keyboards.menu,
        )
        bot.send_message(
            chat_id=deal.customer_id,
            text="❄️ Сделка успешно завершена!",
            reply_markup=keyboards.menu,
        )
    else:
        review = message.text

    offer = queries.new_offer(deal, review)
    if review is not None:
        bot.send_message(
            message.chat.id,
            text="📝 Отзыв успешно оставлен.",
            reply_markup=keyboards.menu,
        )
        bot.send_message(
            offer.seller_id,
            text=f"📝 О вас оставили отзыв!\n\n{message.text}",
            reply_markup=keyboards.menu,
        )
