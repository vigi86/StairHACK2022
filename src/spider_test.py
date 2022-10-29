import requests
from bs4 import BeautifulSoup
#inpit url

print()
print()

inString = ''

#stores url
url = 'https://www.example.com/'

while(inString != 'quit'):
    #red or blue pill
    inString = input("What are we looking for?  ").lower()
    url = f"https://www.cbsnews.com/{inString}/"

    #scoops the url contents
    httpResponse = requests.get(url)
    soup = BeautifulSoup(httpResponse.content, 'html.parser')


    con_article = soup.find(class_="component__item-wrapper")

    #article_list = con_article.find_all(class_='item__anchor')


    try:
        for con_link in con_article.find_all('a'):
            #print(con_link.get('href'))
            use_link = con_link.get('href')

            try:
                httpResponse = requests.get(use_link)
                soup = BeautifulSoup(httpResponse.content, 'html.parser')

                link_article = soup.find(class_="content__body")

                text = ''
                for link_quote in link_article.find('p'):
                    text += link_quote.getText()

                print(text, end='\n\n\n')

            except:
                # do nothing and continue fetch
                var = 0

    except AttributeError:
        print("Section not found. Try something else.", end='\n\n\n')






# searches only specific link names

# for a in soup.findAll('a'):
# if 'word' in a['href']:
#    print 'found a url with 'word' in the link'