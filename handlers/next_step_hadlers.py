from telebot import types

from app.bot import bot
from app import functions
from app import keyboards
from app import config
from models import queries


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
    if not message.text.isdigit():
        bot.send_message(message.chat.id, text="Отмена...")
        return

    user = queries.get_user(message.chat.id)
    output_size = float(message.text)

    if output_size > user.balance:
        bot.send_message(
            message.chat.id, text="⛔️ На балансе недостаточно средств для вывода!"
        )
        return

    if float(output_size) < 10:
        bot.send_message(
            message.chat.id, text="⛔️ Минимальная сумма для вывода 10 рублей"
        )
        return

    amount = output_size * (1 - config.PERCENT / 100)
    queries.new_withdrawal(user.chat_id, user.metamask_address, amount)
    # TODO Добавить здесь фоновую задачу на вывод средств
    bot.send_message(message.chat.id, text="✅ Запрос на вывод успешно отправлен!")


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
    bot.send_message(chat_id=message.chat.id, reply_markup=types.ReplyKeyboardRemove())


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
    bot.send_message(chat_id=message.chat.id, reply_markup=types.ReplyKeyboardRemove())


def set_price(message):
    if message.text.startswith("-") or not message.text.isdigit():
        bot.send_message(message.chat.id, text="Отмена...")
        return

    deal = queries.get_user(message.chat.id).seller_deal
    if deal.amount != 0:
        return

    deal.amount = int(message.text)
    deal.save()

    bot.send_message(
        deal.seller_id,
        text=f"💥 Сумма сделки успешно изменена.\n\n💰 Сделка {functions.format_deal_info(deal)}",
        reply_markup=keyboards.seller_panel,
    )
    bot.send_message(
        deal.customer_id,
        text=f"💥 Была изменена сумма сделки.\n\n💰 Сделка {functions.format_deal_info(deal)}",
        reply_markup=keyboards.seller_panel,
    )
