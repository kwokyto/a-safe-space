# A Safe Space by Love, USP

![a_safe_space_logo]()

A Safe Space was created as a platform for USP students to hold conversations on mental health issues.
This simulates a group chat where students can share experience or advice, while remaining completely anonymous.
The telegram bot can be accessed [here](https://telegram.me/asafespacebot).

## Features

When registered, any message that you sent to the bot will be sent to all other students that are also registered on the bot.
Your message would be accompanied by your username, allowing others to identify messages that are sent.
No other personal information would be shared with anyone in the group.

## General Commands

Below are a list of available commands for students that can be used in the Telegram bot.

### `/start`

Returns a general welcome message.

### `/help`

Returns a bot description, along with the sign up link, FAQ link, and admins’ Telegram handles.

### `/register <NUSNET ID> <password>`

Registers the student into the system.
After being registered, students can send and receive messages.
The password is specific to each student, and will be provided by a Love, USP admin.

### `/username`

Shows the student's username.

### `/leave`

Unregisters the student from the system.
Afterwards, students will no longer be able to receive messages that are sent.
All details of the student that are stored in the system would also be deleted.

## Admin Commands

These commands would only work if the user is an admin.

### `/admin <message>`

Broadcasts the admins message as `uspadmin` to all students in the system.
This could be used to convey messages about downtime, or promotions for Love, USP events.

### `/adminremove <NUSNET ID>`

Unregisters the student with a certain NUSNET ID.
This is to ensure that admins can easily remove any student that may be causing distress in the chat.

### `/adminregister <NUSNETID>`

Creates a registration command for a student.
This is to simplify the registration process, where the admin can send the entire command to the student.

## FAQs

The FAQ for the bot can be found [here](faq.md "A Safe Space FAQ").

## Debugging

The following outlines the procedure for debugging.

1. In asafespace/main.py, ensure `ADMIN_CHAT_ID` is accurate on line 17.
2. In the same file, change `DEBUG_MODE` to `True` on line 18.
3. In the command line, execute `severless deploy`.
4. From now on, all message metadata would be sent to the admin for debugging.
5. Students who sends messages to the bot will also receive an "under maintenance" response.
6. After debugging, change `DEBUG_MODE` in asafespace/main.py back to `True`.
7. In the command line, execute `severless deploy` again.
8. Admins can use the `/admin` command in the bot to broadcast a message to all students.

## AWS and Serverless Deployment

### Installing

```lang-none
# Clone the repository into your local drive
# Open the command window in the bot file location

# Install the Serverless Framework
$ npm install serverless -g

# Install the necessary plugins
$ npm install
```

### Deploying

```lang-none
# Update AWS CLI in .aws/credentials

# Deploy it!
$ serverless deploy

# With the URL returned in the output, configure the Webhook
$ curl -X POST https://<your_url>.amazonaws.com/dev/set_webhook
```

### AWS Configurations

1. From the AWS Console, select AWS Lambda.
2. In AWS Lambda, select "a-safe-space-bot-dev-webhook".
3. Select "Permissions" and select the Lambda role under "Execution role"
4. In AWS IAM, select "Attach policies" under "Permissions" and "Permissions policies"
5. Search for and select "AmazonDynamoDBFullAccess" and "Attach policy"
6. Run the Telegram bot with `/start` and register with `/register`
7. The first attempt at registration should return an error.
8. From the AWS Console, select AWS DynamoDB.
9. Under "Tables", ensure that the "ASafeSpaceTable" table has been created.
10. Re-register with `/register`, and registration should be successful.
