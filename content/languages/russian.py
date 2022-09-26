from models.models import Deal


class ru:
    # technical
    seller = "продавец"
    customer = "покупатель"
    welcome = "✅ Добро пожаловать, {username}!"
    welcome_admin = "✅ {username}, вы авторизованы."
    cancel = "Отмена..."
    back = "❌ Назад"
    accept = "✅ Принять"
    reject = "❌ Отклонить"
    yes = "Да"
    no = "Нет"
    disable_keyboard = "Отключение клавиатуры..."
    have_deal_now = (
        "⛔️ Вы не можете взаимодействовать с ботом, пока не завершите сделку."
    )
    require_username = (
        "⛔️ Вам необходимо установить Имя пользователя для работы с ботом."
    )
    unknown_error = (
        "⛔️ Произошла ошибка. Повторите запрос.\n\n"
        "Если проблема не решилась, обратитесь в поддержку: @{admin}."
    )
    user_not_found = "⛔️ Пользователь с введённым ChatID не найден."

    # main menu
    profile = "👤 Профиль"
    profile_info = (
        "🧾 Профиль:\n\n"
        "❕ Ваш ChatID - <b><code>{chat_id}</code></b>\n"
        "❕ Проведенных сделок - {offers_count}\n\n"
        "💰 Ваш баланс - {balance} USDT\n"
        "💳 Ваш адрес кошелька - {address}"
    )
    format_user_info = (
        "❕ ChatID - <b><code>{chat_id}</code></b>\n"
        "❕ Имя пользователя - @{username}\n"
        "❕ Проведенных сделок - {offers_count}"
    )
    about_us = "⭐️ О нас"
    about = (
        "По всем вопросам: @{admin}.\nНаш чат: {chat}.\n"
        "Инструкция по использованию: {instruction}.\n"
    )
    show_offers = "💵 Прошедшие сделки"
    show_offers_where_you_are = "Вывести ваши последние сделки где вы..."
    no_offers = "⛔️ Сделок не обнаружено."
    offer_info = "💠 C @{username} (ChatID - {user_id}) на сумму {amount} USDT.\n\n"
    switch_language = "🇺🇸 switch language"

    # change address
    change_wallet_button = "Изменить адрес кошелька"
    change_wallet = "📄 Введите адрес кошелька.\nДля отмены напишите \"-\" без кавычек."
    blockchain_address_sets_up = "✅ Адрес в блокчейне установлен."

    # input balance
    input_balance_button = "Пополнение баланса"
    wallet_input = (
        "⚠️ Пополнение баланса\n"
        "Чтобы пополнить баланс, отправьте желаемую сумму на кошелёк сервиса в Binance smart chain.\n"
        "После этого Вам нужно скопировать ID транзакции и вставить его здесь.\n\n"
        "👉 Адрес кошелька - <b><code>{address}</code></b>\n\nДля отмены напишите \"-\" без кавычек."
    )
    this_transaction_already_registered = (
        "⛔️ Эта транзакция уже была зарегистрирована в боте."
    )
    transaction_not_found = "⛔️ Транзакция с таким ID не найдена."
    incorrect_recipient = "⛔️ Перевод был совершён не на кошелёк сервиса."
    complete_input = "Баланс был успешно пополнен на {amount} USDT."

    # withdrawals
    withdrawal_button = "Вывод средств"
    you_have_not_wallet = "⛔️ У Вас не указан адрес кошелька для вывода."
    init_withdrawal = (
        "Ваш адрес в блокчейне - {address}.\n"
        "Баланс - {balance} USDT.\n"
        "Введите сумму для вывода. (Для отмены введите любую букву)"
    )
    perform_withdrawal = "✅ Запрос на вывод успешно отправлен."
    withdrawal_error = (
        "⛔️ Вывод {amount} USDT не удался."
        " Проверьте правильность введённого адреса кошелька."
        " в Binance smart chain в своём профиле и повторите попытку."
    )
    minimal_withdrawal_amount = "⛔️ Минимальная сумма для вывода 1 USDT."
    not_enough_on_balance = "⛔️ На балансе недостаточно средств для вывода."
    withdrawal_complete = (
        "{amount} USDT было выведено на кошелёк - "
        "<b><code>{address}</code></b>\n\n"
        "Хэш транзакции - <b><code>{hex_hash}</code></b>"
    )

    # init deal
    perform_deal = "🔒 Провести сделку"
    in_this_deal_you_are = "В этой сделке вы..."
    init_deal = (
        "Введите ChatID пользователя, с которым хотите провести сделку. \n\n"
        "Для отмены напишите \"-\" без кавычек."
    )
    cannot_init_deal_with_yourself = "⛔️ Нельзя начать сделку с самим собой."
    user_already_in_deal = (
        "⛔️ Пользователь с введённым ChatID в данный момент уже участвует в сделке."
    )
    user_banned = "⛔️ Пользователь с введённым ChatID заблокирован."
    customer_preview = "🧾 Профиль:\n\n {user}\n\n🔥В этой сделке вы будете покупателем."
    seller_preview = "🧾 Профиль:\n\n {user}\n\n🔥В этой сделке вы будете продавцом."
    propose_deal = "📝 Предложить сделку"
    deal_proposal_sent = "✅ Предложение о проведении сделки отправлено."
    deal_proposal_received = "✅ Вам отправлено предложение о сделке."
    deal_proposal_info = "{user_info}\n\n🔥 В этой сделке вы {role}."
    deal_accepted = "💰 Сделка {deal_info}"
    format_deal_info = (
        "№{deal_id}\n"
        "❕ Покупатель - @{customer_username} (ChatID <b><code>{customer_id}</code></b>)\n"
        "❕ Продавец - @{seller_username} (ChatID <b><code>{seller_id}</code></b>)\n"
        "💰 Сумма сделки - {amount} USDT\n"
        "📊 Статус сделки - {status}"
    )
    deal_statuses = {
        Deal.Status.new: "Новая",
        Deal.Status.open: "Открыта",
        Deal.Status.dispute: "Начат Спор",
        Deal.Status.review: "Пишется отзыв",
        Deal.Status.success: "Завершена",
    }

    # set deal amount
    set_deal_amount_button = "Указать стоимость"
    deal_amount_already_sets = (
        "⛔️ Вы уже ввели сумму товара и не можете её редактировать."
    )
    set_deal_amount = (
        "Введите сумму сделки. Обратите внимание, сумму сделки можно ввести всего один раз \n\n"
        "Для отмены напишите \"-\" без кавычек."
    )
    amount_of_deal_set = "💥 Была изменена сумма сделки.\n\n💰 Сделка {deal}"

    # pay deal
    pay_deal = "Оплатить товар"
    seller_not_set_amount = "⛔️ Продавец не указал сумму."
    fund_already_payed = (
        "Вы уже оплатили товар, продавец обязан вам его передать."
        "Если продавец отказывается передать товар, откройте спор."
    )
    not_enough_for_pay = (
        "📉 Вам необходимо пополнить баланс.\n💰 Ваш баланс - {balance} USDT\n"
        "💳 Необходимый баланс - {amount} USDT\n\nВам необходимо отменить сделку."
    )
    fund_payed_seller = (
        "✅ Покупатель оплатил сделку! Теперь Вам необходимо передать товар."
    )
    fund_payed_customer = (
        "✅ Товар был успешно оплачен, ожидайте получения товара."
        "Если товар оказался не валид, или продавец Вас кинул в ЧС, откройте спор."
    )

    # confirm fund
    confirm_fund_button = "Подтвердить получение"
    confirm_fund = (
        "Вы уверены что получили товар, и он валидный? "
        "Если нет, или условия не соблюдены, то вам необходимо открыть спор."
    )
    confirm_reject = "Вы не оплатили сделку, или над ней ведётся спор."
    fund_confirmed_customer = (
        "✅ Сделка успешно завершена!\n" "📝 Хотите оставить отзыв о продавце?"
    )
    fund_confirmed_seller = (
        "✅ Сделка успешно завершена!\n💰 Деньги зачислены на ваш счёт.\n\n"
        "📝 Сейчас покупатель оставляет отзыв, подождите пожалуйста."
    )

    # close deal
    close_deal = "Закрыть сделку"
    cannot_cancel_deal = "⛔️ Сделка уже начата, и не может быть отменена."
    cancel_deal = "⛔️ Сделка отменена."
    close_deal_confirm = "Вы уверены что хотите отменить сделку?"
    close_request_sent = "Запрос на отмену отправлен."
    close_request_received = "{role} предложил отменить сделку."
    deal_canceled_or_dispute_active = "Сделка уже завершена или над ней проходит спор."
    deal_canceled = "✅ Сделка успешно отменена."
    refuse_cancel_deal = "✅ Процесс отмены сделки аннулирован."

    # reviews
    reviews = "📄 Отзывы"
    no_review = "⛔️ Отзывов не обнаружено."
    add_review = "🔥 Напишите отзыв о сделке, для отмены вышлите \"-\" без кавычек."
    cancel_waiting = "💥 Отменить ожидание"
    review_sent_customer = "📝 Отзыв успешно оставлен."
    review_sent_seller = "📝 О вас оставили отзыв.\n\n{text}"
    seller_cancel_review_customer = (
        "❄️ Продавец не захотел ожидать отзыва. Сделка завершена."
    )
    seller_cancel_review_seller = (
        "❄️Ожидание отменено, покупатель не может больше оставить отзыв."
    )
    customer_cancel_review_customer = "❄️ Сделка успешно завершена."
    customer_cancel_review_seller = "❄️ Покупатель отказался оставлять отзыв."

    # disputes
    init_dispute = "Открыть спор"
    dispute_has_been_open = "По вашей сделке начат спор. Если долго ничего не происходит, напишите администратору @{admin}."
    dispute_has_been_open_admin = (
        "Был начат спор.\n\nСделка {info}\n\nСпор инициировал {role}."
    )
    dispute_solving = "Решение спора"
    input_deal_id = "Введите ID сделки.\n\nДля отмены введите \"-\" без кавычек."
    deal_not_found = "⛔️ Сделка не обнаружена."
    dispute_info = "🧾 Информация о сделке {deal}\n\nКто прав в данном споре?"
    customer_dispute_solve_confirm = (
        "Покупатель получит деньги, а сделка будет отменена.\n"
        "Для подтверждения введите ID сделки, для отмены введите \"-\" без кавычек.",
    )
    seller_dispute_solve_confirm = (
        "Продавец получит деньги, а сделка будет отменена.\n"
        "Для подтверждения введите ID сделки, для отмены введите \"-\" без кавычек.",
    )
    dispute_solved_for_you = "✅ Вердикт был вынесен в вашу пользу."
    dispute_solved_seller = "✅ Вердикт был вынесен в пользу продавца."
    dispute_solved_customer = "✅ Вердикт был вынесен в пользу покупателя."
    dispute_status_new = "⛔️ Сделка ещё не открыта."
    dispute_status_open = (
        "⛔️ Передача товара ещё подтверждена. Если Вы считаете,"
        " что другой участник сделки хочет вас обмануть,"
        " закройте сделку и сообщите администратору - @{admin}."
    )
    dispute_status_dispute = "⛔️ Спор уже начат. Если долго ничего не происходит, напишите администратору @{admin}."

    # ban system
    ban_system = "Бан-система"
    what_are_you_want_to_do = "Что вы хотите сделать?"
    ban = "Забанить"
    unban = "Разбанить"
    ban_user = "✅ Пользователь успешно забанен."
    unban_user = "✅ Пользователь успешно разбанен."
    user_id_for_ban = "Введите ChatID пользователя, которого нужно забанить. \n\nДля отмены напишите \"-\" без кавычек."
    user_id_for_unban = (
        "Введите ChatID пользователя, которого нужно разбанить. \n\n"
        "Для отмены напишите \"-\" без кавычек."
    )
    banned = "⛔️ К сожалению, Вы получили блокировку."

    # mailing
    mailing = "Рассылка"
    input_mailing_text = (
        "Введите текст для рассылки.\n\nДля отмены напишите \"-\" без кавычек."
    )
    perform_mailing = "✅ Идёт рассылка..."
    end_mailing = "✅ Рассылка завершена.\nСообщение получили {success} из {all} зарегистрированных пользователей."

    # stats
    statistics = "Статистика"
    statistics_info = "❕ Информация:\n\n❕ Пользователей в боте - {users}\n❕ Проведено сделок - {offers}"

    # system balance
    check_system_balance = "Проверить баланс кошелька"
    you_can_output_money = "Вы можете вывести с системного кошелька {difference} USDT."
    you_must_input_balance = (
        "Настоятельно рекомендуется пополнить системный кошелёк на {difference} USDT."
    )
    perfect_balance = (
        "На системном кошельке ровно столько средств, сколько необходимо для выплат пользователям. "
        "Не рекомендуем снимать с него деньги."
    )
    system_wallet_info = (
        "Баланс сервисного кошелька: {system_balance} USDT.\n\n"
        "Единовременно пользователи могут запросить вывод {users_balance} USDT.\n\n"
        "{conclusion}"
    )

    # referrals
    referral_button = "Реферальная программа"
    referral_info = (
        "💰 Приглашённые пользователи получают скидку {sale}% на комиссию при выводе USDT с баланса.\n\n"
        "💰 При каждом выводе средств приглашённым пользователем, "
        "пригласивший пользователь получает бонус в размере {bonus}% от суммы вывода на свой баланс.\n\n"
        "🧾 Ваш промокод <b><code>{referral_code}</code></b>.\n"
        "🧾 Чтобы пригласить пользователя, он должен ввести ваш промокод в этом разделе.\n"
        "🧾 Ваше приглашение подтвердили {referrals_count} пользователей."
    )
    edit_referral_button = "Изменить свой промокод"
    edit_referral = (
        "Введите свой новый промокод. Промокод должен содержать хотя бы одну букву."
        "Для отмены напишите \"-\" без кавычек."
    )
    referral_not_unique_error = "⛔️ Этот промокод уже занят."
    edit_referral_success = "Ваш промокод изменён."
    referral_input_referral_code_button = "Ввести промокод"
    referral_input_referral_code = (
        "Введите промокод пользователя, который вас пригласил. "
        "Для отмены напишите \"-\" без кавычек."
    )
    referral_not_found_error = (
        "⛔️ Пользователя с таким реферальным кодом не обнаружено."
    )
    referral_yourself_error = "⛔️ Вы не можете пригласить сами себя."
    referral_success = "Реферальная программа подключена."
    new_referral = (
        "Новый пользователь ввёл ваш промокод.\n"
        "Ваше приглашение подтвердили {referrals_count} пользователей."
    )
    referral_withdrawal = (
        "Ваш реферал вывел {amount} USDT. Вы получаете бонус {bonus} USDT."
    )
