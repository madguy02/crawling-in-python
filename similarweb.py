import requests
from bs4 import BeautifulSoup
import time

fw=open("similarweb.txt")
catList = ["facebook.com","bakemycake.in","martopolis.com"]
for j in range (0,2):
	a = "https://www.similarweb.com/website/"+str(catList[j])+"#overview"
	b = requests.get(a).text
	b = BeautifulSoup(b,"lxml")
	c=b.find("span",{"class":"engagementInfo-value engagementInfo-value--large u-text-ellipsis"}).text
	d=b.find_all("span",{"class":"engagementInfo-value u-text-ellipsis"})
	e=b.find_all("span",{"class":"rankingItem-value js-countable"})

	
#f=b.find_all("span",{"class":"rankingItem-value js-countable"})

	print c+"visitors"

	print d[0].text+"bounce rate"
	print d[1].text
	print e[0].text+"global rank"
	print e[1].text+"country rank"
	
