import os

from dotenv import load_dotenv
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler
from telegram import Update

from .commands import start, help, settings, unknown
from Utils import logger


def run():
    # logger
    hostRegistratorLogger = logger.setupLogger("hostRegistratorLogger")

    # get api token from env
    load_dotenv()
    bot_api_token = os.getenv("HOSTREGISTRATOR_BOT_API_TOKEN")
    if(not bot_api_token):
        hostRegistratorLogger.error(
            "You need to set the host registrator bot api token in the .env file. for reference lookup .env.example")
        return

    updater = Updater(token=bot_api_token)
    dispatcher = updater.dispatcher

    handlers = [
        # Global telegram comands (basics)
        CommandHandler('start', start),
        CommandHandler('help', help),
        CommandHandler('settings', settings),
        MessageHandler(Filters.text & (~Filters.command), echo),

        # default fallback
        MessageHandler(Filters.command, unknown)
    ]

    for handler in handlers:
        dispatcher.add_handler(handler)

    updater.start_polling()
    hostRegistratorLogger.info("Started hostregistrator bot")
    updater.idle()


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
