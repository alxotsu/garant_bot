from .models import *
from .models import session


def get_user(chat_id):
    return session.query(User).filter_by(chat_id=chat_id).first()


def get_all_users():
    return session.query(User).filter_by(banned=False).all()


def get_all_users_count():
    return session.query(User).filter_by(banned=False).count()


def new_user(chat_id):
    user = get_user(chat_id)
    if user is None:
        user = User(chat_id=chat_id)
        session.add(user)
        session.commit()
    return user


def get_offers_count():
    return session.query(Offer).all().count()


def get_deal(deal_id):
    return session.query(Deal).filter_by(id=deal_id).first()
