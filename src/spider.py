import requests
import filter
from bs4 import BeautifulSoup

# TODO: feed with correct urls
url = 'https://www.cbsnews.com/health/'

def getSoupPerUrl(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html.parser')

def readCbsNewsPage(soup):
    con_article = soup.find(class_="component__item-wrapper")

    article_list = con_article.find_all(class_='item__anchor')

    for con_link in con_article.find_all('a'):
        #link_name = con_article.find('a') #.text.split('/')
        print(con_link.get('href'))
        

        
print(getSoupPerUrl(url))