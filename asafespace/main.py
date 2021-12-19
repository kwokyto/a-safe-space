import logging

from asafespace.constants import (INVALID_COMMAND_MESSAGE,
                                  INVALID_FORMAT_MESSAGE, TOO_LONG_MESSAGE,
                                  UNAUTHORISED_MESSAGE,
                                  UNDER_MAINTENANCE_MESSAGE)
from asafespace.credentials import ADMIN_CHAT_ID
from asafespace.database import is_registered
from asafespace.logic import (admin_commands, broadcast,
                              postregistation_commands,
                              preregistation_commands)
from asafespace.utilities import (decimal_to_int, extract_chat_id,
                                  get_message_type)

# Logging is cool!
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

DEBUG_MODE = False

def main(bot, body):
    """
    Runs the main logic of the Telegram bot
    """
    
    # for privacy issues, this is commented out
    #logger.info('Event: {}'.format(body))

    # manage updates (https://core.telegram.org/bots/api#getting-updates)
    if "update_id" in body.keys() and len(body.keys()) == 1:
        logger.info("An update_id message has been sent by Telegram.")
        logger.error('Event: {}'.format(body))
        return

    # obtain key message details
    message_type = get_message_type(body)
    chat_id = extract_chat_id(body)

    # for debugging, set DEBUG_MODE to True in line 15
    if DEBUG_MODE:
        logger.warn("Debug mode has been activated.")
        # check for length
        text = str(body)
        if len(text) >= 4000:
            text = "The original text sent was too long."
            logger.warn("The original text sent was too long.")
        bot.send_message(chat_id=ADMIN_CHAT_ID, text=text)
        logger.warn("Event text has been sent to the admin.")
        bot.send_message(chat_id=chat_id, text=UNDER_MAINTENANCE_MESSAGE)
        return

    # check for file types we cannot handle
    if message_type in ("edited_messages", "others"):
        bot.send_message(chat_id=chat_id, text=INVALID_FORMAT_MESSAGE)
        logger.info("A message of invalid format has been sent.")
        return
    
    # check for messages that are too long
    if message_type == "text":
        text = body["message"]["text"]
        if len(text) >= 4000:
            bot.send_message(chat_id=chat_id, text=TOO_LONG_MESSAGE)
            logger.warn("The original text sent was too long.")
            return

    # handle pre-registration commands
    if message_type == "text":
        text = body["message"]["text"]
        if text in ("/start", "/help") or text[:9] == "/register":
            logger.info("A pre-registation command has been sent.")
            preregistation_commands(bot, chat_id, text)
            return
    
    # registration check
    user = is_registered(chat_id)
    if user == False:
        bot.send_message(chat_id=chat_id, text=UNAUTHORISED_MESSAGE)
        logger.info("User is not yet registered.")
        return

    # non-registered users should NOT proceed past here
    logger.info("User is registered.")

    # to override formatting
    user["chat_id"] = decimal_to_int(user["chat_id"])

    # handle all other commands
    if message_type == "text":
        text = body["message"]["text"]

        if text[:6] == "/admin":
            logger.info("An admin command has been sent.")
            admin_commands(bot, user, text)
            return

        if text in ("/username", "/leave"):
            logger.info("A post-registation command has been sent.")
            postregistation_commands(bot, user, text)
            return

        if text[0] == "/":
            bot.send_message(chat_id=user["chat_id"], text=INVALID_COMMAND_MESSAGE)
            logger.info("An invalid command was given.")
            return
    
    # handle broadcasting messages
    logger.info("A normal message requesting broadcasting has been sent.")
    broadcast(bot, user["username"], body, message_type, chat_id)
    return
