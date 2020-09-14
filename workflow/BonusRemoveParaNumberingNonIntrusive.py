import os.path
directory=r'C:\Users\jtmartelli\Desktop\unionstatements\test' #path to the target folder, python script outside of the folder to be on the safe side
for i in (os.scandir(directory)):
	if (i=="sc.py"): #chage this if script name changes
		break
	else:
		a=list()
		file=open(i, encoding="utf-8")  #or encoding='utf-8' or 'latin-1' or 'iso-8859-1' or 'mac_roman'
		for line in file:
			j=0
			if (line=='\n'):
				a.append('\n')	
			elif (len(line)>4): #if a line starts with four digits (like a date yyyy) it will not remove anything.
				if (line[:4].isnumeric()):
					a.append(line[:])
				else:
					while (j<len(line) and line[j].isalpha()==False):
						j+=1
					a.append(line[j:])
			else:
				while (j<len(line) and line[j].isalpha()==False): #it will stop when it meets an alphabet character
					j+=1
				a.append(line[j:])
		file.close()	
		with open(i, mode='wt', encoding='utf-8') as myfile:  #ibid
			myfile.write(''.join(a))
