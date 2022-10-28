def onlyStringsWithKeyword(inputs, keyword):
    return list(filter(lambda x: keyword in x, inputs))


def onlyStringsWithoutKeyword(inputs, keyword):
    return list(filter(lambda x: keyword not in x, inputs))
