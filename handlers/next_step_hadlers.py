from decimal import Decimal

from telebot import types
from web3.exceptions import TransactionNotFound

from app.bot import bot
from app import functions
from app import config
from content import keyboards
from content.languages import get_strings
from models import queries, Deal


def ban_user(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    if functions.ban_or_unban_user(message, True, strings):
        bot.send_message(message.chat.id, text=strings.ban_user)


def unban_user(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    if functions.ban_or_unban_user(message, False, strings):
        bot.send_message(message.chat.id, text=strings.unban_user)


def customer_solve_dispute(message):
    functions.solve_dispute(message, True)


def seller_solve_dispute(message):
    functions.solve_dispute(message, False)


def send_message_for_all_users(message):
    if not functions.check_admin_permission(message.chat.id):
        return
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)

    if message.text == "-":
        bot.send_message(message.chat.id, text=strings.cancel)
    else:
        users = queries.get_all_users()
        bot.send_message(message.chat.id, text=strings.perform_mailing)
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
            text=strings.end_mailing.format(success=count_success, all=count_all),
        )


def search_dispute(message):
    if not functions.check_admin_permission(message.chat.id):
        return
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)

    if message.text.startswith("-") or not message.text.isdigit():
        bot.send_message(message.chat.id, text=strings.cancel)
    else:
        deal = queries.get_deal(int(message.text))
        if deal is None:
            bot.send_message(message.chat.id, text=strings.deal_not_found)
            return
        bot.send_message(
            message.chat.id,
            text=strings.dispute_info.format(
                deal=functions.format_deal_info(deal, strings)
            ),
            reply_markup=keyboards.solve_dispute(strings),
            parse_mode="HTML",
        )


