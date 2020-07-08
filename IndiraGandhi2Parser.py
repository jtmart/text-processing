'''

Imp: RUN USING PYTHON 2.x

Manually set up the range of pages for index
Need to check the Titles, with footer having >= 3 lines are filled multiple times

Note: Run each function one by one to make any changes if required

'''

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from cStringIO import StringIO

Titles = []
footer = []
twoLet = ['of','to','in','it','is','be','as','at','so','we','he','by','or','on','do',
		  'if','me','my','up','an','go','no','us','am','the','for','its','big','ask',
		  'took','time','you','lead','even','him','that','they','war','down','own']
topics = ['SELECTED', 'NATIONAL AFFAIRS', 'ECONOMIC SCENE', 'SCIENCE AND TECHNOLOGY',
		  'EDUCATION AND CULTURE', 'MASS MEDIA', 'HEALTH AND FAMILY WELFARE',
		  'SOCIAL WELFARE', 'INTERNATIONAL AFFAIRS', 'INTERVIEWS', 'THE LAST SPEECH']


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
		print(count)
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
	file = open(name, "w")
	for c in array:
		file.write(c)
	file.close()

def extractTitleFooter(filename):
	global Titles, footer

	text = pdf_to_text(filename, 5 ,15)
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
	text = pdf_to_text(filename, 18 ,499)
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
	file.close()


	file = open(filename)
	text = file.read()
	file.close()

	temp = ""
	finalText = ""
	total = 0

	for c in text:

		if(ord(c) == 10):

			flag = 0

			for c in titles:
				if c == temp.upper():
					total += 1
					if(total != 1):
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
			temp += c

	filen = "temp/speech" + str(total) + ".txt"
	array = [finalText]
	MakeFile(array, filen)

	print(total)


# extractTitleFooter("sample.pdf")
# extractSpeeches("sample.pdf")
# cleanGarbage("speeches.txt")
# splitIntoSpeeches("speeches.txt")