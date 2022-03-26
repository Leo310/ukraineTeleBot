from telegram import Update
from telegram.ext import CallbackContext


def settings(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Settings page. TODO")
