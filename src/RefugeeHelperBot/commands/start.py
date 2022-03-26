# import os
# import requests

from telegram import Update
from telegram.ext import CallbackContext

from Utils import logger


refugeeHelperLogger = logger.getLogger("refugeeHelperLogger")


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="To register and verify yourself please click on the following link.")
    if(not IsRegistered(update.effective_user.id)):
        # get registration service url of identity server
        registrationLink = getRegistrationLink(update.effective_user.id)
        # send url to host
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=registrationLink)
    else:
        # get verification link
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="To verify click on this link: https://test_url_verification.com")
        refugeeHelperLogger.info(update.effective_user.id)


def IsRegistered(userid):
    # telegramUserData = {"userID": "userid", "botID": "there is only this bot atm"}
    # r = requests.post(os.getenv("ID_SERVER_IP")+"/isRegistered",
    #                   headers={"Authorization": os.getenv("HOSTREGISTRATOR_BOT_ID_SERVER_TOKEN")},
    #                   json=telegramUserData)
    # return r.json().isRegistered
    return True


# request a url of registration service with specific telgram user token.
def getRegistrationLink(userid):
    # http client. attach bearer token for id server

    # telegramUserData = {"userID": "userid", "botID": "there is only this bot atm"}
    # r = requests.post(os.getenv("ID_SERVER_IP")+"/getRegistrationLink",
    #                   headers={"Authorization": os.getenv("HOSTREGISTRATOR_BOT_ID_SERVER_TOKEN")},
    #                   json=telegramUserData)
    # return r.json().verificationLink
    return "https://test_url_registration.com"
