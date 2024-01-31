import logging
from key1 import api_key
from main import first
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename="bot.log", level=logging.INFO)
# Логирование подключено
def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь! Дана команда на старт, Бот готов к работе")
def privet(update, context):
        print("Вызван /hello")
        update.message.reply_text("Здравствуй, пользователь! Бот готов к работе")
def main():
    mybot = Updater(api_key, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("hello", privet))
    dp.add_handler(MessageHandler(Filters.text, first))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()