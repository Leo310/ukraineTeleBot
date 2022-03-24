# import os
# import requests

from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="To register and verify yourself please click on the following link.")
    # get registration verivication service url of identity server
    registrationVerificationLink = requestRegistrationVerificationLink()

    # send url to host
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=registrationVerificationLink)


# request a url of registration service with specific telgram user token.
def requestRegistrationVerificationLink():
    # http client. attach bearer token for id server

    # telegramUserData = {"userID": "", "botID": ""}
    # r = requests.post(os.getenv("ID_SERVER_IP")+"/getVerificationLink",
    #                   headers={"Authorization": os.getenv("HOSTREGISTRATOR_BOT_ID_SERVER_TOKEN")},
    #                   json=telegramUserData)
    # return r.json().verificationLink
    return "https://test_url_registration.com"
