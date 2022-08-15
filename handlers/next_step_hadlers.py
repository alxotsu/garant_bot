from app.bot import bot
from app import functions
from app import keyboards
from app import config
from models import queries


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
        seller_username = bot.get_chat(deal.seller.chat_id).username
        customer_username = bot.get_chat(deal.customer.chat_id).username
        bot.send_message(
            message.chat.id,
            text=f"🧾 Информация о сделке №{deal.id}\n\n"
            f"❕ Покупатель - @{customer_username} (ChatID <b><code>{deal.customer_id}</code></b>)\n"
            f"❕ Продавец - @{seller_username} (ChatID <b><code>{deal.seller_id}</code></b>)\n"
            f"💰 Сумма сделки - {deal.amount} рублей\n"
            f"📊 Статус сделки - {deal.status}\n\nКто прав в данном споре?",
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
