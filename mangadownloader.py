import sys
import os
if(len(sys.argv)>1):
	if (sys.argv[1]=='update') :
		file_name='.update'
else:
	file_name='.default'
with open(file_name,'r') as c:
 	for line in c:
 		print(line)
 		pid=os.fork()
 		if pid==0:
 			line=line[0:len(line)-1]
			print(line)
 			os.execlp("python","python","downloader.py",line)
 		elif(pid!=0):
 			os.wait()
