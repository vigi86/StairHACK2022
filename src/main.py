from helpers import getTheUsersInterests
from fileHandler import writeListToFile, createListFromFile, inputType

# greetings to the user
# maybe add asking for username
print("Welcome to TrueNews")

# get the users intrests
print("What are you you interested in? (enter q to quit)")
writeListToFile(getTheUsersInterests(), inputType.INTERESTED_IN)

# get what the user would rather not see
print("What would you rather not see?")
writeListToFile(getTheUsersInterests(), inputType.NOT_INTERESTED_IN)

print(createListFromFile(inputType.INTERESTED_IN))

print("----------------------------------END-------------------------------------")