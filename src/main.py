from dialogHelpers import askForUserInterestsDialog, printCurrentInterests, askForReconfiguration
from fileHandler import userInputFilesExisting, createListFromFile, inputType
import spider

appName = "TrueNews"

# greetings to the user
# TODO: maybe add asking for username
print("Welcome to " + appName)

# check configuration and ask on how to continue
if not userInputFilesExisting():
    askForUserInterestsDialog()
else:
    printCurrentInterests()
    if askForReconfiguration():
        askForUserInterestsDialog()

print()
print("Thank you for your inputs.")
print("We are about to provide a list of articles, which fits your interests.")
baseUrls = createListFromFile(inputType.URLS)
print("The following news pages are supported: ")
for baseUrl in baseUrls:
    print(baseUrl)
print()

allRelevantUrls = spider.crawlAllRelevantUrls(baseUrls, createListFromFile(inputType.INTERESTED_IN), createListFromFile(inputType.NOT_INTERESTED_IN))

print("Your results:")
for url in allRelevantUrls:
    spider.readNewsPage(url)
print()

print("--------------------------------- END ------------------------------------")
print()

print("Thanks for using " + appName + "!")
print("Don't forget to recommend us to your friends and family ;)")
print()
