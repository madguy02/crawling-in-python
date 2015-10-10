import urlparse
import urllib
from bs4 import BeautifulSoup

url="http://www.yourstory.com"
urls=[url]
visited=[url]
while len(urls) >0:
  try:
      htmltext=urllib.urlopen(urls[0]).read()
  except:
    print urls[0]
  soup=BeautifulSoup(htmltext)

  urls.pop(0)
  

for tag in soup.findAll('div','class:list-block clearfix'):
    print(tag.get('title'))
    print (soup.get_text())
    
    if url in tag['class'] and tag['class'] not in visited:
       urls.append(tag['href'])
       visited.append(tag['href'])

       print visited
