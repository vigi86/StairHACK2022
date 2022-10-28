from filter import *

s = [
    "This is an input with a specific keyword (schnabulieren)",
    "This is an input without a specific keyword (zaggzagg)",
    "schnabulieren",
    "Test"
]

# example usage for getting the strings WITH 1 keyword
#print(onlyStringsWithKeyword(s, "This"))
#print(onlyStringsWithKeyword(s, "schnabulieren"))
#print(onlyStringsWithKeyword(s, "hallo"))
#print()

# example usage for getting the strings WITHOUT 1 keyword
#print(onlyStringsWithoutKeyword(s, "This"))
#print(onlyStringsWithoutKeyword(s, "schnabulieren"))
#print(onlyStringsWithoutKeyword(s, "hallo"))
#print()

# example usage for getting the strings WITH 1 or 2 of keywords
print("-------------- This is a test: --------")
print(onlyStringsWithAnyOfKeywords(s, ["This"]))
print("-------------- This is a test: --------")
print(onlyStringsWithAnyOfKeywords(s, ["schnabulieren"]))
print("-------------- This is a test: --------")
print(onlyStringsWithAnyOfKeywords(s, ["This", "schnabulieren"]))
print("-------------- This is a test: --------")
print(onlyStringsWithAnyOfKeywords(s, ["hallo"]))
print()

# example usage for getting the strings WITHOUT 1 keyword

print("=======================================")
print("-------------- This is a test: --------")
print(onlyStringsWithoutAnyOfKeywords(s, "This"))
print("-------------- This is a test: --------")
print(onlyStringsWithoutAnyOfKeywords(s, "schnabulieren"))
print("-------------- This is a test: --------")
print(onlyStringsWithoutAnyOfKeywords(s, ["This", "schnabulieren"]))
print("-------------- This is a test: --------")
print(onlyStringsWithoutAnyOfKeywords(s, "hallo"))
print()


