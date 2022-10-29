from enum import Enum
inputType = Enum('inputType', ['LIKES', 'DISLIKES'])

def getFileNameByInputType(inputType):
    if inputType.LIKES == inputType:
        return 'interestedIn.txt'
    if inputType.DISLIKES == inputType:
        return 'notInterestedIn.txt'
    print('inputType ' + inputType + ' not existing')

def writeListToFile(list, inputType):
    newFile = open(getFileNameByInputType(inputType), "w")
    with newFile as file:
        for item in list:
            file.write("%s\n" % item)

# READ files
def createListFromFile(inputType):
    print("not implemented")
