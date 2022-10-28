import imp
from filter import *

s = [
    "This is an input with a specific keyword (schnabulieren)",
    "This is an input without a specific keyword (zaggzagg)"
]

# example usage for getting the strings WITH keyword
print(onlyStringsWithKeyword(s, "This"))
print(onlyStringsWithKeyword(s, "schnabulieren"))
print(onlyStringsWithKeyword(s, "hallo"))

# example usage for getting the strings WITHOUT keyword
print(onlyStringsWithoutKeyword(s, "This"))
print(onlyStringsWithoutKeyword(s, "schnabulieren"))
print(onlyStringsWithoutKeyword(s, "hallo"))


