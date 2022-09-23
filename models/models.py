import enum
import datetime

import sqlalchemy as sql
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL

__all__ = ["User", "Deal", "Offer", "Withdrawal", "Transaction"]

engine = create_engine(DATABASE_URL)
Base = declarative_base(bind=engine)
session = sessionmaker(bind=engine)()


class SaveDeleteModelMixin:
    def save(self):
        session.add(self)
        session.commit()
        return self

    def delete(self):
        session.delete(self)
        session.commit()


class User(Base, SaveDeleteModelMixin):
    __tablename__ = "user"

    class Language(enum.Enum):
        ru = "ru"
        en = "en"

    chat_id = sql.Column(sql.BIGINT, primary_key=True)
    balance = sql.Column(sql.DECIMAL, default=0, nullable=False)
    blockchain_address = sql.Column(sql.String(64))
    banned = sql.Column(sql.Boolean, nullable=False, default=False)
    language = sql.Column(sql.Enum(Language), default=Language.ru, nullable=False)

    customer_deal = sql.orm.relationship(
        "Deal",
        back_populates="customer",
        uselist=False,
        foreign_keys="Deal.customer_id",
    )
    seller_deal = sql.orm.relationship(
        "Deal", back_populates="seller", uselist=False, foreign_keys="Deal.seller_id"
    )

    customer_offers = sql.orm.relationship(
        "Offer", back_populates="customer", foreign_keys="Offer.customer_id"
    )
    seller_offers = sql.orm.relationship(
        "Offer", back_populates="seller", foreign_keys="Offer.seller_id"
    )

    withdrawals = sql.orm.relationship("Withdrawal", back_populates="user")
    transactions = sql.orm.relationship("Transaction", back_populates="user")


class Deal(Base, SaveDeleteModelMixin):
    __tablename__ = "deal"

    class Status(enum.Enum):
        new = "new"
        open = "open"
        dispute = "dispute"
        review = "review"
        success = "success"

    id = sql.Column(sql.Integer, primary_key=True)
    customer_id = sql.Column(sql.BIGINT, sql.ForeignKey("user.chat_id"), nullable=False)
    seller_id = sql.Column(sql.BIGINT, sql.ForeignKey("user.chat_id"), nullable=False)
    amount = sql.Column(sql.DECIMAL, default=0, nullable=False)
    status = sql.Column(sql.Enum(Status), default=Status.open, nullable=False)

    customer = sql.orm.relationship(
        "User", back_populates="customer_deal", foreign_keys="Deal.customer_id"
    )
    seller = sql.orm.relationship(
        "User", back_populates="seller_deal", foreign_keys="Deal.seller_id"
    )


class Offer(Base, SaveDeleteModelMixin):
    __tablename__ = "offer"

    id = sql.Column(sql.Integer, primary_key=True)
    customer_id = sql.Column(sql.BIGINT, sql.ForeignKey("user.chat_id"), nullable=False)
    seller_id = sql.Column(sql.BIGINT, sql.ForeignKey("user.chat_id"), nullable=False)
    amount = sql.Column(sql.DECIMAL, default=0, nullable=False)
    review = sql.Column(sql.String(1024))

    customer = sql.orm.relationship(
        "User", back_populates="customer_offers", foreign_keys="Offer.customer_id"
    )
    seller = sql.orm.relationship(
        "User", back_populates="seller_offers", foreign_keys="Offer.seller_id"
    )


class Withdrawal(Base, SaveDeleteModelMixin):
    __tablename__ = "withdrawal"

    id = sql.Column(sql.Integer, primary_key=True)
    user_id = sql.Column(sql.BIGINT, sql.ForeignKey("user.chat_id"), nullable=False)
    blockchain_address = sql.Column(sql.String(64), nullable=False)
    amount = sql.Column(sql.DECIMAL, default=0, nullable=False)
    create_time = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)
    close_time = sql.Column(sql.DateTime)
    passed = sql.Column(sql.Boolean)

    user = sql.orm.relationship("User", back_populates="withdrawals")


class Transaction(Base, SaveDeleteModelMixin):
    __tablename__ = "transaction"

    hash = sql.Column(sql.String(64), primary_key=True)
    user_id = sql.Column(sql.BIGINT, sql.ForeignKey("user.chat_id"), nullable=False)
    amount = sql.Column(sql.DECIMAL, nullable=False)

    user = sql.orm.relationship("User", back_populates="transactions")
