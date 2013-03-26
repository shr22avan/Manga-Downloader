#continuing previously stopped or disrupted downloads
#So far downloads only entire manga
from bs4 import BeautifulSoup
import urllib
import os
print("Enter the destination folder:")
destination=raw_input()
try:
	c=open(destination+'counter.txt','r')
	data=c.read()
	data=data.split()
	counter=int(data[0])
	start_url=data[1]	
except IOError:
	print("Enter the source URL:")
	start_url=raw_input()
	counter=1
c=open(destination+'counter.txt','w')
url=start_url
c.write(str(counter)+" "+url)
while (url):
	print("referring:"+url)
#	f=urllib.urlopen(url)
	while(True):
		try:
			f=urllib.urlopen(url)
			break
		except IOError:
			print('Retrying')	
	html=f.read()
	soup=BeautifulSoup(html)
	image=soup.find(id="img")
	url=image.parent.get('href')
	img=image.get('src')
	while(True):
		pid=os.fork()
		if pid==0:
			os.execlp("wget","wget",img,"-O",destination+str(counter)+".jpg")		
		else:
			status=os.wait()	
			if (status[1]==0):
				break		
#			urllib.urlretrieve(img,destination+str(counter)+".jpg")
	print("written "+img)
	counter=counter+1
	url="http://www.mangareader.net"+url
	c=open(destination+'counter.txt','w')
	c.write(str(counter)+" "+url)
	f.close()
	c.close()
