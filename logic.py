import logging

from database import insert_user, is_registered, remove_user
from messages import (ALREADY_REGISTERED_MESSAGE, HELP_MESSAGE, LEAVE_FAILURE_MESSAGE, LEAVE_SUCCESS_MESSAGE,
                      REGISTRATION_CLARIFICATION_MESSAGE,
                      REGISTRATION_FAILURE_MESSAGE,
                      REGISTRATION_SUCCESS_MESSAGE, START_MESSAGE, USERNAME_MESSAGE,
                      WRONG_PASSWORD_MESSAGE)
from utilities import get_random_username, valid_password

# Logging is cool!
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)


def preregistation_commands(bot, chat_id, text):
    """
    Handles the commands that do not require registration
    Commands are "/start", "/help", and "/register"

    Parameters
    ----------
    bot: Telegram both object
    chat_id: int
    text: str
    """
    # start command
    if text == "/start":
        bot.send_message(chat_id=chat_id, text=START_MESSAGE)
        return

    # help command
    if text == "/help":
        bot.send_message(chat_id=chat_id, text=HELP_MESSAGE)
        return

    # register command
    if text[:9] == "/register":
        # if the user is already registered
        if is_registered(chat_id) != False:
            bot.send_message(chat_id=chat_id, text=ALREADY_REGISTERED_MESSAGE)
            logger.info("User requesting registration is already registered.")
            return

        # if the user just puts /register
        if text == "/register":
            bot.send_message(chat_id=chat_id, text=REGISTRATION_CLARIFICATION_MESSAGE)
            logger.info("User only sent /register without arguments..")
            return

        # new user registering
        nusnetid = text[10:18].lower()
        password = text[19:]

        # if password given is wrong
        # use https://www.md5hashgenerator.com/
        # hash must be generated using small 'e'
        if not valid_password(nusnetid, password):
            bot.send_message(chat_id=chat_id, text=WRONG_PASSWORD_MESSAGE)
            logger.info("User supplied either the wrong NUSNET ID or password.")
            return
        
        # if password is correct
        register_user(bot, chat_id, nusnetid)
        return

def register_user(bot, chat_id, nusnetid):
    """
    Registers a user into the database. Also assigns a username to the user.

    Parameters
    ----------
    bot: Telegram both object
    chat_id: int
    nusnetid: str
    """
    try:
        # try adding user to DynamoDB
        username = get_random_username()
        insert_user(chat_id, nusnetid, username)
        bot.send_message(chat_id=chat_id, text=REGISTRATION_SUCCESS_MESSAGE + username)
        logger.info("New user " + username + "has been successfully added.")
    except Exception as error:
        # if there is an error with adding a user to DynamoDB
        bot.send_message(chat_id=chat_id, text=REGISTRATION_FAILURE_MESSAGE)
        logger.error("User was not added due to an error. " + str(error))

def username_command(bot, chat_id, user):
    """
    Sends the username to the user

    Parameters
    ----------
    bot: Telegram both object
    chat_id: int
    user: dic representing the user
    """
    username = user["username"]
    bot.send_message(chat_id=chat_id, text=USERNAME_MESSAGE+username)
    logger.info("User request for username successfully executed.")

def leave_command(bot, chat_id):
    """
    Unregistered the user from the database.

    Parameters
    ----------
    bot: Telegram both object
    chat_id: int
    """
    try:
        remove_user(chat_id)
        bot.send_message(chat_id=chat_id, text=LEAVE_SUCCESS_MESSAGE)
        logger.info("User is now unregistered.")
    except Exception as error:
        bot.send_message(chat_id=chat_id, text=LEAVE_FAILURE_MESSAGE)
        logger.error("User have not been removed due to an error. " + str(error))

