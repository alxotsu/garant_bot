import telebot

from app.config import BOT_TOKEN

__all__ = ["bot"]

bot = telebot.TeleBot(BOT_TOKEN)

import handlers
