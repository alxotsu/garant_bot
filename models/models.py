import enum
import datetime

import sqlalchemy as sql
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.config import DATABASE_URL

__all__ = ['User', 'Deal', 'Review', 'Offer', 'Payment', 'Withdrawal']

engine = create_engine(DATABASE_URL)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'user'

    chat_id = sql.Column(sql.Integer, primary_key=True)
    balance = sql.Column(sql.DECIMAL, default=0, nullable=False)
    metamask_address = sql.Column(sql.String(42))
    banned = sql.Column(sql.Boolean, nullable=False, default=False)

    customer_deal = sql.orm.relationship(
        "Deal", back_populates="customer", uselist=False
    )
    seller_deal = sql.orm.relationship("Deal", back_populates="seller", uselist=False)
    payments = sql.orm.relationship("Payment", back_populates="user")
    withdrawals = sql.orm.relationship("Withdrawal", back_populates="user")


class Deal(Base):
    __tablename__ = 'deal'

    class Status(enum.Enum):
        one = 1
        two = 2
        three = 3

    id = sql.Column(sql.Integer, primary_key=True)
    customer_id = sql.Column(sql.Integer, sql.ForeignKey("user.chat_id"), nullable=False)
    seller_id = sql.Column(sql.Integer, sql.ForeignKey("user.chat_id"), nullable=False)
    amount = sql.Column(sql.DECIMAL, default=0, nullable=False)
    status = sql.Column(sql.Integer, sql.Enum(Status))

    customer = sql.orm.relationship("User", back_populates="customer_deal")
    seller = sql.orm.relationship("User", back_populates="seller_deal")
    review = sql.orm.relationship("Review", back_populates="deal", uselist=False)
    offers = sql.orm.relationship("Offer", back_populates="offers")


class Review(Base):
    __tablename__ = 'review'

    deal_id = sql.Column(sql.Integer, sql.ForeignKey("deal.id"), primary_key=True)
    review_text = sql.Column(sql.String(1024), nullable=False)

    deal = sql.orm.relationship("deal", back_populates="review")


class Offer(Base):
    __tablename__ = 'offer'

    id = sql.Column(sql.Integer, primary_key=True)
    deal_id = sql.Column(sql.Integer, sql.ForeignKey("deal.id"), nullable=False)
    amount = sql.Column(sql.DECIMAL, default=0, nullable=False)

    deal = sql.orm.relationship("deal", back_populates="offers")


class Payment(Base):
    __tablename__ = 'payment'

    id = sql.Column(sql.Integer, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("user.chat_id"), nullable=False)
    metamask_address = sql.Column(sql.String(42), nullable=False)
    close_time = sql.Column(sql.DateTime)

    user = sql.orm.relationship("User", back_populates="payments")


class Withdrawal(Base):
    __tablename__ = 'withdrawal'

    id = sql.Column(sql.Integer, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("user.chat_id"), nullable=False)
    metamask_address = sql.Column(sql.String(42), nullable=False)
    amount = sql.Column(sql.DECIMAL, default=0, nullable=False)
    create_time = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)
    close_time = sql.Column(sql.DateTime)

    user = sql.orm.relationship("User", back_populates="withdrawals")
