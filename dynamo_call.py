## THIS IS ANONYMOUS DYNAMO_CALL

import os
import logging
import boto3
import botocore
import hashlib
import random
from boto3.dynamodb.conditions import Attr

# Logging is cool!
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

# Setting up client with AWS
client = boto3.resource("dynamodb")
TableName = "ASafeSpaceTable"
table = client.Table(TableName)

def is_registered(chat_id):
    # check if chat_id exists in dynamo
    hasher = hashlib.sha256()
    string_to_hash = str(chat_id)
    hasher.update(string_to_hash.encode('utf-8'))
    hashid = hasher.hexdigest()
    try:
        response = table.get_item(
            Key = {
                "hashid": hashid})
        item = response["Item"]
        logger.info("User item found, user is registered")
        return True
    except Exception as e:
        logger.info("ERROR --> " + str(e))
        logger.info("User item not found, user not yet registered")
        return False # COMPLETED AND WORKS

def check_password(matric_number, hash):
    string_to_hash = matric_number + "loveusp"
    password = hashlib.md5(string_to_hash.encode()).hexdigest()
    return hash == password # COMPLETED AND WORKS

def add_id(chat_id, matric_number):
    # add chat_id to dynamo
    # if successful, return true, else return false

    username_list = ["iguana", "jackal", "jaguar", "kangaroo", "koala", "komodo", "kookaburra", "lemur", "leopard", "lion", \
                     "lizard", "llama", "manatee", "meerkat", "mongoose", "monkey", "moose", "nighthawk", "ocelot", "orca", \
                     "ostrich", "otter", "owl", "ox", "parrot", "peacock", "pelican", "penguin", "pigeon", "platypus", \
                     "cow", "coyote", "crab", "crane", "crocodile", "crow", "deer", "dingo", "dog", "dolphin", \
                     "dove", "dragon", "dragonfly", "duck", "eagle", "egret", "elephant", "elk", "emu", "falcon", \
                     "ferret", "flamingo", "fox", "frog", "gazelle", "gecko", "gerbil", "goat", "goose", "gorilla", \
                     "groundhog", "gull", "hawk", "hedgehog", "hen", "heron", "hippoopotamus", "hornbill", "hyena", "ibis", \
                     "porcupine", "possum", "prayingmantis", "puffin", "pygmy", "python", "quail", "rabbit", "raccoon", "rat", \
                     "rattlesnake", "raven", "reindeer", "rhino", "roadrunner", "robin", "salmon", "seal", "shark", "sheep", \
                     "skunk", "sloth", "sparrow", "spider", "squirrel", "starfish", "stork", "swan", "tarantula", \
                     "tiger", "tortoise", "toucan", "turkey", "turtle", "viper", "vulture", "wallaby", "whale", "wolf", \
                     "wombat", "woodpecker", "yak", "zebra", \
                     "alligator", "alpaca", "ant", "anteater", "antelope", "armadillo", "axolotl", "baboon", "badger", "barracuda", \
                     "bat", "bear", "beaver", "beetle", "bird", "bison", "boar", "buffalo", "bulbul", "butterfly", \
                     "camel", "capybara", "cat", "chameleon", "cheetah", "chicken", "chimpanzee", "chipmunk", "cobra", "cockatoo"]
    
    username = "usp" + username_list[random.randint(0,143)]
    partner_id = 0
    blacklist = 0
    hasher = hashlib.sha256()
    string_to_hash = str(chat_id)
    hasher.update(string_to_hash.encode('utf-8'))
    hashid = hasher.hexdigest()

    try: 
        # Stores data in table  if it exists in dynamodb
        response = table.update_item(
        Key = {"hashid": hashid},
        UpdateExpression = "SET {} = :val1, {} =:val2, {} = :val3".format(\
                "chat_id", "matric_number", "username"),
        ExpressionAttributeValues = {":val1": chat_id, ":val2": matric_number, ":val3": username})
        logger.info("New user successfully added into dynamodb")
        return True
    except botocore.exceptions.ClientError as e:
        # Creates table if it doesn't exist in dynamodb
        if e.response["Error"]["Message"] == "Requested resource not found":
                logger.info("Table does not exist, creating table in dynamodb...")
                createtable = client.create_table(
                        TableName = TableName,
                        KeySchema = [
                                {
                                        "AttributeName": 'hashid',
                                        "KeyType": "HASH"
                                        }
                                ],
                        AttributeDefinitions = [
                                {
                                        "AttributeName": "hashid",
                                        "AttributeType": "S"
                                        }
                                ],
                        ProvisionedThroughput = {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            })
                logger.info("Table created, values saved in dynamodb")
        logger.info("ERROR: new user NOT added into dynamodb --> " + str(e))
        return False # COMPLETED AND WORKS

