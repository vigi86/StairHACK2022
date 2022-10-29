#from readline import insert_text
import http
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
    #url = f"https://www.cbsnews.com/{inString}/"
    url = f"https://www.cbsnews.com/"

    #scoops URLs from navigation
    httpResponse = requests.get(url)
    soup = BeautifulSoup(httpResponse.content, 'html.parser')

    con_article = soup.find(class_="site-nav__item--news")
    try:
        urlMapper = {"section":[],"url":[]}

        for link in con_article.find_all('a'):
            use_link = link.get('href')
            if use_link == '#':
                continue
            if use_link.startswith('/'):
                use_link = use_link[1:]

            key = use_link[:-1]

            urlMapper["section"].append(key)
            urlMapper["url"].append(url + use_link)

        print("What are we looking for? (enter 'quit' to exit)")
        if inString == "quit":
            break

        #get sections (science, health, ...)
        urlSelection = []
        for x in range(10):
            print(f'{x}: {list(urlMapper["section"])[x]}')
            urlSelection.append(list(urlMapper["url"])[x])



        inString = input("Your selection: ")

        # for urlDict in urlMapper["url"]:
        # print(urlSelection[int(inString)])
        httpResponse = requests.get(urlSelection[int(inString)])
        soup = BeautifulSoup(httpResponse.content, 'html.parser')

        try:
            con_article = soup.find(class_="component__item-wrapper")
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
        urlMapper.clear()
    except:
        print()