import csv
Titles = {}
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
		  'September', 'October', 'November', 'December']
csvData = []
TitleList = []

def mapTitleToFile():
	global csvData, Titles, TitleList

	file = open("Titles2.txt")
	data = file.read()
	file.close()

	data = data.split('\n')
	data = data[:-1]
	for i in range(len(data)):
		csvData.append([])
		temp = data[i].split('|')
		Titles[temp[0]] = temp[1]
		TitleList.append(temp[0])
		csvData[-1].append(temp[1])

def addLocYearMonthDate():
	global csvData

	for i in range(len(csvData)):
		csvData[i].append('gandhi')
		FileName = csvData[i][0]
		year = FileName[1:5]
		csvData[i].append(year)
		month = FileName[1:7]
		csvData[i].append(month)
		date = FileName[1:9]
		csvData[i].append(date)

def addPeriodTermGovt():
	global csvData

	for i in range(len(csvData)):
		csvData[i].append('pmo')
		csvData[i].append('firstterm')
		csvData[i].append('xxxxx')

def addBlankCol(n):
	global csvData

	for i in range(len(csvData)):
		for j in range(n):
			csvData[i].append('')

def addX():
	global csvData

	for i in range(len(csvData)):
		csvData[i].append('x')

def addTitleSourceUrl():
	global csvData

	for i in range(len(csvData)):
		titlename = TitleList[i].replace(" ","")
		titlename = titlename.lower()
		# for i in range(len(titlename)-1):
		csvData[i].append(titlename)
		csvData[i].append('book')
		csvData[i].append('x')

def addYearPlusPmYear():
	global csvData

	for i in range(len(csvData)):
		csvData[i].append(csvData[i][2])
		csvData[i].append('gandhi' + csvData[i][2])

def Numbering(n):
	global csvData

	for i in range(len(csvData)):
		for j in range(n):
			csvData[i].append(str(i+1))

def addLocationLang():
	global csvData

	file = open("Footer.txt")
	footers = file.read().split('\n')[:-1]
	file.close()
	for i in range(len(footers)):
		if 'delhi' in footers[i].lower() or 'lok sabha' in footers[i].lower() or 'rajya sabha' in footers[i].lower():
			csvData[i].append('India')
			csvData[i].append('ncr')
			csvData[i].append('newdelhi')
			csvData[i].append('capital')
		else:
			csvData[i].append('')
			csvData[i].append('')
			csvData[i].append('')
			csvData[i].append('')
			
		if 'hindi' in footers[i].lower():
			csvData[i].append('hindiother')
		else:
			csvData[i].append('')

def addFormat():
	global csvData

	file = open("Footer.txt")
	footers = file.read().split('\n')[:-1]
	file.close()
	for i in range(len(footers)):
		if 'speech' in footers[i].lower() or 'broadcast' in footers[i].lower() or 'address' in footers[i].lower():
			csvData[i].append('speech')
		elif 'statement' in footers[i].lower():
			csvData[i].append('statement')
		elif 'interview' in footers[i].lower():
			csvData[i].append('interview')
		else:
			csvData[i].append('')

def addCompleted():
	global csvData

	for i in range(len(csvData)):
		csvData[i].append('completed')

def addIndependence():
	global csvData

	for i in range(len(csvData)):
		dayfull = csvData[i][4]
		monthDate = dayfull[4:]
		# print(monthDate)
		if(monthDate == '0815'):
			csvData[i].append('independence')
			csvData[i].append('independencerepublicday')
		else:
			csvData[i].append('other')
			if(monthDate == '0126'):
				csvData[i].append('independencerepublicday')
			else:
				csvData[i].append('other')

def addToken():
	global csvData

	for i in range(len(csvData)):
		FileName = csvData[i][0]
		# print(FileName)
		token = FileName[9:]
		csvData[i].append(token)

header = ["id","loc","year","month","day","period","term","govt","typegeneral",
		  "format","independence","independencerepublicday","typespecific","country",
		  "state","city","area","language","details","source","url","yearplus",
		  "pmyear","no","token","status","old","renum","renum2"]

mapTitleToFile()
addLocYearMonthDate()
addPeriodTermGovt()
addBlankCol(1)
addFormat()
addIndependence()
addX()
addLocationLang()
addTitleSourceUrl()
addYearPlusPmYear()
Numbering(1)
addToken()
addCompleted()
addX()
Numbering(2)
# for i in range(len(csvData)):
# 	print(csvData[i][12:])

with open("indira_gandhi_2_metadata.csv","w") as f:
	write = csv.writer(f)
	write.writerow(header)
	for i in csvData:
		write.writerow(i)

