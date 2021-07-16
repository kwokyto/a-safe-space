# Admin sprecfic links
REGISTRATION_LINK = "tinyurl.com/asafespacesignups"
FAQ_LINK = "tinyurl.com/asafespacefaq"
ADMIN_HANDLE = "@kwokyto"



# Messages sent to the user
PREFIX = "A Safe Space:\n"

INVALID_FORMAT_MESSAGE = PREFIX + \
    "Sorry, only texts messages or stickers are allowed. Editing of messages are also not allowed."

START_MESSAGE = PREFIX + \
    "Welcome! If you have not done so, do fill up the registration form at " + REGISTRATION_LINK + "\n"\
    "Then, you can use /register to register!"

HELP_MESSAGE = PREFIX + \
    "I was created as a platform for USP students to hold conversations on mental health issues. " + \
    "I simulate a group chat where students can share experience or advice, while remaining completely anonymous.\n\n" + \
    "Sign Up Form: " + REGISTRATION_LINK + "\n" + \
    "FAQ: " + FAQ_LINK + "\n" + \
    "Feel free to contact " + ADMIN_HANDLE + " if you have any queries!"

ALREADY_REGISTERED_MESSAGE = PREFIX + "You are already registered!"

REGISTRATION_CLARIFICATION_MESSAGE = PREFIX + \
    "To register, add your NUSNET ID and password behind the register command. For example:\n\n" + \
    "    /register e1234567 sUp3rsEcr3tPa55w0RD\n\n" + \
    "To get your password, fill up the form at " + REGISTRATION_LINK + " and wait for our admins to contact you."

WRONG_PASSWORD_MESSAGE = PREFIX + \
    "Incorrect NUSNET ID or password." + \
    "To register, add your NUSNET ID and password behind the register command. For example:\n\n" + \
    "    /register e1234567 sUp3rsEcr3tPa55w0RD\n\n" + \
    "If you believe that there is a problem, do reach out to " + ADMIN_HANDLE + "."

REGISTRATION_SUCCESS_MESSAGE = PREFIX + \
    "Yay! You can now send and receive messages in this chat. " + \
    "Your username is "

REGISTRATION_FAILURE_MESSAGE = PREFIX + \
    "Something went wrong with your registration. Please contact " + ADMIN_HANDLE + " as soon as you can."

UNAUTHORISED_MESSAGE = PREFIX + \
    "You are not yet registered! " + \
    "To register, add your NUSNET ID and password behind the register command. For example:\n\n" + \
    "    /register e1234567 sUp3rsEcr3tPa55w0RD\n\n" + \
    "To get your password, fill up the form at " + REGISTRATION_LINK + " and wait for our admins to contact you."

USERNAME_MESSAGE = PREFIX + \
    "Your username is "

LEAVE_SUCCESS_MESSAGE = PREFIX + \
    "We are sad to see you go! Use the same password if you wish to re-register."

LEAVE_FAILURE_MESSAGE = PREFIX + \
    "Something went wrong when you tried to leave the bot. Please contact " + ADMIN_HANDLE + " as soon as you can."

INVALID_COMMAND_MESSAGE = PREFIX + \
    "I do not recognise the command you sent me. The available commands are:\n" + \
    "    /start\n    /help\n    /register\n    /username\n    /leave"

SENT_STICKER_MESSAGE = " sent a sticker."

NOT_ADMIN_MESSAGE = PREFIX + "Hey! You are not an admin! Stop using admin commands! ):<"

ADMIN_REMOVE_SUCCESS_MESSAGE = PREFIX + "User has successfully been removed."

ADMIN_REMOVE_FAILURE_MESSAGE = PREFIX + \
    "There was an error trying to remove the user. Please check with " + ADMIN_HANDLE + " immediately."

INVALID_ADMIN_COMMAND_MESSAGE = PREFIX + "The admin command you gave me does not exist."

UNDER_MAINTENANCE_MESSAGE = PREFIX + \
    "I am currently under maintenance. >< Do hang tight and I will be back online soon!"

TOO_LONG_MESSAGE = PREFIX + \
    "The message that you have just sent is too long. Please do not spam the chat and keep to 4000 characters."

INVALID_NUSNETID_MESSAGE = PREFIX + \
    "It seems like the NUSNETID you provided is invalid."



# Other constants
ANIMAL_LIST = ["addax","albatross","alligator","alpaca","ant","anteater","antelope","armadillo","axolotl",
            "babirusa","baboon","badger","barracuda","bat","bear","beaver","bee","beetle","beluga","bird",
            "bison","boar","buffalo","bulbul","butterfly","camel","capybara","cat","chameleon","chamois",
            "cheetah","chicken","chimpanzee","chinchilla","chipmunk","cicada","cobra","cockatoo","cougar",
            "cow","coyote","crab","crane","cricket","crocodile","crow","deer","dingo","dog","dolphin",
            "donkey","dove","dragon","dragonfly","duck","dugong","eagle","earthworm","eel ","egret",
            "elephant","elk","emu","falcon","ferret","flamingo","flounder","fox","frog","gazelle","gecko",
            "gerbil","gharial","goat","goose","gorilla","grasshopper","groundhog","gull","hamster","hawk",
            "hedgehog","hen","heron","herring","hippoopotamus","hornbill","hornet","hyena","ibis","iguana",
            "impala","jackal","jaguar","jellyfish","kangaroo","kingfisher","koala","komodo","kookaburra",
            "ladybug","lemur","leopard","lion","lionfish","lizard","llama","lobster","lynx","macaque","macaw",
            "manatee","marmot","meerkat","mink","mongoose","monkey","moose","mouflon","mouse","mousedeer",
            "mudskipper","narwhal","newt","nighthawk","ocelot","octopus","okapi","orca","ostrich","otter",
            "owl","ox","panda ","pangolin","parrot","peacock","pelican","penguin","pigeon","platypus",
            "plover","porcupine","possum","prayingmantis","puffin","puma","pygmy","python","quail","rabbit",
            "raccoon","rat","rattlesnake","raven","reindeer","rhino","roadrunner","robin","salmon","seal",
            "shark","sheep","skunk","sloth","sparrow","spider","squirrel","starfish","stingray","stork",
            "swan","tapir","tarantula","tiger","tortoise","toucan","turkey","turtle","vaquita","wallaby",
            "walrus","whale","wolf","wombat","woodpecker","yak","zebra"]