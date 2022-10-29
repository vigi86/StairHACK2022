import requests
from bs4 import BeautifulSoup


#input???

#feed with urls
url = ''

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#cbsnews
con_article = soup.find(class_="component__item-wrapper")

article_list = con_article.find_all(class_='item__anchor')


for con_link in con_article.find_all('a'):
    #link_name = con_article.find('a') #.text.split('/')
    
    print(con_link.get('href'))