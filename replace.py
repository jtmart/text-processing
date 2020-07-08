import csv
from shutil import copyfile
import re

metadata = csv.reader(open('metadata.csv', newline=''), delimiter=',', quotechar='|')
data = []

for row in metadata:
	data.append(row[0])

data = data[1:]

for id in data:
	filename = "corpus/"+id+".txt"
	file = open(filename, encoding='utf-8', errors='replace')
	try :
		fileContent = file.read()
		file.close()

		fileContent = fileContent.replace("~", "")
		fileContent = fileContent.replace("�", "'")
		fileContent = fileContent.replace("—", "-")
		fileContent = fileContent.replace("-------", "-")
		fileContent = fileContent.replace("------", "-")
		fileContent = fileContent.replace("-----", "-")
		fileContent = fileContent.replace("----", "-")
		fileContent = fileContent.replace("---", "-")
		fileContent = fileContent.replace("--", "-")

		file = open("corpus2/"+id+".txt", "w", encoding="utf-8")
		file.write(fileContent)
		file.close()
	except UnicodeDecodeError:
		print(id)
		file.close()
		copyfile(filename, "corpus2/"+id+".txt")



for id in data:
	filename = "corpus2/"+id+".txt"
	file = open(filename, encoding='utf-8', errors='replace')
	fileContent = file.read()
	if "--" in fileContent:
		print(id)

