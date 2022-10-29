import requests
from bs4 import BeautifulSoup
#inpit url

print()
print()

inString = input("What are we looking for? (Health (H) or Science (S)) =  ")

print()
print()

#stores url
url = 'https://www.example.com/'

#red or blue pill
if(inString) == "H":
    url = 'https://www.cbsnews.com/health/'
if(inString) == "S":
    url = 'https://www.cbsnews.com/science/'
else:
    print("nah")

#scoops the url contents
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


con_article = soup.find(class_="component__item-wrapper")

#article_list = con_article.find_all(class_='item__anchor')


for con_link in con_article.find_all('a'):
    #print(con_link.get('href'))
    use_link = con_link.get('href')
    
    try:
        r = requests.get(use_link)
        soup = BeautifulSoup(r.content, 'html.parser')
    
        link_article = soup.find(class_="content__body")   
        
        print()
        print()
    
        for link_quote in link_article.find('p'):
            print(link_quote.getText())
            
    except:
        print()
        print()
        print("error")     
    
    
        
    
            
    
# searches only specific link names

# for a in soup.findAll('a'):
# if 'word' in a['href']:
#    print 'found a url with 'word' in the link'