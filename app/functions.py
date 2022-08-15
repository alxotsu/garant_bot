from app import config


def check_admin_permission(chat_id):
    return chat_id in (config.ADMIN_FIRST_CHAT_ID, config.ADMIN_SECOND_CHAT_ID)


def check_user_blocks(user):
    if user.banned:
        return "⛔️ К сожалению, Вы получили блокировку!"
    if user.customer_deal is not None or user.seller_deal is not None:
        return "⛔️ Вы не можете взаимодействовать с ботом, пока не завершите сделку!"
