from telebot import types

from models import queries
from handlers import next_step_hadlers
from app.bot import bot
from app import config
from app import functions
from app import keyboards


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    chat_id = message.chat.id
    if message.from_user.username is None:
        bot.send_message(
            chat_id, "⛔️ Вам необходимо установить Имя пользователя для работы с ботом."
        )
    else:
        user = queries.new_user(chat_id)
        info = functions.check_user_blocks(user)
        if info is not None:
            bot.send_message(chat_id, info)
            return
        bot.send_message(
            chat_id,
            f"✅ Добро пожаловать, {message.from_user.first_name}!",
            reply_markup=keyboards.menu,
        )


@bot.message_handler(commands=["admin"])
def start(message: types.Message):
    if functions.check_admin_permission(message.chat.id):

        user = queries.get_user(message.chat.id)
        if user is not None:
            info = functions.check_user_blocks(user)
            if info is not None:
                bot.send_message(message.chat.id, info)
                return

        bot.send_message(
            message.chat.id,
            f"✅ {message.from_user.first_name}, вы авторизованы.",
            reply_markup=keyboards.admin,
        )


@bot.message_handler(content_types=["text"])
def send_text(message):
    chat_id = message.chat.id
    user = queries.new_user(chat_id)
    try:
        info = functions.check_user_blocks(user)
        if info is not None:
            bot.send_message(chat_id, info)
            return

        if message.text.lower() == "👤 профиль":
            bot.send_message(
                chat_id,
                f"🧾 Профиль:\n\n"
                f"❕ Ваш ChatID - <b><code>{user.chat_id}</code></b>\n"
                f"❕ Проведенных сделок - {len(user.customer_offers) + len(user.seller_offers)}\n\n"
                f"💰 Ваш баланс - {user.balance} USDT\n"
                f"💳 Ваш адрес Metamask - {user.metamask_address if user.metamask_address is not None else 'Не указан'}",
                reply_markup=keyboards.profile,
                parse_mode="HTML",
            )

        elif message.text.lower() == "🔒 провести сделку":
            bot.send_message(
                chat_id, "В этой сделке вы...", reply_markup=keyboards.init_offer
            )

        elif message.text.lower() == "⭐️ о нас":
            bot.send_message(
                chat_id,
                f"По всем вопросам: @{config.ADMIN_USERNAME}\nНаш чат: {config.BOT_CHAT_LINK}\nИнструкция по использованию: {config.INSTRUCTION}",
            )

        elif message.text.lower() == "💵 прошедшие сделки":
            bot.send_message(
                chat_id,
                "Вывести ваши последние сделки где вы...",
                reply_markup=keyboards.show_offers,
            )

        elif message.text == "Бан-система":
            if not functions.check_admin_permission(message.chat.id):
                return
            bot.send_message(
                chat_id, text="Что вы хотите сделать?", reply_markup=keyboards.bou
            )

        elif message.text == "Рассылка":
            if not functions.check_admin_permission(message.chat.id):
                return
            msg = bot.send_message(
                chat_id=chat_id,
                text='Введите текст для рассылки.\n\nДля отмены напишите "-" без кавычек.',
            )
            bot.register_next_step_handler(
                msg, next_step_hadlers.send_message_for_all_users
            )

        elif message.text == "Статистика":
            if not functions.check_admin_permission(message.chat.id):
                return
            bot.send_message(
                chat_id=chat_id,
                text="❕ Информация:\n\n"
                f"❕ Пользователей в боте - {queries.get_all_users_count()}\n"
                f"❕ Проведено сделок - {queries.get_offers_count()}",
            )

        elif message.text == "Решение спора":
            if not functions.check_admin_permission(message.chat.id):
                return
            msg = bot.send_message(
                chat_id,
                text='Введите ID сделки.\n\nДля отмены введите "-" без кавычек.',
            )
            bot.register_next_step_handler(msg, next_step_hadlers.search_dispute)

    except Exception:
        bot.send_message(
            chat_id,
            "⛔️ Произошла ошибка. Повторите запрос.\n\n"
            f"Если проблема не решилась, обратитесь в поддержку: @{config.ADMIN_USERNAME}.",
        )
        raise
