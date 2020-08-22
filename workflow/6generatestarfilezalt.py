import csv
import os
import codecs

def readCSV(fileName):
	data = []
	with open(fileName, 'rt') as csvfile:
		rows = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in rows:
			data.append(row)
		csvfile.close()
	data = data[1:]
	return data

def createCorpus():
	fileWrite = open("concat.txt", "w", encoding = "utf-8")
	string = ""
	rows = readCSV("metadata.csv")
	for row in rows:
		string += "**** "
		i = 0
		for col in row:
			i+=1
			if i<=21:
				if i <= 9:
					string += "*var0" + str(i) + "_" + col+" "
				else:
					string += "*var" + str(i) + "_" + col+" "
		file = open("corpus/"+row[0]+".txt", "r", encoding = "utf-8")
		string += "\n\n"+file.read()+ "\n\n"
		file.close()

	fileWrite.write(string)
	fileWrite.close()

if __name__ == '__main__':
	# data = readCSV("/home/mudit/Desktop/Internship 2018/MMS CSVs/outputMMS3.csv") + readCSV("/home/mudit/Desktop/Internship 2018/MODI CSVs/output4.csv")
	# createCSV("completeCSV.csv", data)
	# createCorpus()
	# changeEncoding()
	createCorpus()
	# replace()