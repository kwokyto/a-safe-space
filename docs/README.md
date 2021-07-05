# A Safe Space FAQ

* [Ground Rules](#ground-rules)
* [Important Links](#important-links)
* [General Questions](#general-questions)
  * [1. What is A Safe Space by Love, USP?](#1-what-is-a-safe-space-by-love-usp)
  * [2. What can I do on A Safe Space?](#2-what-can-i-do-on-a-safe-space)
  * [3. What are the commands I can use?](#3-what-are-the-commands-i-can-use)
* [Registration](#registration)
  * [4. Why should I register?](#4-why-should-i-register)
  * [5. How do I register?](#5-how-do-i-register)
  * [6. Why do I need to provide my NUSNET ID?](#6-why-do-i-need-to-provide-my-nusnet-id)
  * [7. Why must my password be unique?](#7-why-must-my-password-be-unique)
  * [8. Why do I keep getting a registration error message?](#8-why-do-i-keep-getting-a-registration-error-message)
* [Privacy](#privacy)
  * [9. How are the usernames assigned? Can I change my username?](#9-how-are-the-usernames-assigned-can-i-change-my-username)
  * [10. What personal details would be stored?](#10-what-personal-details-would-be-stored)
  * [11. Who can see my messages? Will my messages be logged?](#11-who-can-see-my-messages-will-my-messages-be-logged)
  * [12. I am uncomfortable with how my information is stored, what can I do?](#12-i-am-uncomfortable-with-how-my-information-is-stored-what-can-i-do)
* [Interactions](#interactions)
  * [13. Why do some usual Telegram functions not work?](#13-why-do-some-usual-telegram-functions-not-work)
  * [14. Someone in the chat is making me uncomfortable, what do I do?](#14-someone-in-the-chat-is-making-me-uncomfortable-what-do-i-do)
* [Other Problems](#other-problems)
  * [15. Why is the bot not responding?](#15-why-is-the-bot-not-responding)
  * [16. I have other concerns, who can I contact?](#16-i-have-other-concerns-who-can-i-contact)

## Ground Rules

1. Be kind and respectful to each other - any form of harassment or abuse will not be tolerated. Basically, speak as you will to a person in real life.
2. Respect each other's privacy and confidentiality - do not ask for identifying/contact information unless both sides mutually agree to do so. The onus is on every individual as to how much they're comfortable to share.
3. The admins reserve the right to remove users at their discretion, if they are deemed to have contravened the rules.
4. Do not spam messages or stickers in the chat.

## Important Links

* Telegram Bot: [@asafespacebot](https://telegram.me/asafespacebot)
* Sign Ups: [https://tinyurl.com/asafespacesignups](https://tinyurl.com/asafespacesignups)
* FAQ: [https://tinyurl.com/asafespacefaq](https://tinyurl.com/asafespacefaq)

## General Questions

### 1. What is A Safe Space by Love, USP?

A Safe Space was created as a platform for USP students to hold conversations on mental health issues. This simulates a group chat where students can share experience or advice, while remaining completely anonymous.

### 2. What can I do on A Safe Space?

When registered, any message that you send to the bot will be sent to all other students that are also registered on the bot. Your message would be accompanied by your username, allowing others to identify messages that are sent. No other personal information would be shared with anyone in the group.

### 3. What are the commands I can use?

|Command|Action|
|-------|------|
|`/start`|Returns a general welcome message.|
|`/help`|Returns a bot description, along with the sign up link, FAQ link, and admins' Telegram handles.|
|`/register <NUSNET ID> <password>`|Registers you into the system. A username will be given to you in the form of `usp<animal>`. After registration, you can send and receive messages. The password is specific to each student, and will be provided by Love, USP admin.|
|`/username`|Shows your username.|
|`/leave`|Unregisters you from the system. Afterwards, you will no longer be able to receive messages that are sent. All of your details that are stored in the system would also be deleted.|

## Registration

### 4. Why should I register?

We hope that through this bot, you may find a comfortable platform to discuss sensitive topics relating to mental health. Additionally, because of anonymity, you get to talk about things you may find difficulty in expressing, which is potentially liberating.

### 5. How do I register?

Firstly, fill up the sign up sheet [here](https://tinyurl.com/asafespacesignups), where we will brief you on expected behaviour and ground rules, then get your explicit agreement on these rules. We will then contact you for your NUSNET ID before giving you a unique password. Simply register using the following format:

```lang-none
/register <NUSNET ID> <password>
/register e1234567 p4ssw0rdg1vEn
```

### 6. Why do I need to provide my NUSNET ID?

For accountability reasons, we require to maintain a list of people who are communicating on the bot. We will not be identifying users until and unless we have to intervene in case of harassment.

### 7. Why must my password be unique?

The password given to you is unique only to you. We are taking precautions to ensure that our bots do not circulate outside of USP because we want students to feel safe using it. Therefore, we need to verify if you are a USP student.

### 8. Why do I keep getting a registration error message?

Ensure that the password given to you is also fully copied into the message. There should NOT be any white spaces after the password. If you still face errors, contact the admins.

## Privacy

### 9. How are the usernames assigned? Can I change my username?

All usernames are randomly assigned. Unfortunately, we do not allow the change of usernames. Please note that there is a small possibility that people may share the same username due to the limited number of animal names the admin could come up with.

### 10. What personal details would be stored?

The only personally identifiable data that is stored is your NUSNET ID. The other information that is stored are your Telegram chat ID and your randomly assigned username. These data would be stored in a cloud database on Amazon Web Services and can only be viewed by the admin.

### 11. Who can see my messages? Will my messages be logged?

Anything you send will be sent to everyone registered in the bot, because this simulates an anonymous group chat. No messages are stored or logged in the backend, so admins will NOT be able to view your messages.

### 12. I am uncomfortable with how my information is stored, what can I do?

Use the command `/leave`. This will remove you from the chat and delete all your information stored. However, this would mean that you will no longer be able to use the bot's features.

## Interactions

### 13. Why do some usual Telegram functions not work?

Currently, the bot does not support functions such as GIFs, replying to specific messages, editing messages, and deleting messages. However, you can send emojis, non-English characters, and stickers (yay!). The character limit for each text message is also 4000 characters.

We are slowly looking to expand functionalities to allow more flexibility in conversation. If you discover any bugs or functionalities that do not work as normal, please inform the admin.

### 14. Someone in the chat is making me uncomfortable, what do I do?

Screenshot the conversation and contact the admins. The admins will take it from there. Since deleting messages is not an option on the bot, any offensive messages cannot be deleted from history.

## Other Problems

### 15. Why is the bot not responding?

In order to check if the bot is active, simply send the bot a command. Usually `/start` will do. If the bot does not reply to that command, then the bot is down. It is likely that there is a bug that is clogging the Telegram bot. Do NOT spam the bot, none of your messages from then on will be processed. Contact the admin immediately, and wait until the bugs are fixed. You will be informed when all is well.

### 16. I have other concerns, who can I contact?

For administrative concerns, you can contact Ling Hui (@linggghui), Rachel (@rachtxxy), or Radhika (@radhikaaaaa). For technical concerns regarding the bots, you can contact Ryan (@kwokyto).
