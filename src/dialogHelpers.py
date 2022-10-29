from fileHandler import writeListToFile, inputType, createListFromFile

def askForUserInterestsDialog(user):
    # get the users interests
    print("What are you interested in? (enter q to quit)")
    writeListToFile(getTheUsersInterests(True), inputType.INTERESTED_IN, user)
    print()

    # get what the user would rather not see
    print("What would you rather not see?")
    writeListToFile(getTheUsersInterests(False), inputType.NOT_INTERESTED_IN, user)
    print()
    
def getTheUsersInterests(minOneTopicRequired):
    oneRequired = ""
    if minOneTopicRequired:
        oneRequired = "(min 1 is required; keep it broad, e.g. health, politics, ...)"
    userInput = input("Enter a topic: " + oneRequired)
    userInputList = []
    
    minOneTopicProvided = True
    if minOneTopicRequired:
        minOneTopicProvided = False
    while userInput != "q" or not minOneTopicProvided:
        if userInput == "q" and not minOneTopicProvided:
            print("At least one topic need to be provided")  
        elif userInput == "":
            print("Input must not be empty.")
        elif all(x.isspace() for x in userInput):
            print("Input must not be empty.")
        elif all(x.isalpha() or x.isspace() for x in userInput):
            userInputList.append(userInput) 
            minOneTopicProvided = True
        else:
            print("Input must be alphabetical!")
        userInput = input("Enter a topic: ")
    return userInputList

def printCurrentInterests(user):
    print("you are currently INTERESTED in: ")
    print(*createListFromFile(inputType.INTERESTED_IN, user), sep= ", ")
    print()
    print("you are currently NOT INTERESTED in: ")
    print(*createListFromFile(inputType.NOT_INTERESTED_IN, user), sep= ", ")
    print()

# returns true when reconfiguration is wished by user
def askForReconfiguration():
    print("do you want to reconfigure your interests? enter (y/n)")
    answer = input()
    return True if answer == "y" else False 

def askForUserNameDialog():
    print("Please enter your username to login or create a user by enter a username")
    userName = input()
    while not userName.isalpha():
        print("Username must be alphabetical! Try again!")
        userName = input()
    return userName
