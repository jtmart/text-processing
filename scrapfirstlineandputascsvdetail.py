import os.path
directory=r'C:\Users\anand_zas2udg\Documents\RBI Speeches'
for i in (os.scandir(directory)):
	if (i=="scrapfirstlineandputascsvdetail.py"):
		continue
	n=os.path.join(directory,i)
	for j in os.scandir(n):
		if (j.path.endswith(".txt")):
			file=open(j,encoding="utf-8")
			s=file.readline()
			if (s!="" or s!='\n'):
				print (s.replace('\n',""))
			else:
				print ("not found"+str(j))



