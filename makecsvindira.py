import csv

outputfilename = 'indira1b.csv'
currentCount = 194

ministerLetter = "d"
termDecider = [19710212, 19750509]
termAns = ["firstterm", "secondterm", "emergency"]
govtAns = ["congress4", "congress5", "congress6"]

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
	try:
		month, date = needed.split(" ")
	except:
		print(s)
		print(needed)
	monthNum = getMonth(month)
	

	retyear = "0"*(4-len(year)) + str(year)
	retmonthNum = "0"*(2-len(str(monthNum))) + str(monthNum)
	retdate = "0"*(2-len(date)) + str(date)
	return (retyear, retmonthNum, retdate)

def getPeriod():
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
	if("speech" in s or "reply to" in s or "address" in s or "broadcast" in s):
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

	if("broadcast" in s):
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
data = [['1', 'id', 'idchrono', 'loc', 'year', 'month', 'day', 'period', 'term', 'govt', 'typegeneral', 'format', 'independence', 'independencerepublicday', 'typespecific', 'country', 'state', 'city', 'area', 'language', 'details', 'source'], ['', 'd0001', '', 'indira', '1972', '197211', '19721107', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', 'india', 'meghalaya', 'shillong', 'otherstates', 'english', 'BALANCED REGIONAL DEVELOPMENT', ''], ['', 'd0002', '', 'indira', '1972', '197211', '19721127', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'statement', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'ON MULKI RULES', ''], ['', 'd0003', '', 'indira', '1973', '197302', '19730227', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'STRENGTH AND MATURITY', ''], ['', 'd0004', '', 'indira', '1973', '197302', '19730228', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'FROM ONE AGE TO ANOTHER', ''], ['', 'd0005', '', 'indira', '1973', '197304', '19730419', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', '', 'ncr', 'newdelhi', 'capital', 'english', 'CAMPAIGN AGAINST COMMUNALISM', ''], ['', 'd0006', '', 'indira', '1973', '197305', '19730509', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'CHANGE OF ATTITUDES', ''], ['', 'd0007', '', 'indira', '1973', '197306', '19730611', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'SPIRIT OF TOLERANCE', ''], ['', 'd0008', '', 'indira', '1973', '197308', '19730815', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'ind', 'independencerepublicday', '', 'india', 'ncr', 'newdelhi', 'capital', 'hindi', 'SPIRIT OF DETERMINATION', ''], ['', 'd0009', '', 'indira', '1973', '197311', '19731122', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'THE ROLE OF THE OPPOSITION', ''], ['', 'd0010', '', 'indira', '1974', '197401', '19740103', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', '', 'maharashtra', 'nagpur', 'otherstates', 'english', 'ENVIRONMENTAL ENGINEERING', ''], ['', 'd0011', '', 'indira', '1974', '197402', '19740228', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'APPEAL TO WORK UNITEDLY', ''], ['', 'd0012', '', 'indira', '1974', '197403', '19740301', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'PROGRESS THROUGH HARDSHIPS', ''], ['', 'd0013', '', 'indira', '1974', '197405', '19740509', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'MEETING DEMANDS MADE PEACEFULLY', ''], ['', 'd0014', '', 'indira', '1974', '197407', '19740725', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', "SEEKING OPPOSITION'S CO-OPERATION", ''], ['', 'd0015', '', 'indira', '1974', '197408', '19740815', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'ind', 'independencerepublicday', '', 'india', 'ncr', 'newdelhi', 'capital', 'hindi', 'TOWARDS THE BRIGHT FUTURE', ''], ['', 'd0016', '', 'indira', '1974', '197411', '19741108', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', 'india', 'gujarat', 'ahmedabad', 'otherstates', 'english', 'RESEARCH IN BASIC PROBLEMS NECESSARY', ''], ['', 'd0017', '', 'indira', '1975', '197501', '19750126', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'interview', 'other', 'independencerepublicday', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'DEFEND DEMOCRACY', ''], ['', 'd0018', '', 'indira', '1975', '197501', '19750126', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'interview', 'other', 'independencerepublicday', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'A FUNCTIONING DEMOCRACY', ''], ['', 'd0019', '', 'indira', '1975', '197502', '19750224', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'statement', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'ACCORD ON KASHMIR', ''], ['', 'd0020', '', 'indira', '1975', '197502', '19750226', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'SPIRIT OF THE CONSTITUTION', ''], ['', 'd0021', '', 'indira', '1975', '197502', '19750226', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'GUARD THE NATION', ''], ['', 'd0022', '', 'indira', '1975', '197502', '19750227', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', "OPPOSITION'S ROLE IN DEMOCRACY", ''], ['', 'd0023', '', 'indira', '1975', '197503', '19750304', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'KASHMIR', ''], ['', 'd0024', '', 'indira', '1975', '197503', '19750313', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'ACCORD WITH SHEIKH ABDULLAH', ''], ['', 'd0025', '', 'indira', '1975', '197504', '19750420', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', '', 'kerala', 'vaikkom', 'otherstates', 'english', 'HUMAN DIGNITY AND EQUALITY', ''], ['', 'd0026', '', 'indira', '1975', '197505', '19750509', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'CHALLENGES TO BE OVERCOME', ''], ['', 'd0027', '', 'indira', '1975', '197506', '19750626', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', '', 'ncr', 'newdelhi', 'capital', 'english', 'A. On Proclamation of Emergency', ''], ['', 'd0028', '', 'indira', '1975', '197506', '19750627', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', '', 'ncr', 'newdelhi', 'capital', 'hindi', 'B. Why Emergency', ''], ['', 'd0029', '', 'indira', '1975', '197507', '19750703', 'pmo', 'emergency', 'congress6', 'natonalpol', 'interview', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'C. Reasons for Emergency', ''], ['', 'd0030', '', 'indira', '1975', '197507', '19750722', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'D. What led to Emergency', ''], ['', 'd0031', '', 'indira', '1975', '197508', '19750801', 'pmo', 'emergency', 'congress6', 'natonalpol', 'interview', 'other', 'other', '', '', 'usa', 'newyork', 'otherstates', 'english', 'E. Emergency was inevitable', ''], ['', 'd0032', '', 'indira', '1975', '197508', '19750815', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'ind', 'independencerepublicday', '', 'india', 'ncr', 'newdelhi', 'capital', 'hindi', 'ERADICATION OF POVERTY', ''], ['', 'd0033', '', 'indira', '1975', '197508', '19750829', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'OPPORTUNITIES INTO ACCOMPLISHMENTS', ''], ['', 'd0034', '', 'indira', '1975', '197509', '19750902', 'pmo', 'emergency', 'congress6', 'statepol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'INDIVIDUALS AND SOCIAL SERVICE', ''], ['', 'd0035', '', 'indira', '1975', '197510', '19751018', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'INTEGRATION OF THE UNDERPRIVILEGED', ''], ['', 'd0036', '', 'indira', '1975', '197511', '19751111', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'hindi', 'RIGHTS, DUTIES AND TASKS', ''], ['', 'd0037', '', 'indira', '1975', '197512', '19751229', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'punjab', 'chandigarh', 'otherstates', 'english', 'CHANGE FOR STRENGTHENING DEMOCRACY', ''], ['', 'd0038', '', 'indira', '1976', '197605', '19760507', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'ADMINISTRATIVE IMPROVEMENT', ''], ['', 'd0039', '', 'indira', '1976', '197608', '19760815', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'ind', 'independencerepublicday', '', 'india', 'ncr', 'newdelhi', 'capital', 'hindi', 'WITH DISCIPLINE, A BETTER LIFE', ''], ['', 'd0040', '', 'indira', '1976', '197609', '19760921', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'ASPECTS OF SOCIAL WELFARE', ''], ['', 'd0041', '', 'indira', '1976', '197610', '19761023', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'UNITY THROUGH CO-OPERATION', ''], ['', 'd0042', '', 'indira', '1976', '197610', '19761028', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'PARLIAMENT HAS UNFETTERED RIGHT', ''], ['', 'd0043', '', 'indira', '1976', '197611', '19761108', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'SOVEREIGNTY OF PARLIAMENT', ''], ['', 'd0044', '', 'indira', '1976', '197611', '19761127', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'BE INDIAN', ''], ['', 'd0045', '', 'indira', '1977', '197701', '19770118', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', "SEEKING THE NATION'S MANDATE", ''], ['', 'd0046', '', 'indira', '1977', '197703', '19770322', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', "THE PEOPLE'S VERDICT", ''], ['', 'd0047', '', 'indira', '1972', '197211', '19721103', 'pmo', 'secondterm', 'congress5', 'foreignpolicy', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'CO-OPERATION BETWEEN NATIONS', ''], ['', 'd0048', '', 'indira', '1973', '197301', '19730120', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'DEVELOPMENT AT THE GRASSROOTS', ''], ['', 'd0049', '', 'indira', '1973', '197303', '19730331', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'INDUSTRY', ''], ['', 'd0050', '', 'indira', '1973', '197310', '19731015', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', '', 'westbengal', 'calcutta', 'otherstates', 'english', 'FACING DIFFICULTY WITHOUT DESPONDENCY', ''], ['', 'd0051', '', 'indira', '1973', '197310', '19731028', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', '', 'karnataka', 'bangalore', 'otherstates', 'english', 'MODERN MANAGEMENT', ''], ['', 'd0052', '', 'indira', '1973', '197311', '19731114', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'PLANNING FOR PROGRESS', ''], ['', 'd0053', '', 'indira', '1973', '197312', '19731208', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'INCREASE PRODUCTION', ''], ['', 'd0054', '', 'indira', '1974', '197404', '19740401', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'statement', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'POOL ENERGIES FOR PROSPERITY', ''], ['', 'd0055', '', 'indira', '1974', '197404', '19740415', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'STRENGTHENING THE INDUSTRIAL FRONT', ''], ['', 'd0056', '', 'indira', '1974', '197412', '19741208', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'FILLIP TO SMALL INDUSTRIES', ''], ['', 'd0057', '', 'indira', '1974', '197412', '19741228', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', '', 'maharashtra', 'bombay', 'otherstates', 'english', 'PRODUCTION—NOT PROFITS', ''], ['', 'd0058', '', 'indira', '1975', '197504', '19750403', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'IMPROVING OUR ECONOMY', ''], ['', 'd0059', '', 'indira', '1975', '197504', '19750425', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'REVIVING THE ECONOMY', ''], ['', 'd0060', '', 'indira', '1975', '197511', '19751115', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'LABOUR IN NATIONAL PERSPECTIVE', ''], ['', 'd0061', '', 'indira', '1976', '197601', '19760110', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'FAIR DEAL FOR WORKERS', ''], ['', 'd0062', '', 'indira', '1976', '197603', '19760305', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'LAND REFORMS', ''], ['', 'd0063', '', 'indira', '1976', '197604', '19760410', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'PARTNERS IN DEVELOPMENT', ''], ['', 'd0064', '', 'indira', '1976', '197604', '19760413', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'DYNAMIC INSTRUMENT OF SOCIALISM', ''], ['', 'd0065', '', 'indira', '1976', '197609', '19760925', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'PEOPLE AND PROGRESS', ''], ['', 'd0066', '', 'indira', '1976', '197611', '19761110', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', '', 'ncr', 'newdelhi', 'capital', 'english', 'PRODUCTIVITY FOR PROGRESS', ''], ['', 'd0067', '', 'indira', '1977', '197701', '19770118', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'IMPLEMENTING ECONOMIC PROGRAMME', ''], ['', 'd0068', '', 'indira', '1973', '197301', '19730103', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', '', 'punjab', 'chandigarh', 'otherstates', 'english', 'SCIENCE FOR THE COMMON MAN', ''], ['', 'd0069', '', 'indira', '1973', '197310', '19731030', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', '', 'gujarat', 'ahmedabad', 'otherstates', 'english', 'RATIONAL ATTITUDE', ''], ['', 'd0070', '', 'indira', '1974', '197401', '19740103', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', '', 'maharashtra', 'nagpur', 'otherstates', 'english', 'SCIENCE FOR DEVELOPMENT', ''], ['', 'd0071', '', 'indira', '1974', '197407', '19740722', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'statement', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'NUCLEAR ENERGY FOR PEACEFUL PURPOSES', ''], ['', 'd0072', '', 'indira', '1974', '197409', '19740909', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', '', 'tamilnadu', 'madras', 'otherstates', 'english', 'TECHNOLOGY FOR WELFARE', ''], ['', 'd0073', '', 'indira', '1975', '197501', '19750103', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'SCIENCE OF LIVING', ''], ['', 'd0074', '', 'indira', '1975', '197502', '19750201', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', '', 'maharashtra', 'pune', 'otherstates', 'english', 'CHEMICAL SCIENCE IN NATIONAL LIFE', ''], ['', 'd0075', '', 'indira', '1975', '197502', '19750222', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', '', 'tamilnadu', 'madras', 'otherstates', 'english', 'SELF-RELIANT SCIENTISTS', ''], ['', 'd0076', '', 'indira', '1975', '197510', '19751027', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'SCIENCE FOR EVERYDAY LIFE', ''], ['', 'd0077', '', 'indira', '1975', '197512', '19751223', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'SCIENCE FOR BETTERMENT OF THE POOR', ''], ['', 'd0078', '', 'indira', '1976', '197601', '19760103', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'andhrapradesh', 'visakhapatnam', 'otherstates', 'english', 'NEW GOALS FOR SCIENCE', ''], ['', 'd0079', '', 'indira', '1976', '197603', '19760302', 'pmo', 'emergency', 'congress6', 'statepol', 'speech', 'other', 'other', '', '', 'westbengal', 'kharagpur', 'otherstates', 'english', 'THE ROLE OF SCIENCE', ''], ['', 'd0080', '', 'indira', '1976', '197611', '19761102', 'pmo', 'emergency', 'congress6', 'statepol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'ARYABHATA', ''], ['', 'd0081', '', 'indira', '1977', '197701', '19770103', 'pmo', 'emergency', 'congress6', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'odisha', 'bhubaneswar', 'otherstates', 'english', 'SCIENCE AND SPIRITUALITY', ''], ['', 'd0082', '', 'indira', '1972', '197209', '19720907', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', '', 'maharashtra', 'bombay', 'otherstates', 'english', 'TECHNOLOGY FOR BETTER LIFE', ''], ['', 'd0083', '', 'indira', '1972', '197211', '19721102', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', '', 'maharashtra', 'bombay', 'otherstates', 'english', 'NEHRU AS A TEACHER', ''], ['', 'd0084', '', 'indira', '1972', '197211', '19721121', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'hindi', 'WELFARE OF THE BACKWARD', ''], ['', 'd0085', '', 'indira', '1972', '197212', '19721227', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', '', 'westbengal', 'calcutta', 'otherstates', 'english', 'PURPOSE OF POLITICAL SCIENCE', ''], ['', 'd0086', '', 'indira', '1972', '197212', '19721230', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', '', 'westbengal', 'santiniketan', 'otherstates', 'english', 'YOUTH AS BUILDERS', ''], ['', 'd0087', '', 'indira', '1973', '197303', '19730307', 'pmo', 'secondterm', 'congress5', 'statepol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'THE CHALLENGE BEFORE WOMEN', ''], ['', 'd0088', '', 'indira', '1973', '197304', '19730411', 'pmo', 'secondterm', 'congress5', 'natonalpol', 'speech', 'other', 'other', '', 'india', 'ncr', 'newdelhi', 'capital', 'english', 'THE RELEVANCE OF THE VEDAS', '']]


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

	col_8 = getPeriod()
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
