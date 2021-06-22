import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def start(update, context):
    """Send a message when the command /start is issued."""
    reply = str(context.chat_data)
    update.message.reply_text(reply)

def error(update, context):
    # Log Errors caused by Updates.
    logger.warning('Update "%s" caused error "%s"', update, context.error)