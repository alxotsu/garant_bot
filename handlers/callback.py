from handlers import functions, keyboards, var
from app.bot import bot

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
    info = functions.profile(user_id=chat_id)
    if info[3] == "Не указан":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="⛔️ У Вас не указан кошелёк для вывода(Qiwi)!",
            reply_markup=keyboards.qiwi,
        )
    else:
        msg = bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Ваш Qiwi - {qiwi}\nБаланс - {balance} рублей\n\nВведите сумму для вывода. (Для отмены введите любую букву)".format(
                qiwi=info[3], balance=info[2]
            ),
        )
        bot.register_next_step_handler(msg, output)


@register_bot_callback_handler("qiwi_num")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("seller")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("customer")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("menu")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("bor")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("unban")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("ban")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("edit_balance")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("input")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("check_payment")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("cancel_payment")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("message")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("seller_offer")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("customer_offer")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("proposal_customer")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("proposal_seller")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("delete_customer")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("delete_seller")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("statistics")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("accept_customer")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("accept_seller")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("input_panel")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("price")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("cancel_open")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("No_cancel")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("Yes_cancel")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("Yes_cancel_seller")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("cancel_open_seller")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("Yes_cancel_seller1")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("No_cancel_seller1")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("No_cancel_seller")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("Yes_cancel_customer")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("No_cancel_customer")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("ok")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("ok_cancel")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("ok_ok")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("open_dispute")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("open_dispute_seller")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("dispute_admin")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("customer_true")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("seller_true")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("no_true")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("cancel_open_offer")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("cancel_open_offer_seller")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("reviews")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("add_review")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("up_login")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("no_review")
def callback_handler(call):
    chat_id = call.message.chat.id


@register_bot_callback_handler("cancel_wait")
def callback_handler(call):
    chat_id = call.message.chat.id
    try:
        info = functions.info_offers_seller(chat_id)
        if info[4] == "review":
            functions.close_offer_seller(chat_id)
            bot.send_message(
                chat_id,
                text="❄️ Ожидание отменено, покупатель не может больше оставить отзыв.",
                reply_markup=keyboards.menu,
            )
            bot.send_message(
                info[1],
                "Продавец не захотел ожидать отзыва. Сделка заверешна",
                reply_markup=keyboards.menu,
            )
        else:
            bot.send_message(chat_id, var.ERROR)
    except:
        bot.answer_callback_query(
            callback_query_id=call.id, show_alert=True, text=var.ERROR
        )

