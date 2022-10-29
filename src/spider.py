import requests
import filter
from bs4 import BeautifulSoup
from fileHandler import createListFromFile, inputType

# baseUrls:         list(str)   base urls of the webpages one is interested in
# interestedIn:     list(str)   topics / keywords which MUST be in the url (ignored if empty)
# notInterestedIn:  list(str)   topics / keywords which MUST NOT be in the url (ignored if empty)
# return:           list(str)   filtered url list
def crawlAllRelevantUrls(baseUrls, interestedIn, notInterestedIn):
    soups = getSoups(baseUrls)
    urlsPerBaseUrls = list(map(lambda soup: crawlRelevantUrlsPerSoup(soup, interestedIn, notInterestedIn), soups))
    return flattenUrlList(urlsPerBaseUrls, baseUrls)
    
def flattenUrlList(urlsPerBaseUrls, baseUrls):
    flatList = []
    index = 0
    for urls in urlsPerBaseUrls:
        for url in urls:
            if url.startswith("/"):
                flatList.append(baseUrls[index] + url)
            else:    
                flatList.append(url)
        index += 1 
    return flatList

def getSoups(urls):
    return list(map(lambda url: getSoupPerUrl(url), urls))

def getSoupPerUrl(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html.parser')

# soup:             BeautifulSoup() source of urls
# interestedIn:     list(str)       topics / keywords which MUST be in the url (ignored if empty)
# notInterestedIn:  list(str)       topics / keywords which MUST NOT be in the url (ignored if empty)
# return:           list(str)       filtered url list
def crawlRelevantUrlsPerSoup(soup, interestedIn, notInterestedIn):
    urls = list(map(lambda x: x['href'], soup.find_all('a', href=True)))
    urls = filter.findStringsNotContainingKeywords(urls, createListFromFile(inputType.IGNORE_BY_DEFAULT))
    if interestedIn != []:
        urls = filter.findStringsContainingKeyword(urls, interestedIn)
    if notInterestedIn != []:
        urls = filter.findStringsNotContainingKeywords(urls, notInterestedIn)
    return urls

def readNewsPage(soup):
    print(soup)
        