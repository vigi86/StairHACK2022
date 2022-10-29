#from readline import insert_text
import requests
from bs4 import BeautifulSoup
#inpit url

# Print two lines
def print2():
    print("\n")

# Print tree lines
def print3():
    print("\n\n")


print2()
inString = ''

while(True):
    inString = input("What are we looking for? ").lower()
    if inString == "quit":
        break
    url = f"https://www.cbsnews.com/{inString}/"

    #scoops the url contents
    httpResponse = requests.get(url)
    soup = BeautifulSoup(httpResponse.content, 'html.parser')

    con_article = soup.find(class_="component__item-wrapper")

    try:
        for link in con_article.find_all('a'):
            use_link = link.get('href')

            try:
                httpResponse = requests.get(use_link)
                soup = BeautifulSoup(httpResponse.content, 'html.parser')

                linkArticle = soup.find(class_="content__body")

                text = ''
                for linkQuote in linkArticle.find('p'):
                    text += linkQuote.getText()

                print(text, end='\n\n\n')

            except:
                # do nothing and continue fetch
                var = 0

    except AttributeError:
        print(f"Section not found in {url}. Try something else.", end='\n\n\n')