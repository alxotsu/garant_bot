from threading import Thread
from time import sleep

from app import config
from app.bot import bot
import handlers  # Setting up handlers here (DO NOT REMOVE!)
from app.functions import monitor_payments

me = bot.get_me()
print(
    f"Бот настроен и запущен.\nUsername бота - @{me.username}\nНазвание бота - {me.full_name}"
)


def run_bot_pooling():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            print("\n\nБот перезапущен.\n\n")


def run_monitoring():
    while True:
        monitor_payments()
        sleep(config.MONITOR_PAYMENTS_TIME_INTERVAL)


thread_pooling = Thread(target=run_bot_pooling)
thread_monitoring = Thread(target=run_monitoring)

thread_pooling.start()
thread_monitoring.start()
