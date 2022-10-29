from helpers import getTheUsersIntrests
from fileHandler import writeListToFile, createListFromFile, inputType

# greetings to the user
# maybe add asking for username
print("Welcome to TrueNews")

# get the users intrests
print("What are you you interested in? (enter q to quit)")
writeListToFile(getTheUsersInterests(), inputType.LIKES)

# get what the user would rather not see
print("What would you rather not see?")
writeListToFile(getTheUsersInterests(), inputType.DISLIKES)

print(createListFromFile(inputType.LIKES))

print("----------------------------------END-------------------------------------")