from decimal import Decimal

from telebot import types

from models import queries
from handlers import next_step_hadlers
from app.bot import bot
from app import config, transfers
from app import functions
from content.languages import get_strings
from content import keyboards


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    chat_id = message.chat.id
    user = queries.new_user(chat_id)
    strings = get_strings(user.language)

    if message.from_user.username is None:
        bot.send_message(chat_id, strings.require_username)
    else:
        info = functions.check_user_blocks(user)
        if info is not None:
            bot.send_message(chat_id, info)
            return
        bot.send_message(
            chat_id,
            strings.welcome.format(username=message.from_user.first_name),
            reply_markup=keyboards.menu(strings),
        )


@bot.message_handler(commands=["admin"])
def admin(message: types.Message):
    if functions.check_admin_permission(message.chat.id):
        chat_id = message.chat.id
        user = queries.new_user(chat_id)
        strings = get_strings(user.language)

        user = queries.get_user(message.chat.id)
        if user is not None:
            info = functions.check_user_blocks(user)
            if info is not None:
                bot.send_message(message.chat.id, info)
                return

        bot.send_message(
            message.chat.id,
            strings.welcome_admin.format(username=message.from_user.first_name),
            reply_markup=keyboards.admin(strings),
        )


@bot.message_handler(content_types=["text"])
def send_text(message):
    chat_id = message.chat.id
    user = queries.new_user(chat_id)
    strings = get_strings(user.language)

    try:
        info = functions.check_user_blocks(user)
        if info is not None:
            bot.send_message(chat_id, info)
            return
        if message.text == strings.switch_language:
            if user.language == user.Language.ru:
                user.language = user.language.en
            else:
                user.language = user.language.ru
            user.save()

            strings = get_strings(user.language)
            bot.send_message(
                chat_id,
                strings.welcome.format(username=message.from_user.first_name),
                reply_markup=keyboards.menu(strings),
            )

        if message.text == strings.profile:
            bot.send_message(
                chat_id,
                strings.profile_info.format(
                    chat_id=user.chat_id,
                    offers_count=len(user.customer_offers) + len(user.seller_offers),
                    balance=user.balance,
                    address=user.blockchain_address,
                ),
                reply_markup=keyboards.profile(strings),
                parse_mode="HTML",
            )

        elif message.text == strings.perform_deal:
            bot.send_message(
                chat_id,
                strings.in_this_deal_you_are,
                reply_markup=keyboards.init_offer(strings),
            )

        elif message.text == strings.about_us:
            bot.send_message(
                chat_id,
                strings.about,
            )

        elif message.text == strings.show_offers:
            bot.send_message(
                chat_id,
                strings.show_offers_where_you_are,
                reply_markup=keyboards.show_offers(strings),
            )

        elif message.text == strings.ban_system:
            if not functions.check_admin_permission(message.chat.id):
                return
            bot.send_message(
                chat_id,
                text=strings.what_are_you_want_to_do,
                reply_markup=keyboards.bou(strings),
            )

        elif message.text == strings.mailing:
            if not functions.check_admin_permission(message.chat.id):
                return
            msg = bot.send_message(
                chat_id=chat_id,
                text=strings.input_mailing_text,
            )
            bot.register_next_step_handler(
                msg, next_step_hadlers.send_message_for_all_users
            )

        elif message.text == strings.statistics:
            if not functions.check_admin_permission(message.chat.id):
                return
            bot.send_message(
                chat_id=chat_id,
                text=strings.statistics_info.format(
                    users=queries.get_all_users_count(),
                    offers=queries.get_offers_count(),
                ),
            )

        elif message.text == strings.dispute_solving:
            if not functions.check_admin_permission(message.chat.id):
                return
            msg = bot.send_message(
                chat_id,
                text=strings.input_deal_id,
            )
            bot.register_next_step_handler(msg, next_step_hadlers.search_dispute)

        elif message.text == strings.check_system_balance:
            if not functions.check_admin_permission(message.chat.id):
                return

            system_balance = transfers.check_trc20_usdt_system_balance()
            users_balance = 0
            for user in queries.get_all_users():
                if user.balance < 1:
                    continue
                users_balance += user.balance
            users_balance *= Decimal(str(1 - config.TAX_PERCENT / 100))
            difference = system_balance - users_balance

            if difference >= 0.01:
                conclusion = strings.you_can_output_money.format(difference=difference)
            elif difference <= -0.01:
                conclusion = strings.you_must_input_balance.format(
                    difference=-difference
                )
            else:
                conclusion = strings.perfect_balance

            bot.send_message(
                chat_id,
                text=strings.system_wallet_info.format(
                    system_balance=system_balance,
                    users_balance=users_balance,
                    conclusion=conclusion,
                ),
            )

        elif message.text == strings.referral_button:
            bot.send_message(
                chat_id,
                text=strings.referral_info.format(
                    sale=config.REFERRAL_TAX_SALE,
                    bonus=config.REFERRAL_BONUS,
                    referral_code=user.referral_code,
                    referrals_count=len(queries.get_referrals(chat_id)),
                ),
                reply_markup=keyboards.referral(strings, user),
                parse_mode="HTML",
            )

    except Exception:
        bot.send_message(
            chat_id,
            strings.unknown_error.format(admin=config.ADMIN_USERNAME),
        )
        raise
