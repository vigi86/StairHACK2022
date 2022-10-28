def onlyStringsWithAnyOfKeywords(inputs, keywords):
    print("keywords: ")
    print(keywords)
    validInputs = set([])
    for keyword in keywords:
        filteredList = onlyStringsWithKeyword(inputs, keyword)
        for input in filteredList:
            validInputs.add(input)
    return validInputs

# already if only 1 keyword got a hit, the link is filter out
def onlyStringsWithoutAnyOfKeywords(inputs, keywords):
    print("keywords: ")
    print(keywords)
    validInputs = set(inputs)
    for keyword in keywords:
        filteredList = onlyStringsWithKeyword(inputs, keyword)
        for input in filteredList:
            validInputs.remove(input)
    return validInputs


def onlyStringsWithKeyword(inputs, keyword):
    return set(filter(lambda x: keyword in x, inputs))

def onlyStringsWithoutKeyword(inputs, keyword):
    return set(filter(lambda x: keyword not in x, inputs))
