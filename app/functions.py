import re
from decimal import Decimal
from datetime import datetime

from app import config
from app.bot import bot
from app import transfers
from models import queries
from content.languages import get_strings


def check_admin_permission(chat_id):
    return chat_id in (config.ADMIN_FIRST_CHAT_ID, config.ADMIN_SECOND_CHAT_ID)


def check_user_blocks(user):
    strings = get_strings(user.language)
    if user.banned:
        return strings.banned
    if user.customer_deal is not None or user.seller_deal is not None:
        return strings.have_deal_now


def search_second_user(message, strings):
    if message.text.startswith("-") or not message.text.isdigit():
        bot.send_message(message.chat.id, text=strings.cancel)
        return

    if int(message.text) == message.chat.id:
        bot.send_message(message.chat.id, text=strings.cannot_init_deal_with_yourself)
        return

    second_user = queries.get_user(int(message.text))
    if second_user is None:
        bot.send_message(message.chat.id, text=strings.user_not_found)
        return

    if second_user.banned:
        bot.send_message(message.chat.id, text=strings.user_banned)
        return

    if second_user.customer_deal is not None or second_user.seller_deal is not None:
        bot.send_message(
            message.chat.id,
            text=strings.user_already_in_deal,
        )
        return

    return second_user


def ban_or_unban_user(message, ban, strings):
    if not check_admin_permission(message.chat.id):
        return
    if message.text.startswith("-") or not message.text.isdigit():
        bot.send_message(message.chat.id, text=strings.cancel)
        return

    user = queries.get_user(int(message.text))
    if user is None:
        bot.send_message(message.chat.id, text=strings.user_not_found)
        return
    user.banned = ban
    user.save()
    return True


def solve_dispute(message, customer_solve):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    if not check_admin_permission(message.chat.id):
        return
    if message.text.startswith("-") or not message.text.isdigit():
        bot.send_message(message.chat.id, text=strings.cancel)
        return

    deal = queries.get_deal(int(message.text))
    if deal is None:
        bot.send_message(
            message.chat.id, text=f"{strings.deal_not_found} {strings.cancel}"
        )
        return
    if customer_solve:
        bot.send_message(deal.customer_id, strings.dispute_solved_for_you)
        bot.send_message(deal.customer_id, strings.dispute_solved_customer)
        bot.send_message(message.chat.id, strings.dispute_solved_customer)
        deal.customer.balance += deal.amount
        deal.customer.save()
    else:
        bot.send_message(deal.customer_id, strings.dispute_solved_seller)
        bot.send_message(deal.customer_id, strings.dispute_solved_for_you)
        bot.send_message(message.chat.id, strings.dispute_solved_seller)
        deal.seller.balance += deal.amount
        deal.seller.save()
    deal.delete()


def format_user_info(user, strings):
    return strings.format_user_info.format(
        chat_id=user.chat_id,
        username=bot.get_chat(user.chat_id).username,
        offers_count=len(user.customer_offers) + len(user.seller_offers),
    )


def format_deal_info(deal, strings):
    seller_username = bot.get_chat(deal.seller.chat_id).username
    customer_username = bot.get_chat(deal.customer.chat_id).username

    return strings.format_deal_info.format(
        deal_id=deal.id,
        customer_username=customer_username,
        customer_id=deal.customer_id,
        seller_username=seller_username,
        seller_id=deal.seller_id,
        amount=deal.amount,
        status=strings.deal_statuses[deal.status],
    )


def process_withdrawal(withdrawal, language):
    strings = get_strings(language)

    try:
        trans_hex = transfers.process_trc20_usdt_withdrawal(withdrawal)

        bot.send_message(
            withdrawal.user_id,
            strings.withdrawal_complete.format(
                amount=withdrawal.amount,
                address=withdrawal.blockchain_address,
                hex_hash=trans_hex,
            ),
            parse_mode="HTML",
        )

        if withdrawal.user.referral_id:
            referral = queries.get_user(withdrawal.user.referral_id)
            strings = get_strings(referral.language)
            bonus = transfers.get_royalty(withdrawal) * Decimal(str(config.REFERRAL_BONUS)) / 100
            referral.balance += bonus
            referral.save()
            bot.send_message(
                referral.chat_id,
                strings.referral_withdrawal.format(
                    amount=withdrawal.amount,
                    bonus=bonus,
                ),
                parse_mode="HTML",
            )

    except Exception as e:
        withdrawal.user.balance += withdrawal.amount
        withdrawal.user.save()
        withdrawal.passed = False
        withdrawal.close_time = datetime.utcnow()
        withdrawal.save()
        bot.send_message(
            withdrawal.user_id,
            strings.withdrawal_error.format(
                amount=withdrawal.amount, admin=config.ADMIN_USERNAME
            ),
        )
        raise


def is_wallet_amount(text):
    return bool(re.fullmatch(r"\d+(\.\d+)?", text))
