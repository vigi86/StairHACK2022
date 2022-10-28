import requests
from bs4 import BeautifulSoup
#inpit url
inString = input("What are we looking for? (Health (H) or Science (S))")
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

article_list = con_article.find_all(class_='item__anchor')


for con_link in con_article.find_all('a'):
    #link_name = con_article.find('a') #.text.split('/')
    
    print(con_link.get('href'))
    


#for link in soup.find_all('a', href=True):
#    print(link['href'])
        
    
# searches only specific link names

# for a in soup.findAll('a'):
# if 'word' in a['href']:
#    print 'found a url with 'word' in the link'