import logging

from constants import (INVALID_COMMAND_MESSAGE, INVALID_FORMAT_MESSAGE,
                       UNAUTHORISED_MESSAGE)
from database import is_registered
from logic import (admin_commands, broadcast, postregistation_commands,
                   preregistation_commands)
from utilities import decimal_to_int, extract_chat_id, get_message_type

# Logging is cool!
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

def main(bot, body):
    """
    Runs the main logic of the Telegram bot
    """

    # obtain key message details
    message_type = get_message_type(body)
    chat_id = extract_chat_id(body)

    # check for file types we cannot handle
    if message_type in ("edited_messages", "others"):
        bot.send_message(chat_id=chat_id, text=INVALID_FORMAT_MESSAGE)
        logger.info("A message of invalid format has been sent.")
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


