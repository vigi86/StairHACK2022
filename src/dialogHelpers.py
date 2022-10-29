from fileHandler import writeListToFile, inputType, createListFromFile

def askForUserInterestsDialog():
    # get the users interests
    print("What are you you interested in? (enter q to quit)")
    writeListToFile(getTheUsersInterests(), inputType.INTERESTED_IN)

    # get what the user would rather not see
    print("What would you rather not see?")
    writeListToFile(getTheUsersInterests(), inputType.NOT_INTERESTED_IN)

def getTheUsersInterests():
    userInput = input("Enter a topic: ")
    userInputList = []
    while userInput != "q":
        if all(x.isalpha() or x.isspace() for x in userInput):
            userInputList.append(userInput) 
        else:
            print("Input should be alphabetical!")
        userInput = input("Enter a topic: ")
    return userInputList

def printCurrentInterests():
    print("you are currently INTERESTED in: ")
    print(*createListFromFile(inputType.INTERESTED_IN), sep= ", ")
    print("you are currently NOT INTERESTED in: ")
    print(*createListFromFile(inputType.NOT_INTERESTED_IN), sep= ", ")

# returns true when reconfiguration is wished by user
def askForReconfiguration():
    print("do you want to reconfigure your interests? enter (y/n)")
    answer = input()
    return True if answer == "y" else False 
