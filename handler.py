from asafespace.credentials import ADMIN_CHAT_ID
import json
import logging
import os
import telegram

from asafespace.main import main

# Logging is cool!
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

OK_RESPONSE = {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps('ok')
}

ERROR_RESPONSE = {
    'statusCode': 400,
    'body': json.dumps('Oops, something went wrong!')
}

def configure_telegram():
    """
    Configures the bot with a Telegram Token.

    Returns a bot instance.
    """

    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    if not TELEGRAM_TOKEN:
        logger.error('The TELEGRAM_TOKEN must be set')
        raise NotImplementedError

    return telegram.Bot(TELEGRAM_TOKEN)

def set_webhook(event, context):
    """
    Sets the Telegram bot webhook.
    """

    logger.info('Event: {}'.format(event))
    bot = configure_telegram()
    url = 'https://{}/{}/'.format(
        event.get('headers').get('Host'),
        event.get('requestContext').get('stage'),
    )
    webhook = bot.set_webhook(url)

    if webhook:
        return OK_RESPONSE

    return ERROR_RESPONSE

def webhook(event, context):
    """
    Runs the Telegram webhook.
    https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html
    """

    bot = configure_telegram()

    if event.get('httpMethod') == 'POST' and event.get('body'): 
        logger.info('Message received')
        body = telegram.Update.de_json(json.loads(event.get('body')), bot).to_dict()

        try:
            main(bot, body)
        except Exception as error:
            error_message = "There is an unhandled exception, please debug immediately.\n" + error.__str__()
            bot.send_message(chat_id=ADMIN_CHAT_ID, text=error_message)
            logger.error(error_message)
        
        return OK_RESPONSE

    return ERROR_RESPONSE
