import requests
import filter
from bs4 import BeautifulSoup

def crawlAllRelevantUrls(baseUrls, interestedIn, notInterestedIn):
    relevantUrls = []
    for soup in getSoups(baseUrls):
        relevantUrls.extend(crawlRelevantUrlsPerSoup(soup, interestedIn, notInterestedIn))
    return relevantUrls
    
def getSoups(urls):
    #soups = []
    #for url in urls:
    #    soups.append(getSoupPerUrl(url))
    #return soups
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
    if interestedIn != []:
        urls = filter.findStringsContainingKeyword(urls, interestedIn)
    if notInterestedIn != []:
        urls = filter.findStringsNotContainingKeywords(urls, notInterestedIn)
    return urls



def readCbsNewsPage(soup):
    con_article = soup.find(class_="component__item-wrapper")

    article_list = con_article.find_all(class_='item__anchor')

    for con_link in con_article.find_all('a'):
        #link_name = con_article.find('a') #.text.split('/')
        print(con_link.get('href'))
        
