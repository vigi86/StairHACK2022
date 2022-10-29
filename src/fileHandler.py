
def writeListToFile(list, inputType):
    newFile = open("intrestedIn.txt", "w")
    print(inputType)
    with newFile as file:
        for item in list:
            file.write("%s\n" % item)

# READ files
def createListFromFile():
    print("not implemented")
