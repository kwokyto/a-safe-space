import json
import telegram
import os
import logging

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
    ##logger.info('Event: {}'.format(event)) ## for privacy issues, this is commented out

    if event.get('httpMethod') == 'POST' and event.get('body'): 
        logger.info('Message received')
        body = telegram.Update.de_json(json.loads(event.get('body')), bot)
        
        chat_id = body.message.chat.id
        text = body.message.text
        bot.sendMessage(chat_id=chat_id, text=text)
        bot.sendMessage(chat_id=chat_id, text=str(body))
        return OK_RESPONSE

    return ERROR_RESPONSE