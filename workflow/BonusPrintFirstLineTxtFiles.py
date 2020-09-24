#import os.path
#directory=r'C:\Users\jtmartelli\Desktop\unionstatements\test2'
#for i in (os.scandir(directory)):
	#if (i=="fl.py"):
		#continue
	#n=os.path.join(directory,i)
	#for j in os.scandir(n):
		#if (j.path.endswith(".txt")):
			#file=open(j,encoding="utf-8")
			#s=file.readline()
			#if (s!="" or s!='\n'):
				#print (s.replace('\n',""))
			#else:
				#print ("not found"+str(j))

import os.path
directory=r'C:\Users\jtmartelli\Desktop\unionstatements\test2' #where txt are, python file can be outside of target directory
for i in (os.scandir(directory)):
	if (i=="fl.py"): #change python script name if filename.py changes
		continue
	#n=os.path.join(directory,i)
	#for j in os.scandir(n):
	if (i.path.endswith(".txt")):
		file=open(i,encoding="utf-8") #alt encoding if necessary
		s=file.readline()
		if (s!="" or s!='\n'):
			print (s.replace('\n',""))
		else:
			print ("not found"+str(j))




