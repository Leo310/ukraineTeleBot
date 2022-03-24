from telegram import Update
from telegram.ext import CallbackContext


def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Help page. TODO")
