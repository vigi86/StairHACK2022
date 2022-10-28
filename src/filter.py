from queue import Empty


s = [
    "This is an input with a specific keyword (schnabulieren)",
    "This is an input without a specific keyword (schnab)"
]

def filterForStringsWithKeyword(inputs, keyword):
    return list(filter(lambda x: keyword in x, inputs))


def filterForStringsWithoutKeyword(inputs, keyword):
    return list(filter(lambda x: keyword not in x, inputs))



print(filterForStringsWithKeyword(s, "This"))
print(filterForStringsWithKeyword(s, "schnabulieren"))
print(filterForStringsWithKeyword(s, "hallo"))

print(filterForStringsWithoutKeyword(s, "This"))
print(filterForStringsWithoutKeyword(s, "schnabulieren"))
print(filterForStringsWithoutKeyword(s, "hallo"))
