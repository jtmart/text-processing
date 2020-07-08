import csv

outputfilename = 'nehru4.csv'
currentCount = 0

ministerLetter = "e"
periodDecider = 19520212
termDecider = [19520212, 19570328, 19620206]
termAns = ["prefirstterm", "firstterm", "secondterm", "thirdterm"]
govtAns = ["congress0", "congress1", "congress2", "congress3"]

places = dict()
places = eval(open('temp.txt', 'r').read())

def getID(ministerLetter, count):
	return ministerLetter + "0"*(4-len(str(count))) + str(count)

def goodFormat(s):
	return s[:s.rfind(".")]

def getMonth(s):
	if("anuary" in s):
		return 1
	if("ebruary" in s):
		return 2
	if("arch" in s):
		return 3
	if("pril" in s):
		return 4
	if("ay" in s and len(s) == 3):
		return 5
	if("une" in s):
		return 6
	if("uly" in s):
		return 7
	if("ugust" in s):
		return 8
	if("eptember" in s):
		return 9
	if("ctober" in s):
		return 10
	if("ovember" in s):
		return 11
	if("ecember" in s):
		return 12

	error = "ERROR : " + s + " "
	n = input(error)
	return n
	

def parseDate(s):
	s = goodFormat(s)
	year = s[-4:]
	s = s[:len(s) - 6]
	# print(s)
	needed  = s[s.rfind(", ")+2:]
	month, date = needed.split(" ")
	monthNum = getMonth(month)
	

	retyear = "0"*(4-len(year)) + str(year)
	retmonthNum = "0"*(2-len(str(monthNum))) + str(monthNum)
	retdate = "0"*(2-len(date)) + str(date)
	return (retyear, retmonthNum, retdate)

def getPeriod(date, decider):
	d = int(date)
	if(d <= decider):
		return "independenceleader"
	else:
		return "pmo"

def getTerm(date, decider, ans):
	d = int(date)
	for i in range(len(decider)):
		if(d <= decider[i]):
			return ans[i]
	return ans[-1]

def getGovt(s, decider, ans):
	for i in range(len(decider)):
		if(s == decider[i]):
			return ans[i]

	print("ERROR in getGovt")
	a = input()

def getFormat(s):
	s = goodFormat(s)
	s = s.lower()
	if("speech" in s or "reply to" in s or "address" in s or "broadcast to" in s):
		return "speech"
	if("statement" in s):
		return "statement"
	if("interview" in s):
		return "interview"

	print("\n",s)
	Format = input("1) Speech 2) Statement 3) Interview : ")
	if Format == "1":
		return "speech"
	elif Format == "2":
		return "statement"
	elif Format == "3":
		return "interview"
	else:
		return "speech"
	
def getIndepDay(d):
	d = str(d)
	a = "other" # ind
	b = "other" # independencerepublicday

	if(d[4:] == "0815"):
		a = "ind"
	if(d[4:] == "0126"  or a == "ind"):
		b = "independencerepublicday"
	return a,b

def parseRegion(s):
	global places
	s = goodFormat(s)
	s = s[s.find(": ")+2 : s.rfind(",")]
	s = s[:s.rfind(",")]
	s = s.lower()

	country = ""
	state = ""
	city = ""
	area = ""

	if("sabha" in s or "delhi" in s):
		country = "india"
		state = "ncr"
		city = "newdelhi"
	else:
		print("\n",s)
		pcity = input("\nCity : ").lower()
		
		city = pcity

		if(city in places.keys()):
			pstate = places[city]
		else:
			pstate = input("\nState : ").lower()
			places[city] = pstate
		
		state = pstate

		if(state in places.keys() and places[state] != ""):
			pcountry = places[state]
		else:
			pcountry = input("\n1) India 2) Abroad : ")

			if (pcountry == "2"):
				country = "abroad"
			else:
				country = "india"
			places[state] = country
		
		

	if(country == "abroad"):
		area = "abroad"
	elif(state == "up"):
		area = "up"
	elif (city == "newdelhi" or city == "delhi"):
		area = "capital"
	else:
		area = "otherstates"

	return (country, state, city, area)

def getLang(s):
	s = goodFormat(s)
	s = s[s.find(": ")+2 : s.rfind(",")]
	s = s[:s.rfind(",")]
	s = s.lower()

	if("hindi" in s):
		return "hindi"
	if("translation" in s):
		print("\n",s)
		return input("Enter Language : ")

	return "english"

def getTitle(s):
	s = goodFormat(s)
	s = s[:s.find(" : ")]
	return s

def getTypeGen(s, country):
	s = goodFormat(s)
	s = s[: s.rfind(",")]
	s = s[:s.rfind(",")]
	s = s.lower()

	if(country == "abroad"):
		return "foreignpolicy"

	if("sabha" in s and ("lok" in s or "rajya" in s)):
		return "natonalpol"

	if("broadcast" in s and "nation" in s):
		return "natonalpol"

	if("independence day" in s):
		return "natonalpol"

	if("central" in s or "national" in s):
		return "natonalpol"
	
	print(country)
	print("\n",s)
	inp = input("1) National policy 2) Foreign policy 3) State policy : ")
	if(inp == "1"):
		return "natonalpol"
	if(inp == "2"):
		return "foreignpolicy"
	if(inp == "3"):
		return "statepol"
	else:
		return "natonalpol"



data = [["1", "id", "idchrono", "loc", "year", "month", "day", "period", "term", "govt", "typegeneral", "format", "independence", "independencerepublicday", "typespecific", "country", "state", "city", "area", "language", "details", "source"]]
nameOfMinister = {"e" : "nehru", "d" : "indira"}

file = open("index.txt", "r")
for line in file:
	currentCount += 1

	# print(line)
	col_1 = ""
	col_2 = getID(ministerLetter, currentCount)
	col_3 = ""
	col_4 = nameOfMinister[ministerLetter]
	
	year, month, date = parseDate(line)
	col_5 = year
	col_6 = year+month
	col_7 = year+month+date

	col_8 = getPeriod(col_7, periodDecider)
	col_9 = getTerm(col_7, termDecider, termAns)

	col_10 = getGovt(col_9, termAns, govtAns)
	
	col_12 = getFormat(line)

	col_13, col_14 = getIndepDay(col_7)

	col_15 = "" # typespecific

	col_16, col_17, col_18, col_19 = parseRegion(line)

	col_20 = getLang(line)

	col_21 = getTitle(line)
	col_22 = ""

	col_11 = getTypeGen(line, col_16) # typeGeneral here

	row = []

	row.append(col_1)
	row.append(col_2)
	row.append(col_3)
	row.append(col_4)
	row.append(col_5)
	row.append(col_6)
	row.append(col_7)
	row.append(col_8)
	row.append(col_9)
	row.append(col_10)
	row.append(col_11)
	row.append(col_12)
	row.append(col_13)
	row.append(col_14)
	row.append(col_15)
	row.append(col_16)
	row.append(col_17)
	row.append(col_18)
	row.append(col_19)
	row.append(col_20)
	row.append(col_21)
	row.append(col_22)
	data.append(row)

	f = open('temp.txt', 'w')
	f.write(str(places))
	f.close()

	f = open('data.txt', 'w')
	f.write(str(data))
	f.close()


	
myFile = open(outputfilename, 'w')

with myFile:
	writer = csv.writer(myFile)
	writer.writerows(data)

print("Writing complete")
