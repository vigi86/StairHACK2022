from helpers import getTheUsersIntrests
from fileHandler import writeListToFile, createListFromFile
from enum import Enum

inputType = Enum('inputType', ['LIKES', 'DISLIKES'])

# greetings to the user
# maybe add asking for username
print("Welcome to TrueNews")

# get the users intrests
print("What are you you interested in? (enter q to quit)")
writeListToFile(getTheUsersIntrests(), inputType.LIKES)

# get what the user would rather not see
print("What would you rather not see?")
writeListToFile(getTheUsersIntrests(), inputType.DISLIKES)

print("----------------------------------END-------------------------------------")