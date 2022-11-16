from telebot import types

from models import queries
from models.models import Deal
from app import functions
from app import config
from app.bot import bot
from content import keyboards
from content.languages import get_strings
from handlers import next_step_hadlers

__all__ = ["register_bot_callback_handler"]


def register_bot_callback_handler(data: str):
    def wrapper(handler: callable):
        bot.register_callback_query_handler(handler, lambda call: call.data == data)
        return handler

    return wrapper


@register_bot_callback_handler("output")
def callback_handler(call):
    # TODO cac
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    if user.blockchain_address is None:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=strings.you_have_not_wallet,
            reply_markup=keyboards.change_address(strings),
        )
    else:
        msg = bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=strings.init_withdrawal.format(
                address=user.blockchain_address, balance=user.balance
            ),
        )
        bot.register_next_step_handler(msg, next_step_hadlers.output)


@register_bot_callback_handler("input")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    if user.blockchain_address is None:
        bot.send_message(
            chat_id=chat_id,
            text=strings.must_set_address,
            parse_mode="HTML",
            reply_markup=keyboards.change_address(strings),
        )
        return

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=strings.wallet_input.format(address=config.SYSTEM_WALLET_ADDRESS),
        parse_mode="HTML",
    )
    bot.register_next_step_handler(msg, next_step_hadlers.register_transaction_hash)


@register_bot_callback_handler("change_address")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=strings.change_wallet,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.change_address)


@register_bot_callback_handler("seller_offer_init")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=strings.init_deal,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.search_customer_for_init)


@register_bot_callback_handler("customer_offer_init")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=strings.init_deal,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.search_seller_for_init)


@register_bot_callback_handler("seller_offer_get")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    if len(user.seller_offers) == 0:
        bot.send_message(chat_id, text=strings.no_offers)
        return

    text = ""
    for offer in user.seller_offers:
        username = bot.get_chat(offer.customer_id).username
        text += strings.offer_info.format(
            username=username, user_id=offer.customer_id, amount=offer.amount
        )

    bot.send_message(chat_id, text=text)


@register_bot_callback_handler("customer_offer_get")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    if len(user.customer_offers) == 0:
        bot.send_message(chat_id, text=strings.no_offers)
        return

    text = ""
    for offer in user.customer_offers:
        username = bot.get_chat(offer.seller_id).username
        text += strings.offer_info.format(
            username=username, user_id=offer.seller_id, amount=offer.amount
        )

    bot.send_message(chat_id, text=text)


@register_bot_callback_handler("ban")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if not functions.check_admin_permission(chat_id):
        return
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=strings.user_id_for_ban,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.ban_user)


@register_bot_callback_handler("unban")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if not functions.check_admin_permission(chat_id):
        return
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=strings.user_id_for_unban,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.unban_user)


@register_bot_callback_handler("customer_solve_dispute")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    msg = bot.send_message(
        chat_id,
        text=strings.customer_dispute_solve_confirm,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.customer_solve_dispute)


@register_bot_callback_handler("seller_solve_dispute")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    msg = bot.send_message(
        chat_id,
        text=strings.seller_dispute_solve_confirm,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.seller_solve_dispute)


@register_bot_callback_handler("proposal")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=strings.deal_proposal_sent,
        reply_markup=keyboards.cancel_deal(strings),
    )

    deal = user.seller_deal or user.customer_deal
    if user.seller_deal:
        second_user = deal.customer
        strings = get_strings(second_user.language)
        role = strings.customer

    else:
        second_user = deal.seller
        strings = get_strings(second_user.language)
        role = strings.seller

    bot.send_message(
        second_user.chat_id,
        text=strings.deal_proposal_received,
        reply_markup=types.ReplyKeyboardRemove(),
    )
    bot.send_message(
        second_user.chat_id,
        strings.deal_proposal_info.format(
            user_info=functions.format_user_info(user, strings), role=role
        ),
        reply_markup=keyboards.accept_deal(strings),
        parse_mode="HTML",
    )


@register_bot_callback_handler("cancel_deal")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.seller_deal or user.customer_deal

    if deal.status != Deal.Status.new:
        bot.send_message(chat_id, text=strings.cannot_cancel_deal)
        return

    bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=strings.cancel_deal
    )
    deal.delete()


