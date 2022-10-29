from helpers import getTheUsersInterests
from fileHandler import writeListToFile, createListFromFile, inputType
import spider

appName = "TrueNews"

# greetings to the user
# TODO: maybe add asking for username
print("Welcome to " + appName)
print()

# get the users interests
print("What are you interested in? (enter q to quit)")
writeListToFile(getTheUsersInterests(), inputType.INTERESTED_IN)
print()

# get what the user would rather not see
print("What would you rather not see?")
writeListToFile(getTheUsersInterests(), inputType.NOT_INTERESTED_IN)
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
    print(url)
print()

print("----------------------------------END-------------------------------------")
print()

print("Thanks for using " + appName + "!")
print("Don't forget to recommend us to your friends and family ;)")
print()
