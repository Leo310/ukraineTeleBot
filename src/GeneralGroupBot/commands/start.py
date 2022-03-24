from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm the general group bot, if you want to register as a host talk to him: https://t.me/ukrainge_hc_host_registrator_bot!")
