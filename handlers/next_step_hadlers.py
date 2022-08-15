from app.bot import bot
from app import functions
from app import keyboards
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
            f"❕ Покупатель - ID{deal.customer_id}(@{customer_username})\n"
            f"❕ Продавец - ID{deal.seller_id}(@{seller_username})\n"
            f"💰 Сумма сделки - {deal.amount} рублей\n"
            f"📊 Статус сделки - {deal.status.name}\n\nКто прав в данном споре?",
            reply_markup=keyboards.solve_dispute,
        )
