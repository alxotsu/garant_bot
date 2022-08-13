import telebot

from config import BOT_TOKEN

__all__ = ["bot"]

bot = telebot.TeleBot(BOT_TOKEN)
