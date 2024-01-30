import logging
from key1 import api_key
from main import first
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename="bot.log", level=logging.INFO)

def main():
    mybot = Updater(api_key, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, first))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()