from threading import Thread
from time import sleep

from app import config
from app.bot import bot
import handlers  # Setting up handlers here (DO NOT REMOVE!)
from app.functions import monitor_payments


def run_bot_pooling():
    me = bot.get_me()
    print(
        f"Бот настроен и запущен.\nUsername бота - @{me.username}\nНазвание бота - {me.full_name}\n"
    )
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            print("\n\nБот перезапущен.\n\n")


def run_monitoring():
    print("Запущен мониторинг платежей\n")
    while True:
        try:
            sleep(config.MONITOR_PAYMENTS_TIME_INTERVAL)
            monitor_payments()
        except Exception as e:
            print(e)
            print("\n\nМониторинг перезапущен.\n\n")


thread_pooling = Thread(target=run_bot_pooling)
thread_monitoring = Thread(target=run_monitoring)

thread_pooling.start()
sleep(1)
thread_monitoring.start()