####################################


    elif call.data == "qiwi_num":
        msg = bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="📄 Введите номер в формате +70000000000",
        )
        bot.register_next_step_handler(msg, write_qiwi1)

    elif call.data == "seller":
        info = functions.last_offers_seller(chat_id)
        if len(info) > 0:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=info)
        elif len(info) == 0:
            bot.edit_message_text(
                chat_id=chat_id, message_id=message_id, text="⛔️ Сделок не обнаружено!"
            )

    elif call.data == "customer":
        info = functions.last_offers_customer(chat_id)
        if len(info) > 0:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=info)
        elif len(info) == 0:
            bot.edit_message_text(
                chat_id=chat_id, message_id=message_id, text="⛔️ Сделок не обнаружено!"
            )

    elif call.data == "menu":
        bot.edit_message_text(
            chat_id=call.message.chat.id, message_id=message_id, text="Главное меню"
        )

    elif call.data == "bor":
        bot.send_message(chat_id, text="Что вы хотите сделать?", reply_markup=keyboards.bor)

    elif call.data == "unban":
        msg = bot.send_message(
            chat_id,
            text="Введите ID человека, которого хотите разбанить. (Для отмены введите любую букву)",
        )
        bot.register_next_step_handler(msg, unban1)

    elif call.data == "ban":
        msg = bot.send_message(
            chat_id,
            text="Введите ID человека, которого хотите забанить. (Для отмены введите любую букву)",
        )
        bot.register_next_step_handler(msg, ban1)

    elif call.data == "edit_balance":
        msg = bot.send_message(
            chat_id=chat_id,
            text="Введите ID человека, которому хотите изменить балнс. (Для отмены введите любую букву)",
        )
        bot.register_next_step_handler(msg, give_balance1)

    elif call.data == "input":
        info = functions.replenish_balance(chat_id)
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=info[0],
            reply_markup=keyboards.replenish_balance,
            parse_mode="HTML",
        )
        bot.send_message(
            chat_id,
            text="Отключение клавиатуры",
            reply_markup=types.ReplyKeyboardRemove(),
        )
    elif call.data == "check_payment":
        check = functions.check_payment(user_id=chat_id)
        if check == None:
            bot.send_message(chat_id=chat_id, text="❌ Оплата не найдена")
        else:
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="✅ Успешное пополнение\nСумма - " + str(check) + " рублей",
            )
            bot.send_message(
                ADMIN_FIRST_CHAT_ID,
                text="✅ Произошло пополнение баланса!\nСумма - "
                     + str(check)
                     + " рублей",
            )
            bot.send_message(chat_id, text=var.ENABLE_KEYBOARD, reply_markup=keyboards.menu)

    elif call.data == "canel_payment":
        functions.canel_payment(user_id=chat_id)
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"Меню")
        bot.send_message(chat_id, text="Включение клавиатуры", reply_markup=keyboards.menu)

    elif call.data == "message":
        msg = bot.send_message(
            chat_id=chat_id,
            text='Введите текст для рассылки. \n\nДля отмены напишите "-" без кавычек!',
        )
        bot.register_next_step_handler(msg, message1)

    elif call.data == "seller_offer":
        msg = bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='Введите логин пользователя(Без @), с которым хотите провести сделку. \n\nДля отмены напишите "-" без кавычек!',
        )
        bot.register_next_step_handler(msg, search_seller)

    elif call.data == "customer_offer":
        msg = bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='Введите логин пользователя(Без @), с которым хотите провести сделку. \n\nДля отмены напишите "-" без кавычек!',
        )
        bot.register_next_step_handler(msg, search_customer)

    elif call.data == "proposal_customer":
        try:
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="✅ Предложение о проведении сделки отправленно!",
                reply_markup=keyboards.canel_offer_customer,
            )
            info = functions.info_deal_customer(chat_id)
            info1 = functions.profile(chat_id)
            bot.send_message(
                info[0],
                text="✅ Вам отправлено предложение о сделке!",
                reply_markup=types.ReplyKeyboardRemove(),
            )
            bot.send_message(
                info[0],
                "❕ id - <b><code>{id}</code></b>\n❕ Логин - @{nick}\n❕ Проведенных сделок - {offers}\n\n🔥 В этой сделке вы продавец!".format(
                    id=info1[0], offers=info1[1], nick=info1[5]
                ),
                reply_markup=keyboards.choise_seller,
                parse_mode="HTML",
            )
        except:
            bot.send_message(chat_id, text=var.ERROR)

    elif call.data == "proposal_seller":
        try:
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="✅ Предложение о проведении сделки отправленно!",
                reply_markup=keyboards.canel_offer_seller,
            )
            info = functions.info_deal_seller(chat_id)
            info1 = functions.profile(chat_id)
            bot.send_message(
                info[0],
                text="✅ Вам отправлено предложение о сделке!",
                reply_markup=types.ReplyKeyboardRemove(),
            )
            bot.send_message(
                info[0],
                "❕ id - <b><code>{id}</code></b>\n❕ Логин - @{nick}\n❕ Проведенных сделок - {offers}\n\n🔥 В этой сделке вы покупатель!".format(
                    id=info1[0], offers=info1[1], nick=info1[5]
                ),
                reply_markup=keyboards.choise,
                parse_mode="HTML",
            )
        except:
            bot.send_message(chat_id, text=var.ERROR)

    elif call.data == "delete_customer":
        try:
            info = functions.info_offers_customer(chat_id)
            if info[4] == "dont_open":
                functions.delete_customer(chat_id)
                bot.edit_message_text(
                    chat_id=chat_id, message_id=message_id, text="⛔️ Сделка отменена."
                )
                bot.send_message(chat_id, text=var.ENABLE_KEYBOARD, reply_markup=keyboards.menu)
                bot.send_message(
                    info[0],
                    text="🌧 Ваше предложение о проведении сделки отклонили, или с вами пытались её провести, но передумали.",
                    reply_markup=keyboards.menu,
                )
            else:
                bot.send_message(
                    chat_id, text="⛔️ Сделка уже начата, и не может быть отменена."
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "delete_seller":
        try:
            info = functions.info_offers_seller(chat_id)
            if info[4] == "dont_open":
                functions.delete_seller(chat_id)
                bot.edit_message_text(
                    chat_id=chat_id, message_id=message_id, text="⛔️ Сделка отменена."
                )
                bot.send_message(chat_id, text=var.ENABLE_KEYBOARD, reply_markup=keyboards.menu)
                bot.send_message(
                    info[1],
                    text="🌧 Ваше предложение о проведении сделки отклонили, или с вами пытались её провести, но передумали.",
                    reply_markup=keyboards.menu,
                )
            else:
                bot.send_message(
                    chat_id, text="⛔️ Сделка уже начата, и не может быть отменена."
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "statistics":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=functions.stats(),
            reply_markup=keyboards.admin,
        )

    elif call.data == "accept_customer":
        try:
            functions.accept_customer(chat_id)
            info = functions.info_offers_customer(chat_id)
            info_c = functions.profile(info[1])
            info_s = functions.profile(info[0])
            sum_offer = info[2]
            status = info[4]
            if sum_offer == None:
                sum_offer = "0"
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="💰 Сделка №{id}\n👤 Покупатель - {customer_id}(@{customer_nick})\n💎 Продавец - {seller_id}(@{seller_nick})\n\n💳 Сумма - {sum} рублей\n📄 Статус сделки - {status}".format(
                    id=info[3],
                    customer_id=info_c[0],
                    customer_nick=info_c[5],
                    seller_id=info_s[0],
                    seller_nick=info_s[5],
                    sum=sum_offer,
                    status=status,
                ),
                reply_markup=keyboards.customer_panel,
            )
            bot.send_message(
                info_s[0],
                text="💰 Сделка №{id}\n👤 Покупатель - {customer_id}(@{customer_nick})\n💎 Продавец - {seller_id}(@{seller_nick})\n\n💳 Сумма - {sum} рублей\n📄 Статус сделки - {status}".format(
                    id=info[3],
                    customer_id=info_c[0],
                    customer_nick=info_c[5],
                    seller_id=info_s[0],
                    seller_nick=info_s[5],
                    sum=sum_offer,
                    status=status,
                ),
                reply_markup=keyboards.seller_panel,
            )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "accept_seller":
        try:
            functions.accept_seller(chat_id)
            info = functions.info_offers_seller(chat_id)
            info_c = functions.profile(info[1])
            info_s = functions.profile(info[0])
            sum_offer = info[2]
            status = info[4]
            if sum_offer == None:
                sum_offer = "0"
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="💰 Сделка №{id}\n👤 Покупатель - {customer_id}(@{customer_nick})\n💎 Продавец - {seller_id}(@{seller_nick})\n\n💳 Сумма - {sum} рублей\n📄 Статус сделки - {status}".format(
                    id=info[3],
                    customer_id=info_c[0],
                    customer_nick=info_c[5],
                    seller_id=info_s[0],
                    seller_nick=info_s[5],
                    sum=sum_offer,
                    status=status,
                ),
                reply_markup=keyboards.seller_panel,
            )
            bot.send_message(
                info_c[0],
                text="💰 Сделка №{id}\n👤 Покупатель - {customer_id}(@{customer_nick})\n💎 Продавец - {seller_id}(@{seller_nick})\n\n💳 Сумма - {sum} рублей\n📄 Статус сделки - {status}".format(
                    id=info[3],
                    customer_id=info_c[0],
                    customer_nick=info_c[5],
                    seller_id=info_s[0],
                    seller_nick=info_s[5],
                    sum=sum_offer,
                    status=status,
                ),
                reply_markup=keyboards.customer_panel,
            )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "input_panel":
        try:
            info = functions.profile(chat_id)
            offer = functions.info_offers_customer(chat_id)
            if offer[2] == None:
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    show_alert=True,
                    text="⛔️ Продавец не указал сумму!",
                )
            else:
                if offer[4] == "success":
                    bot.answer_callback_query(
                        callback_query_id=call.id,
                        show_alert=True,
                        text="Вы уже оплатили товар, продавец обязан вам его передать. Если продавец отказывается передать товар, откройте спор.",
                    )
                else:
                    if float(info[2]) < float(offer[2]):
                        bot.send_message(
                            chat_id,
                            text="📉 Вам необходимо пополнить баланс!\n💰 Ваш баланс - {user} рублей\n💳 Необходимый баланс - {offer} рублей\n\nДля этого вам необходимо отменить сделку!".format(
                                user=info[2], offer=offer[2]
                            ),
                        )
                    else:
                        bal = float(info[2]) - float(offer[2])
                        functions.success(chat_id, bal)
                        info = functions.info_offers_customer(chat_id)
                        bot.send_message(
                            info[0],
                            text="✅ Покупатель оплатил товар! \nВам необходимо передать товар.",
                        )
                        bot.send_message(
                            info[1],
                            text="✅ Товар был успешно оплачен, ожидайте получения товара. Если тот не валид, или продавец кинул в ЧС, откройте спор.",
                        )
        except:
            bot.send_message(chat_id, text=var.ERROR)

    elif call.data == "price":
        try:
            info = functions.info_offers_seller(chat_id)
            if info[2] == None:
                msg = bot.send_message(
                    chat_id,
                    text='Введите сумму товара. \n\nДля отмены напишите "-" без кавычек!',
                )
                bot.register_next_step_handler(msg, price)
            else:
                bot.send_message(
                    chat_id,
                    text="Вы уже ввели сумму товара, и не можете её редактировать!",
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "canel_open":
        bot.send_message(
            chat_id,
            text="Вы уверены что хотите отменить сделку?",
            reply_markup=keyboards.choise_canel,
        )

    elif call.data == "No_canel":
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text="Процесс отмены сделки аннулирован",
        )

    elif call.data == "Yes_canel":
        try:
            info = functions.info_offers_customer(chat_id)
            if info[4] == "open":
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    show_alert=True,
                    text="Запрос на отмену отправлен продавцу",
                )
                bot.send_message(
                    info[0],
                    text="Покупатель предложил отменить сделку.",
                    reply_markup=keyboards.choise_canel_seller2,
                )
            else:
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    show_alert=True,
                    text="Сделка уже завершена или над ней проходит спор.",
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "Yes_canel_seller":
        try:
            info = functions.info_offers_seller(chat_id)
            if info[4] == "open":
                functions.yes_canel_seller2(chat_id)
                bot.send_message(
                    info[0], text="✅ Сделка успешно отменена.", reply_markup=keyboards.menu
                )
                bot.send_message(
                    info[1], text="✅ Сделка успешно отменена.", reply_markup=keyboards.menu
                )
            else:
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    show_alert=True,
                    text="✅ Сделка уже завершена или над ней проходит спор.",
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "canel_open_seller":
        bot.send_message(
            chat_id,
            text="Вы уверены что хотите отменить сделку?",
            reply_markup=keyboards.choise_canel_seller,
        )

    elif call.data == "Yes_canel_seller1":
        try:
            info = functions.info_offers_seller(chat_id)
            if info[4] == "open":
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    show_alert=True,
                    text="Запрос на отмену отправлен покупателю",
                )
                bot.send_message(
                    info[1],
                    text="Продавец предложил отменить сделку.",
                    reply_markup=keyboards.choise_canel_customer,
                )
            else:
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    show_alert=True,
                    text="Сделка уже завершена или над ней проходит спор.",
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "No_canel_seller1":
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text="✅ Процесс отмены сделки аннулирован",
        )

    elif call.data == "No_canel_seller":
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text="✅ Процесс отмены сделки аннулирован",
        )

    elif call.data == "Yes_canel_customer":
        try:
            info = functions.info_offers_customer(chat_id)
            if info[4] == "open":
                functions.yes_canel_customer2(chat_id)
                bot.send_message(
                    info[0], text="✅ Сделка успешно отменена.", reply_markup=keyboards.menu
                )
                bot.send_message(
                    info[1], text="✅ Сделка успешно отменена.", reply_markup=keyboards.menu
                )
            else:
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    show_alert=True,
                    text="✅ Сделка уже завершена или над ней проходит спор.",
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "No_canel_customer":
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text="✅ Процесс отмены сделки аннулирован",
        )

    elif call.data == "ok":
        try:
            info = functions.info_offer_customer(chat_id)
            if info[0] == "success":
                bot.send_message(
                    chat_id,
                    text="Вы уверены что получили товар, и он валидный? Если нет, или условия не соблюдены, то вам необходимо открыть спор.",
                    reply_markup=keyboards.ok_choise,
                )
            else:
                bot.send_message(
                    chat_id, text="✅ Вы не оплатили сделку, или над ней ведётся спор."
                )
        except:
            bot.send_message(chat_id, text=var.ERROR)

    elif call.data == "ok_canel":
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text="Вы подтвердили, что товар не получен.",
        )

    elif call.data == "ok_ok":
        try:
            info = functions.info_offers_customer(chat_id)
            if info[4] == "success":
                info1 = functions.profile(info[0])
                info2 = functions.profile(info[1])
                functions.ok(
                    chat_id,
                    info[0],
                    info[2],
                    info[3],
                    info1[2],
                    info1[5],
                    info2[5],
                    info1[1],
                    info2[1],
                )
                bot.send_message(
                    chat_id,
                    text="✅ Сделка успешно завершена!\n📝 Хотите оставить отзыв о продавце?",
                    reply_markup=keyboards.add_review,
                )
                bot.send_message(
                    info[0],
                    text="✅ Сделка успешно завершена!\n💰 Деньги зачислены на ваш счёт.\n\n📝 Сейчас покупатель оставляет отзыв, подождите пожалуйста.",
                    reply_markup=keyboards.cancel_wait,
                )
                bot.send_message(
                    chat_id_bot,
                    text="✅ Cделка успешно завершена!\n💰 Сумма - {sum_offer} рублей\n\n👤 Продавец - @{seller_nick}\n👤 Покупатель - @{customer_nick}".format(
                        sum_offer=info[2], seller_nick=info1[5], customer_nick=info2[5]
                    ),
                )
            else:
                bot.send_message(
                    chat_id, text="Вы не оплатили сделку, или над ней ведётся спор."
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "open_dispute":
        try:
            info = functions.info_offers_customer(chat_id)
            if info[4] == "dont_open":
                bot.send_message(chat_id, text="⛔️ Сделка ещё не открыта!")
            else:
                if info[4] == "open":
                    bot.send_message(
                        chat_id,
                        text="⛔️ Товар ещё не был вам передан. Если вы считаете что продавец хочет вас обмануть, отмените сделку и напишите администратору @{}.".format(
                            ADMIN_USERNAME
                        ),
                    )
                else:
                    if info[4] == "dispute":
                        bot.send_message(chat_id, text="⛔️ Спор уже начат.")
                    else:
                        info_c = functions.profile(info[1])
                        info_s = functions.profile(info[0])
                        functions.dispute_customer(chat_id)
                        bot.send_message(
                            chat_id,
                            text="Спор начат, продавец оповещён. Если долго ничего не происходит, напишите администратору @{}.".format(
                                ADMIN_USERNAME
                            ),
                        )
                        bot.send_message(
                            info[0],
                            text="Покупатель начал спор по вашему товару, скоро вам напишет администратор. Если долго ничего не происходит, напишите администратору @{}.".format(
                                ADMIN_USERNAME
                            ),
                        )
                        bot.send_message(
                            ADMIN_FIRST_CHAT_ID,
                            text="Был начат спор!\n\nID сделки - <b><code>{id}</code></b>\nПродавец - @{seller}\nПокупатель(Организовал спор) - @{customer}".format(
                                id=info[3], seller=info_s[5], customer=info_c[5]
                            ),
                            parse_mode="HTML",
                        )
        except:
            bot.send_message(chat_id, text=var.ERROR)

    elif call.data == "open_dispute_seller":
        try:
            info = functions.info_offers_seller(chat_id)
            if info[4] == "dont_open":
                bot.send_message(chat_id, text="⛔️ Сделка ещё не открыта!")
            else:
                if info[4] == "open":
                    bot.send_message(
                        chat_id,
                        text="Товар ещё не был вам передан. Если вы считаете что продавец хочет вам скамнуть, отмените сделку и напишите администратору @{}.".format(
                            ADMIN_USERNAME
                        ),
                    )
                else:
                    if info[4] == "dispute":
                        bot.send_message(chat_id, text="⛔️ Спор уже начат.")
                    else:
                        info_c = functions.profile(info[1])
                        info_s = functions.profile(info[0])
                        functions.dispute_customer(chat_id)
                        bot.send_message(
                            chat_id,
                            text="Спор начат, покупатель оповещён. Если долго ничего не происходит, напишите администратору @{}.".format(
                                ADMIN_USERNAME
                            ),
                        )
                        bot.send_message(
                            info[1],
                            text="Продавец начал спор, скоро вам напишет администратор. Если долго ничего не происходит, напишите администратору @{}.".format(
                                ADMIN_USERNAME
                            ),
                        )
                        bot.send_message(
                            ADMIN_FIRST_CHAT_ID,
                            text="Был начат спор!\n\nID сделки - <b><code>{id}</code></b>\nПродавец - @{seller}\nПокупатель(Организовал спор) - @{customer}".format(
                                id=info[3], seller=info_s[5], customer=info_c[5]
                            ),
                            parse_mode="HTML",
                        )
        except:
            bot.send_message(chat_id, text=var.ERROR)

    elif call.data == "dispute_admin":
        msg = bot.send_message(
            chat_id, text='Введите ID сделки. (Для отмены введите "-" без кавычек)'
        )
        bot.register_next_step_handler(msg, dispute_admin_func)

    elif call.data == "customer_true":
        msg = bot.send_message(
            chat_id,
            text='Покупатель вернёт деньги, а сделка будет отменена!\nДля подтверждения введите ID сделки, для отмены введите "-" без кавычек',
        )
        bot.register_next_step_handler(msg, customer_true_func)

    elif call.data == "seller_true":
        msg = bot.send_message(
            chat_id,
            text='Продавец получит деньги, а сделка будет отменена!\nДля подтверждения введите ID сделки, для отмены введите "-" без кавычек.',
        )
        bot.register_next_step_handler(msg, seller_true_func)

    elif call.data == "no_true":
        msg = bot.send_message(
            chat_id,
            text='Покупатель вернёт деньги, а сделка будет отменена!\nДля подтверждения введите ID сделки, для отмены введите "-" без кавычек.',
        )
        bot.register_next_step_handler(msg, customer_true_func)

    elif call.data == "canel_open_offer":
        try:
            info = functions.canel_open_offer(chat_id)
            if info[0] == "OK":
                bot.send_message(
                    chat_id,
                    text="🔥 Предложение о проведении сделки отозвано.",
                    reply_markup=keyboards.menu,
                )
                bot.send_message(
                    info[1],
                    text="🔥 Покупатель отозвал своё предложение о проведении сделки.",
                    reply_markup=keyboards.menu,
                )
            else:
                bot.send_message(
                    chat_id,
                    text="🔥 Вы не можете отозвать предложение когда продавец его уже принял.",
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "canel_open_offer_seller":
        try:
            info = functions.canel_open_offer_seller(chat_id)
            if info[0] == "OK":
                bot.send_message(
                    chat_id,
                    text="🔥 Предложение о проведении сделки отозвано.",
                    reply_markup=keyboards.menu,
                )
                bot.send_message(
                    info[1],
                    text="🔥 Продавец отозвал своё предложение о проведении сделки.",
                    reply_markup=keyboards.menu,
                )
            else:
                bot.send_message(
                    chat_id,
                    text="🔥 Вы не можете отозвать предложение когда покупатель его уже принял.",
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "reviews":
        try:
            info1 = functions.info_offers_customer(chat_id)
            if info1 == None:
                info1 = functions.info_offers_seller(chat_id)
                info = functions.reviews(info1[1])
                if len(info) > 0:
                    bot.send_message(chat_id=chat_id, text=info)
                elif len(info) == 0:
                    bot.send_message(chat_id=chat_id, text="⛔️ отзывов не обнаружено!")
            else:
                info = functions.reviews(info1[0])
                if len(info) > 0:
                    bot.send_message(chat_id=chat_id, text=info)
                elif len(info) == 0:
                    bot.send_message(chat_id=chat_id, text="⛔️ отзывов не обнаружено!")
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    if call.data == "add_review":
        try:
            info = functions.info_offer_customer(chat_id)
            if info[0] == "review":
                msg = bot.send_message(
                    chat_id,
                    text='🔥 Напишите отзыв о сделке, для отмены вышлите "-" без кавычек.',
                )
                bot.register_next_step_handler(msg, add_review)
            else:
                bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text="Вы не можете оставить отзыв, так как не завершили сделку.",
                    reply_markup=keyboards.menu,
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "up_login":
        try:
            info = functions.up_login(call.message.chat.username, call.message.chat.id)
            if info == None:
                bot.send_message(chat_id, text="Ваш логин обновлён!")
            else:
                bot.send_message(
                    chat_id,
                    text="Логин, который вы хотите занять уже получил другой пользователь, или вы его уже заняли!",
                )
        except:
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=True, text=var.ERROR
            )

    elif call.data == "no_review":
        try:
            info = functions.info_offers_customer(chat_id)
            bot.send_message(
                info[0],
                text="❄️ Покупатель отказался оставлять отызв.",
                reply_markup=keyboards.menu,
            )
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="❄️ Сделка успешно завершена!",
            )
            bot.send_message(chat_id, text=var.ENABLE_KEYBOARD, reply_markup=keyboards.menu)
            functions.close_offer(chat_id)
        except:
            bot.send_message(chat_id, text=var.ERROR)




