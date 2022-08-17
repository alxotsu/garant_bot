from telebot import types

from models import queries
from models.models import Deal
from app import keyboards, functions
from app import config
from app.bot import bot
from handlers import next_step_hadlers

__all__ = ["register_bot_callback_handler"]


def register_bot_callback_handler(data: str):
    def wrapper(handler: callable):
        bot.register_callback_query_handler(handler, lambda call: call.data == data)
        return handler

    return wrapper


@register_bot_callback_handler("output")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    if user.metamask_address is None:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="⛔️ У Вас не указан адрес кошелька для вывода.",
            reply_markup=keyboards.change_metamask,
        )
    else:
        msg = bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=f"Ваш адрес Metamask - {user.metamask_address}\n"
            f"Баланс - {user.balance} рублей\n"
            f"Введите сумму для вывода. (Для отмены введите любую букву)",
        )
        bot.register_next_step_handler(msg, next_step_hadlers.output)


@register_bot_callback_handler("input")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    if user.metamask_address is None:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="⛔️ Вы должны указать адрес кошелька перед пополнением баланса.",
            reply_markup=keyboards.change_metamask,
        )
    else:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="⚠️ Пополнение баланса\n"
            "Чтобы пополнить баланс, отправьте желаемую сумму на кошелёк сервиса в Metamask.\n"
            "Ваш баланс будет пополнен автоматически.\n\n"
            f"👉 Адрес кошелька - <b><code>{config.METAMASK_ADDRESS}</code></b>\n\n"
            "⛔️Обратите внимание! Перевод должен осуществляться с того же кошелька, адрес которого указан в вашем профиле, иначе средства не зачислятся.",
            parse_mode="HTML",
        )


@register_bot_callback_handler("change_metamask")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text="📄 Введите адрес кошелька.\n\n" 'Для отмены напишите "-" без кавычек.',
    )
    bot.register_next_step_handler(msg, next_step_hadlers.change_metamask)


@register_bot_callback_handler("seller_offer_init")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Введите ChatID пользователя, с которым хотите провести сделку. \n\nДля отмены напишите "-" без кавычек.',
    )
    bot.register_next_step_handler(msg, next_step_hadlers.search_customer_for_init)


@register_bot_callback_handler("customer_offer_init")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Введите ChatID пользователя, с которым хотите провести сделку. \n\nДля отмены напишите "-" без кавычек.',
    )
    bot.register_next_step_handler(msg, next_step_hadlers.search_seller_for_init)


@register_bot_callback_handler("seller_offer_get")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)

    if len(user.seller_offers) == 0:
        bot.send_message(chat_id, text="⛔️ Сделок не обнаружено.")
        return

    text = ""
    for offer in user.seller_offers:
        username = bot.get_chat(offer.customer_id).username
        text += f"💠 C @{username} (ChatID - {offer.customer_id}) на сумму {offer.amount} рублей.\n\n"

    bot.send_message(chat_id, text=text)


@register_bot_callback_handler("customer_offer_get")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)

    if len(user.customer_offers) == 0:
        bot.send_message(chat_id, text="⛔️ Сделок не обнаружено.")
        return

    text = ""
    for offer in user.customer_offers:
        username = bot.get_chat(offer.seller_id).username
        text += f"💠 C @{username} (ChatID - {offer.seller_id}) на сумму {offer.amount} рублей.\n\n"

    bot.send_message(chat_id, text=text)


@register_bot_callback_handler("ban")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if not functions.check_admin_permission(chat_id):
        return

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Введите ChatID пользователя, которого нужно забанить. \n\nДля отмены напишите "-" без кавычек.',
    )
    bot.register_next_step_handler(msg, next_step_hadlers.ban_user)


@register_bot_callback_handler("unban")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if not functions.check_admin_permission(chat_id):
        return

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Введите ChatID пользователя, которого нужно разбанить. \n\nДля отмены напишите "-" без кавычек.',
    )
    bot.register_next_step_handler(msg, next_step_hadlers.unban_user)


