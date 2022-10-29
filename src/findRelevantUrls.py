import requests
import filter
from bs4 import BeautifulSoup

url = 'https://www.cbsnews.com/health/'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

http_encoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None


filterFor = ['CBSNews']
filterOut = ['twitter']

links = map(lambda x: x['href'], soup.find_all('a', href=True))
links = filter.findStringsContainingKeyword(links, filterFor)
links = filter.findStringsNotContainingKeywords(links, filterOut)

for link in links:
    print(link)
