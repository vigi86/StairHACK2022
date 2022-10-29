def onlyStringsWithAnyOfKeywords(inputs, keywords):
    validInputs = set([])
    for keyword in keywords:
        filteredList = onlyStringsWithKeyword(inputs, keyword)
        for input in filteredList:
            validInputs.add(input)
    return validInputs

# already if only 1 keyword got a hit, the link is filter out
def onlyStringsWithoutAnyOfKeywords(inputs, keywords):
    validInputs = set(inputs)
    for keyword in keywords:
        filteredList = onlyStringsWithKeyword(inputs, keyword)
        for input in filteredList:
            validInputs.discard(input)
    return validInputs


def onlyStringsWithKeyword(inputs, keyword):
    return set(filter(lambda x: keyword in x, inputs))

