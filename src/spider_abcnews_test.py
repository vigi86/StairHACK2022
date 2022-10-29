import requests
from bs4 import BeautifulSoup

inString = ''

#stores url
url = 'https://www.example.com/'

while(inString != 'quit'):
    #red or blue pill
    inString = input("What are we looking for?  ").lower()
    url = f"https://abcnews.go.com/{inString}/"

    #scoops the url contents
    httpResponse = requests.get(url)
    soup = BeautifulSoup(httpResponse.content, 'html.parser')

    con_article = soup.find(class_="ContentRoll")

    try:
        for con_link in con_article.find_all('a'):
            #print(con_link.get('href'))
            use_link = con_link.get('href')

            try:
                httpResponse = requests.get(use_link)
                soup = BeautifulSoup(httpResponse.content, 'html.parser')

                link_article = soup.find('div', attrs={"data-testid": 'prism-headline'})

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