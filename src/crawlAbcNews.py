import requests
from bs4 import BeautifulSoup

def printArticle(url):
    try:
        httpResponse = requests.get(url)
        soup = BeautifulSoup(httpResponse.content, 'html.parser')

        print("source: "+ url)
        
        text = ''
        for headlines in soup.find("h1"):
            text += headlines.getText()

        print(text, end='\n\n\n')

    except:
        # do nothing and continue fetch
        var = 0

def printRelatedArticles(url):
    httpResponse = requests.get(url)
    soup = BeautifulSoup(httpResponse.content, 'html.parser')
    
    con_article = soup.find(class_="ContentRoll")

    if con_article:
        for link in set(con_article.find_all('a')):
            printArticle(link.get('href'))