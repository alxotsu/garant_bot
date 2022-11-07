from models.models import Deal


class en:
    # technical
    seller = "seller"
    customer = "buyer"
    welcome = "✅ Welcome, {username}!"
    welcome_admin = "✅ {username}, you are logged in."
    cancel = "Cancel..."
    back = "❌ Back"
    accept = "✅ Accept"
    reject = "❌ Reject"
    yes = "Yes"
    no = "No"
    disable_keyboard = "Keyboard disable..."
    have_deal_now = "⛔️ You cannot interact with the bot until you complete the deal."
    require_username = "⛔️ You need to set a Username to work with the bot."
    unknown_error = (
        "⛔️ An error has occurred. Repeat the request.\n\n"
        "If the problem persists, contact support: @{admin}."
    )
    user_not_found = "⛔️ The user with the ChatID entered was not found."

    # main menu
    profile = "👤 Profile"
    profile_info = (
        "🧾 Profile:\n\n"
        "❕  Your ChatID - <b><code>{chat_id}</code></b>\n"
        "❕ Completed deals - {offers_count}\n\n"
        "💰 Your balance is {balance} USDT\n"
        "💳 Your wallet address - {address}"
    )
    format_user_info = (
        "❕ ChatID - <b><code>{chat_id}</code></b>\n"
        "❕ Username - @{username}\n"
        "❕ Completed deals - {offers_count}"
    )
    about_us = "⭐️ About us"
    about = (
        "For all questions: @{admin}\n"
        "Email: {email}\n"
        "Our chat: {chat}\n"
        "Instructions for use: {instruction}"
    )
    show_offers = "💵 Deals"
    show_offers_where_you_are = "Show your latest deals where are you..."
    no_offers = "⛔️ No deals detected."
    offer_info = "💠 With @{username} (ChatID - {user_id}) for {amount} USDT.\n\n"
    switch_language = "🇷🇺 сменить язык"

    # change address
    change_wallet_button = "Change wallet address"
    change_wallet = (
        "📄 Enter the wallet address.\nTo cancel, write \"-\" without quotes."
    )
    blockchain_address_sets_up = "✅ The address in the blockchain is set."

    # input balance
    input_balance_button = "Balance top up"
    wallet_input = (
        "⚠️ Balance top up\n"
        "To replenish the balance, send the desired amount to the service wallet in TRC20.\n"
        "After that, you need to copy the transaction ID and paste it here.\n\n"
        "👉 Wallet address - <b><code>{address}</code></b>\n\n To cancel, write \"-\" without quotes."
    )
    this_transaction_already_registered = (
        "⛔️ This transaction has already been registered in the bot."
    )
    transaction_not_found = "⛔️ Transaction with such ID was not found."
    incorrect_recipient = "⛔️ The transfer was not made to the service's wallet."
    complete_input = "The balance was successfully replenished to {amount} USDT."

    # withdrawals
    withdrawal_button = "Withdrawal of funds"
    you_have_not_wallet = "⛔️ You have not specified a wallet address for withdrawal."
    init_withdrawal = (
        "Your blockchain address is {address}.\n"
        "Balance is {balance} USDT.\n"
        "Enter the amount to withdraw. (To cancel, enter any letter)"
    )
    perform_withdrawal = "✅ The withdrawal request has been sent successfully."
    withdrawal_error = (
        "⛔️ Withdrawal of {amount} USDT failed."
        " Check the correctness of the entered wallet address"
        " in TRC20 in your profile and try again.\n"
        "If that's exactly not the problem, write to the support service: {admin}"
    )
    minimal_withdrawal_amount = "⛔️ The minimum withdrawal amount is 2 USDT."
    not_enough_on_balance = (
        "⛔️ There are not enough funds on the balance for withdrawal."
    )
    withdrawal_complete = (
        "{amount} USDT was withdrawn to the wallet - "
        "<b><code>{address}</code></b>\n\n"
        "Transaction hash - <b><code>{hex_hash}</code></b>"
    )

    # init deal
    perform_deal = "🔒 Make a deal"
    in_this_deal_you_are = "In this deal you are..."
    init_deal = (
        "Enter the ChatID of the user with whom you want to conduct a deal. \n\n"
        "To cancel, write \"-\" without quotes."
    )
    cannot_init_deal_with_yourself = "⛔️ You can't start a deal with yourself."
    user_already_in_deal = (
        "⛔️ The user with the entered chatId is already"
        "participating in the deal at the moment."
    )
    user_banned = "⛔️ The user with the Chat ID entered is blocked."
    customer_preview = "🧾 Profile:\n\n {user}\n\n🔥In this deal you will be the buyer."
    seller_preview = "🧾 Profile:\n\n {user}\n\n🔥In this deal you will be the seller."
    propose_deal = "📝 Offer a deal"
    deal_proposal_sent = "✅ The offer to conduct the deal has been sent."
    deal_proposal_received = "✅ A deal offer has been sent to you."
    deal_proposal_info = "{user_info}\n\n🔥 In this deal you are the {role}."
    deal_accepted = "💰 The deal {deal_info}"
    format_deal_info = (
        "№{deal_id}\n"
        "❕ The buyer - @{customer_username} (ChatID <b><code>{customer_id}</code></b>)\n"
        "❕ The seller - @{seller_username} (ChatID <b><code>{seller_id}</code></b>)\n"
        "💰 Deal amount - {amount} USDT\n"
        "📊 Deal status - {status}"
    )
    deal_statuses = {
        Deal.Status.new: "New",
        Deal.Status.open: "Open",
        Deal.Status.dispute: "Dispute",
        Deal.Status.review: "Review writing",
        Deal.Status.success: "Success",
    }

    # set deal amount
    set_deal_amount_button = "Set the amount"
    deal_amount_already_sets = (
        "⛔️ You have already entered the amount of the product and cannot edit it."
    )
    set_deal_amount = (
        "Enter the deal amount. Please note that the deal amount can be entered only once.\n\n"
        "To cancel, write \"-\" without quotes."
    )
    amount_of_deal_set = "💥 The deal amount has been changed.\n\n💰 The deal {deal}"

    # pay deal
    pay_deal = "Pay for the goods"
    seller_not_set_amount = "⛔️ The seller did not set the amount."
    fund_already_payed = (
        "You have already paid for the goods, the seller is obliged to give it to you."
        "If the seller refuses to hand over the goods, open a dispute."
    )
    not_enough_for_pay = (
        "📉 You need to top up your balance.\n💰 Your balance is {balance} USDT\n"
        "💳 The required balance is {amount} USDT\n\nYou need to cancel the deal."
    )
    fund_payed_seller = (
        "✅ The buyer paid for the deal! Now you need to transfer the goods."
    )
    fund_payed_customer = (
        "✅ The product has been successfully paid for, expect to receive the product."
        "If the product was not valid, or the seller has blacklisted you, open a dispute."
    )

    # confirm fund
    confirm_fund_button = "Confirm receipt"
    confirm_fund = (
        "Are you sure that you have received the product and it is valid? "
        "If not, or the conditions are not met, then you need to open a dispute."
    )
    confirm_reject = "You have not paid for the deal, or there is a dispute over it."
    fund_confirmed_customer = (
        "✅ The deal has been successfully completed!\n"
        "📝 Do you want to leave a review about the seller?"
    )
    fund_confirmed_seller = (
        "✅ The deal has been successfully completed!\n"
        "💰 The money has been credited to your account.\n\n"
        "📝 Now the buyer leaves a review, please wait."
    )

    # close deal
    close_deal = "Close the deal"
    cannot_cancel_deal = "⛔️ The deal has already started, and cannot be canceled."
    cancel_deal = "⛔️ The deal canceled."
    close_deal_confirm = "Are you sure you want to cancel the deal?"
    close_request_sent = "The cancellation request has been sent."
    close_request_received = "The {role} offered to cancel the deal."
    deal_canceled_or_dispute_active = (
        "The deal has already been completed or there is a dispute over it."
    )
    deal_canceled = "✅ The deal canceled."
    refuse_cancel_deal = "✅ The deal cancellation process has been canceled."

    # reviews
    reviews = "📄 Reviews"
    no_review = "⛔️ No reviews found."
    add_review = (
        "🔥 Write a review about the deal. To cancel, send \"-\" without quotes."
    )
    cancel_waiting = "💥 Cancel waiting"
    review_sent_customer = "📝 The review was successfully left."
    review_sent_seller = "📝 The buyer left a review about you.\n\n{text}"
    seller_cancel_review_customer = (
        "❄️ The seller did not want to wait for a review. The deal is completed."
    )
    seller_cancel_review_seller = (
        "❄️The waiting is canceled, the buyer can no longer leave a review."
    )
    customer_cancel_review_customer = "❄️ The deal has been successfully completed."
    customer_cancel_review_seller = "❄️ The buyer refused to leave a review."

    # disputes
    init_dispute = "Open dispute"
    dispute_has_been_open = (
        "A dispute has been initiated on your deal."
        "If nothing happens for a long time, write to the administrator @{admin}."
    )
    dispute_has_been_open_admin = (
        "A dispute was started.\n\nThe deal {info}\n\nDispute initiated by {role}."
    )
    dispute_solving = "Dispute resolution"
    input_deal_id = "Enter the deal ID.\n\nTo cancel, type \"-\" without quotes."
    deal_not_found = "⛔️ The deal is not found."
    dispute_info = (
        "🧾 Information about the deal {deal}\n\nWho is right in this dispute?"
    )
    customer_dispute_solve_confirm = (
        "The buyer will receive the money, and the deal will be canceled.\n"
        "To confirm, enter the deal ID, to cancel, enter \"-\" without quotes.",
    )
    seller_dispute_solve_confirm = (
        "The seller will receive the money, and the deal will be canceled.\n"
        "To confirm, enter the deal ID, to cancel, enter \"-\" without quotes.",
    )
    dispute_solved_for_you = "✅ The verdict was in your favor."
    dispute_solved_seller = "✅ The verdict was in favor of the seller."
    dispute_solved_customer = "✅ The verdict was in favor of the buyer."
    dispute_status_new = "⛔️ The deal is not open yet."
    dispute_status_open = (
        "⛔️ The transfer of the goods is still confirmed. If you think"
        " that another participant in the deal wants to deceive you,"
        " close the deal and inform the administrator - @{admin}"
    )
    dispute_status_dispute = (
        "⛔️ The dispute has already begun."
        "If nothing happens for a long time, write to the administrator @{admin}."
    )

    # ban system
    ban_system = "Ban-system"
    what_are_you_want_to_do = "What do you want to do?"
    ban = "Ban"
    unban = "Unban"
    ban_user = "✅ The user has been successfully banned."
    unban_user = "✅ The user has been successfully unbanned."
    user_id_for_ban = "Enter the Chat ID of the user you want to ban.\n\nTo cancel, write \"-\" without quotes."
    user_id_for_unban = (
        "Enter the Chat ID of the user you want to unban.\n\n"
        "To cancel, write \"-\" without quotes."
    )
    banned = "⛔️ Unfortunately, you have received a lock."

    # mailing
    mailing = "Mailing"
    input_mailing_text = (
        "Enter the text for the newsletter.\n\nTo cancel, write \"-\" without quotes."
    )
    perform_mailing = "✅ mailing..."
    end_mailing = "✅ The newsletter is completed.\nThe message was received by {success} from {all} registered users."

    # stats
    statistics = "Statistics"
    statistics_info = (
        "❕ Information:\n\n❕ Users in the bot - {users}\n❕ Conducted deals - {offers}"
    )

    # system balance
    check_system_balance = "Check wallet balance"
    you_can_output_money = "You can withdraw from the system wallet {difference} USDT."
    you_must_input_balance = (
        "It is strongly recommended to top up the system wallet with {difference} USDT."
    )
    perfect_balance = (
        "There are exactly as many funds on the system wallet as necessary for payments to users. "
        "We do not recommend withdrawing money from it."
    )
    system_wallet_info = (
        "Service wallet balance: {system_balance} USDT.\n\n"
        "At the same time, users can request the withdrawal of {users_balance} USDT.\n\n"
        "{conclusion}"
    )

    # referrals
    referral_button = "Referral program"
    referral_info = (
        "💰 Invited users receive a {sale}% discount on commission when withdrawing USDT from the balance.\n\n"
        "💰 With each withdrawal of funds by your referral, "
        "you receive a bonus of {bonus}% of the withdrawal amount to your balance.\n\n"
        "🧾 Your promo code is <b><code>{referral_code}</code></b>.\n"
        "🧾 To invite a user, they must enter your promo code in this section.\n"
        "🧾 Your invitation was confirmed by {referrals_count} users."
    )
    edit_referral_button = "Change your promo code"
    edit_referral = (
        "Enter your new promo code. The promo code must contain at least one letter."
        "To cancel, write \"-\" without quotes."
    )
    referral_not_unique_error = "⛔️ This promo code is already taken."
    edit_referral_success = "Your promo code has been changed."
    referral_input_referral_code_button = "Input promo code"
    referral_input_referral_code = (
        "Enter the promo code of the user who invited you. "
        "To cancel, write \"-\" without quotes."
    )
    referral_not_found_error = "⛔️ No user with such referral code was found."
    referral_yourself_error = "⛔️ You can't invite yourself."
    referral_success = "The referral program is enabled."
    new_referral = (
        "A new user has entered your promo code.\n"
        "Your invitation has been confirmed by {referrals_count} users."
    )
    referral_withdrawal = (
        "Your referral has withdrawn {amount} USDT. You get a {bonus} USDT bonus."
    )
