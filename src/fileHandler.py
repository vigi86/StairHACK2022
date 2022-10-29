from enum import Enum
inputType = Enum('inputType', ['INTERESTED_IN', 'NOT_INTERESTED_IN', 'URLS'])

def writeListToFile(list, inputType):
    newFile = createFile(inputType)
    with newFile as file:
        for item in list:
            file.write("%s\n" % item)
            file.close()

def createListFromFile(inputType):
    inputFile = readFile(inputType)
    with inputFile as file:
        lines = [line.rstrip() for line in file]
        file.close()
    return lines

    
def createFile(inputType):
    return open(getFileName(inputType), "w")

def readFile(inputType):
    return open(getFileName(inputType), "r")

def getFileName(inputType):
    if inputType == inputType.INTERESTED_IN:
        return "interestedIn.txt"
    elif inputType == inputType.NOT_INTERESTED_IN:
        return "notInterestedIn.txt"
    elif inputType == inputType.URLS:
        return "urls.txt"
    print('inputType ' + inputType + ' not existing')