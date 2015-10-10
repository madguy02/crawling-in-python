import requests
from bs4 import BeautifulSoup

#fw=open("careercup.txt","a")
html_text=requests.get("http://careercup.com/page")

plain_text=html_text
soup=BeautifulSoup(plain_text,'lxml')
for k in soup.find_all('a'):
		info=k.get('href')
		print info