@register_bot_callback_handler("refuse_deal")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.seller_deal or user.customer_deal

    if user.seller_deal:
        second_user = deal.customer
    else:
        second_user = deal.seller

    if deal.status != Deal.Status.new:
        bot.send_message(chat_id, text=strings.cannot_cancel_deal)
        return

    bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=strings.cancel_deal
    )
    strings = get_strings(second_user.language)
    bot.send_message(chat_id=second_user.chat_id, text=strings.cancel_deal)
    deal.delete()


@register_bot_callback_handler("reviews")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    if user.seller_deal:
        second_chat_id = user.seller_deal.customer_id
    else:
        second_chat_id = user.customer_deal.seller_id

    offers = queries.get_user(second_chat_id).seller_offers

    text = ""
    for offer in offers:
        if offer.review is not None:
            text += f"💠 {offer.review}\n\n"

    if text == "":
        bot.send_message(chat_id=chat_id, text=strings.no_review)
        return

    bot.send_message(chat_id=chat_id, text=text)


@register_bot_callback_handler("accept_deal")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    deal = user.seller_deal or user.customer_deal

    if deal.status != deal.Status.new:
        return
    deal.status = Deal.Status.open
    deal.save()

    strings = get_strings(deal.customer.language)
    bot.send_message(
        chat_id=deal.customer_id,
        text=strings.deal_accepted.format(
            deal_info=functions.format_deal_info(deal, strings)
        ),
        reply_markup=keyboards.customer_panel(strings),
        parse_mode="HTML",
    )
    strings = get_strings(deal.seller.language)
    bot.send_message(
        chat_id=deal.seller_id,
        text=strings.deal_accepted.format(
            deal_info=functions.format_deal_info(deal, strings)
        ),
        reply_markup=keyboards.seller_panel(strings),
        parse_mode="HTML",
    )


@register_bot_callback_handler("set_price")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.seller_deal

    if deal.amount != 0:
        bot.send_message(chat_id, text=strings.deal_amount_already_sets)
        return

    msg = bot.send_message(
        chat_id,
        text=strings.set_deal_amount,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.set_price)


@register_bot_callback_handler("open_dispute")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.seller_deal or user.customer_deal

    if deal.status == Deal.Status.new:
        bot.send_message(chat_id, text=strings.dispute_status_new)
        return

    if deal.status == Deal.Status.open:
        bot.send_message(
            chat_id,
            text=strings.dispute_status_open.format(admin=config.ADMIN_USERNAME),
        )
        return

    if deal.status == Deal.Status.dispute:
        bot.send_message(
            chat_id,
            text=strings.dispute_status_new.dispute.format(admin=config.ADMIN_USERNAME),
        )
        return

    deal.status = Deal.Status.dispute
    deal.save()

    strings = get_strings(deal.customer.language)
    bot.send_message(
        deal.customer_id,
        text=strings.dispute_has_been_open.format(admin=config.ADMIN_USERNAME),
    )
    strings = get_strings(deal.seller.language)
    bot.send_message(
        deal.seller_id,
        text=strings.dispute_has_been_open.format(admin=config.ADMIN_USERNAME),
    )

    admin = queries.get_user(config.ADMIN_FIRST_CHAT_ID)
    strings = get_strings(admin.language)
    bot.send_message(
        config.ADMIN_FIRST_CHAT_ID,
        text=strings.dispute_has_been_open_admin.format(
            info=functions.format_deal_info(deal, strings),
            role=strings.seller if user.seller_deal else strings.customer,
        ),
        parse_mode="HTML",
    )


@register_bot_callback_handler("confirm_fund")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.customer_deal

    if deal.status == Deal.Status.success:
        bot.send_message(
            chat_id,
            text=strings.confirm_fund,
            reply_markup=keyboards.confirm_fund(strings),
        )
    else:
        bot.send_message(chat_id, text=strings.confirm_reject)


@register_bot_callback_handler("confirm_confirm_fund")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    deal = user.customer_deal

    if deal.status == Deal.Status.success:
        deal.seller.balance += deal.amount
        deal.status = Deal.Status.review
        deal.seller.save()
        deal.save()

        strings = get_strings(deal.customer.language)
        bot.send_message(
            deal.customer_id,
            text=strings.fund_confirmed_customer,
            reply_markup=keyboards.add_review(strings),
        )
        strings = get_strings(deal.seller.language)
        bot.send_message(
            deal.seller_id,
            text=strings.fund_confirmed_seller,
            reply_markup=keyboards.cancel_wait(strings),
        )
    else:
        strings = get_strings(user.language)
        bot.send_message(chat_id, text=strings.confirm_reject)


