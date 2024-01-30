import logging
from key1 import api_key
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename="bot.log", level=logging.INFO)

def first(update, context):
    text = update.message.text
    nums_sum = sum(float(x) for x in text.split())
    print(nums_sum)
    update.message.reply_text(nums_sum)

def main():
    mybot = Updater(api_key, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, first))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()