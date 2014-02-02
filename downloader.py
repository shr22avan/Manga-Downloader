from bs4 import BeautifulSoup
import urllib
import os
import sys
if (len(sys.argv)==1):
	print("Usage: python downloader.py <destination> <url>")
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

c=open(destination+'counter.txt','w')
url=start_url
c.write(str(counter)+" "+url)

while (url):
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

	img=image.get('src')

	while(True):
		pid=os.fork()
		if pid==0:
			os.execlp("wget","wget",img,"-O",destination+str(counter)+".jpg")		
		else:
			status=os.wait()	
			if (status[1]==0):
				break		

	print("written "+img)
	counter=counter+1
	url="http://www.mangareader.net"+url
	c=open(destination+'counter.txt','w')
	c.write(str(counter)+" "+url)

	f.close()
	c.close()
