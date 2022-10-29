from enum import Enum
import os
inputType = Enum('inputType', ['INTERESTED_IN', 'NOT_INTERESTED_IN', 'URLS', 'IGNORE_BY_DEFAULT'])

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

def userInputFilesExisting():
    return os.path.isfile(getFileName(inputType.INTERESTED_IN)) and os.path.isfile(getFileName(inputType.NOT_INTERESTED_IN))

def getFileName(inputType):
    if inputType == inputType.INTERESTED_IN:
        return "userInput/interestedIn.txt"
    elif inputType == inputType.NOT_INTERESTED_IN:
        return "userInput/notInterestedIn.txt"
    elif inputType == inputType.URLS:
        return "config/urls.txt"
    elif inputType == inputType.IGNORE_BY_DEFAULT:
        return "config/ignoreByDefault.txt"
    print('inputType ' + inputType + ' not existing')