def get_username(chat_id):
    # get username from chat id
    hasher = hashlib.sha256()
    string_to_hash = str(chat_id)
    hasher.update(string_to_hash.encode('utf-8'))
    hashid = hasher.hexdigest()
    try:
        response = table.get_item(
            Key = {
                "hashid": hashid})
        item = response["Item"]
        logger.info("User item found, username returned")
        return item["username"]
    except Exception as e:
        logger.info("ERROR User item not found--> " + str(e))
        return False # COMPLETED AND WORKS

def delete_user(matric_number, password):
    # delete user entry using NUSNET ID
    if password != "IAMTHELOVEUSPADMIN":
        return False

    response = table.scan(
        FilterExpression = Attr("matric_number").eq(matric_number)
    )
    items = response["Items"]

    logger.info("Items is: " + str(items))

    if len(items) == 0:
        logger.info("Matric number not found.")
        return False

    hashid = items[0]["hashid"]

    try:
        table.delete_item(
            Key = {"hashid": hashid}
        )
        logger.info("User item deleted")
        return True
    except Exception as e:
        logger.info("ERROR --> " + str(e))
        logger.info("User item not deleted")
        return False # COMPLETED AND WORKS

def get_responses_list(chat_id, text):
    username = str(get_username(chat_id))
    text = username + ":\n" + text
    template = {"message": text, "receiver_id": ""}
    response = table.scan(
        FilterExpression = ~ Attr("chat_id").eq(chat_id)
    )
    items = response["Items"]
    logger.info("Items is: " + str(items))

    responses_list = []
    for user in items:
        response = template.copy()
        response["receiver_id"] = str(user["chat_id"])
        responses_list.append(response)

    return responses_list

def leave(chat_id):
    # delete user entry using chat_id
    response = table.scan(
        FilterExpression = Attr("chat_id").eq(chat_id)
    )
    items = response["Items"]

    logger.info("Items is: " + str(items))

    if len(items) == 0:
        logger.info("Chat_id not found.")
        return False

    hashid = items[0]["hashid"]

    try:
        table.delete_item(
            Key = {"hashid": hashid}
        )
        logger.info("User item deleted")
        return True
    except Exception as e:
        logger.info("ERROR --> " + str(e))
        logger.info("User item not deleted")
        return False # COMPLETED AND WORKS

def debugging_mode(chat_id, text):
    ADMIN_ID = 197107238 # change to current tester chat_id
    debug_message = "The bot is currently under maintenance. We will inform you when the bot is back up. Thank you for your patience."
    template = {"message": "", "receiver_id": ""}
    responses_list = []

    if chat_id != ADMIN_ID: # if someone send message during debugging
        template["message"] = debug_message
        template["receiver_id"] = chat_id
        responses_list.append(template)
        return responses_list

    if text == "/broadcast_debug": # inform everyone that debugging has started
        response = table.scan(
            FilterExpression = ~ Attr("username").eq("")
        )
        items = response["Items"]
        logger.info("Items is: " + str(items))

        template["message"] = "uspadmin:\n" + debug_message
        for user in items:
            response = template.copy()
            response["receiver_id"] = str(user["chat_id"])
            responses_list.append(response)
        logger.info("Broadcast message sent")
        return responses_list

    return True # allow only tester to continue testing code

def all_ok(password):
    if password != "IAMTHELOVEUSPADMIN":
        return False

    all_ok_message = "uspadmin:\nThe bot is back in business! Thank you for your patience."
    template = {"message": all_ok_message, "receiver_id": ""}
    responses_list = []

    response = table.scan(
        FilterExpression = ~ Attr("username").eq("")
    )
    items = response["Items"]
    logger.info("Items is: " + str(items))

    for user in items:
        response = template.copy()
        response["receiver_id"] = str(user["chat_id"])
        responses_list.append(response)
    logger.info("Broadcast message sent")
    return responses_list