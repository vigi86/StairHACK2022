from filter import *

s = [
    "This is an input with a specific keyword (schnabulieren)",
    "This is an input without a specific keyword (zaggzagg)",
    "Schnabulieren",
    "Test"
]

# example usage for getting the strings WITH 1 or 2 of keywords
print("==================== findStringsContainingKeyword ===================")
print("-------------- Demo 1 (1 input, multiple hits): --------")
print(findStringsContainingKeyword(s, ["This"]))
# output:
# {'This is an input with a specific keyword (schnabulieren)', 'This is an input without a specific keyword (zaggzagg)'}

print("-------------- Demo 2 (2 inputs, multiple hits): --------")
print(findStringsContainingKeyword(s, ["This", "schnabulieren"]))
# output:
# {'schnabulieren', 'This is an input with a specific keyword (schnabulieren)', 'This is an input without a specific keyword (zaggzagg)'}

print("-------------- Demo 3 (1 input, no hits): --------")
print(findStringsContainingKeyword(s, ["hallo"]))
# output:
# set()

print("-------------- Demo 4 (case insensitivity): --------")
print(findStringsContainingKeyword(s, ["this", "Schnabulieren"]))
# output:
# {'schnabulieren', 'This is an input with a specific keyword (schnabulieren)', 'This is an input without a specific keyword (zaggzagg)'}


print()

# example usage for getting the strings WITHOUT at least 1 keyword
print("==================== findStringsNotContainingKeywords ===================")
print("-------------- Demo 1 (1 input, multiple hits): --------")
print(findStringsNotContainingKeywords(s, ["This"]))
# output:
# {'schnabulieren', 'Test'}

print("-------------- Demo 2 (2 inputs, multiple hits): --------")
print(findStringsNotContainingKeywords(s, ["This", "schnabulieren"]))
# output:
# {'Test'}

print("-------------- Demo 3 (1 input, no hits): --------")
print(findStringsNotContainingKeywords(s, ["hallo"]))
# output:
# {'schnabulieren', 'Test', 'This is an input with a specific keyword (schnabulieren)', 'This is an input without a specific keyword (zaggzagg)'}

print("-------------- Demo 4 (case insensitivity): --------")
print(findStringsNotContainingKeywords(s, ["this", "Schnabulieren"]))
# output:
# {'Test'}


print()
