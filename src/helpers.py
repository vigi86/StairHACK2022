def getTheUsersInterests():
    userInput = input("Enter a topic:")
    userInputList = []
    while userInput != "q":
        if all(x.isalpha() or x.isspace() for x in userInput):
            userInputList.append(userInput) 
        else:
            print("Input should be alphabetical!")
        userInput = input("Enter a topic:")
    return userInputList
