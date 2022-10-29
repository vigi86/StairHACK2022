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

# example usage for getting the strings WITH 1 or 2 of keywords
print("-------------- Test 1: --------")
print(onlyStringsWithAnyOfKeywords(s, ["This"]))
# output:
# {'This is an input with a specific keyword (schnabulieren)', 'This is an input without a specific keyword (zaggzagg)'}

print("-------------- Test 2: --------")
print(onlyStringsWithAnyOfKeywords(s, ["schnabulieren"]))
# output:
# {'This is an input with a specific keyword (schnabulieren)', 'schnabulieren'}

print("-------------- Test 3: --------")
print(onlyStringsWithAnyOfKeywords(s, ["This", "schnabulieren"]))
# output:
# {'schnabulieren', 'This is an input with a specific keyword (schnabulieren)', 'This is an input without a specific keyword (zaggzagg)'}

print("-------------- Test 4: --------")
print(onlyStringsWithAnyOfKeywords(s, ["hallo"]))
# output:
# set()

print()

# example usage for getting the strings WITHOUT at least 1 keyword
print("=======================================")
print("-------------- Test 1: --------")
print(onlyStringsWithoutAnyOfKeywords(s, ["This"]))
# output:
# {'schnabulieren', 'Test'}

print("-------------- Test 2: --------")
print(onlyStringsWithoutAnyOfKeywords(s, ["schnabulieren"]))
# output:
# {'Test', 'This is an input without a specific keyword (zaggzagg)'}

print("-------------- Test 3: --------")
print(onlyStringsWithoutAnyOfKeywords(s, ["This", "schnabulieren"]))
# output:
# {'Test'}

print("-------------- Test 4: --------")
print(onlyStringsWithoutAnyOfKeywords(s, ["hallo"]))
# output:
# {'schnabulieren', 'Test', 'This is an input with a specific keyword (schnabulieren)', 'This is an input without a specific keyword (zaggzagg)'}

print()
