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