@register_bot_callback_handler("close_deal")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    bot.send_message(
        chat_id,
        text=strings.close_deal_confirm,
        reply_markup=keyboards.choice_close_deal(strings),
    )


@register_bot_callback_handler("close_close_deal")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.seller_deal or user.customer_deal

    if deal.status == Deal.Status.open:
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text=strings.close_request_sent,
        )

        if user.seller_deal:
            second_user = deal.customer
            strings = get_strings(second_user.language)
            role = strings.seller
        else:
            second_user = deal.seller
            strings = get_strings(second_user.language)
            role = strings.customer

        bot.send_message(
            second_user.chat_id,
            text=strings.close_request_received.format(role=role),
            reply_markup=keyboards.choice_accept_cancel(strings),
        )
    else:
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text=strings.deal_canceled_or_dispute_active,
        )


@register_bot_callback_handler("self_delete")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    bot.delete_message(chat_id, message_id)


@register_bot_callback_handler("pay")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.customer_deal

    if deal.amount == 0:
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text=strings.seller_not_set_amount,
        )
        return

    if deal.status == Deal.Status.success:
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text=strings.fund_already_payed,
        )
        return

    if user.balance < deal.amount:
        bot.send_message(
            chat_id,
            text=strings.not_enough_for_pay.format(
                balance=user.balance,
                amount=deal.amount,
            ),
        )
        return

    deal.customer.balance -= deal.amount
    deal.customer.save()
    deal.status = Deal.Status.success
    deal.save()

    bot.send_message(
        deal.customer_id,
        text=strings.fund_payed_customer,
    )
    strings = get_strings(deal.seller.language)
    bot.send_message(
        deal.seller_id,
        text=strings.fund_payed_seller,
    )


@register_bot_callback_handler("add_review")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.customer_deal

    if deal.status != Deal.Status.review:
        return

    msg = bot.send_message(chat_id, text=strings.add_review)
    bot.register_next_step_handler(msg, next_step_hadlers.add_review)


@register_bot_callback_handler("no_review")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.seller_deal or user.customer_deal

    if deal.status != Deal.Status.review:
        return

    if user.seller_deal:
        bot.send_message(
            chat_id=chat_id,
            text=strings.seller_cancel_review_seller,
            reply_markup=keyboards.menu(strings),
        )
        second_user = deal.customer
        strings = get_strings(second_user.language)
        bot.send_message(
            second_user.chat_id,
            text=strings.seller_cancel_review_customer,
            reply_markup=keyboards.menu(strings),
        )

    else:
        bot.send_message(
            chat_id=chat_id,
            text=strings.customer_cancel_review_customer,
            reply_markup=keyboards.menu(strings),
        )
        second_user = deal.seller
        strings = get_strings(second_user.language)
        bot.send_message(
            second_user.chat_id,
            text=strings.customer_cancel_review_seller,
            reply_markup=keyboards.menu(strings),
        )

    queries.new_offer(deal, None)


@register_bot_callback_handler("accept_close")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)
    deal = user.seller_deal or user.customer_deal

    if deal.status == Deal.Status.open:
        strings = get_strings(deal.customer.language)
        bot.send_message(
            deal.customer_id,
            text=strings.deal_canceled,
            reply_markup=keyboards.menu(strings),
        )
        strings = get_strings(deal.seller.language)
        bot.send_message(
            deal.seller_id,
            text=strings.deal_canceled,
            reply_markup=keyboards.menu(strings),
        )
        deal.delete()
    else:
        bot.answer_callback_query(
            callback_query_id=call.id,
            show_alert=True,
            text=strings.deal_canceled_or_dispute_active,
        )


@register_bot_callback_handler("refuse_close")
def callback_handler(call):
    chat_id = call.message.chat.id
    user = queries.get_user(chat_id)
    deal = user.seller_deal or user.customer_deal

    strings = get_strings(deal.customer.language)
    bot.send_message(deal.customer_id, text=strings.refuse_cancel_deal)

    strings = get_strings(deal.customer.seller)
    bot.send_message(deal.seller_id, text=strings.refuse_cancel_deal)


@register_bot_callback_handler("input_referral")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=strings.referral_input_referral_code,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.input_referral)


@register_bot_callback_handler("change_referral")
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = queries.get_user(chat_id)
    strings = get_strings(user.language)

    msg = bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=strings.edit_referral,
    )
    bot.register_next_step_handler(msg, next_step_hadlers.change_referral)
