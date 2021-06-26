import hashlib
import random
import json

from asafespace.constants import ANIMAL_LIST, SENT_STICKER_MESSAGE


def get_message_type(body):
    """
    Determines the Telegram message type

    Parameters
    ----------
    body: dic
        Body of webhook event
    
    Returns
    -------
    string
        Description of message type
    """

    if "message" in body.keys():
        if "text" in body["message"]:
            return "text"
        elif "sticker" in body["message"]:
            return "sticker"
    
    if "edited_message" in body.keys():
        return "edited_message"
    
    return "others"

def extract_chat_id(body):
    """
    Obtains the chat ID from the event body

    Parameters
    ----------
    body: dic
        Body of webhook event
    
    Returns
    -------
    int
        Chat ID of user
    """

    if "edited_message" in body.keys():
        chat_id = body["edited_message"]["chat"]["id"]
    else:
        chat_id = body["message"]["chat"]["id"]
    return chat_id

def get_sha256_hash(plaintext):
    """
    Hashes an object using SHA256. Usually used to generate hash of chat ID for lookup

    Parameters
    ----------
    plaintext: int or str
        Item to hash
    
    Returns
    -------
    str
        Hash of the item
    """

    hasher = hashlib.sha256()
    string_to_hash = str(plaintext)
    hasher.update(string_to_hash.encode('utf-8'))
    hash = hasher.hexdigest()
    return hash

def get_md5_hash(plaintext):
    """
    Hashes an object using MD5. Usually used to generate hash of NUSNET ID

    Parameters
    ----------
    plaintext: int or str
        Item to hash
    
    Returns
    -------
    str
        Hash of the item
    """

    hasher = hashlib.md5()
    string_to_hash = str(plaintext)
    hasher.update(string_to_hash.encode('utf-8'))
    hash = hasher.hexdigest()
    return hash

def valid_password(nusnetid, password):
    """
    Validates the given password.

    Parameters
    ----------
    nustnetid: str
    password: str

    Returns
    -------
    bool
        True if password is valid, False otherwise
    """

    SALT = "loveusp"
    hash = get_md5_hash(nusnetid + SALT)
    return hash == password
    
def get_random_username():
    """
    Retrieves a random username.

    Returns
    -------
    str
    """
    
    index = random.randint(0,len(ANIMAL_LIST))
    username = "usp" + ANIMAL_LIST[index]
    return username

def get_message(username, body, message_type):
    """
    Obtains the message to be broadcasted.
    Message is custom if original was a sticker.

    Parameters
    ----------
    username: str
    body: dic
        Body of webhook event
    message_type: str
        Either "text" or "sticker"

    Returns
    -------
    str
        Message to be broadcasted
    """

    if message_type == "sticker":
        return username + SENT_STICKER_MESSAGE

    if message_type == "admin":
        original = body[7:]
    else:
        original = body["message"]["text"]
        
    message = username + ":\n" + original
    return message

def decimal_to_int(decimal):
    """
    Converts a json decimal to an integer.
    Mostly used to convert chat_id
    """
    
    integer = int(str(decimal))
    return integer

def extract_sticker_id(body):
    """
    Obtains the sticker ID from the event body

    Parameters
    ----------
    body: dic
        Body of webhook event
    
    Returns
    -------
    str
        file_id of sticker
    """

    file_id = body["message"]["sticker"]["file_id"]
    return file_id

def get_admins():
    """
    Obtains a dictionary of admins
    """
    
    line = open("ADMINS.txt","r").readline()
    admins = json.loads(line)
    return admins

def authenticate_admin(nusnetid):
    """
    Determines if a user is an admin
    """
    
    hash = get_md5_hash(nusnetid)
    admins = get_admins()
    return hash in admins.values()
