import hashlib
import random

from messages import ANIMAL_LIST


def get_message_type(body):
    """
    Determines the Telegram message type

    Parameters
    ----------
    body : dic
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
    elif "edited_message" in body.keys():
        return "edited_message"
    else:
        return "others"

def extract_chat_id(body):
    """
    Obtains the chat ID from the event body

    Parameters
    ----------
    body : dic
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
    plaintext : int or str
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
    plaintext : int or str
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
    SALT = "loveusp"
    hash = get_md5_hash(nusnetid + SALT)
    return hash == password
    
def get_random_username():
    index = random.randint(0,len(ANIMAL_LIST))
    username = "usp" + ANIMAL_LIST[index]
    return username
