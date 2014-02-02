from bs4 import BeautifulSoup
import urllib
import os
import sys
if (len(sys.argv)<=2):
	print("Usage: python counter.py <destination> <url> <counter limit>")
	exit()

destination=sys.argv[1]
try:
	c=open(destination+'counter.txt','r')	
	data=c.read()
	data=data.split()
	counter=int(data[0])
	start_url=data[1]	
except IOError:
	start_url=sys.argv[2]
	counter=1
counter_limit=sys.argv[2]

c=open(destination+'counter.txt','w')
url=start_url
c.write(str(counter)+" "+url)

while (url and counter <= counter_limit):
	print("referring:"+url)
	while(True):
		try:
			f=urllib.urlopen(url)
			break
		except:
			print('Retrying')	

	html=f.read()
	soup=BeautifulSoup(html)
	image=soup.find(id="img")

	try:
		url=image.parent.get('href')
	except AttributeError:
		print("No More Images . . .")
		exit(1)

	counter=counter+1
	url="http://www.mangareader.net"+url
	c=open(destination+'counter.txt','w')
	c.write(str(counter)+" "+url)

	f.close()
	c.close()
