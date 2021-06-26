import logging

from logic import preregistation_commands
from messages import INVALID_FORMAT_MESSAGE
from utilities import extract_chat_id, get_message_type

# Logging is cool!
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

COMMANDS = ("/start")

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
        return
    
    # handle text type messages
    if message_type == "text":
        text = body["message"]["text"]

        # handle pre-registration commands
        if text == "/start" or text == "/help" or text[:9] == "/register":
            preregistation_commands(bot, chat_id, text)
            return

    bot.send_message(chat_id=chat_id, text="This is the default response.")
    return
