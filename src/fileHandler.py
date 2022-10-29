from enum import Enum
inputType = Enum('inputType', ['LIKES', 'DISLIKES'])

def writeListToFile(list, inputType):
    newFile = createFile(inputType)
    print(inputType)
    with newFile as file:
        for item in list:
            file.write("%s\n" % item)

def createFile(inputType):
    if inputType == inputType.LIKES:
        return open("interestedIn.txt", "w")
    elif inputType == inputType.DISLIKES:
        return open("notInterestedIn.txt", "w")
    print('inputType ' + inputType + ' not existing')

# READ files
def createListFromFile(inputType):
    print("not implemented")
