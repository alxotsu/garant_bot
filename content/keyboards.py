from telebot import types


def menu(strings):
    menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_kb.add(
        types.KeyboardButton(strings.show_offers),
        types.KeyboardButton(strings.profile),
        types.KeyboardButton(strings.about_us),
        types.KeyboardButton(strings.perform_deal),
        types.KeyboardButton(strings.referral_button),
        types.KeyboardButton(strings.switch_language),
    )
    return menu_kb


def admin(strings):
    admin_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(
        types.KeyboardButton(strings.ban_system),
        types.KeyboardButton(strings.mailing),
        types.KeyboardButton(strings.statistics),
        types.KeyboardButton(strings.dispute_solving),
        types.KeyboardButton(strings.check_system_balance),
    )
    return admin_kb


def profile(strings):
    profile_kb = types.InlineKeyboardMarkup(row_width=2)
    profile_kb.add(
        types.InlineKeyboardButton(strings.withdrawal_button, callback_data="output"),
        types.InlineKeyboardButton(strings.input_balance_button, callback_data="input"),
        types.InlineKeyboardButton(
            strings.change_wallet_button, callback_data="change_address"
        ),
    )
    return profile_kb


def init_offer(strings):
    init_offer_kb = types.InlineKeyboardMarkup()
    init_offer_kb.add(
        types.InlineKeyboardButton(
            f"💎 {strings.customer}", callback_data="customer_offer_init"
        ),
        types.InlineKeyboardButton(
            f"💰 {strings.seller}", callback_data="seller_offer_init"
        ),
    )
    return init_offer_kb


def show_offers(strings):
    show_offers_kb = types.InlineKeyboardMarkup()
    show_offers_kb.add(
        types.InlineKeyboardButton(
            f"💎 {strings.customer}", callback_data="customer_offer_get"
        ),
        types.InlineKeyboardButton(
            f"💰 {strings.seller}", callback_data="seller_offer_get"
        ),
    )
    return show_offers_kb


def bou(strings):
    bou_kb = types.InlineKeyboardMarkup(row_width=2)
    bou_kb.add(
        types.InlineKeyboardButton(strings.ban, callback_data="ban"),
        types.InlineKeyboardButton(strings.unban, callback_data="unban"),
    )
    return bou_kb


def solve_dispute(strings):
    solve_dispute_kb = types.InlineKeyboardMarkup(row_width=2)
    solve_dispute_kb.add(
        types.InlineKeyboardButton(
            f"💎 {strings.customer}", callback_data="customer_solve_dispute"
        ),
        types.InlineKeyboardButton(
            f"💰 {strings.seller}", callback_data="seller_solve_dispute"
        ),
    )
    return solve_dispute_kb


def change_address(strings):
    change_address_kb = types.InlineKeyboardMarkup()
    change_address_kb.add(
        types.InlineKeyboardButton(
            strings.change_wallet_button, callback_data="change_address"
        )
    )
    return change_address_kb


def sentence_deal(strings):
    sentence_deal_kb = types.InlineKeyboardMarkup(row_width=2)
    sentence_deal_kb.add(
        types.InlineKeyboardButton(strings.propose_deal, callback_data="proposal"),
        types.InlineKeyboardButton(strings.reviews, callback_data="reviews"),
        types.InlineKeyboardButton(strings.back, callback_data="cancel_deal"),
    )
    return sentence_deal_kb


def cancel_deal(strings):
    cancel_deal_kb = types.InlineKeyboardMarkup(row_width=2)
    cancel_deal_kb.add(
        types.InlineKeyboardButton(strings.back, callback_data="refuse_deal"),
    )
    return cancel_deal_kb


def accept_deal(strings):
    accept_deal_kb = types.InlineKeyboardMarkup()
    accept_deal_kb.add(
        types.InlineKeyboardButton(strings.accept, callback_data="accept_deal"),
        types.InlineKeyboardButton(strings.reject, callback_data="refuse_deal"),
    )
    return accept_deal_kb


def seller_panel(strings):
    seller_panel_kb = types.InlineKeyboardMarkup(row_width=2)
    seller_panel_kb.add(
        types.InlineKeyboardButton(strings.init_dispute, callback_data="open_dispute"),
        types.InlineKeyboardButton(strings.close_deal, callback_data="close_deal"),
        types.InlineKeyboardButton(
            strings.set_deal_amount_button, callback_data="set_price"
        ),
    )
    return seller_panel_kb


def customer_panel(strings):
    customer_panel_kb = types.InlineKeyboardMarkup(row_width=2)
    customer_panel_kb.add(
        types.InlineKeyboardButton(strings.pay_deal, callback_data="pay"),
        types.InlineKeyboardButton(strings.close_deal, callback_data="close_deal"),
        types.InlineKeyboardButton(strings.init_dispute, callback_data="open_dispute"),
        types.InlineKeyboardButton(
            strings.confirm_fund_button, callback_data="confirm_fund"
        ),
    )
    return customer_panel_kb


def confirm_fund(strings):
    confirm_fund_kb = types.InlineKeyboardMarkup()
    confirm_fund_kb.add(
        types.InlineKeyboardButton(
            strings.accept, callback_data="confirm_confirm_fund"
        ),
        types.InlineKeyboardButton(
            f"❌ {strings.init_dispute}", callback_data="open_dispute"
        ),
    )
    return confirm_fund_kb


def choice_close_deal(strings):
    choice_close_deal_kb = types.InlineKeyboardMarkup()
    choice_close_deal_kb.add(
        types.InlineKeyboardButton(
            f"✅ {strings.yes}", callback_data="close_close_deal"
        ),
        types.InlineKeyboardButton(f"❌ {strings.no}", callback_data="self_delete"),
    )
    return choice_close_deal_kb


def add_review(strings):
    add_review_kb = types.InlineKeyboardMarkup(row_width=2)
    add_review_kb.add(
        types.InlineKeyboardButton(f"✨ {strings.yes}", callback_data="add_review"),
        types.InlineKeyboardButton(f"💤 {strings.no}", callback_data="no_review"),
    )
    return add_review_kb


def cancel_wait(strings):
    cancel_wait_kb = types.InlineKeyboardMarkup()
    cancel_wait_kb.add(
        types.InlineKeyboardButton(strings.cancel_waiting, callback_data="no_review"),
    )
    return cancel_wait_kb


def choice_accept_cancel(strings):
    choice_accept_cancel_kb = types.InlineKeyboardMarkup()
    choice_accept_cancel_kb.add(
        types.InlineKeyboardButton(strings.accept, callback_data="accept_close"),
        types.InlineKeyboardButton(strings.reject, callback_data="refuse_close"),
    )
    return choice_accept_cancel_kb


def referral(strings, user):
    referral_kb = types.InlineKeyboardMarkup()
    if user.referral_id is None:
        referral_kb.add(
            types.InlineKeyboardButton(
                strings.referral_input_chat_id_button, callback_data="input_referral"
            ),
        )
    referral_kb.add(
        types.InlineKeyboardButton(strings.back, callback_data="self_delete"),
    )
    return referral_kb
