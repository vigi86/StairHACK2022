def getTheUsersInterests():
    userInput = input("Enter a topic: ")
    userInputList = []
    while userInput != "q":
        if userInput == "":
            print("Input must not be empty.")
        elif all(x.isalpha() or x.isspace() for x in userInput):
            userInputList.append(userInput) 
        else:
            print("Input must be alphabetical.")
        userInput = input("Enter a topic: ")
    return userInputList
