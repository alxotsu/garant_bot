from models import queries
from app import functions
from app import keyboards
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
