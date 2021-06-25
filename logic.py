import logging
from dynamodb import *

# Logging is cool!
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

def main(bot, body):
    chat_id = body.message.chat.id
    bot.sendMessage(chat_id=chat_id, text=str(body))