from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler
from telegram import Update
import os
from dotenv import load_dotenv
import logging


def main():
    # get api token from env
    load_dotenv()
    bot_api_token = os.getenv("BOT_API_TOKEN")
    if(not bot_api_token):
        print("You need to set the api token in the .env file. for reference lookup .env.example")
        exit(1)

    # setup logger
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater = Updater(token=bot_api_token)
    dispatcher = updater.dispatcher

    handlers = [CommandHandler('start', start),
                MessageHandler(Filters.text & (~Filters.command), echo)
                ]

    for handler in handlers:
        dispatcher.add_handler(handler)

    updater.start_polling()


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
