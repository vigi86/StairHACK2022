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
    a = 1
    # not required