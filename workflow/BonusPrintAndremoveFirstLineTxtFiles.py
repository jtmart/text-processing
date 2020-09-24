import os.path
directory=r'C:\Users\jtmartelli\Desktop\unionstatements\test4' #where txt are, python file can be outside of target directory
for i in (os.scandir(directory)):
	if (i=="flu.py"): #change python script name if filename.py changes
		continue
	#n=os.path.join(directory,i)
	#for j in os.scandir(n):
	if (i.path.endswith(".txt")):
		try: 

			file=open(i,encoding="utf-8") #alt encoding if necessary
			#s=file.readline()
			#print (s)
			lines=file.readlines()
			print(lines[0])
			
			del lines[0]
			
			file.close()
			file=open(i, "w+", encoding='utf-8')
			for line in (lines):
				file.write(line)
			file.close()
		except:
			print (" ")
	
		# if (s!="" or s!='\n'):
		# 	print (s.replace('\n',""))
		# else:
		# 	print ("not found"+str(j))



