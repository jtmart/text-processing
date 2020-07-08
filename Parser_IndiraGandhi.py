'''

Manually set up the range of pages for index
Need to check the Titles, with footer having >= 3 lines are filled multiple times

Note: Run each function one by one to make any changes if required

'''

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from cStringIO import StringIO
from random import randint

Titles = []
footer = []
dates = []
twoLet = ['of','to','in','it','is','be','as','at','so','we','he','by','or','on','do',
		  'if','me','my','up','an','go','no','us','am','the','for','its','big','ask',
		  'took','time','you','lead','even','him','that','they','war','down','own']
topics = ["SELECTED", "DEMOCRACY AND NATIONAL STRENGTH", "THE ECONOMIC SCENE", "SCIENCE, TECHNOLOGY AND ENVIRONMENT", "EDUCATION AND CULTURE", "ARTS AND THE MASS MEDIA", "HEALTH, FAMILY PLANNING AND SOCIAL WELFARE", "INTERNATIONAL AFFAIRS", "HOMAGES, TRIBUTES AND REMINISCENCES", "PERSONAL VIEWPOINT"]


def pdf_to_text(pdfname, fromPage, tillPage):

	# PDFMiner boilerplate
	rsrcmgr = PDFResourceManager()
	sio = StringIO()
	codec = 'utf-8'
	laparams = LAParams()
	device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)

	# Extract text
	count = 1
	fp = file(pdfname, 'rb')
	for page in PDFPage.get_pages(fp):
		# print(count)
		count += 1
		if(count <= fromPage - 1):
			continue
		interpreter.process_page(page)
		if(count == tillPage):
			break
	fp.close()

	# Get text from StringIO
	text = sio.getvalue()

	# Cleanup
	device.close()
	sio.close()

	return text

def MakeFile(array, name):
	file = open(name, "w+")
	for c in array:
		file.write(c)
	file.close()

def extractTitleFooter(filename):
	global Titles, footer

	text = pdf_to_text(filename, 5 ,18)
	text = text.replace("  ", " ")
	temp = ""
	lastOneCap = 0
	countFootersForOne = 0

	for c in text:
		if(ord(c) == 10):

			if(len(temp) <= 5):
				temp = ""
				continue

			flag = 0

			for i in temp:
				if(i == " "):
					continue
				if not i.isdigit():
					flag = 1
					break

			if flag == 0:
				temp = ""
				continue
			
			isCap = 1
			for i in temp:
				if i>='a' and i<='z':
					isCap = 0
					break

			temp += '\n'
			
			if isCap == 1:
				if(lastOneCap == 1):
					Titles.pop()
				Titles.append(temp)
				lastOneCap = 1
				countFootersForOne = 0
			else:
				countFootersForOne += 1
				if(countFootersForOne >= 3):
					Titles.append(Titles[-1])
					countFootersForOne = 1
				footer.append(temp)
				lastOneCap = 0
			temp = ""

		else:
			temp += c

	MakeFile(Titles, "Titles.txt")
	MakeFile(footer, "Footer.txt")

def extractSpeeches(filename):
	text = pdf_to_text(filename, 19 ,597)
	array = [text]
	MakeFile(array, "speeches.txt")

def cleanGarbage(filename):
	global topics 

	file = open(filename)
	text = file.read()
	file.close()
	text = text.replace("", "")
	text = text.replace("(cid:173)", "-")

	temp = ""
	finalText = ""
	newLine = 0
	count = 0
	for c in text:

		temp = temp.replace("  ", " ")

		if(ord(c) == 10):
			count += 1

			flag = 0
			for c in topics:
				if c in temp:
					flag = 1
					break

			if(flag == 1):
				temp = ""
				continue

			if(temp == " " or temp == ""):
				if(newLine == 0):
					temp = ""
					finalText += '\n'
					newLine = 1
					continue

			if(temp != '* ' and temp != ' '):
				flag = 0
				for i in temp:
					if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
						flag = 1
						break
				if flag == 0:
					
					temp = ""
					continue

			
			flag = 0
			if(len(temp) <= 5):
				for c in twoLet:
					if c in temp.lower():
						flag = 1
						break
				if(flag == 0):
					temp = ""
					continue

			flag = 0
			for i in temp.lower():
				if i >= 'a' and i <= 'z':
					if i != 'i' and i != 'j' and i!='l':
						flag = 1
						break
			
			if(flag == 0):
				temp = ""
				continue

			temp += '\n'
			finalText += temp
			newLine = 0
			temp = ""

		else:
			temp += c

	array = [finalText]
	MakeFile(array, filename)