def output(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    if not functions.is_wallet_amount(message.text):
        bot.send_message(message.chat.id, text=strings.cancel)
        return

    user = queries.get_user(message.chat.id)
    output_size = Decimal(message.text)

    if output_size > user.balance:
        bot.send_message(message.chat.id, text=strings.not_enough_on_balance)
        return

    if float(output_size) < 1:
        bot.send_message(
            message.chat.id,
            text=strings.minimal_withdrawal_amount,
        )
        return

    user.balance -= output_size
    user.save()
    bot.send_message(message.chat.id, text=strings.perform_withdrawal)
    queries.new_withdrawal(user.chat_id, user.blockchain_address, output_size)


def register_transaction_hash(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    if message.text.startswith("-"):
        bot.send_message(message.chat.id, text=strings.cancel)
        return

    hash_str = message.text[2:]

    if queries.get_transaction(hash_str) is not None:
        bot.send_message(
            message.chat.id, text=strings.this_transaction_already_registered
        )
        return

    web3 = functions.get_web3_remote_provider()
    try:
        transaction = web3.eth.get_transaction(bytes.fromhex(hash_str))
    except TransactionNotFound:
        bot.send_message(message.chat.id, text=strings.transaction_not_found)
        return

    abi = [
        {
            "constant": False,
            "inputs": [
                {"name": "to", "type": "address"},
                {"name": "value", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "type": "function",
        }
    ]
    contract = functions.get_token_contract(web3, abi)
    transaction_info = contract.decode_function_input(transaction.input)[1]

    if transaction_info["to"] != config.SYSTEM_WALLET_ADDRESS:
        bot.send_message(message.chat.id, text=strings.incorrect_recipient)
        return

    user = queries.get_user(message.chat.id)
    amount = Decimal(str(transaction_info["value"] / 10**18))
    queries.new_transaction(hash_str, user.chat_id, amount)
    user.balance += amount
    user.save()
    bot.send_message(message.chat.id, text=strings.complete_input.format(amount=amount))


def change_address(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    if message.text.startswith("-"):
        bot.send_message(message.chat.id, text=strings.cancel)
        return

    user = queries.get_user(message.chat.id)
    user.blockchain_address = message.text
    user.save()
    bot.send_message(message.chat.id, text=strings.blockchain_address_sets_up)


def search_seller_for_init(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    second_user = functions.search_second_user(message, strings)

    if second_user is None:
        return

    queries.new_deal(message.chat.id, second_user.chat_id)

    bot.send_message(
        message.chat.id,
        strings.customer_preview.format(
            user=functions.format_user_info(second_user, strings)
        ),
        reply_markup=keyboards.sentence_deal(strings),
        parse_mode="HTML",
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=strings.disable_keyboard,
        reply_markup=types.ReplyKeyboardRemove(),
    )


def search_customer_for_init(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    second_user = functions.search_second_user(message, strings)

    if second_user is None:
        return

    queries.new_deal(second_user.chat_id, message.chat.id)

    bot.send_message(
        message.chat.id,
        strings.seller_preview.format(
            user=functions.format_user_info(second_user, strings)
        ),
        reply_markup=keyboards.sentence_deal(strings),
        parse_mode="HTML",
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=strings.disable_keyboard,
        reply_markup=types.ReplyKeyboardRemove(),
    )


def set_price(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    if message.text.startswith("-") or not functions.is_wallet_amount(message.text):
        bot.send_message(message.chat.id, text=strings.cancel)
        return

    deal = queries.get_user(message.chat.id).seller_deal
    if deal.amount != 0:
        return

    deal.amount = float(message.text)
    deal.save()

    bot.send_message(
        deal.seller_id,
        text=strings.amount_of_deal_set.format(
            deal=functions.format_deal_info(deal, strings)
        ),
        reply_markup=keyboards.seller_panel(strings),
        parse_mode="HTML",
    )
    strings = get_strings(deal.customer.language)
    bot.send_message(
        deal.customer_id,
        text=strings.amount_of_deal_set.format(
            deal=functions.format_deal_info(deal, strings)
        ),
        reply_markup=keyboards.customer_panel(strings),
        parse_mode="HTML",
    )


def add_review(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    deal = queries.get_user(message.chat.id).customer_deal
    if deal.status != Deal.Status.review:
        return

    if message.text == "-":
        review = None
        bot.send_message(
            chat_id=deal.customer_id,
            text=strings.customer_cancel_review_customer,
            reply_markup=keyboards.menu(strings),
        )
        strings = get_strings(deal.seller.language)
        bot.send_message(message.chat.id, text=strings.cancel)
        bot.send_message(
            deal.seller_id,
            text=strings.customer_cancel_review_seller,
            reply_markup=keyboards.menu(strings),
        )

    else:
        review = message.text

    offer = queries.new_offer(deal, review)
    if review is not None:
        bot.send_message(
            message.chat.id,
            text=strings.review_sent_customer,
            reply_markup=keyboards.menu(strings),
        )
        strings = get_strings(deal.seller.language)
        bot.send_message(
            offer.seller_id,
            text=strings.review_sent_seller.format(text=message.text),
            reply_markup=keyboards.menu(strings),
        )


def input_referral(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    if message.text.startswith("-"):
        bot.send_message(message.chat.id, text=strings.cancel)
        return

    ref_code = message.text.upper()
    referral = queries.get_user_by_referral_code(ref_code)
    if referral is None:
        bot.send_message(message.chat.id, text=strings.referral_not_found_error)
        return

    if referral.chat_id == message.chat.id:
        bot.send_message(message.chat.id, text=strings.referral_yourself_error)
        return

    user.referral_id = referral.chat_id
    user.save()

    bot.send_message(message.chat.id, text=strings.referral_success)

    strings = get_strings(referral.language)
    bot.send_message(
        referral.chat_id,
        text=strings.new_referral.format(
            referrals_count=len(queries.get_referrals(referral.chat_id))
        ),
    )


def change_referral(message):
    user = queries.get_user(message.chat.id)
    strings = get_strings(user.language)
    if message.text.startswith("-") or message.text.isdigit():
        bot.send_message(message.chat.id, text=strings.cancel)
        return

    ref_code = message.text.upper()
    if queries.get_user_by_referral_code(ref_code) not in (None, user):
        bot.send_message(message.chat.id, text=strings.referral_not_unique_error)
        return

    user.referral_code = ref_code
    user.save()
    bot.send_message(message.chat.id, text=strings.edit_referral_success)
