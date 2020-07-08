import csv
import os
import codecs

def readCSV(fileName):
	data = []
	count = 1
	with open(fileName, 'rt') as csvfile:
		rows = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in rows:
			data.append(row)
		csvfile.close()
	data = data[1:]
	return data

def createPrimeFiles():
	countSpeech = {}
	speeches = {}

	rows = readCSV("metadata.csv")

	for row in rows:
		name = row[1]
		typ = row[9]
		fname = row[0]
		if typ[0] == '"':
			typ = typ[1:]
		if typ[-1] == '"':
			typ = typ[:-1]
		if fname[0] == '"':
			fname = fname[1:]
		if fname[-1] == '"':
			fname = fname[:-1]
		if name[0] == '"':
			name = name[1:]
		if name[-1] == '"':
			name = name[:-1]

		if typ == "speech":
			
			file = open("11pmos_Final/" + fname +".txt", "r", encoding = "utf-8")
			data = file.read()
			file.close()

			if name not in countSpeech:
				countSpeech[name] = 1
				speeches[name] = data
			else:
				countSpeech[name] += 1
				speeches[name] += "\n\n" + data

	prefix = {}
	prefix["nehru"] = "01"
	prefix["indira"] = "02"
	prefix["desai"] = "03"
	prefix["charan"] = "04"
	prefix["rajiv"] = "05"
	prefix["vpsingh"] = "06"
	prefix["chandra"] = "07"
	prefix["rao"] = "08"
	prefix["vajpayee"] = "09"
	prefix["mms"] = "10"
	prefix["modi"] = "11"

	for i in speeches:
		file = open(prefix[i] + i +".txt", "w")
		file.write(speeches[i])
		file.close()

if __name__ == '__main__':
	createPrimeFiles()