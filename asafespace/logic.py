import logging

from asafespace.constants import (ADMIN_REMOVE_FAILURE_MESSAGE,
                       ADMIN_REMOVE_SUCCESS_MESSAGE,
                       ALREADY_REGISTERED_MESSAGE, HELP_MESSAGE,
                       INVALID_ADMIN_COMMAND_MESSAGE, LEAVE_FAILURE_MESSAGE,
                       LEAVE_SUCCESS_MESSAGE, NOT_ADMIN_MESSAGE,
                       REGISTRATION_CLARIFICATION_MESSAGE,
                       REGISTRATION_FAILURE_MESSAGE,
                       REGISTRATION_SUCCESS_MESSAGE, START_MESSAGE,
                       USERNAME_MESSAGE, WRONG_PASSWORD_MESSAGE)
from asafespace.database import (admin_remove, get_all_chat_ids, insert_user,
                      is_registered, remove_user)
from asafespace.utilities import (authenticate_admin, extract_sticker_id, get_message,
                       get_random_username, valid_password)

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

def admin_commands(bot, user, text):
    """
    Handles the commands that require registration
    Commands are "/admin", "/adminremove"

    Parameters
    ----------
    bot: Telegram both object
    user: dict
        Dictionary representing a user
    text: str
    """
    chat_id = user["chat_id"]
    if not authenticate_admin(user["nusnetid"]):
        bot.send_message(chat_id=chat_id, text=NOT_ADMIN_MESSAGE)
        logger.warn("A non-admin attempted to use admin commands.")
        return
    
    if text[:7] == "/admin ":
        broadcast(bot, "uspadmin", text, "admin", chat_id)
        return

    if text[:12] == "/adminremove":
        admin_remove(bot, text, chat_id)
        return
    
    bot.send_message(chat_id=chat_id, text=INVALID_ADMIN_COMMAND_MESSAGE)
    logger.info("Admin action: AN invalid admin command was given.")

def admin_remove(bot, text, chat_id):
    try:
        nustnetid = text[13:].lower()
        admin_remove(nustnetid)
        bot.send_message(chat_id=chat_id, text=ADMIN_REMOVE_SUCCESS_MESSAGE)
        logger.info("Admin action: User has been successfuly removed.")
    except Exception as error:
        bot.send_message(chat_id=chat_id, text=ADMIN_REMOVE_FAILURE_MESSAGE)
        logger.error("Admin action: User removal failed due to an error." + str(error))

def postregistation_commands(bot, user, text):
    """
    Handles the commands that require registration
    Commands are "/username", "/leave"

    Parameters
    ----------
    bot: Telegram both object
    chat_id: int
    text: str
    """
    if text == "/username":
        username_command(bot, user)
        return
    
    if text == "/leave":
        leave_command(bot, user)
        return

def username_command(bot, user):
    """
    Sends the username to the user

    Parameters
    ----------
    bot: Telegram both object
    user: dic
        Represents a user
    """
    
    chat_id = user["chat_id"]
    username = user["username"]
    bot.send_message(chat_id=chat_id, text=USERNAME_MESSAGE+username)
    logger.info("User request for username successfully executed.")

def leave_command(bot, user):
    """
    Unregistered the user from the database.

    Parameters
    ----------
    bot: Telegram both object
    user: dic
        Represents a user
    """

    try:
        remove_user(user["hashid"])
        chat_id = user["chat_id"]
        bot.send_message(chat_id=chat_id, text=LEAVE_SUCCESS_MESSAGE)
        logger.info("User is now unregistered.")
    except Exception as error:
        bot.send_message(chat_id=chat_id, text=LEAVE_FAILURE_MESSAGE)
        logger.error("User have not been removed due to an error. " + str(error))

def broadcast(bot, username, body, message_type, chat_id):
    """
    Broadcasts both text and sticker messages to everyone

    Parameters
    ----------
    bot: a Telegram bot object
    username: str
    body: dic
        Body of webhook event
    message_type: str
        Either "text" or "sticker"
    """

    message = get_message(username, body, message_type)
    recipients = get_all_chat_ids()
    broadcast_message(bot, message, recipients, chat_id)

    if message_type == "sticker":
        file_id = extract_sticker_id(body)
        broadcast_sticker(bot, file_id, recipients, chat_id)
    return

def broadcast_message(bot, message, recipients, skip):
    """
    Broadcasts only text messages to everyone

    Parameters
    ----------
    bot: a Telegram bot object
    message: str
        Message should already be set with usernames at the beginning of the message
    recipients: list
        List of all chat_id
    """
    
    for chat_id in recipients:
        if chat_id == skip:
            continue
        try:
            bot.send_message(chat_id=chat_id, text=message)
        except Exception as error:
            logger.error("Message could not be sent to user with chat_id " + str(chat_id) + ". " + str(error))
    logger.info("Message has been sent to all users")

def broadcast_sticker(bot, file_id, recipients, skip):
    """
    Broadcasts only stickers messages to everyone

    Parameters
    ----------
    bot: a Telegram bot object
    file_id: str
        Sticker to send, pass a file_id as String to send a file that exists on the Telegram servers
    recipients: list
        List of all chat_id
    """
    
    for chat_id in recipients:
        if chat_id == skip:
            continue
        try:
            bot.send_sticker(chat_id=chat_id, sticker=file_id)
        except Exception as error:
            logger.error("Sticker could not be sent to user with chat_id " + str(chat_id) + ". " + str(error))
    logger.info("Sticker has been sent to all users")
