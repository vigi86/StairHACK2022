# filters out any string with has no hits for the given keywords
# checkout filterDemo.py for examples
# inputs:   list(str)   strings which need to be filtered
# keywords: list(str)   filter criteria - if an input str does not contain any keyword, the input str gets removed from the list 
# return:   set(str)    filtered inputs
def findStringsContainingKeyword(inputs, keywords):
    validInputs = set([])
    for keyword in keywords:
        filteredList = filterInputsContainingKeywordCaseInsensitive(inputs, keyword)
        for input in filteredList:
            validInputs.add(input)
    return validInputs

# filters out any string with at least one hits for the given keywords
# checkout filterDemo.py for examples
# inputs:   list(str)   strings which need to be filtered
# keywords: list(str)   filter criteria - if a keyword is in a input str, the input str gets removed from the list
# return:   set(str)    filtered inputs
def findStringsNotContainingKeywords(inputs, keywords):
    validInputs = set(inputs)
    for keyword in keywords:
        filteredList = filterInputsContainingKeywordCaseInsensitive(inputs, keyword)
        for input in filteredList:
            validInputs.discard(input)
    return validInputs


def filterInputsContainingKeywordCaseInsensitive(inputs, keyword):
    return set(filter(lambda x: keyword.casefold() in x.casefold(), inputs))

