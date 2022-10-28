import requests
from bs4 import BeautifulSoup

inString = input("What are we looking for? (Health (H) or Science (S))")
url = 'https://www.example.com/'

if(inString) == "H":
    url = 'https://www.cbsnews.com/health/'
if(inString) == "S":
    url = 'https://www.cbsnews.com/science/'
else:
    print("nah")


r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# for link in soup.find_all('a'):
#    print(link.get('href'))

http_encoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None

for link in soup.find_all('a', href=True):
    print(link['href'])

# print(r.content)