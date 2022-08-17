from telebot import types

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton("💵 Прошедшие сделки"),
    types.KeyboardButton("👤 Профиль"),
    types.KeyboardButton("⭐️ О нас"),
    types.KeyboardButton("🔒 Провести сделку"),
)

admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
admin.add(
    types.KeyboardButton("Бан-система"),
    types.KeyboardButton("Рассылка"),
    types.KeyboardButton("Статистика"),
    types.KeyboardButton("Решение спора"),
)

profile = types.InlineKeyboardMarkup(row_width=2)
profile.add(
    types.InlineKeyboardButton("Вывод средств", callback_data="output"),
    types.InlineKeyboardButton("Пополнение баланса", callback_data="input"),
    types.InlineKeyboardButton("Изменить Metamask", callback_data="change_metamask"),
)

init_offer = types.InlineKeyboardMarkup()
init_offer.add(
    types.InlineKeyboardButton("💎 Покупатель", callback_data="customer_offer_init"),
    types.InlineKeyboardButton("💰 Продавец", callback_data="seller_offer_init"),
)

show_offers = types.InlineKeyboardMarkup()
show_offers.add(
    types.InlineKeyboardButton("💎 Продавец", callback_data="seller_offer_get"),
    types.InlineKeyboardButton("💰 Покупатель", callback_data="customer_offer_get"),
)

bou = types.InlineKeyboardMarkup(row_width=2)
bou.add(
    types.InlineKeyboardButton("Забанить", callback_data="ban"),
    types.InlineKeyboardButton("Разбанить", callback_data="unban"),
)

solve_dispute = types.InlineKeyboardMarkup(row_width=2)
solve_dispute.add(
    types.InlineKeyboardButton("💎 Покупатель", callback_data="customer_solve_dispute"),
    types.InlineKeyboardButton("💰 Продавец", callback_data="seller_solve_dispute"),
)

change_metamask = types.InlineKeyboardMarkup()
change_metamask.add(
    types.InlineKeyboardButton("Изменить Metamask", callback_data="change_metamask")
)

sentence_deal = types.InlineKeyboardMarkup(row_width=2)
sentence_deal.add(
    types.InlineKeyboardButton("📝 Предложить сделку", callback_data="proposal"),
    types.InlineKeyboardButton("📄 Отзывы", callback_data="reviews"),
    types.InlineKeyboardButton("❌ Назад", callback_data="cancel_deal"),
)

cancel_deal = types.InlineKeyboardMarkup(row_width=2)
cancel_deal.add(
    types.InlineKeyboardButton("❌ Назад", callback_data="refuse_deal"),
)

accept_deal = types.InlineKeyboardMarkup()
accept_deal.add(
    types.InlineKeyboardButton("✅ Принять", callback_data="accept_deal"),
    types.InlineKeyboardButton("❌ Отклонить", callback_data="refuse_deal"),
)

seller_panel = types.InlineKeyboardMarkup(row_width=2)
seller_panel.add(
    types.InlineKeyboardButton("Открыть спор", callback_data="open_dispute"),
    types.InlineKeyboardButton("Закрыть сделку", callback_data="close_deal"),
    types.InlineKeyboardButton("Указать стоимость", callback_data="set_price"),
)

customer_panel = types.InlineKeyboardMarkup(row_width=2)
customer_panel.add(
    types.InlineKeyboardButton("Оплатить товар", callback_data="pay"),
    types.InlineKeyboardButton("Закрыть сделку", callback_data="close_deal"),
    types.InlineKeyboardButton("Открыть спор", callback_data="open_dispute"),
    types.InlineKeyboardButton("Подтвердить получение", callback_data="confirm_fund"),
)


confirm_fund = types.InlineKeyboardMarkup()
confirm_fund.add(
    types.InlineKeyboardButton(
        "✅ Согласиться", callback_data="confirm_confirm_fund"
    ),  # TODO
    types.InlineKeyboardButton("❌ Открыть спор", callback_data="open_dispute"),
)


choice_close_deal = types.InlineKeyboardMarkup()
choice_close_deal.add(
    types.InlineKeyboardButton("✅ Да", callback_data="close_close_deal"),  # TODO
    types.InlineKeyboardButton("❌ Нет", callback_data="self_delete"),
)


#####


choise_cancel_seller = types.InlineKeyboardMarkup()
choise_cancel_seller.add(
    types.InlineKeyboardButton("✅ Да", callback_data="Yes_cancel_seller1"),
    types.InlineKeyboardButton("❌ Нет", callback_data="No_cancel_seller1"),
)

choise_cancel_seller2 = types.InlineKeyboardMarkup()
choise_cancel_seller2.add(
    types.InlineKeyboardButton("✅ Согласиться", callback_data="Yes_cancel_seller"),
    types.InlineKeyboardButton("❌ Отказаться", callback_data="No_cancel_seller"),
)

choise_cancel_customer = types.InlineKeyboardMarkup()
choise_cancel_customer.add(
    types.InlineKeyboardButton("✅ Согласиться", callback_data="Yes_cancel_customer"),
    types.InlineKeyboardButton("❌ Отказаться", callback_data="No_cancel_customer"),
)


cancel_offer_customer = types.InlineKeyboardMarkup()
cancel_offer_customer.add(
    types.InlineKeyboardButton("💥 Отменить сделку", callback_data="cancel_open_offer")
)

cancel_offer_seller = types.InlineKeyboardMarkup()
cancel_offer_seller.add(
    types.InlineKeyboardButton(
        "💥 Отменить сделку", callback_data="cancel_open_offer_seller"
    )
)

add_review = types.InlineKeyboardMarkup(row_width=2)
add_review.add(
    types.InlineKeyboardButton("✨ Да", callback_data="add_review"),
    types.InlineKeyboardButton("💤 Нет", callback_data="no_review"),
)

cancel_wait = types.InlineKeyboardMarkup()
cancel_wait.add(
    types.InlineKeyboardButton("💥 Отменить ожидание", callback_data="cancel_wait")
)
