from telebot import types

from bot import bot
import functions
import keyboards
import config
import var


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    chat_id = message.chat.id
    if message.from_user.username is None:
        bot.send_message(
            chat_id, "⛔️ Вам необходимо установить Имя пользователя для работы с ботом!"
        )
    else:
        functions.first_join(user_id=chat_id, username=message.from_user.username)
        bot.send_message(
            chat_id,
            f"✅ Добро пожаловать, {message.from_user.first_name}!",
            reply_markup=keyboards.menu,
        )


@bot.message_handler(commands=["admin"])
def start(message: types.Message):
    if message.chat.id in (config.ADMIN_FIRST_CHAT_ID, config.ADMIN_SECOND_CHAT_ID):
        bot.send_message(
            message.chat.id,
            f"✅ {message.from_user.first_name}, вы авторизованы!",
            reply_markup=keyboards.admin,
        )


@bot.message_handler(content_types=["text"])
def send_text(message):
    chat_id = message.chat.id
    try:
        info = functions.check_user_blocks(chat_id)
        if info:
            bot.send_message(chat_id, info)
            return

        if message.text.lower() == "👤 профиль":
            info = functions.profile(user_id=chat_id)
            bot.send_message(
                chat_id,
                f"🧾 Профиль:\n\n❕ Ваш id - <b><code>{info[0]}</code></b>\n❕ Проведенных сделок - {info[1]}\n\n💰 Ваш баланс - {info[2]} рублей\n💳 Ваш Qiwi - {info[3]}",
                reply_markup=keyboards.profile,
                parse_mode="HTML",
            )

        elif message.text.lower() == "🔒 провести сделку":
            bot.send_message(
                chat_id, "В этой сделке вы...", reply_markup=keyboards.choise_offer
            )

        elif message.text.lower() == "⭐️ о нас":
            bot.send_message(
                chat_id,
                f"По всем вопросам: @{config.ADMIN_USERNAME}\nНаш чат: {config.BOT_CHAT_LINK}\nИнструкция по использованию:  {config.INSTRUCTION}",
            )

        elif message.text.lower() == "💵 прошедшие сделки":
            bot.send_message(
                chat_id,
                "Вывести ваши последние сделки где вы...",
                reply_markup=keyboards.cors,
            )

    except Exception as e:
        print(e)
        bot.send_message(chat_id, var.ERROR)
        functions.first_join(user_id=chat_id, username=message.from_user.username)
