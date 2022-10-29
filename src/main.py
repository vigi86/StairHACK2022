from tkinter import N
from dialogHelpers import askForUserInterestsDialog, printCurrentInterests, askForReconfiguration, askForUserNameDialog
from fileHandler import userInputFilesExisting, createListFromFile, inputType
import spider

appName = "NewsRazor"

#ask for the username
user = askForUserNameDialog()
# greetings to the user
print("Welcome to " + appName + ", " + user + "\n")

# check configuration and ask on how to continue
if not userInputFilesExisting(user):
    askForUserInterestsDialog(user)
else:
    printCurrentInterests(user)
    if askForReconfiguration():
        askForUserInterestsDialog(user)

print()
print("Thank you for your inputs.")
print("We are about to provide a list of articles, which fits your interests.")
baseUrls = createListFromFile(inputType.URLS, user)
print("The following news pages are supported: ")
for baseUrl in baseUrls:
    print(baseUrl)
print()

allRelevantUrls = spider.crawlAllRelevantUrls(baseUrls, createListFromFile(inputType.INTERESTED_IN, user), createListFromFile(inputType.NOT_INTERESTED_IN, user))

print("Your results:")
for url in allRelevantUrls:
    spider.readNewsPage(url)
print()

print("--------------------------------- END ------------------------------------")
print()

print("Thanks for using " + appName + "!")
print("Don't forget to recommend us to your friends and family ;)")
print()
