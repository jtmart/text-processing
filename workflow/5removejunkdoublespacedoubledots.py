import os
import re



#PathOfCode = os.getcwd()
folder_name="all" #keep the python script outside of the target folder (in this case the folder is called all)
Files = []
PathMain = folder_name 
print(PathMain)
for (dirpath, dirnames, filenames) in os.walk(PathMain):
	Files.extend(filenames)
	print(Files)

for File in Files:
	print(File)
	WFile = open(PathMain + "\\" + File,'r',encoding='utf-8') #this removes target characters, 'utf-8' or 'latin-1', try to open files without encoding ",encoding='utf-8'" and rerun
	line = WFile.read()
	WFile.close()
	line_replaced = re.sub(r'\.+', ".", line) #two or more dots, reads line by line
	line_replaced = re.sub(r'\.\s+', ".", line_replaced) #empty space between two dots
	line_replaced = re.sub(r'\.+', ".", line_replaced) 
	line_replaced = re.sub(r'\*+', "", line_replaced)
	line_replaced = re.sub(r'\*\s+', "", line_replaced)
	line_replaced = re.sub(r'\*+', "", line_replaced)
	line_replaced = re.sub(r'(\.)([A-Z])', r"\1 \2", line_replaced) #fix is here: it re-adds the space btw dots and next letter
	line_replaced = re.sub(r'(\.)([0-9]+)(\.)', r"\1 \2\3", line_replaced) #fix is here: it re-adds the space btw dots and next letter
	line_replaced = re.sub(r'(\.)([0-9]+)(\))', r"\1 \2\3", line_replaced) #fix is here: it re-adds the space btw dots and next letter
	WFile = open(PathMain+"\\"+File,'w',encoding='utf-8')
	WFile.write(line_replaced)
	WFile.close()