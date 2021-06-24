import os
import logging
import boto3
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

def create_table():
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
        }
    )
    logger.info("Table named " + TableName + " was created in DynamoDB.")

def get_all_users():
    response = table.scan()
    logger.info("All users has been retrieved and returned")
    return response

def get_user(hashid):
    response = table.get_item(
        Key = {"hashid": hashid}
    )
    item = response["Item"]
    logger.info("User item found and returned.")
    return item

def insert_user(hashid, chat_id, matric_number, username):
    response = table.update_item(
        Key = {"hashid": hashid},
        UpdateExpression = "SET {} = :val1, {} =:val2, {} = :val3".format("chat_id", "matric_number", "username"),
        ExpressionAttributeValues = {":val1": chat_id, ":val2": matric_number, ":val3": username}
        )
    logger.info("New user successfully added into DynamoDB.")
