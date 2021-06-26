import boto3
import logging

from utilities import get_sha256_hash

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

def create_table():
    """
    Creates a DynamoDB table
    """
    try:
        client.create_table(
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
            }
        )
        logger.info("Table named " + TableName + " was created in DynamoDB.")
    except:
        logger.info("Table named " + TableName + " already exists in DynamoDB.")
    return

def get_all_users():
    """
    Retrieve all contents of the table
    """
    response = table.scan()
    logger.info("All users has been retrieved and returned")
    return response

def get_user(chat_id):
    """
    Query a specific entry in the table

    Returns
    -------
    dic
        Dictionary representing the user if user is found
    None
        If user was not found
    """
    hashid = get_sha256_hash(chat_id)
    response = table.get_item(
        Key = {"hashid": hashid}
    )
    if "Item" in response.keys():
        user = response["Item"]
        logger.info("User item found and returned.")
        return user
    else:
        logger.warning("User was not found in the table.")
        return None

def insert_user(chat_id, nusnetid, username):
    """
    Insert a new entry into the table
    """
    hashid = get_sha256_hash(chat_id)
    table.update_item(
        Key = {"hashid": hashid},
        UpdateExpression = "SET {} = :val1, {} =:val2, {} = :val3".format("chat_id", "nusnetid", "username"),
        ExpressionAttributeValues = {":val1": chat_id, ":val2": nusnetid, ":val3": username}
        )
    logger.info("New user successfully added into DynamoDB.")

def remove_user(chat_id):
    """
    Removes a user from the table
    """
    hashid = get_sha256_hash(chat_id)
    table.delete_item(
        Key = {"hashid": hashid}
    )
    logger.info("User has been successfully removed from the database.")

def is_registered(chat_id):
    """
    Checks if a user is registered. Since this will be the first logical access to the table,
    the method also creates a table if it does not exist.

    Returns
    -------
    dic
        Dictionary representing the user if user is registered
    bool
        False if user is not registered
    """
    try:
        user = get_user(chat_id)
        if user == None:
            return False
        return user
    except:
        create_table()
        return False
