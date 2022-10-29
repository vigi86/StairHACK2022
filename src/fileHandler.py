from enum import Enum
import os

inputType = Enum('inputType', ['INTERESTED_IN', 'NOT_INTERESTED_IN', 'URLS', 'IGNORE_BY_DEFAULT'])

def writeListToFile(list, inputType, user):
    newFile = createFile(inputType, user)
    with newFile as file:
        for item in list:
            file.write("%s\n" % item)
        file.close()
            
def createListFromFile(inputType, user):
    inputFile = readFile(inputType, user)
    with inputFile as file:
        lines = [line.rstrip() for line in file]
        file.close()
    return lines

def createIgnoredByDefaultList():
    inputFile = readDefaultFile()
    with inputFile as file:
        lines = [line.rstrip() for line in file]
        file.close()
    return lines

def createFile(inputType, user):
    return open(getFileName(inputType, user), "w")

def readFile(inputType, user):
    return open(getFileName(inputType, user), "r")

def readDefaultFile(inputType = inputType.IGNORE_BY_DEFAULT, user = None):
    return open(getFileName(inputType, user))

def userInputFilesExisting(user):
    return os.path.isfile(getFileName(inputType.INTERESTED_IN, user)) and os.path.isfile(getFileName(inputType.NOT_INTERESTED_IN, user))

def getFileName(inputType, user):
    if inputType == inputType.INTERESTED_IN:
        return "userInput/" + user + "_interestedIn.txt"
    elif inputType == inputType.NOT_INTERESTED_IN:
        return "userInput/" + user + "_notInterestedIn.txt"
    elif inputType == inputType.URLS:
        return "config/urls.txt"
    elif inputType == inputType.IGNORE_BY_DEFAULT:
        return "config/ignoreByDefault.txt"
    print('inputType ' + inputType + ' not existing')
