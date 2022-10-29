from dialogHelpers import askForUserInterestsDialog, printCurrentInterests, askForReconfiguration
from fileHandler import userInputFilesExisting

# greetings to the user
print("Welcome to TrueNews")

# maybe add asking for username

# check configuration and ask on how to continue
if not userInputFilesExisting():
    askForUserInterestsDialog()
else:
    printCurrentInterests()
    if askForReconfiguration():
        askForUserInterestsDialog()

print("----------------------------------END-------------------------------------")