def splitIntoSpeeches(filename):
	file = open("Titles.txt")
	titles = file.read().split('\n')[:-1]
	#titles.extend(["Teachers and Nation-Building ", "Common Commitment to Peace ", "INDO-SOVIET FRIENDSHIP ", "PUTTING THE FACTS STRAIGHT-2 ", "ON DEFENCE-2 ", "STATE OF THE NATION-2 ", "WILDLIFE-2 ", "MESSAGE-1 ", "STATEMENT-1 ", "MAHARAJA RANJIT SINGH "])
	# lines=file.readlines()
	# for i in range(len(lines)):
	# 	lines[i]=lines[i][:-2]
	# titles = lines
	# print(len(titles))
	file.close()

	file = open(filename)
	text = file.read()
	file.close()

	temp = ""
	finalText = ""
	total = 0
	for k in text:
		if(ord(k) == 10):

			flag = 0

			for c in titles:

				if c == temp.upper():
					total += 1
					if(total != 1):
						if total>160 and total<175:
							print(total, c)
						filen = "temp/speech" + str(total-1) + ".txt"
						array = [finalText]
						MakeFile(array, filen)
						temp = ""
						finalText = ""
						flag = 1
					break

			if(flag == 1):
				continue

			temp += '\n'
			finalText += temp
			temp = ""

		else:
			temp += k
	filen = "temp/speech" + str(total) + ".txt"
	array = [finalText]
	MakeFile(array, filen)

	print(total)

def extract_dates():
	global dates

	footer_file = open("Footer.txt", "r")
	foot = footer_file.readlines()
	for line in foot:
		month,find, end=get_month(line)
		if (end!=-1):
			day = line[find+end+1:find+end+3]
			year = line[find+end+5:find+end+9]
			dates.append(year+month+day)
	footer_file.close()

def get_month(line):
	if "January" in line:
		f=line.find("January")
		return ("01",f, 7)
	elif "February" in line:
		f=line.find("February")
		return ("02",f,8)
	elif "March" in line:
		f=line.find("March")
		return ("03",f,5)
	elif "April" in line:
		f=line.find("April")
		return ("04",f,5)
	elif "May" in line:
		f=line.find("May")
		return ("05",f,3)
	elif "June" in line:
		f=line.find("June")
		return ("06",f,4)
	elif "July" in line:
		f=line.find("July")
		return ("07",f,4)
	elif "August" in line:
		f=line.find("August")
		return ("08",f,6)
	elif "September" in line:
		f=line.find("September")
		return ("09",f,9)
	elif "October" in line:
		f=line.find("October")
		return ("10",f,7)
	elif "November" in line:
		f=line.find("November")
		return ("11",f,8)
	elif "December" in line:
		f=line.find("December")
		return ("12",f,8)
	else:
		return ("-1", -1, -1)

def convert_file_names(dates):
	for i in range(len(dates)):
		f1 = open("temp/speech"+str(i+1)+".txt", "r")
		cpy = f1.readlines()
		f1.close()
		fname = "t"+str(dates[i])+ str(randint(100000,999999))
		f2 = open("temp2/"+fname+".txt", "w")
		f2.writelines(cpy)
# extractTitleFooter("gandhi_volume4ocr.pdf")
# print("Footer done!")
# extractSpeeches("gandhi_volume4ocr.pdf")
# print("speeches extracted!")
# cleanGarbage("speeches.txt")
# print("garbage cleaned!")
# splitIntoSpeeches("speeches.txt")
# print("splitting done!")
extract_dates()
convert_file_names(dates)

