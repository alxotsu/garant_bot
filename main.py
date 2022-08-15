from app.bot import bot

me = bot.get_me()
print(
    f"Бот настроен и запущен.\nUsername бота - @{me.username}\nНазвание бота - {me.full_name}"
)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        print("\n\nБот перезапущен.\n\n")