@register_bot_callback_handler("customer_solve_dispute")
def callback_handler(call):
    chat_id = call.message.chat.id
    msg = bot.send_message(
        chat_id,
        text='Покупатель получит деньги, а сделка будет отменена.\nДля подтверждения введите ID сделки, для отмены введите "-" без кавычек',
    )
    bot.register_next_step_handler(msg, next_step_hadlers.customer_solve_dispute)


@register_bot_callback_handler("seller_solve_dispute")
def callback_handler(call):
    chat_id = call.message.chat.id
    msg = bot.send_message(
        chat_id,
        text='Продавец получит деньги, а сделка будет отменена.\nДля подтверждения введите ID сделки, для отмены введите "-" без кавычек.',
    )
    bot.register_next_step_handler(msg, next_step_hadlers.seller_solve_dispute)


@register_bot_callback_handler("proposal")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text="✅ Предложение о проведении сделки отправлено.",
        reply_markup=keyboards.cancel_deal,
    )

    user = queries.get_user(chat_id)
    deal = user.seller_deal or user.customer_deal
    if user.seller_deal:
        role = "покупатель"
        second_chat_id = deal.customer_id
    else:
        role = "продавец"
        second_chat_id = deal.seller_id

    bot.send_message(
        second_chat_id,
        text="✅ Вам отправлено предложение о сделке.",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    bot.send_message(
        second_chat_id,
        functions.format_user_info(user) + f"\n\n🔥 В этой сделке вы {role}.",
        reply_markup=keyboards.accept_deal,
        parse_mode="HTML",
    )


@register_bot_callback_handler("cancel_deal")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    user = queries.get_user(chat_id)
    deal = user.seller_deal or user.customer_deal

    if deal.status != Deal.Status.new:
        bot.send_message(
            chat_id, text="⛔️ Сделка уже начата, и не может быть отменена."
        )
        return

    bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text="⛔️ Сделка отменена."
    )
    deal.delete()


@register_bot_callback_handler("refuse_deal")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    user = queries.get_user(chat_id)
    deal = user.seller_deal or user.customer_deal
    if user.seller_deal:
        second_chat_id = deal.customer_id
    else:
        second_chat_id = deal.seller_id

    if deal.status != Deal.Status.new:
        bot.send_message(
            chat_id, text="⛔️ Сделка уже начата, и не может быть отменена."
        )
        return

    bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text="⛔️ Сделка отменена."
    )
    bot.edit_message_text(
        chat_id=second_chat_id, message_id=message_id, text="⛔️ Сделка отменена."
    )
    deal.delete()


@register_bot_callback_handler("reviews")
def callback_handler(call):
    chat_id = call.message.chat.id

    user = queries.get_user(chat_id)
    if user.seller_deal:
        second_chat_id = user.seller_deal.customer_id
    else:
        second_chat_id = user.customer_deal.seller_id

    reviews = queries.get_reviews(second_chat_id)

    if len(reviews) == 0:
        bot.send_message(chat_id=chat_id, text="⛔️ отзывов не обнаружено.")
        return
    text = "💠 " + "\n\n💠 ".join(reviews)
    bot.send_message(chat_id=chat_id, text=text)


@register_bot_callback_handler("accept_deal")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    user = queries.get_user(chat_id)
    deal = user.seller_deal or user.customer_deal
    deal.status = Deal.Status.open
    deal.save()

    bot.edit_message_text(
        chat_id=deal.customer_id,
        message_id=message_id,
        text=f"💰 Сделка {functions.format_deal_info(deal)}",
        reply_markup=keyboards.customer_panel,
    )
    bot.edit_message_text(
        chat_id=deal.seller_id,
        message_id=message_id,
        text=f"💰 Сделка {functions.format_deal_info(deal)}",
        reply_markup=keyboards.seller_panel,
    )
